for i in range(52):
    w = "week%02d.md" % (i+1)
    print (w)
    fout = open (w, "w")
    fout.write ("# Week %d \n\n" % (i+1))
    fout.close()
    
