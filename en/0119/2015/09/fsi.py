import pandas as pd, urllib.request as urllib2, io
urls = \
['/2022/07/fsi-2022-download.xlsx','/2021/05/fsi-2021.xlsx',
 '/2020/05/fsi-2020.xlsx','/2019/04/fsi-2019.xlsx',
 '/2018/04/fsi-2018.xlsx','/data/fsi-2017.xlsx',
 '/data/fsi-2016.xlsx','/data/fsi-2015.xlsx',
 '/data/fsi-2014.xlsx','/data/fsi-2013.xlsx',
 '/data/fsi-2012.xlsx','/data/fsi-2011.xlsx',
 '/data/fsi-2010.xlsx','/data/fsi-2009.xlsx',
 '/data/fsi-2008.xlsx','/data/fsi-2007.xlsx',
 '/data/fsi-2006.xlsx']
hdr = {'User-Agent':'Mozilla/5.0'}
dfs = []
for url in urls: 
    req = urllib2.Request("https://fragilestatesindex.org/wp-content/uploads/"+url,headers=hdr)
    file = io.BytesIO(urllib2.urlopen(req).read())
    dfs.append(pd.read_excel(file))
df = pd.concat(dfs)
df.to_csv('fsi.csv',index=None)
