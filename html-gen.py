import markdown, os, sys

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
                    res = markdown.markdown(content, extensions=['fenced_code'])
                    fout = open(path + "/" + fhtml, "w")
                    fout.write(res)
                    fout.close()

                    
gen_html()
