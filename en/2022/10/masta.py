"""
Mastodon crawler
"""
import requests, json, pandas as pd, util, glob, csv
from multiprocessing import Process

def get_masto_peers(host):
    response = requests.get("https://%s/api/v1/instance/peers" % host,timeout=3)
    if len(response.text) > 0: 
        res = json.loads(response.text) # this converts the json to a python list of dictionary
        return res
    else:
        return []

def get_masto_detail(host):
    response = requests.get("https://%s/api/v1/instance" % host,  timeout=3)
    res = json.loads(response.text) # this converts the json to a python list of dictionary
    cd = pd.to_datetime(res['contact_account']['created_at'])
    return res['stats']['user_count'],cd.strftime('%Y-%m-%d')

def init():
    fout = open("./iter0/neighs-0.csv","w")
    res = get_masto_peers("mastodon.social")
    for x in res: fout.write(x + "\n")    
    fout.close()
    d = pd.DataFrame([['mastodon.social',880434,'2016-03-16']])
    d.to_csv("iter0/details.csv",header=None,index=None)

def run(iter):

    class MastJob:
        def __init__(self,ci):
            self.ci = ci
            self.detfile = open("./iter%d/details-%d.csv" % (iter,self.ci), "w")        
            self.nfile = open("./iter%d/neighs-%d.csv" % (iter,self.ci), "w")        
        def exec(self,line):        
            h = line.strip()
            try:            
                print (h)       
                c,d = get_masto_detail(h)
                if int(c) < 100: return                
                print (c,d)
                ns = get_masto_peers(h)
                print ('ns',len(ns))
                for n in ns:
                    self.nfile.write(n)
                    self.nfile.write("\n")
                    self.nfile.flush()                        

                self.detfile.write("%s,%s,%s" % (h,c,d))
                self.detfile.write("\n")
                self.detfile.flush()                        
                self.nfile.flush()
            except Exception as e:
                print ('*')
                pass
        def post(self):
            self.detfile.close()
            self.nfile.close()

    f = "./iter%d/input.csv" % iter
    #util.process(file_name=f, N=4, hookobj = MastJob(0))
    N = 10
    ps = [Process(target=util.process, args=(f, N, MastJob(i))) for i in range(N)]
    for p in ps: p.start()
                    
def combine(iter):
    dd = {}
    detfiles = glob.glob("./*/input*")
    for file in detfiles:
        dd = dict(dd, **pd.read_csv(file,index_col=0,header=None).to_dict('index'))

    nd = {}
    nfiles = glob.glob("./iter%d/neigh*" % iter)
    for file in nfiles:
        print (file)
        fin = open(file)
        for line in fin.readlines():
            h = line.strip()
            if h not in dd: nd[h] = ""
            
    print (len(nd))
    wd = {}
    fout = open("./iter%d/input.csv" % (iter+1),"w")
    for k in nd: fout.write(k + "\n")
    fout.close()

def final():
    dd = {}
    detfiles = glob.glob("./*/details*")
    for file in detfiles:
        print (file)
        dd = dict(dd, **pd.read_csv(file,index_col=0,header=None).to_dict('index'))
    
    fout = open("final.csv","w")
    for k in dd:
        fout.write("%s,%s,%s\n" % (k,dd[k][1],dd[k][2]))
    fout.close()

# running requires some babysitting, run init before start, and after each
# iteration run combine manually.
    
#init()
#run(3)
#combine(2)
#final()

