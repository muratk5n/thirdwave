'''
Scrapes Yahoo Finance and gets the information listed below.
'''
from yahoo_fin.stock_info import get_income_statement, get_earnings_history, get_quote_table
from bs4 import BeautifulSoup
from bs4.element import Comment
import re, requests, pandas as pd

headers = { 'User-Agent': 'UCWEB/2.0 (compatible; Googlebot/2.1; +google.com/bot.html)'}

ksurl = "https://finance.yahoo.com/quote/%s/key-statistics?p=%s"
cfurl = "https://finance.yahoo.com/quote/%s/cash-flow?p=%s"
isurl = "https://finance.yahoo.com/quote/%s/financials?p=%s"

labels_cf = ['Operating Cash Flow','Investing Cash Flow','Financing Cash Flow',
             'Capital Expenditure','Issuance of Debt','Free Cash Flow']

labels_is = ['Total Revenue','Pretax Income']

labels_ks = ['Market Cap \(intraday\)','Enterprise Value','Trailing P/E',
             'Forward P/E','PEG Ratio \(5 yr expected\)','Price/Sales  \(ttm\)',
             'Price/Book  \(mrq\)','Enterprise Value/Revenue','Enterprise Value/EBITDA',
             'Profit Margin','Operating Margin  \(ttm\)','Return on Assets  \(ttm\)',
             'Return on Equity  \(ttm\)','Revenue  \(ttm\)','Revenue Per Share  \(ttm\)',
             'Quarterly Revenue Growth  \(yoy\)','Gross Profit  \(ttm\)','EBITDA',
             'Net Income Avi to Common  \(ttm\)','Diluted EPS  \(ttm\)',
             'Quarterly Earnings Growth  \(yoy\)', 'Total Cash  \(mrq\)','Total Cash Per Share  \(mrq\)',
             'Total Debt  \(mrq\)','Total Debt/Equity  \(mrq\)','Current Ratio  \(mrq\)',
             'Book Value Per Share  \(mrq\)','Operating Cash Flow  \(ttm\)','Levered Free Cash Flow  \(ttm\)',
             'Beta \(5Y Monthly\)','52-Week Change','P500 52-Week Change','52 Week High','52 Week Low','50-Day Moving Average',
             '200-Day Moving Average','Avg Vol \(3 month\)','Avg Vol \(10 day\)','Shares Outstanding','Implied Shares Outstanding',
             'Float','% Held by Insiders','% Held by Institutions','Shares Short \(... \d\d, \d\d\d\d\)',
             'Short Ratio \(... \d\d, \d\d\d\d\)','Short % of Float \(... \d\d, \d\d\d\d\)',
             'Short % of Shares Outstanding \(... \d\d, \d\d\d\d\)','Forward Annual Dividend Rate',
             'Forward Annual Dividend Yield','Trailing Annual Dividend Rate','Trailing Annual Dividend Yield',
             'Year Average Dividend Yield','Payout Ratio','Last Split Factor']


def tag_visible(element):
    if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
        return False
    if isinstance(element, Comment):
        return False
    return True

def text_from_html(body):
    soup = BeautifulSoup(body, 'html.parser')
    texts = soup.findAll(text=True)
    visible_texts = filter(tag_visible, texts)  
    return u" ".join(t.strip() for t in visible_texts)


def get_keystats(ticker):
    furl = ksurl % (ticker,ticker) 
    resp = requests.get(furl, headers=headers, timeout=2)
    s = text_from_html(resp.text)

    s = s.replace(" 1 ", "")
    s = s.replace(" 2 ", "")
    s = s.replace(" 3 ", "")
    s = s.replace(" 4 ", "")
    s = s.replace(" 5 ", "")
    s = s.replace(" 6 ", "")
    s = s.replace(" 7 ", "")
    
    labels_ks_dict = dict((k,"") for k in labels_ks)

    for k in labels_ks_dict:
        regex = k + "\s*(.*?)\s"
        res = re.findall(regex,s)
        labels_ks_dict[k] = res[0]

    labels_ks_dict = dict((k.replace("\\(","("),labels_ks_dict[k]) for k in labels_ks_dict)
    labels_ks_dict = dict((k.replace("\\)",")"),labels_ks_dict[k]) for k in labels_ks_dict)
    labels_dict2 = {}
    for k in labels_ks_dict:
        if "Shares Short" in k: labels_dict2["Shares Short"] = labels_ks_dict[k]
        elif "Short Ratio" in k: labels_dict2["Short Ratio"] = labels_ks_dict[k]
        else:
            labels_dict2[k] = labels_ks_dict[k]
    
    return labels_dict2

def get_cashflow(ticker):
    furl = cfurl % (ticker,ticker)
    resp = requests.get(furl, headers=headers, timeout=2)
    s = text_from_html(resp.text)
    labels_cf_dict = dict((k,"") for k in labels_cf)

    for k in labels_cf_dict:
        regex = k + "\s*(.*?)\s(.*?)\s(.*?)\s"
        res = re.findall(regex,s)
        labels_cf_dict[k] = res[0]

    return labels_cf_dict

def get_financials(ticker):
    ks = get_keystats(ticker)
    cf = get_cashflow(ticker)
    res = {**ks, **cf}
    return res

def get_income(ticker):
    res = get_income_statement(ticker,yearly=False).T
    df = res.sort_index()
    df = df / 1e6
    df['grossProfitMargin'] = df.grossProfit / df.totalRevenue * 100.0
    return (df)

def get_earnings(ticker):
    res =  get_earnings_history(ticker)
    df = pd.DataFrame.from_dict(res)
    return df

def fetch_quote_table(ticker):
    res = get_quote_table(ticker)
    return res
    
def get_disp(ticker, atts):
    q = get_financials(ticker)
    print (ticker, [(a + ': ' + str(q[a])) for a in atts])

if __name__ == "__main__": 
    
    res = get_financials("AMZN")
    print (res)
    atts = ["Revenue  (ttm)", "Capital Expenditure"] 
    q = get_disp("SHOP", atts)

    res = get_income("DIS")
    
