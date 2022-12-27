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
    cols = ['city','population','crime-index-total','modified-crime-index-total','homicide','rape','robbery','aggravated-assault','dummy1','burglary','larceny','motor-vehicle-theft','arson','dummy2','state']
    df = pd.read_excel("~/Downloads/fbi/xls/%d.xls" % year,skiprows=6,header=None)
    def f(x):
        if pd.isnull(x[0])==False and pd.isnull(x[1])==True: return x[0] 
    df['state'] = df.apply(f, axis=1)    
    df['state'] = df['state'].str.replace('\d+', '')
    df['state'] = df['state'].str.lower()
    df.loc[:,'state'] = df.loc[:,'state'].ffill()
    df = df.dropna(subset=[1])
    df = df.dropna(subset=[0])
    df.columns = cols
    df['city'] = df['city'].str.replace('\d+', '')
    return df
    
def get_fbi_ucr2(year):
    cols = ['city','population','crime-index-total','modified-crime-index-total','homicide','rape','robbery','aggravated-assault','burglary','larceny','motor-vehicle-theft','arson','state']
    df = pd.read_excel("~/Downloads/fbi/xls/%d.xls" % year,skiprows=6,header=None)
    def f(x):
        if pd.isnull(x[0])==False and pd.isnull(x[1])==True: return x[0] 
    df['state'] = df.apply(f, axis=1)    
    df['state'] = df['state'].str.replace('\d+', '')
    df['state'] = df['state'].str.lower()
    df.loc[:,'state'] = df.loc[:,'state'].ffill()
    df = df.dropna(subset=[1])
    df = df.dropna(subset=[0])
    df = df.drop(columns=[12,13,14,15,16,17,18])
    df.columns = cols
    df['city'] = df['city'].str.replace('\d+', '')
    return df
    
def get_fbi_ucr3(year):
    cols = ['city','population','crime-index-total','modified-crime-index-total','homicide','rape','robbery','aggravated-assault','burglary','larceny','motor-vehicle-theft','arson','state']
    df = pd.read_excel("~/Downloads/fbi/xls/%d.xls" % year,skiprows=5,header=None)
    def f(x):
        if pd.isnull(x[0])==False and pd.isnull(x[1])==True: return x[0] 
    df['state'] = df.apply(f, axis=1)    
    df['state'] = df['state'].str.replace('\d+', '')
    df['state'] = df['state'].str.lower()
    df.loc[:,'state'] = df.loc[:,'state'].ffill()
    df = df.dropna(subset=[1])
    df = df.dropna(subset=[0])
    df = df.drop(columns=[12,13,14,15,16])
    df.columns = cols
    df['city'] = df['city'].str.replace('\d+', '')
    return df

def get_fbi_ucr4(year):
    cols = ['city','population','crime-index-total','modified-crime-index-total','homicide','rape','robbery','aggravated-assault','burglary','larceny','motor-vehicle-theft','arson','state']
    df = pd.read_excel("~/Downloads/fbi/xls/%d.xls" % year,skiprows=5,header=None)
    def f(x):
        if pd.isnull(x[0])==False and pd.isnull(x[1])==True: return x[0] 
    df['state'] = df.apply(f, axis=1)    
    df['state'] = df['state'].str.replace('\d+', '')
    df['state'] = df['state'].str.lower()
    df.loc[:,'state'] = df.loc[:,'state'].ffill()
    df = df.dropna(subset=[1])
    df = df.dropna(subset=[0])
    df = df.drop(columns=[12,13,14,15,16,17])
    df.columns = cols
    df['city'] = df['city'].str.replace('\d+', '')
    return df
    
def get_fbi_ucr5(year):
    cols = ['state','city','population','violent-crime','homicide','rape','robbery','aggravated-assault','property-crime','burglary','larceny','motor-vehicle-theft','arson']
    df = pd.read_excel("~/Downloads/fbi/xls/%d.xls" % year,skiprows=4,header=None)
    df.columns = cols
    df['state'] = df['state'].str.lower()
    df.loc[:,'state'] = df.loc[:,'state'].ffill()
    return df
    
def get_fbi_ucr6(year):
    cols = ['state','city','population','violent-crime','homicide','rape','robbery','aggravated-assault','property-crime','burglary','larceny','motor-vehicle-theft','arson']
    df = pd.read_excel("~/Downloads/fbi/xls/%d.xls" % year,skiprows=4,header=None)
    df = df.drop(columns=[13,14])
    df.columns = cols
    df['state'] = df['state'].str.lower()
    df.loc[:,'state'] = df.loc[:,'state'].ffill()    
    return df
    
def get_fbi_ucr7(year):
    cols = ['state','city','population','violent-crime','homicide','rape','robbery','aggravated-assault','property-crime','burglary','larceny','motor-vehicle-theft','arson']
    df = pd.read_excel("~/Downloads/fbi/xls/%d.xls" % year,skiprows=4,header=None)
    df = df.drop(columns=[13,14,15,16])
    df.columns = cols
    df['state'] = df['state'].str.lower()
    df.loc[:,'state'] = df.loc[:,'state'].ffill()    
    return df
    
def get_fbi_ucr8(year):
    cols = ['state','city','population','violent-crime','homicide','rape','robbery','aggravated-assault','property-crime','burglary','larceny','motor-vehicle-theft','arson']
    df = pd.read_excel("~/Downloads/fbi/xls/%d.xls" % year,skiprows=4,header=None)
    df = df.drop(columns=[13,14,15,16,17])
    df.columns = cols
    df['state'] = df['state'].str.lower()
    df.loc[:,'state'] = df.loc[:,'state'].ffill()    
    return df
    
