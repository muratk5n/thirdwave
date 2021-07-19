# Codebook 1

Run this first, then you can skip to other parts

```python
import statsmodels.formula.api as smf
import pandas as pd
df = pd.read_csv('../bdm2s2_nation_year_data_may2002.csv')
df = df.sort_index(by=['ccode','year'],ascending=True)
# take out all W,S effects from Polity's 'democracy', the residuals
# are what remains in 'democracy' after W,S is accounted for
resdem = smf.ols('democ ~ W + S', data=df).fit()
df['demres'] = resdem.resid
```

Growth and lagged change in W

If ccode at t-2 is different for current, than delta W for this instance
makes no sense, drop them.

```python
df2 = df.copy()
df2['polchange'] = (df2.W-df2.shift(2).W)**2
df2['DW20'] = df2.W-df2.shift(2).W
df2['dummy'] = df2.ccode-df2.shift(2).ccode
df2 = df2[df2.dummy == 0]
print len(df2)
```

```
19059
```

```python
import statsmodels.formula.api as smf
results = smf.ols('WB_growth ~ W + S + DW20 + polchange + np.log(pop)', data=df2).fit()
print results.summary()
```

```
                            OLS Regression Results                            
==============================================================================
Dep. Variable:              WB_growth   R-squared:                       0.005
Model:                            OLS   Adj. R-squared:                  0.003
Method:                 Least Squares   F-statistic:                     3.315
Date:                Tue, 25 Aug 2015   Prob (F-statistic):            0.00545
Time:                        20:18:07   Log-Likelihood:                -10866.
No. Observations:                3457   AIC:                         2.174e+04
Df Residuals:                    3451   BIC:                         2.178e+04
Df Model:                           5                                         
Covariance Type:            nonrobust                                         
===============================================================================
                  coef    std err          t      P>|t|      [95.0% Conf. Int.]
-------------------------------------------------------------------------------
Intercept       4.6960      0.550      8.532      0.000         3.617     5.775
W               0.3292      0.382      0.861      0.390        -0.421     1.079
S              -0.7225      0.341     -2.121      0.034        -1.390    -0.055
DW20            1.8791      0.646      2.910      0.004         0.613     3.145
polchange      -2.4816      1.047     -2.371      0.018        -4.534    -0.429
np.log(pop)    -0.0261      0.056     -0.468      0.640        -0.136     0.083
==============================================================================
Omnibus:                      408.738   Durbin-Watson:                   1.512
Prob(Omnibus):                  0.000   Jarque-Bera (JB):             4176.816
Skew:                          -0.006   Prob(JB):                         0.00
Kurtosis:                       8.385   Cond. No.                         99.7
==============================================================================
```

```python
%load_ext rpy2.ipython
%R library(lme4)
```

```python
import pandas as pd
df['Klepto'] = (df['TAXGDP']-df['Expenditure']).abs()
df = df[['regyr','ccode','aid_gdp','lrgdpc','pop','year','W','S','Klepto','laglrgdpc']]
```

```python
import statsmodels.formula.api as smf
results = smf.ols('Klepto ~ W + S + aid_gdp + np.log(pop)', data=df).fit()
print results.summary()
```

```
                            OLS Regression Results                            
==============================================================================
Dep. Variable:                 Klepto   R-squared:                       0.205
Model:                            OLS   Adj. R-squared:                  0.202
Method:                 Least Squares   F-statistic:                     65.82
Date:                Mon, 06 Apr 2015   Prob (F-statistic):           1.43e-49
Time:                        20:29:15   Log-Likelihood:                -3297.9
No. Observations:                1027   AIC:                             6606.
Df Residuals:                    1022   BIC:                             6630.
Df Model:                           4                                         
Covariance Type:            nonrobust                                         
===============================================================================
                  coef    std err          t      P>|t|      [95.0% Conf. Int.]
-------------------------------------------------------------------------------
Intercept       4.8089      1.223      3.933      0.000         2.410     7.208
W              -3.9128      0.879     -4.453      0.000        -5.637    -2.189
S               3.9783      0.675      5.892      0.000         2.653     5.303
aid_gdp        39.3581      2.858     13.770      0.000        33.750    44.967
np.log(pop)    -0.1965      0.115     -1.702      0.089        -0.423     0.030
==============================================================================
Omnibus:                      510.462   Durbin-Watson:                   0.657
Prob(Omnibus):                  0.000   Jarque-Bera (JB):             3672.715
Skew:                           2.179   Prob(JB):                         0.00
Kurtosis:                      11.176   Cond. No.                         141.
==============================================================================
```

```python
import statsmodels.formula.api as smf
results = smf.ols('lrgdpc ~ W + S + aid_gdp + np.log(pop) + laglrgdpc', data=df).fit()
print results.summary()
```


