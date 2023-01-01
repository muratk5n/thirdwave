import datetime, sys, os, re, urllib.request
import datetime, random, glob

if len(sys.argv) < 2:
    print ("options: years")
    exit()  

if sys.argv[1] == 'years':
    for year in range(2005,2022):
        d = os.getcwd() + "/" + str(year)
        if os.path.exists(d):
            os.system("echo '# %d\n' > %d/README.md" % (year,year))
            os.system("python -u gen.py %d >> %d/README.md" % (year,year))

if sys.argv[1] == 'pdf-unite':
    os.system("pdfunite /opt/Downloads/udgpdf/*.pdf ~/Downloads/udg-all.pdf")
        
if sys.argv[1] == 'pdf':
    retpath = os.getcwd()
    files = glob.glob("**/**/*.md")
    files = sorted(files)
    files = [f for f in files if "tweets" not in f]
    for i,file in enumerate(files):
        f = os.path.basename(file).replace(".md",".pdf")
        dir = os.path.dirname(file)
        res = re.findall("(\d\d\d\d\/\d\d)",file)[0]
        i = int(res.replace("/",""))
        f = "/opt/Downloads/udgpdf/%04d-%s" % (i,f)
        os.chdir(dir)
        cmd = "pandoc %s --latex-engine=xelatex -fmarkdown-implicit_figures -o %s" % (os.path.basename(file),f)
        if not os.path.isfile(f): 
            print (cmd)                
            os.system(cmd)
        os.chdir(retpath)
    
            
