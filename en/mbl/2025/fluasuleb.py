import sys, os, matplotlib.pyplot as plt, pandas as pd
import re, zipfile, json, numpy as np, datetime, folium
import urllib.request, textwrap, math, requests
from timeit import default_timer as timer
from multiprocessing import Process
from shapely.geometry import Polygon
from shapely.ops import unary_union
from pandas_datareader import data
from functools import lru_cache
from datetime import timedelta
from shapely.ops import unary_union
from itertools import islice
from shapely.geometry import Polygon
from shapely import affinity

def get_coords_for_label(content, reg):
    q = "<Placemark>.*?" + reg + "(.*?)</Placemark>"
    print (q)
    res = re.findall(q, content,re.DOTALL)
    res = res[0]
    res2 = re.findall("<coordinates>(.*?)</coordinates>", res,re.DOTALL)
    tmp = res2[0].split(",0")
    coords = [x.strip().split(",") for x in tmp if len(x.strip()) > 8]
    coords = [[float(x),float(y)] for x,y in coords]
    return coords

def prep_isr_suriyak():
    # =======================================================================
    with zipfile.ZipFile(os.environ['HOME'] + '/Downloads/Palestine-Lebanon Map.kmz') as myzip:
        with myzip.open('doc.kml') as myfile:
            content = myfile.read().decode('utf-8')                
    fout = open("/tmp/isr.kml","w")
    fout.write(content)
    fout.close()
    
def map_isr_suriyak():
    prep_isr_suriyak()
    isr_regs = ["Polígono 17"]
    
    content = open("/tmp/isr.kml").read()

    rrrs = []
    for i,reg in enumerate(isr_regs):
        coords = get_coords_for_label(content, reg)
        rrrs.append(coords)
    print (len(rrrs[0]))
    total = []
    #total += rrrs[0][0:200]
    #total += rrrs[0][400:600]
    total += rrrs[0][700:910]
    total += rrrs[0][0:535]
    rrrs[0] = total
        
    for x in rrrs:
        xx = np.array(x)
        plt.plot(xx[:,0].T,xx[:,1].T,'r')
    plt.savefig('/tmp/out.jpg')
        
    fout = open("/tmp/out.json","w")
    fout.write('[\n')
    for i,rrr in enumerate(rrrs):
        fout.write(json.dumps(rrr))
        if i < len(rrrs)-1: fout.write(',')
        fout.write('\n')
    fout.write(']\n')
    fout.close()


def prep_sahel():
    ###########################################################################33333333
    with zipfile.ZipFile(os.environ['HOME'] + '/Downloads/Sahel.kmz') as myzip:
        with myzip.open('doc.kml') as myfile:
            content = myfile.read().decode('utf-8')

            content = re.sub("RSF-W. Darfur<",
                             "RSF-W. Darfur 1<",
                             content,count=1)

            content = re.sub("RSF-W. Darfur<",
                             "RSF-W. Darfur 2<",
                             content,count=1)
        
    fout = open("/tmp/sahel.kml","w")
    fout.write(content)
    fout.close()

def map_sahel_suriyak():
    """
    Data from https://www.google.com/maps/d/u/0/viewer?mid=19IxdgUFhNYyUIXEkYmQgmaYHz6OTMEk
    """
    prep_sahel()

    sudan_regs1 = [
        "RSF-N.Kordofan",
        "RSF- White Nile",
        "RSF-Khartoum",
        "RSF-Gezira",
        "RSF-W.Kordofan",
        "RSF-S.Darfur",
        "RSF-N.Darfur",
        "RSF-C.Darfur",
        "RSF-W. Darfur 1",
        "RSF-W. Darfur 2",
        "RSF-E.Darfur",
        "RSF-W.Kordofan"]
    
    content = open("/tmp/sahel.kml").read()

    rrrs = []              
    polys = []              
    for i,reg in enumerate(sudan_regs1):
        coords = get_coords_for_label(content, reg)
        polys.append(Polygon(coords))
    res = unary_union(polys)    
    rrr = list(res.exterior.coords)
    c = np.array(rrr)
    rrrs.append(c)

    sudan_regs2 = [
        "RSF-Sennar",
        "RSF-Blue Nile"]
    
    content = open("/tmp/sahel.kml").read()

    polys = []              
    for i,reg in enumerate(sudan_regs2):
        coords = get_coords_for_label(content, reg)
        polys.append(Polygon(coords))
    res = unary_union(polys)    
    rrr = list(res.exterior.coords)
    c = np.array(rrr)
    rrrs.append(c)

    
    for x in rrrs:
        plt.plot(x[:,0].T,x[:,1].T,'r')
    plt.savefig('/tmp/out.jpg')
    
    np.set_printoptions(threshold=sys.maxsize)
    fout = open("/tmp/out.json","w")
    fout.write('[\n')
    for i,rrr in enumerate(rrrs):
        fout.write(json.dumps(rrr.tolist()))
        if i < len(rrrs)-1: fout.write(',')
        fout.write('\n')
    fout.write(']\n')
    fout.close()