```
                            OLS Regression Results                            
==============================================================================
Dep. Variable:                 lrgdpc   R-squared:                       0.993
Model:                            OLS   Adj. R-squared:                  0.993
Method:                 Least Squares   F-statistic:                 7.123e+04
Date:                Mon, 06 Apr 2015   Prob (F-statistic):               0.00
Time:                        22:08:39   Log-Likelihood:                 3221.6
No. Observations:                2541   AIC:                            -6431.
Df Residuals:                    2535   BIC:                            -6396.
Df Model:                           5                                         
Covariance Type:            nonrobust                                         
===============================================================================
                  coef    std err          t      P>|t|      [95.0% Conf. Int.]
-------------------------------------------------------------------------------
Intercept       0.0560      0.020      2.861      0.004         0.018     0.094
W               0.0262      0.007      3.992      0.000         0.013     0.039
S              -0.0086      0.004     -1.916      0.055        -0.017     0.000
aid_gdp        -0.0706      0.021     -3.339      0.001        -0.112    -0.029
np.log(pop)    -0.0012      0.001     -1.323      0.186        -0.003     0.001
laglrgdpc       0.9954      0.002    482.672      0.000         0.991     0.999
==============================================================================
Omnibus:                      476.268   Durbin-Watson:                   1.702
Prob(Omnibus):                  0.000   Jarque-Bera (JB):             4091.930
Skew:                          -0.635   Prob(JB):                         0.00
Kurtosis:                       9.086   Cond. No.                         221.
==============================================================================

```


```python
%R -i df
%R resp_lmer <- lmer(Klepto ~ W + S + log(pop) + aid_gdp + ( 1 | regyr), data = df)
%R -o res res = summary(resp_lmer)
print res
```

```
Linear mixed model fit by REML ['lmerMod']
Formula: Klepto ~ W + S + log(pop) + aid_gdp + (1 | regyr)
   Data: df

REML criterion at convergence: 6569.8

Scaled residuals: 
    Min      1Q  Median      3Q     Max 
-1.9820 -0.6057 -0.1908  0.3338  7.5056 

Random effects:
 Groups   Name        Variance Std.Dev.
 regyr    (Intercept)  5.245   2.290   
 Residual             32.296   5.683   
Number of obs: 1027, groups:  regyr, 122

Fixed effects:
            Estimate Std. Error t value
(Intercept)   6.1930     1.2722   4.868
W            -4.0960     0.8626  -4.748
S             3.5409     0.6541   5.414
log(pop)     -0.2682     0.1175  -2.284
aid_gdp      42.9981     2.9760  14.448

Correlation of Fixed Effects:
         (Intr) W      S      lg(pp)
W        -0.256                     
S        -0.171 -0.651              
log(pop) -0.903  0.195 -0.033       
aid_gdp  -0.417  0.071  0.043  0.329

```

```python
%R -i df
%R resp_lmer <- lmer(lrgdpc ~ W + S + log(pop) + aid_gdp + laglrgdpc + ( 1 | regyr), data = df)
%R -o res res = summary(resp_lmer)
print res
```

```
Linear mixed model fit by REML ['lmerMod']
Formula: lrgdpc ~ W + S + log(pop) + aid_gdp + laglrgdpc + (1 | regyr)
   Data: df

REML criterion at convergence: -6453.3

Scaled residuals: 
    Min      1Q  Median      3Q     Max 
-9.6023 -0.4385  0.0367  0.5086  4.5498 

Random effects:
 Groups   Name        Variance  Std.Dev.
 regyr    (Intercept) 0.0003723 0.01930 
 Residual             0.0042945 0.06553 
Number of obs: 2541, groups:  regyr, 217

Fixed effects:
              Estimate Std. Error t value
(Intercept)  0.0593032  0.0229343     2.6
W            0.0184700  0.0065761     2.8
S           -0.0042964  0.0043957    -1.0
log(pop)    -0.0017439  0.0009528    -1.8
aid_gdp     -0.0347754  0.0226003    -1.5
laglrgdpc    0.9957743  0.0023887   416.9

Correlation of Fixed Effects:
          (Intr) W      S      lg(pp) ad_gdp
W          0.152                            
S         -0.138 -0.644                     
log(pop)  -0.678  0.086 -0.044              
aid_gdp   -0.580 -0.058  0.044  0.453       
laglrgdpc -0.918 -0.296  0.122  0.370  0.472

```

Construction

```python
import statsmodels.formula.api as smf
results = smf.ols('build ~ W + np.log(pop) + rgdpch + demres', data=df).fit()
print results.summary()
```

```
                            OLS Regression Results                            
==============================================================================
Dep. Variable:                  build   R-squared:                       0.047
Model:                            OLS   Adj. R-squared:                  0.045
Method:                 Least Squares   F-statistic:                     19.00
Date:                Thu, 03 Sep 2015   Prob (F-statistic):           2.91e-15
Time:                        09:54:14   Log-Likelihood:                -7501.5
No. Observations:                1534   AIC:                         1.501e+04
Df Residuals:                    1529   BIC:                         1.504e+04
Df Model:                           4                                         
Covariance Type:            nonrobust                                         
===============================================================================
                  coef    std err          t      P>|t|      [95.0% Conf. Int.]
-------------------------------------------------------------------------------
Intercept     109.3877      5.666     19.306      0.000        98.274   120.502
W             -10.4276      3.533     -2.952      0.003       -17.357    -3.498
np.log(pop)     0.8733      0.552      1.583      0.114        -0.209     1.956
rgdpch          0.0018      0.000      7.663      0.000         0.001     0.002
demres         -0.1573      0.084     -1.880      0.060        -0.321     0.007
==============================================================================
Omnibus:                      444.538   Durbin-Watson:                   0.092
Prob(Omnibus):                  0.000   Jarque-Bera (JB):             1421.627
Skew:                           1.436   Prob(JB):                    1.98e-309
Kurtosis:                       6.741   Cond. No.                     5.21e+04
==============================================================================
```


