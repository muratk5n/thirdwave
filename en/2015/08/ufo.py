import sys; sys.path.append("../../2019/05")
import pandas as pd, zipfile, random, folium, mygeo

def regular():

      with zipfile.ZipFile('nuforc-ufo.zip', 'r') as z:
            df =  pd.read_csv(z.open('scrubbed.csv'))
      clat,clon=33, 40
      m = folium.Map(location=[clat, clon], zoom_start=4, tiles="Stamen Terrain")
      for index, row in df.iterrows():
          try: 
              year = pd.to_datetime(row['datetime']).year
              if year<2010: continue
              if random.choice(range(12))!=0: continue
              folium.CircleMarker(location=[row['latitude'], row['longitude']],
                                  tooltip=row['comments'],
                                  radius=6,
                                  color='red',
                                  weight=1).add_to(m)        
          except:
              pass
      m.save('ufo-out.html')

def signif():      
      
      dfpop = pd.read_csv('../../2019/05/statepop.csv')

      with zipfile.ZipFile('nuforc-ufo.zip', 'r') as z:
            df =  pd.read_csv(z.open('scrubbed.csv'), parse_dates=True)
      df = df[(df.country == 'us') & (df.datetime > '2010-01-01')]
      df['ST'] = df.state.str.upper()
      ufoc = pd.DataFrame( {'counts': df.groupby('ST').size()  })
      ufoc = ufoc.reset_index()

      df1 = dfpop.merge(ufoc, left_on='state', right_on='ST',how='left')

      from statsmodels.stats.proportion import proportions_ztest

      nobs = [df1.population.sum(), df1.counts.sum()]
      def f(x):
          count = [x.population, x.counts]
          stat, pval = proportions_ztest(count, nobs, alternative='smaller')
          return pval

      df1['pval'] = df1.apply(lambda x: f(x), axis=1)

      df2 = df1[(df1.pval < 1e-20)]
      print (df2.state)

      clat,clon=33, -111
      m = folium.Map(location=[clat, clon], zoom_start=4, tiles="Stamen Terrain")
      for xx in df2.state:
          df4 = df[df.ST == xx]
          cs = df4[['latitude','longitude']].values.tolist()
          mid = mygeo.average(cs)
          folium.Marker(
              [mid[0], mid[1]],
          ).add_to(m)    

      dfn = pd.read_csv('../../2019/05/nuke.csv')
      for index, row in dfn.iterrows():
          folium.CircleMarker(location=[row['latitude'], row['longitude']],
                              radius=6,
                              color='red',
                              weight=1).add_to(m)

      m.save('ufo-sig-out.html')

if __name__ == "__main__": 
      #regular()
      signif()
      