def get_fbi_ucr9(year):
    cols = ['state','city','population','violent-crime','homicide','rape','robbery','aggravated-assault','property-crime','burglary','larceny','motor-vehicle-theft','arson']
    df = pd.read_excel("~/Downloads/fbi/xls/%d.xls" % year,skiprows=4,header=None)
    df = df.drop(columns=[6])
    df.columns = cols
    df['state'] = df['state'].str.lower()
    df.loc[:,'state'] = df.loc[:,'state'].ffill()    
    return df
    
def get_fbi_ucr10(year):
    cols = ['state','city','population','violent-crime','homicide','rape','robbery','aggravated-assault','property-crime','burglary','larceny','motor-vehicle-theft','arson']
    df = pd.read_excel("~/Downloads/fbi/xls/%d.xls" % year,skiprows=4,header=None)
    df = df.drop(columns=[13,14,15,16,17,18])
    df.columns = cols
    df['state'] = df['state'].str.lower()
    df.loc[:,'state'] = df.loc[:,'state'].ffill()    
    return df

def conv_xls_csv():
    year = 1999; df = get_fbi_ucr1(year)
    df.to_csv("~/Downloads/fbi/fbi-data/%d.csv" % year,index=None)

    year = 2000; df = get_fbi_ucr2(year)
    df.to_csv("~/Downloads/fbi/fbi-data/%d.csv" % year,index=None)

    year = 2001; df = get_fbi_ucr2(year)
    df.to_csv("~/Downloads/fbi/fbi-data/%d.csv" % year,index=None)

    year = 2002; df = get_fbi_ucr3(year)
    df.to_csv("~/Downloads/fbi/fbi-data/%d.csv" % year,index=None)

    year = 2003; df = get_fbi_ucr4(year)
    df.to_csv("~/Downloads/fbi/fbi-data/%d.csv" % year,index=None)

    year = 2005; df = get_fbi_ucr5(year)
    df.to_csv("~/Downloads/fbi/fbi-data/%d.csv" % year,index=None)

    year = 2006; df = get_fbi_ucr6(year)
    df.to_csv("~/Downloads/fbi/fbi-data/%d.csv" % year,index=None)

    year = 2007; df = get_fbi_ucr6(year)
    df.to_csv("~/Downloads/fbi/fbi-data/%d.csv" % year,index=None)

    year = 2008; df = get_fbi_ucr7(year)
    df.to_csv("~/Downloads/fbi/fbi-data/%d.csv" % year,index=None)

    year = 2009; df = get_fbi_ucr5(year)
    df.to_csv("~/Downloads/fbi/fbi-data/%d.csv" % year,index=None)

    year = 2010; df = get_fbi_ucr5(year)
    df.to_csv("~/Downloads/fbi/fbi-data/%d.csv" % year,index=None)

    year = 2011; df = get_fbi_ucr8(year)
    df.to_csv("~/Downloads/fbi/fbi-data/%d.csv" % year,index=None)

    year = 2012; df = get_fbi_ucr5(year)
    df.to_csv("~/Downloads/fbi/fbi-data/%d.csv" % year,index=None)

    year = 2013; df = get_fbi_ucr7(year)
    df.to_csv("~/Downloads/fbi/fbi-data/%d.csv" % year,index=None)

    year = 2014; df = get_fbi_ucr9(year)
    df.to_csv("~/Downloads/fbi/fbi-data/%d.csv" % year,index=None)

    year = 2015; df = get_fbi_ucr9(year)
    df.to_csv("~/Downloads/fbi/fbi-data/%d.csv" % year,index=None)

    year = 2016; df = get_fbi_ucr5(year)
    df.to_csv("~/Downloads/fbi/fbi-data/%d.csv" % year,index=None)

    year = 2017; df = get_fbi_ucr10(year)
    df.to_csv("~/Downloads/fbi/fbi-data/%d.csv" % year,index=None)

    year = 2018; df = get_fbi_ucr5(year)
    df.to_csv("~/Downloads/fbi/fbi-data/%d.csv" % year,index=None)

    year = 2019; df = get_fbi_ucr5(year)
    df.to_csv("~/Downloads/fbi/fbi-data/%d.csv" % year,index=None)

def get_crime_year(year,init=True):
    key = open("../../2019/05/.key/.datagov").read()
    outfile = '%s/Downloads/fbi/fbi-data/csv/%d.csv' % (os.environ['HOME'], year)
    if (init):
        out = open(outfile,"w")
        out.write("state,city,violent-crime,homicide,rape,robbery,aggravated-assault,property-crime,burglary,larceny,motor-vehicle-theft,arson,lat,lon\n")
        out.flush()
    else:
        out = open(outfile,"a")
        df = pd.read_csv(outfile,header=None)
        last = list(df[1].tail(1))[0]
        print (last)
    with open('%s/Downloads/fbi/fbi-data/agencies.csv' % os.environ['HOME']) as csvfile:
        rd = csv.reader(csvfile,delimiter='|')
        headers = {k: v for v, k in enumerate(next(rd))}
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
                    row[headers['agency_name']],
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


    
if __name__ == "__main__":
    #conv_xls_csv()
    get_crime_year(2020,init=False)
