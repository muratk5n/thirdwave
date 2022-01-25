import pandas as pd

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


if __name__ == "__main__": 

    df = biden_approval()
    print (df.net.tail(10))
