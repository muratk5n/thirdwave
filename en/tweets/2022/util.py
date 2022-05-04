import requests, urllib.parse, json
from pandas_datareader import data, wb
import matplotlib.pyplot as plt
import pandas as pd
import datetime
import numpy as np

def fetch_ukr_war_map(dt):
    base = "https://www.understandingwar.org/sites/default/files/DraftUkraineCoT"
    sd = dt.strftime("%B%-d,%Y")
    url = base + sd + ".png"
    print (url)
    outfile = "/tmp/isw-ukr-%d%d%02d.png" % (dt.year,dt.month,dt.day)
    import urllib.request as urllib2
    request = urllib2.Request(url)
    pic = urllib2.urlopen(request)
    with open(outfile, 'wb') as localFile:
        localFile.write(pic.read())        

def pollution(lat,lon):
    """
    Register with Openweathermap site and get a API key, place it
    in a file called .owm under .key directory. For limited use
    it is free.
    """    
    url = 'http://api.openweathermap.org/data/2.5/air_pollution?'
    weatherapi = open(".key/.owm").read() # your api key goes in that file    
    payload = { 'lat': str(lat), 'lon': str(lon), 'appid': weatherapi }
    r = requests.get(url, params=payload)
    res = [json.loads(x.decode()) for x in r.iter_lines()]
    aqi = res[0]['list'][0]['main']
    comp = res[0]['list'][0]['components']
    return aqi, comp

def gdp_download():
    countries = ['ABW', 'AFG', 'AGO', 'AIA', 'ALB', 'AND', 'ARE', 'ARG', 'ARM', 'ASM', 'ATF', 'ATG', 'AUS', 'AUT', 'AZE', 'BDI', 'BEN', 'BES', 'BFA', 'BGD', 'BGR', 'BHR', 'BHS', 'BIH', 'BLR', 'BLX', 'BLZ', 'BMU', 'BOL', 'BRA', 'BRB', 'BRN', 'BTN', 'CAF', 'CAN', 'CCK', 'CHE', 'CHL', 'CHN', 'CIV', 'CMR', 'COD', 'COG', 'COK', 'COL', 'COM', 'CPV', 'CRI', 'CUB', 'CUW', 'CXR', 'CYM', 'CYP', 'CZE', 'DEU', 'DJI', 'DMA', 'DNK', 'DOM', 'DZA', 'ECU', 'EGY', 'ERI', 'ESP', 'EST', 'ETH', 'FIN', 'FJI', 'FLK', 'FRA', 'FSM', 'GAB', 'GBR', 'GEO', 'GHA', 'GIB', 'GIN', 'GMB', 'GNB', 'GNQ', 'GRC', 'GRD', 'GRL', 'GTM', 'GUM', 'GUY', 'HKG', 'HND', 'HRV', 'HTI', 'HUN', 'IDN', 'IND', 'IOT', 'IRL', 'IRN', 'IRQ', 'ISL', 'ISR', 'ITA', 'JAM', 'JOR', 'JPN', 'KAZ', 'KEN', 'KGZ', 'KHM', 'KIR', 'KNA', 'KOR', 'KWT', 'LAO', 'LBN', 'LBR', 'LBY', 'LCA', 'LKA', 'LTU', 'LVA', 'MAC', 'MAF', 'MAR', 'MDA', 'MDG', 'MDV', 'MEX', 'MHL', 'MKD', 'MLI', 'MLT', 'MMR', 'MNE', 'MNG', 'MNP', 'MOZ', 'MRT', 'MSR', 'MUS', 'MWI', 'MYS', 'NCL', 'NER', 'NFK', 'NGA', 'NIC', 'NIU', 'NLD', 'NOR', 'NPL', 'NRU', 'NZL', 'OMN', 'PAK', 'PAN', 'PCN', 'PER', 'PHL', 'PLW', 'PNG', 'POL', 'PRK', 'PRT', 'PRY', 'PSE', 'PYF', 'QAT', 'ROU', 'RUS', 'RWA', 'SAU', 'SDN', 'SEN', 'SGP', 'SHN', 'SLB', 'SLE', 'SLV', 'SMR', 'SOM', 'SPM', 'SRB', 'SSD', 'STP', 'SUR', 'SVK', 'SVN', 'SWE', 'SYC', 'SYR', 'TCA', 'TCD', 'TGO', 'THA', 'TJK', 'TKL', 'TKM', 'TLS', 'TON', 'TTO', 'TUN', 'TUR', 'TUV', 'TZA', 'UGA', 'UKR', 'URY', 'USA', 'UZB', 'VCT', 'VEN', 'VGB', 'VNM', 'VUT', 'WLF', 'WSM', 'XXB', 'YEM', 'ZAF', 'ZMB', 'ZWE']
    res = []
    for i,c in enumerate(countries):
        try:
            print (i,c)
            dat = wb.download(indicator='NY.GDP.PCAP.KD', country=[c], start=2014, end=2016)
            gdp = list(dat['NY.GDP.PCAP.KD']) 
            res.append([c, gdp[0], gdp[2]])
            #if len(res) > 5: break
        except:
            print ('error')

    df = pd.DataFrame(res)
    df.columns = ['code','gdp2014','gdp2016']
    df.to_csv('gdp1416.csv',index=None)    

def biden_approval():
    url = "https://projects.fivethirtyeight.com/biden-approval-data/approval_topline.csv"
    df = pd.read_csv(url,parse_dates=True,index_col='modeldate')
    df = df[df.subgroup=='All polls']
    df = df.sort_index()
    df = df[df.index > '2021-06-01']
    df['net'] = df['approve_estimate'] - df['disapprove_estimate']
    return df

def trump_approval():
    url = "https://projects.fivethirtyeight.com/trump-approval-data/approval_polllist.csv"
    df = pd.read_csv(url,parse_dates=True,index_col='modeldate')
    df = df[df.subgroup=='All polls']
    df = df[df.pollster=='Gallup']
    df = df.sort_index()
    df['net'] = df['approve'] - df['disapprove']
    return df

def isw_scale(pix):
    a=(402,423,47.08663463830697, 37.5382073671603) # mariopol
    b=(418,329,48.01772552348221, 37.80499020789566) # donetsk

    dx = (a[3]-b[3])/(a[0]-b[0])
    dy = (a[2]-b[2])/(a[1]-b[1])
    res = []
    for p in pix:
      x = ((p[0]-b[0])*dx) + b[3]
      y = ((p[1]-b[1])*dy) + b[2]
      res.append([np.round(y,4),np.round(x,4)])
    return res

if __name__ == "__main__": 

    '''
    df = biden_approval()
    print (df.net.tail(10))
    df.net.plot()
    plt.show()
    '''

    fetch_ukr_war_map(datetime.datetime(2022,5,1))
    