def prep_ukraine():
    ###########################################################################33333333
    
    with zipfile.ZipFile(os.environ['HOME'] + '/Downloads/Guerra Ruso-Ucraniana 2022.kmz') as myzip:
        with myzip.open('doc.kml') as myfile:
            content = myfile.read().decode('utf-8')

            content = re.sub("Luhansk People's Republic \(East Luhansk\)",
                             "Luhansk People's Republic (East Luhansk 1)",
                             content,count=1)

            content = re.sub("Luhansk People's Republic \(East Luhansk\)",
                             "Luhansk People's Republic (East Luhansk 2)",
                             content,count=1)

            content = re.sub("Donetsk People's Republic \(Central Donetsk\)",
                             "Donetsk People's Republic (Central Donetsk 1)",
                             content,count=1)

            content = re.sub("Donetsk People's Republic \(Central Donetsk\)",
                             "Donetsk People's Republic (Central Donetsk 2)",
                             content,count=1)

            content = re.sub("N.Kharkov-Russian Armed Forces\<",
                             "N.Kharkov-Russian Armed Forces 1<",
                             content,count=1)

            content = re.sub("N.Kharkov-Russian Armed Forces\<",
                             "N.Kharkov-Russian Armed Forces 2<",
                             content,count=1)

            content = re.sub("Kursk-Russian Armed Forces<",
                             "Kursk-Russian Armed Forces 1<",
                             content,count=1)

            content = re.sub("Kursk-Russian Armed Forces<",
                             "Kursk-Russian Armed Forces 2<",
                             content,count=1)
                    
    fout = open("/tmp/ukraine.kml","w")
    fout.write(content)
    fout.close()

    
def map_ukraine_suriyak():
    """
    Data from https://www.google.com/maps/d/viewer?mid=1V8NzjQkzMOhpuLhkktbiKgodOQ27X6IV
    """
    prep_ukraine()
    
    regs = [
        "S..Zaporizhia-Russian Armed Forces",
        "E..Zaporizhia-Russian Armed Forces",
        "Luhansk People's Republic \(North Luhansk\)",
        "Luhansk People's Republic \(East Luhansk 1\)",
        "Luhansk People's Republic \(East Luhansk 2\)",
        "Luhansk People's Republic \(West Luhansk\)",
        "Luhansk People's Republic \(South Luhansk\)",
        "Donetsk People's Republic \(Central Donetsk 1\)",
        "Donetsk People's Republic \(Central Donetsk 2\)",
        "Donetsk People's Republic \(East Donetsk\)",
        "Donetsk People's Republic \(West Donetsk\)",
        "Donetsk People's Republic \(South Donetsk\)",
        "E.Kharkov-Russian Armed Forces",
        "Kherson-Russian Armed Forces",
        "Nykolaiv-Russian Forces"]
    
    reg_ext1 = "N.Kharkov-Russian Armed Forces 1"
    reg_ext2 = "N.Kharkov-Russian Armed Forces 2"
    reg_ext3 = "Kursk-Russian Armed Forces 1"
    reg_ext4 = "Kursk-Russian Armed Forces 2"    
    
    content = open("/tmp/ukraine.kml").read()

    rrrs = []
    
    cext1_coords = get_coords_for_label(content, reg_ext1)
    rrrs.append(np.array(cext1_coords))
    cext2_coords = get_coords_for_label(content, reg_ext2)
    rrrs.append(np.array(cext2_coords))
    cext3_coords = get_coords_for_label(content, reg_ext3)
    cext4_coords = get_coords_for_label(content, reg_ext4)


    polys = []
    polys.append(Polygon(cext3_coords))
    polys.append(Polygon(cext4_coords))
    res = unary_union(polys)    
    cext3_cext4 = list(res.exterior.coords)
    cext3_cext4 = np.array(cext3_cext4)[350:1000]
    rrrs.append(cext3_cext4)
          
    polys = []
    for i,reg in enumerate(regs):
        coords = get_coords_for_label(content, reg)
        polys.append(Polygon(coords))
    res = unary_union(polys)    
    rrr = list(res.exterior.coords)
    rrr = rrr[0:-3700]
    c = np.array(rrr)
    rrrs.append(c)

    for x in rrrs:
        plt.plot(x[:,0].T,x[:,1].T,'r')
    plt.savefig('/tmp/out.jpg')
    
    np.set_printoptions(threshold=sys.maxsize)
    fout = open("/tmp/out.json","w")
    fout.write('[\n')
    for i,rrr in enumerate(rrrs):
        fout.write(json.dumps(rrr.tolist()))
        if i < len(rrrs)-1: fout.write(',')
        fout.write('\n')
    fout.write(']\n')
    fout.close()
                    
if __name__ == "__main__": 

    if sys.argv[1] == "ukr":
        map_ukraine_suriyak()

    if sys.argv[1] == "sudan":
        map_sahel_suriyak()

    if sys.argv[1] == "isr":
        map_isr_suriyak()
    
