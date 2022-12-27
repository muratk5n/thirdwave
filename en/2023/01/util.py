import requests, json, csv
import urllib.request as urllib2
from io import BytesIO
import pandas as pd

def get_agencies():
    key = open(".key/.datagov").read()
    out = open("agencies.csv","w")

    with open('states.csv') as csvfile:
        rd = csv.reader(csvfile)
        headers = {k: v for v, k in enumerate(next(rd))}
        for row in rd:
            print (row[headers['state']])
            url = "https://api.usa.gov/crime/fbi/sapi/api/agencies/byStateAbbr/%s?api_key=%s" % (row[headers['code']],key)
            response = requests.get(url)
            res = json.loads(response.text)
            cres = res['results']
            for i in range(len(cres)):
                res = cres[i]
                line = "%s|%s|%s|%s|%s|%s\n" % (res['state_abbr'],res['state_name'],res['ori'],res['agency_name'],res['latitude'],res['longitude'])
                out.write(line)
                out.flush()
    out.close()
    

def get_crime_year(year):
    key = open(".key/.datagov").read()
    out = open("/tmp/%d.csv" % year,"w")
    with open('agencies.csv') as csvfile:
        rd = csv.reader(csvfile,delimiter='|')
        headers = {k: v for v, k in enumerate(next(rd))}
        for row in rd:
            print (row[headers['agency']])
            if row[headers['state_name']] != "Connecticut": continue
            if "Police Department" not in row[headers['agency_name']]: continue
            url = "https://api.usa.gov/crime/fbi/sapi/api/summarized/agencies/%s/offenses/%d/%d?api_key=%s" % (row[headers['agency']],year,year,key)
            response = requests.get(url)
            res = json.loads(response.text)['results']
            print (len(res))
            if len(res)==0: continue
            d = dict((res[i]['offense'],res[i]['actual']) for i in range(len(res)))
            print (d)
            exit()
            line = "%s,%s,%s,%s,%s\n" % (row[headers['state_name']],
                                         row[headers['agency_name']],
                                         d['violent-crime'],row[headers['lat']],
                                         row[headers['lon']])
            out.write(line)
            out.flush()
    out.close()

def get_fbi_ucr(year):
    cols = ['state','city','population','violent-crime','homicide','rape','robbery','aggravated-assault','property-crime','burglary','larceny','motor-vehicle-theft','arson']
    hdr = {'User-Agent':'Mozilla/5.0'}
    url = "https://ucr.fbi.gov/crime-in-the-u.s/%d/crime-in-the-u.s.-%d/tables/table-8/table-8.xls" % (year,year)
    print (url)
    req = urllib2.Request(url,headers=hdr)
    file = BytesIO(urllib2.urlopen(req).read())
    df = pd.read_excel(file,skiprows=4,header=None)
    df.columns = cols
    df.loc[:,'state'] = df.loc[:,'state'].ffill()
    return df
    
if __name__ == "__main__":
    df = get_fbi_ucr(2019)
    df.to_csv("/tmp/%d.csv" % year,index=None)

