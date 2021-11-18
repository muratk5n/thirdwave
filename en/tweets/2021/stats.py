"""
Structural break analysis 
"""
from statsmodels.regression.linear_model import OLS
from statsmodels.formula.api import ols
from numpy.linalg import pinv
import scipy.stats as st
import numpy as np

def struct_break_test_pt(y, x, t):
    x1 = x[:t]
    x2 = x[t:]
    res1 = OLS(y[:t],x1).fit()
    res2 = OLS(y[t:],x2).fit()
    res_r = OLS(y,x).fit()
    S_1 = np.sum(res1.resid**2)
    S_2 = np.sum(res2.resid**2)
    S_r = np.sum(res_r.resid**2)
    k = x.shape[1] 
    tmp1 = (S_r-(S_1+S_2))/k
    tmp2 = (S_1+S_2)/(len(x)-2*k-1)
    F = tmp1/tmp2
    f = st.f(k,len(x)-2*k-1)
    pval = 1-f.cdf(F)    
    return F,pval

def structural_break_find(y, x, p):
    N = len(x)
    F_stat = np.zeros(N)
    for t in range(2,N):
        print (t)
        F,pval = struct_break_test_pt(y, x, t)
        if pval < p: F_stat[t] = F        
    return F_stat.argmax(),F_stat.max()
    

def popularity_2021_pre_aug():

    import pandas as pd
    url = "https://projects.fivethirtyeight.com/biden-approval-data/approval_topline.csv"
    df = pd.read_csv(url,parse_dates=True,index_col='modeldate')
    df = df.sort_index()
    df = df[df.index < '2021-08-15']
    df['net'] = df['approve_estimate'] - df['disapprove_estimate']

    p = 0.05
    df['idx'] = range(len(df))
    df_x = df[['idx']]; df_y = df['net']
    i,v = structural_break_find(df_y, df_x, p)
    print (df.index[i])

if __name__ == "__main__": 
 
    popularity_2021_pre_aug()
