import re, json, glob, string, os
from collections import defaultdict
from unidecode import unidecode

WORD = re.compile(r'\w+')

def clean_text(text):
    text = text.replace("\n"," ").replace("\r"," ")
    punc_list = '!"#$%^()*+,-./:;<=>?@[\]^_{|}~' + '0123456789'
    t = str.maketrans(dict.fromkeys(punc_list, " "))
    text = text.translate(t)
    t = str.maketrans(dict.fromkeys("'`",""))
    text = text.translate(t)
    return text

def reg_tokenize(text):
    text = clean_text(text)
    words = WORD.findall(text)
    return words

def index_dir():

    invidx = defaultdict(lambda: defaultdict(int))
    dir = os.getcwd()
    files = glob.glob(dir + "/**/**/*.md")
    files = files + glob.glob(dir + "/**/**/**/*.md")
    files = sorted(files)
    for file in enumerate(files):
        doc = file[1].replace(dir,"")    
        for word in reg_tokenize(open(file[1]).read()):
            word = unidecode(word).lower()
            invidx[word][doc] += 1
        print (doc)

    fout = open("/tmp/invidx.json","w")
    fout.write(json.dumps(invidx))
    fout.close()

    # split the index

    invidx = json.loads(open("/tmp/invidx.json").read())
    invidx_dict = {}

    for c in  string.ascii_lowercase:
        invidx_dict[c] = defaultdict(lambda: defaultdict(int))

    for k,v in invidx.items():
        if len(k)==0: continue
        first_letter = k[0]
        if first_letter in string.ascii_lowercase:
            invidx_dict[first_letter][k] = v

    for k,v in invidx_dict.items():
        fout = open("/tmp/invidx-%s.json" % k,"w")
        fout.write(json.dumps(v))
        fout.close()
        
    print ("""
    
    Index files are now under /tmp. They need to be copied manually to
    $DIR/thirdwave/en or $DIR/codeberg/pages/en
    
    """)

def test1():
    search = "arrival"
    stok = search.split()
    stok_hits = {}
    results = []
    for tok in stok:
        stok_hits[tok] = json.loads(open("/tmp/invidx-%s.json" % tok[0]).read())[tok]
        results.append(set(stok_hits[tok]))

    u = set.intersection(*results)

    hits = []
    for f in u:
        hits.append([f,sum([stok_hits[tok][f] for tok in stok])])
    
    sorted_hits = sorted(range(len(hits)), key=lambda x: hits[x][1], reverse=True)
    for i in range(30):
        print (hits[sorted_hits[i]][0])
    
        
    
if __name__ == "__main__": 

    index_dir()
    #test1()
