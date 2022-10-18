import scipy.sparse as sps, scipy.io as io
from timeit import default_timer as timer
from multiprocessing import Process
from datetime import timedelta
import util, os

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


dir = '/tmp'
file_name = dir + "/" + "BACI_HS17_Y2019_V202201.csv"

start = timer()
N = 4
ps = [Process(target=util.lineproc,args=(file_name, i, N, TJob(),1)) for i in range(N)]
for p in ps: p.start()
for p in ps: p.join()
end = timer()
print('elapsed time', timedelta(seconds=end-start))
