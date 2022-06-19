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
    #df.to_csv('out.csv',sep=';',index=None)

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

        df['weight'] = df[df['DRUG_UNIT']=='Gram']['AMOUNT']/1000.0
        df['weight'] = df[df['DRUG_UNIT']=='Kilogram']['AMOUNT']
        df = df.dropna(subset=['weight'])
        
        def chgcountry(x,y):
            df.loc[df['DESTINATION_COUNTRY']==x,'DESTINATION_COUNTRY'] = y
            df.loc[df['COUNTRY']==x,'COUNTRY'] = y
            df.loc[df['DEPARTURE_COUNTRY']==x,'DEPARTURE_COUNTRY'] = y
            df.loc[df['PRODUCING_COUNTRY']==x,'PRODUCING_COUNTRY'] = y
            
        chgcountry('Russian Federation','Russia')
        chgcountry('Bolivia, Plurinational State of','Bolivia')
        chgcountry('Macedonia, the former Yugoslav Republic of','Macedonia')
        chgcountry('Iran, Islamic Republic of','Iran')
        chgcountry('Venezuela, Bolivarian Republic of','Venezuela')
        chgcountry('Tanzania, United Republic of','Tanzania')
        chgcountry('Korea, Republic of','South Korea')
        chgcountry('Taiwan, Province of China','Taiwan')
        chgcountry('Congo, the Democratic Republic of the','Congo')
        chgcountry('United Kingdom (England and Wales)','United Kingdom')
        chgcountry('Iraq (Central Iraq)','Iraq')
        chgcountry('Cabo Verde','Cape Verde')
        chgcountry("Côte d'Ivoire","Ivory Coast")
        chgcountry('Trinidad and Tobago','Trinidad And Tobago')
        chgcountry('Viet Nam','Vietnam')
        chgcountry('Libyan Arab Jamahiriya','Libya')
        chgcountry('Syrian Arab Republic','Syria')
        chgcountry('Kosovo under UNSCR 1244','Kosovo')
        chgcountry('Lao Peoples Democratic Republic','Laos')
        chgcountry('Macau, SAR of China','Macau')
        chgcountry("Netherlands Antilles","Sint Maarten")
        chgcountry('Guernsey','Guernsey and Alderney')
        chgcountry("Korea, Democratic People's Republic of","North Korea")
        chgcountry('Réunion','Reunion')
        chgcountry('Bosnia and Herzegovina','Bosnia')
        
        df['dest'] = df['DESTINATION_COUNTRY']
        def chg_dest(x):
            if x['dest']=='nan' or x['dest']=='Unknown':
                if x['COUNTRY']!='nan' and x['COUNTRY'] != 'Unknown':
                    return x['COUNTRY']
            return x['dest']
               
        df['dest'] = df.apply(chg_dest, axis=1)        
        
        df['source'] = df['DEPARTURE_COUNTRY']
        def chg_source(x):
            if x['source']=='nan' or x['source']=='Unknown':
                if x['PRODUCING_COUNTRY']!='nan' and x['PRODUCING_COUNTRY']!='Unknown':
                    return x['PRODUCING_COUNTRY']
            return x['source']

        
        df['source'] = df.apply(chg_source, axis=1)        

        df = df[df['source'].str.contains('Unknown')==False]
        df = df[df['dest'].str.contains('Unknown')==False]

        g = df.groupby(['source','dest']).sum()[['weight']]
        g = g.reset_index()
        
        m = folium.Map(location=[30, 20], zoom_start=3, tiles="Stamen Terrain")
        for index, row in g.iterrows():
            if row['source']==row['dest']: continue
            if row['source']=='Other' or row['dest']=='Other': continue
            if row['weight'] < 300: continue
            points = [
                [cdict[row['source']]['latitude'],cdict[row['source']]['longitude']],
                [cdict[row['dest']]['latitude'],cdict[row['dest']]['longitude']]
            ]
            ts = row['source']+"-"+row['dest'] + " " + str(int(row['weight']))
            folium.PolyLine(points, color='blue', weight=2.0, tooltip=ts).add_to(m)

        m.save('drugs-out.html')
                            
if __name__ == "__main__": 

    drugs()

    
