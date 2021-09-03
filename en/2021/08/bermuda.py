import pandas as pd

fin = open("MarCas_Part1/vcas.txt")
fout = open("out.csv","w")
for line in fin.readlines():
    tokens = line.split('\t')
    if len(tokens[11])==0: continue
    if len(tokens[4])==0: continue
    if "FNDRNG" not in line: continue
    t9 = ";".join(tokens[9].split(" "))
    t11 = ";".join(tokens[11].split(" "))
    l = "%s;%s;%s;%s;%s\n" % (tokens[4],tokens[8],t9,tokens[10],t11)
    l = l.replace(";;",";")
    fout.write(l)
fout.close()
df = pd.read_csv("out.csv",sep=';',error_bad_lines=False,header=None)
print (df)

