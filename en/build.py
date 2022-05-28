import datetime, sys, os, re, urllib.request
import datetime, random

if len(sys.argv) < 2:
    print ("options: week | years")
    exit()  
    
if sys.argv[1] == 'week':
    my_date = datetime.date.today() # if date is 01/01/2018
    #my_date = datetime.datetime.strptime('2022-3-22', "%Y-%m-%d")
    year, week_num, day_of_week = my_date.isocalendar()
    print (my_date)
    print("Week #" + str(week_num) + " of year " + str(year))

if sys.argv[1] == 'years':
    for year in range(2008,2023):
        os.system("echo '# %d\n' > %d/README.md" % (year,year))
        os.system("python -u gen.py %d >> %d/README.md" % (year,year))

if sys.argv[1] == 'release':
    seed = int(datetime.datetime.now().strftime("%Y%m%d"))
    random.seed(seed)
    print (random.choice([False,True]))
    
if sys.argv[1] == 'twimg':
    # python -u build.py twimg tweets/2022/week01.md
    fin = sys.argv[2]
    content = open(fin).read()
    print (fin)
    res = re.findall('https://pbs.twimg.com(.*?)["\)]',content)
    for x in res:
        url = "https://pbs.twimg.com" + x
        print (url)
        urllib.request.urlretrieve(url, "out.png")
        break
