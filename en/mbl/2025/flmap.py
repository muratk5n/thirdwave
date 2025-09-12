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

def downsample_to_proportion(rows, proportion=1):
    return list(islice(rows, 0, len(rows), int(1/proportion)))

def conv_text_coords_to_list(txt_coords):
    tmp = txt_coords.split(",0")
    coords = [x.strip().split(",") for x in tmp if len(x.strip()) > 8]
    coords = [[float(x),float(y)] for x,y in coords]
    return coords

def get_coords_for_regex(label):
    print ('matching')
    content = open("/tmp/syria.kml").read()
    res = re.findall("<name>.*?" + label + ".*?</name>.*?<coordinates>(.*?)</coordinates>", content, re.DOTALL)
    print ('done')
    return res

#########################################################################
#
# SYRIA
#
#########################################################################
def prep_syria():    
    with zipfile.ZipFile(os.environ['HOME'] + '/Downloads/Guerra Civil Siria.kmz') as myzip:
        with myzip.open('doc.kml') as myfile:
            content = myfile.read().decode('utf-8')                
    fout = open("/tmp/syria.kml","w")
    fout.write(content)
    fout.close()            

def get_coords_for_regex2(label,skips = []):
    fin = open("/tmp/syria.kml").read()
    start_label, start_data = False, False
    res = []
    coords = ""
    for line in fin.split("\n"):        
        if label in line: start_label = True
        if start_label and "<coordinates>" in line: start_data = True
        if start_label:
            c = line.replace("<coordinates>","")
            c = c.replace("</coordinates>","")
            if start_data: coords += c
            #print (line)
        if start_data  and "</coordinates>" in line:
            start_label = False
            start_data = False
            res.append(conv_text_coords_to_list(coords))
            coords = ""
            
    return res

def create_polygon(coord_group,scale=0):    
    polys = [Polygon(x) for x in coord_group]
    polys = [affinity.scale(p, xfact=1+scale, yfact=1+scale) for p in polys]
    comb = unary_union(polys)
    comb = affinity.scale(comb, xfact=1-scale, yfact=1-scale)
    rrr = list(comb.exterior.coords)
    rrr = downsample_to_proportion(rrr, 0.2)    
    return rrr

def do_syria():
    # clean up SDF-Deir al-Zur, Armed Groups-W.Aleppo
    tr1 = get_coords_for_regex2("Operation Eufrates Shield")
    tr2 = get_coords_for_regex2("Operation Olive Branch")
    res = tr1 + tr2
    print ('tr1',len(res))    
    c1 = create_polygon(res)
    c1 = [list(x) for x in c1]

    tr1 = get_coords_for_regex2("Operation Peace Spring")
    res = tr1 
    print ('tr2',len(res))    
    c2 = create_polygon(res, scale = 1e-14)
    c2 = [list(x) for x in c2]

    hts = get_coords_for_regex2("Armed Groups-W. Aleppo") + \
          get_coords_for_regex2("Armed Groups-W.Aleppo") + \
          get_coords_for_regex2("Armed Groups-S.E.Idlib") + \
          get_coords_for_regex2("Armed Groups-S.Idlib") + \
          get_coords_for_regex2("Armed Groups-S.E.Idlib") + \
          get_coords_for_regex2("Armed Groups-N.Hama") + \
          get_coords_for_regex2("Armed Groups-Homs") + \
          get_coords_for_regex2("Armed Groups-E.Homs") + \
          get_coords_for_regex2("Armed Groups-E Homs") + \
          get_coords_for_regex2("Armed Groups-W. Homs") + \
          get_coords_for_regex2("Armed Groups-S.Rif Damascus") + \
          get_coords_for_regex2("Armed Groups-W Rif Damascus") + \
          get_coords_for_regex2("Armed Groups-S. Rif Damascus") + \
          get_coords_for_regex2("Armed Groups-N Rif Damascus") + \
          get_coords_for_regex2("Armed Groups-E Rif Damascus") + \
          get_coords_for_regex2("Armed Groups-Dar") + \
          get_coords_for_regex2("Armed Groups-N.W.Idlib") + \
          get_coords_for_regex2("Armed Groups-W.Aleppo") + \
          get_coords_for_regex2("Armed Groups-Idlib") + \
          get_coords_for_regex2("Armed Groups-N.W.Idlib") + \
          get_coords_for_regex2("Armed Groups-Hama") + \
          get_coords_for_regex2("Armed Groups-Der al-zur") + \
          get_coords_for_regex2("Armed Groups-S.Raqqa") + \
          get_coords_for_regex2("TIP-Idlib/Hama") + \
          get_coords_for_regex2("Armed Groups-NW.Hama") + \
          get_coords_for_regex2("Polígono 57") + \
          get_coords_for_regex2("Armed Groups-Quneitra")
    
    chts1 = create_polygon(hts)
    print ('hts 1',len(hts))
    chts1 = [list(x) for x in chts1]

    saa = get_coords_for_regex2("Armed Groups-Tartus") + \
          get_coords_for_regex2("Armed Groups-Latakia")
    
    csaa = create_polygon(saa)
    print ('saa',len(csaa))    
    csaa = [list(x) for x in csaa]

    idf = get_coords_for_regex2("IDF-Occupied Golan") + \
          get_coords_for_regex2("IDF Area of operations") + \
          get_coords_for_regex2("IDF permanent presence")
    
    cidf = create_polygon(idf)
    print ('idf',len(cidf))    
    cidf = [list(x) for x in cidf]    

    druze = get_coords_for_regex2("Druze Armed Groups-Suwayda") 
    
    cdr = create_polygon(druze)
    print ('dru',len(cdr))    
    cdr = [list(x) for x in cdr]

    sdf = get_coords_for_regex2("SDF-Aleppo") + \
          get_coords_for_regex2("SDF-Raqqa") + \
          get_coords_for_regex2("SDF-Ain Issa") + \
          get_coords_for_regex2("E. Aleppo-SDF") + \
          get_coords_for_regex2("SDF-E. Hasakah") + \
          get_coords_for_regex2("SDF-Qamishli") + \
          get_coords_for_regex2("SDF-Hasakah") + \
          get_coords_for_regex2("SDF-Deir al-Zur")
        
    csdf = create_polygon(sdf)
    print ('sdf',len(csdf))    
    csdf = [list(x) for x in csdf]    

    isis = get_coords_for_regex2("ISIS presence")         
    cis = create_polygon(isis,scale = 0.2)
    print ('isis',len(cis))    
    cis = [list(x) for x in cis]    
    
    d = { "TR": [c1, c2], "HTS": chts1, "SAA": csaa, "ISR": cidf, "DRUZE": cdr, "SDF": csdf, "ISIS": cis}
    fout = open("/tmp/out.json","w")
    fout.write(json.dumps(d))
    fout.close()

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

