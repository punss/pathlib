""" run on console to get url list
var urls = document.getElementsByTagName('a');

for (url in urls) {
    console.log ( urls[url].href );
}"""



from bs4 import BeautifulSoup
import requests
import os
import glob
from pathlib import Path

z=Path()
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def findtxt(word):

    st="wordlists"
    for i in os.listdir("./"+st):
        tempvar=Path(str(z.resolve())+"/wordlists").joinpath(str(i))
        #print(tempvar)
        q=Path(tempvar)
        r=Path(str(z.resolve())+"/lis.txt")
        t=r.open("a")
        with q.open("r", encoding="ascii", errors='ignore') as u:
            worl=u.readlines()
            worl=list(map(str.rstrip, worl))
        if word in worl:
            print(str(word)+" found")
            t.write(word+': ')
            t.write(i[3:i.index('_wordlist')])
            return
    else:
        print(str(word)+ " not found")
        t.write(str(word)+ " not found\n")
        u.close()

def wrdlist(x):
    url=("http://video.google.com/timedtext?lang=en&v=%s" % (x))
    headers={'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'}
    response=requests.get(url,headers=headers)
    soup=BeautifulSoup(response.text,'lxml')

    g=Path(str(z.resolve())+"/IDs/ID:%s.txt" % x)
    f=g.open("w+")
    f.write(soup.get_text())
    f.close()
    l=[]
    m=[]
    with g.open("r") as f:
        for words in f:
            for word in words.split():
                if word.lower() not in l:
                    l.append(word.lower())

        for i in l:
            i=i.replace("&#39;","'")
            i=i.replace("&quot;","")
            i=i.replace("&gt;","")
            i=i.replace(",","")
            i=i.replace(".","\n")
            i=i.replace("?","")
            i=i.replace("!","")
            m.append(i)
        
        n=Path(str(z.resolve())+"/wordlists/ID:%s_wordlist.txt" % x)
        f=n.open("w+")
        for i in m:
            f.write(i)
            f.write("\n")
        f.close()

g=int(input("How many videos do you want to convert to word lists?: "))
j=Path(str(z.resolve())+"/pewds.txt")
d=Path(str(z.resolve())+"/lis.txt")
f=j.open("r")
c=0
t=d.open("w")
t.close()
if not os.path.exists('./wordlists'):
    os.mkdir('./wordlists')
else:
    pass
if not os.path.exists('./IDs'):
    os.mkdir('./IDs')
else:
    pass

while (c!=g):
    temp_=f.readline()
    wrdlist(temp_)
    c+=1
    cls()
    print(str(c)+" of " + str(g) +" videos converted into word lists.")
cls()
print(str(c)+" videos converted into word lists.")

ans=input("Do you want to look for the files that match the lyrics now?: ")

if (ans=="y" or ans=="Y"):
    lyr=list(map(str,input("Enter the text: ").split(" ")))
    for word in lyr:
        findtxt(word)
else:
    exit(0)