"""
Structural break analysis of >2020 WH populatiry
"""
from statsmodels.regression.linear_model import OLS
from statsmodels.formula.api import ols
from numpy.linalg import pinv
import scipy.stats as st
import pandas as pd

def supf(y, x, p):
    N = y.shape[0]
    range = np.floor(np.array([N * p, N * (1 - p)]))
    range = np.arange(range[0], range[1] + 1, dtype=np.int32)
    x = x - np.mean(x)
    y = y - np.mean(y)
    e = OLS(y,x).fit().resid
    S_r = np.sum(e**2)
    k = x.shape[1]
    F_stat = np.zeros(N)
    for t in range:
        X1 = x[:t]
        X2 = x[t:]
        e[:t] = OLS(y[:t],X1).fit().resid
        e[t:] = OLS(y[t:],X2).fit().resid
        R2_u = 1 - e.dot(e) / y.dot(y)
        S_u = np.sum(e**2)
        F_stat[t] = ((S_r - S_u) / k) / (( S_u) / (N-2*k))
    return F_stat.argmax(),F_stat.max()

if __name__ == "__main__": 
 
    url = "https://projects.fivethirtyeight.com/biden-approval-data/approval_topline.csv"
    df = pd.read_csv(url,parse_dates=True,index_col='modeldate')
    df = df.sort_index()
    df = df[df.index < '2021-08-15']
    df['net'] = df['approve_estimate'] - df['disapprove_estimate']

    df['idx'] = range(len(df))
    p = 0.05
    df_x = df[['idx']]
    df_y = df['net']
    idx,val = supf(df_y, df_x, p)
    print (df.index[idx])

