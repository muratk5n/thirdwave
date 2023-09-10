import sys, glob, os, shutil, re, argparse
import markdown, os, sys

def deleteDir(path):
    mswindows = (sys.platform == "win32")
    if mswindows: 
        cmd = "RMDIR "+ path +" /s /q"
    else:
        cmd = "rm -rf "+path
    result = getstatusoutput(cmd)
    if(result[0]!=0):
        raise RuntimeError(result[1])

def deleteFile(path):
    print (path)
    mswindows = (sys.platform == "win32")
    if mswindows: 
        cmd = 'DEL /F /S /Q "%s"' % path
    else:
        cmd = 'rm -rf "' + path + '"'
    result = getstatusoutput(cmd)
    if(result[0]!=0):
        raise RuntimeError(result[1])

def getstatusoutput(cmd):
    pipe = os.popen(cmd + ' 2>&1', 'r')
    text = pipe.read()
    sts = pipe.close()
    if sts is None: sts = 0
    if text[-1:] == '\n': text = text[:-1]
    return sts, text
        
def ls(d,ignore_list=[]):
    print ('ls ignore lst', ignore_list)
    dirs = []; files = []
    for root, directories, filenames in os.walk(d):
        for directory in directories:
            path = os.path.join(root, directory)
            do_add = True
            for ignore in ignore_list:
                if ignore in path:
                    print ('ignoring', path); do_add = False
            if do_add: dirs.append(path)
        for filename in filenames: 
            path = os.path.join(root,filename)
            do_add = True
            for ignore in ignore_list:
                if ignore in path: do_add = False
            if do_add: files.append((path, os.path.getsize(path)))
    return dirs, files

def purge(dir, pattern, inclusive=True):
    regexObj = re.compile(pattern)
    for root, dirs, files in os.walk(dir, topdown=False):
        for name in files:
            path = os.path.join(root, name)
            if bool(regexObj.search(path)) == bool(inclusive):
                os.remove(path)
                
def copy_files_and_dirs(fr,to,ignore_list):
    if ignore_list == None:
        ignore_list = []
    else:
        ignore_list = ignore_list.split(',')
    frdirs,frfiles =  ls(fr,ignore_list)
    todirs,tofiles = ls(to)

    tofilesdict = dict(tofiles)
    print ('create dirs')
    todirs_tmp = dict([(x.replace(fr,to),0) for x in todirs])
    diff = [x for x in frdirs if x.replace(fr,to) not in todirs_tmp]
    for x in diff:
        x=x.replace(fr,to)
        if os.path.exists(x) == False:            
            os.mkdir(x)

    print ('a files not in b')
    for (x,size) in frfiles:
        x_to=x.replace(fr,to)
        if x_to in tofilesdict and tofilesdict[x_to] != size: 
            print ('copying %s %s' % (x,x_to))
            shutil.copy(x,x_to)
        elif x_to not in tofilesdict: 
            print ('copying %s %s' % (x,x_to))
            shutil.copy(x,x_to)
            
    return frdirs, todirs

def del_not_in_from(fr, to, frdirs, todirs):
    print ('b files not in a')
    frdirs_tmp = dict([(x.replace(to,fr),0) for x in frdirs])
    diff = [x for x in todirs if x.replace(to,fr) not in frdirs_tmp]    
    for x in diff:
        print ('deleting directory %s' % x)
        if os.path.isdir(x): deleteDir("'%s'" % x)

    frdirs,frfiles =  ls(fr)
    todirs,tofiles = ls(to)
    frfilesdict = dict(frfiles)
    
    for (x,size) in tofiles:
        x_fr=x.replace(to,fr)
        if x_fr not in frfilesdict:
            print ('deleting %s' % x)
            deleteFile(x)

def ls(d,ignore_list=[]):
    print ('ls ignore lst', ignore_list)
    dirs = []; files = []
    for root, directories, filenames in os.walk(d):
        for directory in directories:
            path = os.path.join(root, directory)
            do_add = True
            for ignore in ignore_list:
                if ignore in path:
                    print ('ignoring', path); do_add = False
            if do_add: dirs.append(path)
        for filename in filenames: 
            path = os.path.join(root,filename)
            do_add = True
            for ignore in ignore_list:
                if ignore in path: do_add = False
            if do_add: files.append((path, os.path.getsize(path)))
    return dirs, files


head = """
<html>
  <head>
      <meta charset='utf-8'>
      <link rel="stylesheet" type="text/css" href="../css/jekyll.css" media="screen" />
      <meta http-equiv="X-UA-Compatible" content="IE=edge">
      <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
      <script type="text/x-mathjax-config">MathJax.Hub.Config({  tex2jax: {inlineMath: [["$","$"]  ]}});</script>
      <script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/MathJax.js?config=TeX-AMS_HTML-full">
      </script>
      <link rel="stylesheet" type="text/css" media="screen" href="https://muratk5n.codeberg.page/css/jekyll.css">
      <title>thirdwave</title>
      <link rel="canonical" href="https://muratk5n.codeberg.page/en/" />
    </head>        
    <body>
      <div id="header_wrap" class="outer">
        <header class="inner">
          <h1 id="project_title">
            <a href="https://muratk5n.codeberg.page/en" style="text-decoration:none; color:inherit;">thirdwave</a>
          </h1>
          <font color="gray" size="2">Codeberg Main</font>
          <h2 id="project_tagline"></h2>          
        </header>
      </div>
      <div id="main_content_wrap" class="outer">        
        <section id="main_content" class="inner">
"""

bottom = """
        </section>          
      </div>
    </body>
</html>
"""

def gen_html():
    dirs, files = ls(os.getcwd())
    for (f,size) in files:
        if ".md" in f:
            path = os.path.dirname(f)
            fmd = os.path.basename(f)
            fhtml = os.path.basename(f).replace(".md",".html")
            update = True
            if os.path.isfile(path + "/" + fhtml):
                mdtime = os.path.getmtime(path + "/" + fmd)
                htmltime = os.path.getmtime(path + "/" + fhtml)
                if htmltime > mdtime: update = False
            if update:
                print ('Generating html for', f)
                content = open(path + "/" + fmd).read()
                res = head
                html = markdown.markdown(content, extensions=['fenced_code'])
                html = html.replace("}<em>{","}_{")
                html = html.replace("}</em>{","}_{")
                res += html
                res += bottom
                fout = open(path + "/" + fhtml, "w")
                fout.write(res)
                fout.close()

def clean_html(to):
    d = to + "/en"
    deleteDir(d)
    d = to + "/tr"
    deleteDir(d)


if __name__ == "__main__":
        
    fr = os.getcwd()
    to = os.environ['HOME'] + "/Documents/repos/codeberg/pages"

    if sys.argv[1] == 'html': 
        frdirs, todirs = copy_files_and_dirs(fr, to, ".git,.key,_layouts,_config.yml")
        os.chdir(to)
        gen_html()

    if sys.argv[1] == 'clean': 
        clean_html(to)

    if sys.argv[1] == 'tw':
        fr = os.environ['HOME'] + "/Documents/tw"
        to = os.environ['HOME'] + "/Documents/thirdwave"
        frdirs, todirs = copy_files_and_dirs(fr, to, ".git")
        
