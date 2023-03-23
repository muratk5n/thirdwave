import requests, json, csv
import urllib.request as urllib2
from io import BytesIO
import pandas as pd, re, os

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

def get_fbi_ucr1(year):
    cols = ['city','population','crime-index-total','modified-crime-index-total','homicide','rape','robbery','aggravated-assault','burglary','larceny','motor-vehicle-theft','arson','state']
    df = pd.read_excel("~/Downloads/fbi/fbi-data/xls/%d.xls" % year,skiprows=5,header=None)
    def f(x):
        if pd.isnull(x[0])==False and pd.isnull(x[1])==True: return x[0] 
    df['state'] = df.apply(f, axis=1)    
    df['state'] = df['state'].str.replace('\d+', '')
    df['state'] = df['state'].str.lower()
    df.loc[:,'state'] = df.loc[:,'state'].ffill()
    df = df.dropna(subset=[1])
    df = df.dropna(subset=[0])
    for c in [12,13,14,15,16,17,18]:
        if c in df.columns:
            df = df.drop(columns=c)
    df.columns = cols
    df['city'] = df['city'].str.replace('\d+', '')
    return df

def get_fbi_ucr2(year):
    skiprows = 4
    if year == 2016: skiprows = 5
    cols = ['state','city','population','violent-crime','homicide','rape','robbery','aggravated-assault','property-crime','burglary','larceny','motor-vehicle-theft','arson']
    df = pd.read_excel("~/Downloads/fbi/fbi-data/xls/%d.xls" % year,skiprows=skiprows,header=None)
    for c in [13,14,15,16,17,18]:
        if c in df.columns:
            df = df.drop(columns=c)
    df.columns = cols
    df['state'] = df['state'].str.lower()
    df.loc[:,'state'] = df.loc[:,'state'].ffill()    
    df['state'] = df['state'].str.replace('\d+', '')
    df['state'] = df['state'].str.lower()
    df['state'] = df['state'].str.replace(' - metropolitan counties','')
    df['state'] = df['state'].str.replace(' - nonmetropolitan counties','')
    df['city'] = df['city'].str.replace('\d+', '')
    return df

def conv_xls_csv():

    for year in range(1999,2004):
        df = get_fbi_ucr1(year)
        df.to_csv("~/Downloads/fbi/fbi-data/csv/%d.csv" % year,index=None)
    
    for year in range(2005,2020):
        df = get_fbi_ucr2(year)
        df.to_csv("~/Downloads/fbi/fbi-data/csv/%d.csv" % year,index=None)
    
def get_crime_year(year,init=True):
    key = open("../../0119/2019/05/.key/.datagov").read()
    outfile = '/opt/Downloads/fbi/fbi-data/csv/%d.csv' % year
    if (init):
        out = open(outfile,"w")
        out.write("state,city,violent-crime,homicide,rape,robbery,aggravated-assault,property-crime,burglary,larceny,motor-vehicle-theft,arson,lat,lon\n")
        out.flush()
    else:
        out = open(outfile,"a")
        df = pd.read_csv(outfile,header=None)
        last = list(df[1].tail(1))[0]
        print (last)
    with open('/opt/Downloads/fbi/fbi-data/agencies.csv') as csvfile:
        rd = csv.reader(csvfile,delimiter='|')
        headers = {k: v for v, k in enumerate(next(rd))}
        if not init:
            while True:
                row = next(rd)
                if row[headers['agency_name']] == last: break
        for row in rd:
            print (row[headers['agency']])
            if "Police Department" not in row[headers['agency_name']]: continue
            url = "https://api.usa.gov/crime/fbi/sapi/api/summarized/agencies/%s/offenses/%d/%d?api_key=%s" % (row[headers['agency']],year,year,key)
            response = requests.get(url)
            res = json.loads(response.text)['results']
            if len(res)==0: continue
            d = dict((res[i]['offense'],res[i]['actual']) for i in range(len(res)))
            line = "%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s\n" % \
                   (row[headers['state_name']],
                    row[headers['agency_name']].replace(",",""),
                    d['violent-crime'],
                    d['homicide'],
                    d['rape'],
                    d['robbery'],
                    d['aggravated-assault'],
                    d['property-crime'],
                    d['burglary'],
                    d['larceny'],
                    d['motor-vehicle-theft'],
                    d['arson'],
                    row[headers['lat']],
                    row[headers['lon']])
            out.write(line)
            out.flush()
    out.close()

def crime_annual_summary(cols):
    d = "/opt/Downloads/fbi/fbi-data"
    data = []
    for i in range(1999,2022):
        f = d + '/csv/%d.csv' % i
        if os.path.exists(f) == False: continue
        df = pd.read_csv(f,na_values=['-',' '])
        df = df[cols]
        data.append([i,df.sum().sum()])
    df = pd.DataFrame(data)
    df.columns = ['year','crime']
    df = df.set_index('year')
    pop = pd.read_csv(d + '/uspop.csv',index_col=0)
    df['pop'] = pop
    df['rate'] = (df['crime'] / df['pop']) * 100000
    return df

        
if __name__ == "__main__":
    #conv_xls_csv()
    get_crime_year(2022,init=True)
    #df = crime_annual_summary(['homicide','rape','robbery','aggravated-assault'])
    
