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

def prep_syria():    
    # =======================================================================
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
          get_coords_for_regex2("Armed Groups-Quneitra")
    
    chts1 = create_polygon(hts)
    print ('hts 1',len(hts))
    chts1 = [list(x) for x in chts1]

    saa = get_coords_for_regex2("SAA-Latakia") + \
          get_coords_for_regex2("SAA-Tartus") + \
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
                    
if __name__ == "__main__": 

    #prep_syria()
    do_syria()
    
