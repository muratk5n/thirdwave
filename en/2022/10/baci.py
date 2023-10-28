import pandas as pd
import numpy as np
import scipy.sparse as sps, scipy.io as io, glob
from timeit import default_timer as timer
from multiprocessing import Process
from datetime import timedelta
import impl as u, os, folium

# Parallel task to be called from lineproc
class TJob:
    def __init__(self):
        self.infile = "" # to be set from process
        self.chunk = -1 # to be set from process
        self.A = sps.lil_matrix((900,900))
        self.header = {'t':0,'i':1,'j':2,'k':3,'v':4,'q':5}
    def exec(self,line):        
        tok = line.strip().replace(' ','').split(',')
        i,j = tok[self.header['i']], tok[self.header['j']]
        i,j = int(i),int(j)
        val = self.A[i,j] + float(tok[self.header['v']])
        self.A[i,j] = val
        self.A[j,i] = val
    def post(self):
        print (self.infile)
        outfile = "/tmp/A-%s-%d.mtx" % (os.path.basename(self.infile), self.chunk)
        io.mmwrite(outfile, self.A)

def runjob():
        
    dir = '/tmp'
    file_name = dir + "/" + "BACI_HS17_Y2019_V202201.csv"

    start = timer()
    N = 4 # number of parallel tasks
    ps = [Process(target=u.lineproc,args=(file_name, i, N, TJob(),1)) for i in range(N)]
    for p in ps: p.start()
    for p in ps: p.join()
    end = timer()
    print('elapsed time', timedelta(seconds=end-start))

def combine():
    # combine output pieces from each job into one matrix
    A = sps.lil_matrix((900,900))
    for f in glob.glob("/tmp/A-BACI_HS17_Y2019_V202201*"):
        print (f)
        tmp = io.mmread(f).tolil()
        A = A + tmp
    A = sps.tril(A).tolil()
    io.mmwrite("/tmp/A-final", A)

def map():
    A = io.mmread("/tmp/A-final").tolil()
    cdict1 = pd.read_csv('../../2019/05/countries.csv')[['iso3','latitude','longitude']].set_index('iso3').to_dict('index')
    cdict2 = pd.read_csv('/tmp/country_codes_V202201.csv')[['country_code','iso_3digit_alpha']].set_index('country_code').to_dict('index')    
    rows,cols = A.nonzero()
    vals = np.array([A[row,col] for row,col in zip(rows,cols)])
    mean,std = np.mean(vals),np.std(vals)
    
    m = folium.Map(location=[30, 20], zoom_start=3)
    for row,col in zip(rows,cols):
        val = float(A[row,col])
        if val < mean+4*std: continue
        if row not in cdict2: continue    
        code1 = cdict2[row]['iso_3digit_alpha']
        if code1 not in cdict1: continue
        d = cdict1[code1]
        lat1,lon1 = d['latitude'], d['longitude']

        if col not in cdict2: continue    
        code2 = cdict2[col]['iso_3digit_alpha']
        if code2 not in cdict1: continue
        d = cdict1[code2]
        lat2,lon2 = d['latitude'], d['longitude']

        points = [[lat1,lon1],[lat2,lon2]]
        ts = code1 + "-" + code2 + " " + str(int(val / 1e6)) + " billion"
        folium.PolyLine(points, color='blue', weight=2.0, tooltip=ts).add_to(m)
    m.save('trade-out.html')    

if __name__ == "__main__": 
     
    #runjob()
    #combine()
    map()    
