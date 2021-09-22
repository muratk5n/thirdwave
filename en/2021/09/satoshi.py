from collections import defaultdict
import pickle, os, glob, re, numpy as np
from scipy.spatial import distance

max_vec_len=100000
CANDIDATES = ["gavin-andresen", "hal-finney", "jed-mccaleb",
              "nick-szabo", "roger-ver", "craig-steven-wright", "wei-dai"]

def vectorize_author(c,word_dict=defaultdict(int)):
    for path in glob.iglob("/tmp/satoshi/data/satoshi/%s/*.txt" % c, recursive=True):        
        with open(path, "r", encoding="utf-8") as f:
            text = f.read()
            text = re.sub('https:.*?\s','http ',text)
            text = text.replace("("," ").replace(")"," ")
            text = text.replace(":"," : ")
            text = text.replace(","," KOMMA")
            text = text.replace("."," DOT")
            text = text.lower()
            tokens = re.split('\s',text)
            for token in tokens: word_dict[token] += 1

    v1 = np.zeros(max_vec_len)
    for i,k in enumerate(word_dict.keys()):
        v1[i] = word_dict[k]

    v1 = v1 / v1.sum()
    return v1, word_dict

def compare():
    sato,wd = vectorize_author('satoshi-nakamoto')
    print ('sato dict',len(wd))

    for cand in CANDIDATES:
        dnew = wd.copy()
        for k in dnew.keys(): dnew[k] = 0
        v,dummy = vectorize_author(cand,dnew)
        #v[len(wd):-1] = 0.0
        print (cand, np.round(distance.cosine(sato,v),3), len(dummy))

def kl_divergence(p, q):
    res = []
    for i in range(len(p)):
        if q[i]>0.0: res.append(p[i] * np.log2(p[i]/q[i]))
    return np.round(np.sum(np.array(res)),3)

def compare_kl():
    sato,wd = vectorize_author('satoshi-nakamoto')
    print ('sato dict',len(wd))

    for cand in CANDIDATES:
        dnew = wd.copy()
        for k in dnew.keys(): dnew[k] = 0
        v,dummy = vectorize_author(cand,dnew)
        v[len(wd):-1] = 0.0
        print (cand, kl_divergence(sato, v))
    

        
