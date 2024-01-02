import matplotlib.pyplot as plt
from shapely.geometry import Polygon
import pandas as pd, numpy as np
from shapely.ops import unary_union
import geopandas as gpd, re

def biden_approval():
    url = "https://projects.fivethirtyeight.com/biden-approval-data/approval_topline.csv"
    df = pd.read_csv(url,parse_dates=True,index_col='end_date')
    df = df[df.subgroup=='All polls']
    df = df.sort_index()
    df = df[df.index > '2021-06-01']
    df['net'] = df['approve_estimate'] - df['disapprove_estimate']
    return df

def mov_profit(budget, gross):
  marketing = budget / 2
  return np.round(gross - (budget + marketing + gross*0.4),2)

regs = [
    "Luhansk People's Republic \(North Luhansk\)",
    "Luhansk People's Republic \(East Luhansk\)",
    "Luhansk People's Republic \(East Luhansk 2\)",
    "Luhansk People's Republic \(West Luhansk\)",
    "Luhansk People's Republic \(South Luhansk\)",
    "Donetsk People's Republic \(Central Donetsk\)",
    "Donetsk People's Republic \(Central Donetsk 2\)",
    "Donetsk People's Republic \(Central Donetsk 3\)",
    "Donetsk People's Republic \(Central Donetsk 4\)",
    "Donetsk People's Republic \(East Donetsk\)",
    "Donetsk People's Republic \(West Donetsk\)",
    "Donetsk People's Republic \(South Donetsk\)",
    "E.Kharkiv-Russian Armed Forces",
    "Zaporizhia-Russian Armed Forces",
    "Kherson-Russian Armed Forces",
    "Nykolaiv-Russian Forces"]

def prepare_suriyak():
    """
    Data from https://www.google.com/maps/d/viewer?mid=1V8NzjQkzMOhpuLhkktbiKgodOQ27X6IV
    Code searches coordinate blocks by name. Must rename some like Central Donetsk,
    or East Luhansk inside the kml file which repeat, I add 2, 3, at the end. 
    """
    content = open("/tmp/suriyak.kml").read()
    polys = []
    for i,reg in enumerate(regs):
        q = "<Placemark>.*?" + reg + "(.*?)</Placemark>"
        print (q)
        res = re.findall(q, content,re.DOTALL)
        res = res[0]
        res2 = re.findall("<coordinates>(.*?)</coordinates>", res,re.DOTALL)
        for r in res2:
            tmp = r.split(",0")
            coords = [x.strip().split(",") for x in tmp if len(x.strip()) > 8]
            coords = [[float(x),float(y)] for x,y in coords]
            polys.append(Polygon(coords))
            

    res = unary_union(polys)
    
    rrr = list(res.geoms[0].exterior.coords)

    rrr = rrr[0:-3700]
    c = np.array(rrr)
    plt.plot(c[:,0].T,c[:,1].T)
    plt.savefig('/tmp/out.jpg')    
    
    fout = open("/tmp/out.json","w")
    fout.write(str(rrr).replace("(","[").replace(")","]"))
    fout.close()

if __name__ == "__main__": 

    prepare_suriyak()
    
