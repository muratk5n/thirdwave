import zipfile, folium
import pandas as pd

# country lat,lon in countries.csv

# data from https://dataunodc.un.org/ids DS Report 2011-2016.xlsx
def preproc():
    xls = pd.ExcelFile('drugs.xlsx')
    df1 = pd.read_excel(xls, '2011') # repeat for 2012,2013,..
    df1.to_csv('drugs-2011.csv',sep=';',index=None)

def concat():    
    res = []
    for i in range(2011,2017):
        res.append(pd.read_csv("drugs-%d.csv" % i,sep=';'))

    df = pd.concat(res)
    df = df[df['DRUG_NAME'].str.contains("Cannabis")==False]
    df.to_csv('out.csv',sep=';',index=None)

# ecstasy $30 per 300 mg tablet 
# pseudoephedrine $11 for a supply of 24 30 mg tablets 
# methamphetamine $50 per gram
# synthetic cannabinoid
# buprenorphine $72.33 for 10, 8MG Tablet Sublingual
# heroine $152 per gram 
# cocaine $100 per gram
# opium $34 per gram, estimated yields of heroin from raw opium are between 6 percent and 10 percent.
    
def drugs():

    f = 'drug-trafficking-unodc.zip'
    c = 'countries.csv'
    c = pd.read_csv(c)
    cdict = c[['name','latitude','longitude']].set_index('name').to_dict('index')

    with zipfile.ZipFile(f, 'r') as z:
        df = pd.read_csv(z.open('drug-trafficking-unodc.csv'),sep=';')

        def chgcountry(x,y):
            df.loc[df['DESTINATION_COUNTRY']==x,'DESTINATION_COUNTRY'] = y
            df.loc[df['COUNTRY']==x,'COUNTRY'] = y
            df.loc[df['DEPARTURE_COUNTRY']==x,'DEPARTURE_COUNTRY'] = y
            
        chgcountry('Russian Federation','Russia')
        chgcountry('Bolivia, Plurinational State of','Bolivia')
        chgcountry('Macedonia, the former Yugoslav Republic of','Macedonia')
        chgcountry('Iran, Islamic Republic of','Iran')
        chgcountry('Venezuela, Bolivarian Republic of','Venezuela')
        chgcountry('Tanzania, United Republic of','Tanzania')
        chgcountry('Korea, Republic of','South Korea')
        chgcountry('Taiwan, Province of China','Taiwan')
        chgcountry('Congo, the Democratic Republic of the','Congo')
        
        df['dest'] = df['DESTINATION_COUNTRY']
        f = df['dest'].str.contains('nan') | df['dest'].str.contains('Unknown')
        df.loc[f,'dest'] = df['COUNTRY']
        
        for index, row in df.iterrows():
            if 'Unknown' in str(row['dest']) or 'nan' in str(row['dest']): continue
            print (row['dest'])

    #    dest=row['DESTINATION_COUNTRY']
    #if row['DEPARTURE_COUNTRY']=='nan' or row['DEPARTURE_COUNTRY']=='Unknown':
    #    if row['PRODUCING_COUNTRY']!='nan' and row['PRODUCING_COUNTRY']!='Unknown':
    #        source = row['PRODUCING_COUNTRY']
    #else:
    #    dest = row['DEPARTURE_COUNTRY']
    #if source=='' or dest == '' or 'nan' in source or 'nan' in dest: continue
    #print (source,'-',dest)
    
if __name__ == "__main__": 

    drugs()

    
