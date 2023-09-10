import datetime, sys, os, re
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
    for year in range(2020,2024):
        os.system("echo '# %d\n' > %d/index.md" % (year,year))
        os.system("python -u gen.py %d >> %d/index.md" % (year,year))
    print ('title done')

if sys.argv[1] == 'new-year':
    for week in range(53):
        os.system("echo '# Week %d\n' > /tmp/2023/week%02d.md" % (week+1,week+1))
        os.system("echo '\n[Week %d](week%02d.html)' >> /tmp/2023/README.md" % (week+1,week+1))
                    
if sys.argv[1] == 'rel':
    seed = int(datetime.datetime.now().strftime("%Y%m%d"))
    random.seed(seed)
    print (random.choice([False, True]))

if sys.argv[1] == 'pdf-unite':
    os.system("pdfunite /opt/Downloads/twpdf/*.pdf ~/Downloads/tw-all.pdf")
        
if sys.argv[1] == 'pdf':
    retpath = os.getcwd()
    files1 = glob.glob("**/**/**/*.md")
    files1 = sorted(files1)
    files2 = glob.glob("**/**/*.md")
    files2 = sorted(files2)
    files = files1 + files2
    files = [f for f in files if "mbl" not in f]
    for i,file in enumerate(files):
        if "index.md" in file: continue
        print (file)
        file2 = file.replace("0119/","")
        f = os.path.basename(file).replace(".md",".pdf")
        dir = os.path.dirname(file)
        res = re.findall("(\d\d\d\d\/\d\d)",file2)[0]
        i = int(res.replace("/",""))
        f = "/opt/Downloads/twpdf/%04d-%s" % (i,f)
        os.chdir(dir)
        cmd = "pandoc %s --latex-engine=xelatex -fmarkdown-implicit_figures -o %s" % (os.path.basename(file),f)
        if not os.path.isfile(f): 
            print (cmd)                
            os.system(cmd)
        os.chdir(retpath)
        
if sys.argv[1] == 'git-change':    
    os.system('git log --since="7 day ago" --name-only --pretty=format: | sort | uniq')
    
