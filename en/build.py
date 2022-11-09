import datetime, sys, os, re, urllib.request
import datetime, random, glob

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

if sys.argv[1] == 'rel':
    seed = int(datetime.datetime.now().strftime("%Y%m%d"))
    random.seed(seed)
    print (random.choice([False, True]))

if sys.argv[1] == 'pdf':
    retpath = os.getcwd()
    files = glob.glob("**/**/*.md")
    files = sorted(files)
    files = [f for f in files if "tweets" not in f]
    for i,file in enumerate(files):        
        f = os.path.basename(file).replace(".md",".pdf")
        dir = os.path.dirname(file)
        f = "/tmp/tw/%04d-%s" % (i,f)
        os.chdir(dir)
        cmd = "pandoc %s -fmarkdown-implicit_figures -o %s" % (os.path.basename(file), f)
        if not os.path.isfile(f): 
            print (cmd)                
            os.system(cmd)
        os.chdir(retpath)
    
if sys.argv[1] == 'twimg':
    # python -u build.py twimg tweets/2022/week39.md
    content = open(sys.argv[2]).read()
    res = re.findall('https://pbs.twimg.com(.*?)["\)]',content)
    for x in res:
        print ('--------------------------------------')
        print (x)
        fres = re.findall('format=(\w*)\&',x)
        print (fres[0])
        nres = re.findall('media\/(.*?)\?format',x)
        print (nres[0])
        url = "https://pbs.twimg.com" + x
        fout = nres[0] + "." + fres[0]
        urllib.request.urlretrieve(url, "/tmp/twimg/" + fout)
        content = content.replace(url,"twimg/" + fout)        
    fout = open("/tmp/" + os.path.basename(sys.argv[2]),"w")
    fout.write(content)
    fout.close()
    
