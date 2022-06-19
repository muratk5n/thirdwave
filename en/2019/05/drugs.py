import pandas as pd

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

    
