import sys, os, matplotlib.pyplot as plt
import re, zipfile, json, numpy as np, datetime
from shapely.geometry import Polygon
from shapely.ops import unary_union
from pandas_datareader import data

def get_fred(year, series):
    today = datetime.datetime.now()
    start=datetime.datetime(year, 1, 1)
    end=datetime.datetime(today.year, today.month, today.day)
    df = data.DataReader(series, 'fred', start, end)
    return df

##############################################################################    
##############################################################################    
##############################################################################    

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
