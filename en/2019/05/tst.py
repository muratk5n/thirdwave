#https://www.eia.gov/opendata/v1/qb.php?category=711302

#('coal','TOTAL.CLPRPUS.M')
#('solar','TOTAL.SOTEPUS.M') # million kwh
#('biomass','TOTAL.BMPRBUS.M') # trillion btu


import util
df = util.get_eia("TOTAL.SOTEPUS.M")
print (df)

