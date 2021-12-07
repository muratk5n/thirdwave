import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from scipy.optimize import minimize
import pandas as pd
from scipy.stats import gamma


def get_data_combined():
    """
    Code from https://towardsdatascience.com/covid-19-data-processing-58aaa3663f6
    """
    confirmed_df  = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv')
    deaths_df     = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv')
    recovered_df = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv')

    dates = confirmed_df.columns[4:]
    confirmed_df_long = confirmed_df.melt(
        id_vars=['Province/State', 'Country/Region', 'Lat', 'Long'], 
        value_vars=dates, 
        var_name='Date', 
        value_name='Confirmed'
    )
    deaths_df_long = deaths_df.melt(
        id_vars=['Province/State', 'Country/Region', 'Lat', 'Long'], 
        value_vars=dates, 
        var_name='Date', 
        value_name='Deaths'
    )
    recovered_df_long = recovered_df.melt(
        id_vars=['Province/State', 'Country/Region', 'Lat', 'Long'], 
        value_vars=dates, 
        var_name='Date', 
        value_name='Recovered'
    )

    recovered_df_long = recovered_df_long[recovered_df_long['Country/Region']!='Canada']
    full_table = confirmed_df_long.merge(
      right=deaths_df_long, 
      how='left',
      on=['Province/State', 'Country/Region', 'Date', 'Lat', 'Long']
    )

    full_table = full_table.merge(
      right=recovered_df_long, 
      how='left',
      on=['Province/State', 'Country/Region', 'Date', 'Lat', 'Long']
    )

    full_table['Date'] = pd.to_datetime(full_table['Date'])
    full_table['Recovered'] = full_table['Recovered'].fillna(0)
    ship_rows = full_table['Province/State'].str.contains('Grand Princess') | full_table['Province/State'].str.contains('Diamond Princess') | full_table['Country/Region'].str.contains('Diamond Princess') | full_table['Country/Region'].str.contains('MS Zaandam')
    full_table = full_table[~(ship_rows)]
    ship_rows = full_table['Province/State'].str.contains('Grand Princess') | full_table['Province/State'].str.contains('Diamond Princess') | full_table['Country/Region'].str.contains('Diamond Princess') | full_table['Country/Region'].str.contains('MS Zaandam')
    full_ship = full_table[ship_rows]
    full_table = full_table[~(ship_rows)]
    full_grouped = full_table.groupby(['Date', 'Country/Region'])['Confirmed', 'Deaths', 'Recovered'].sum().reset_index()
    temp = full_grouped.groupby(['Country/Region', 'Date', ])['Confirmed', 'Deaths', 'Recovered']
    temp = temp.sum().diff().reset_index()
    mask = temp['Country/Region'] != temp['Country/Region'].shift(1)
    temp.loc[mask, 'Confirmed'] = np.nan
    temp.loc[mask, 'Deaths'] = np.nan
    temp.loc[mask, 'Recovered'] = np.nan
    temp.columns = ['Country/Region', 'Date', 'New cases', 'New deaths', 'New recovered']
    full_grouped = pd.merge(full_grouped, temp, on=['Country/Region', 'Date'])
    full_grouped = full_grouped.fillna(0)
    cols = ['New cases', 'New deaths', 'New recovered']
    full_grouped[cols] = full_grouped[cols].astype('int')
    full_grouped['New cases'] = full_grouped['New cases'].apply(lambda x: 0 if x<0 else x)
    full_grouped = full_grouped.set_index("Date")
    return full_grouped

def mortality_rate():

    covid_confirmed = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv')
    covid_deaths = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv')
    covid_recovered = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv')

    covid_worldwide_confirmed = covid_confirmed.iloc[:, 4:].sum(axis=0)
    covid_worldwide_deaths = covid_deaths.iloc[:, 4:].sum(axis=0)
    covid_worldwide_recovered = covid_recovered.iloc[:, 4:].sum(axis=0)
    covid_worldwide_active = covid_worldwide_confirmed - covid_worldwide_deaths - covid_worldwide_recovered

    world_rate_df = pd.DataFrame({
        'confirmed': covid_worldwide_confirmed,
        'deaths': covid_worldwide_deaths,
        'recovered': covid_worldwide_recovered,
        'active': covid_worldwide_active
    }, index=covid_worldwide_confirmed.index)

    world_rate_df['recovered / 100 confirmed'] = world_rate_df['recovered'] / world_rate_df['confirmed'] * 100

    world_rate_df['deaths / 100 confirmed'] = world_rate_df['deaths'] / world_rate_df['confirmed'] * 100

    world_rate_df['date'] = world_rate_df.index

    print (world_rate_df['deaths / 100 confirmed'].tail(4))
    return world_rate_df

def si_distr(N, si_mean, si_sd):
    """ serial interval distribution
    input:
      N = number of data points
      si_mean = mean of serial interval
      si_sd = standard deviation of serial interval
    return:
      w = gamma distribution for serial interval
          discretized with triangular window function
      w[i] = probability of reproduction on i-th day
             (i=0,1,...,N-1); w[0]=0
    reference:
      A. Cori et al
        American Journal of Epidemiology 178 (2013) 1505
          Web Appendix 11
    """
    a = ((si_mean-1)/si_sd)**2
    b = (si_mean-1)/a
    k = np.arange(-2,N)
    return np.diff(k*gamma.cdf(k,a,0,b)
                   - a*b*gamma.cdf(k,a+1,0,b), 2)

def Reff(data, si_mean, si_sd,
         tau=7, conf=0.95, mu=5):
    """ effective reproduction number
    assuming exponential distribution for prior Reff
    input:
      data = daily number of incidence
      si_mean = mean of serial interval
      si_sd = standard deviation of serial interval
      tau = length of time window (integer in days)
      conf = confidence level of estimated Reff
      mu = mean of prior ditribution of Reff
    return:
      R = daily Reff of shape (3,len(data))
      R[0:3] = median, min, max
    reference:
      A. Cori et al
        American Journal of Epidemiology 178 (2013) 1505
          Web Appendix 1
    """
    N = len(data)
    w = si_distr(N, si_mean, si_sd)
    L = np.convolve(data, w)[:N]
    u = np.ones(tau)
    a = 1 + np.convolve(data,u)[:N]
    b = mu/(1 + mu*np.convolve(L,u)[:N])
    return np.vstack([gamma.median(a,0,b),
                      gamma.interval(conf,a,0,b)])