#########################################################################
#
# ISRAEL
#
#########################################################################

def prep_isr_suriyak():
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


#########################################################################
#
# SUDAN
#
#########################################################################
    
def prep_sahel():
    with zipfile.ZipFile(os.environ['HOME'] + '/Downloads/Sahel.kmz') as myzip:
        with myzip.open('doc.kml') as myfile:
            content = myfile.read().decode('utf-8')

            content = re.sub("RSF-W. Darfur<",
                             "RSF-W. Darfur 1<",
                             content,count=1)

            content = re.sub("RSF-W. Darfur<",
                             "RSF-W. Darfur 2<",
                             content,count=1)

            content = re.sub("RSF-N.Kordofan<",
                             "RSF-N.Kordofan 1<",
                             content,count=1)            

            content = re.sub("RSF-N.Kordofan<",
                             "RSF-N.Kordofan 2<",
                             content,count=1)

            content = re.sub("RSF-N.Kordofan<",
                             "RSF-N.Kordofan 3<",
                             content,count=1)

            content = re.sub("RSF-S.Darfur<",
                             "RSF-S.Darfur 1<",
                             content,count=1)

            content = re.sub("RSF-S.Darfur<",
                             "RSF-S.Darfur 2<",
                             content,count=1)

            content = re.sub("RSF-S.Darfur<",
                             "RSF-S.Darfur 3<",
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
        "RSF-N.Kordofan 1",
        "RSF-N.Kordofan 2",
        "RSF-N.Kordofan 3",
        "RSF-S.Kordofan",
        "RSF-W.Kordofan",
        "RSF-S.Darfur 1",
        "RSF-S.Darfur 2",
        "RSF-S.Darfur 3",
        "RSF-N.Darfur",
        "RSF-C.Darfur",
        "RSF-W. Darfur 1",
        "RSF-W. Darfur 2",
        "RSF-E.Darfur"]
    
    content = open("/tmp/sahel.kml").read()

    rrrs = []              
    polys = []
    scale = 1e-14
    for i,reg in enumerate(sudan_regs1):
        coords = get_coords_for_label(content, reg)
        polys.append(Polygon(coords))
    polys = [affinity.scale(p, xfact=1+scale, yfact=1+scale) for p in polys]
    res = unary_union(polys)
    res = affinity.scale(res, xfact=1-scale, yfact=1-scale)
    rrr = list(res.exterior.coords)
    c = np.array(rrr)
    rrrs.append(c)

    sudan_regs2 = ["RSF-Northern State"]
    polys = []
    scale = 1e-14
    for i,reg in enumerate(sudan_regs2):
        coords = get_coords_for_label(content, reg)
        polys.append(Polygon(coords))
    polys = [affinity.scale(p, xfact=1+scale, yfact=1+scale) for p in polys]
    res = unary_union(polys)
    res = affinity.scale(res, xfact=1-scale, yfact=1-scale)
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

#########################################################################
#
# UKRAINE
#
#########################################################################
    
def prep_ukraine():
    
    with zipfile.ZipFile(os.environ['HOME'] + '/Downloads/Guerra Ruso-Ucraniana 2022.kmz') as myzip:
        with myzip.open('doc.kml') as myfile:
            content = myfile.read().decode('utf-8')

            content = re.sub("Luhansk People's Republic \(East Luhansk\)",
                             "Luhansk People's Republic (East Luhansk 1)",
                             content,count=1)

            content = re.sub("Luhansk People's Republic \(East Luhansk\)",
                             "Luhansk People's Republic (East Luhansk 2)",
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
        "Donetsk People's Republic \(Central Donetsk\)",
        "Donetsk People's Republic \(East Donetsk\)",
        "Donetsk People's Republic \(North East Donetsk\)",
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
        
    if sys.argv[1] == "syria":
        prep_syria()
        do_syria()
        
    exit()
