import datetime, sys, os

if len(sys.argv) < 2:
    print ("options: years")
    exit()  

if sys.argv[1] == 'years':
    for year in range(2005,2022):
        d = os.getcwd() + "/" + str(year)
        if os.path.exists(d):
            os.system("echo '# %d\n' > %d/README.md" % (year,year))
            os.system("python -u gen.py %d >> %d/README.md" % (year,year))
