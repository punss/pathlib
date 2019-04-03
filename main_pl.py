""" run on console to get url list
var urls = document.getElementsByTagName('a');

for (url in urls) {
    console.log ( urls[url].href );
}"""


from bs4 import BeautifulSoup
import requests
import os
from pathlib import Path

z = Path()
"""z = z.resolve()
Z_STRING = str(z)
g = Path(Z_STRING)"""
g = Path(str(z.resolve))


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


def find_text(word):

    v = g / "wordlists"
    for i in v.iterdir():
        path_of_file = v / (str(i))
        q = Path(path_of_file)
        r = g / "lis.txt"
        t = r.open("a")
        with q.open("r", encoding="ascii", errors='ignore') as u:
            WORD_LIST = u.readlines()
            WORD_LIST = list(map(str.rstrip, WORD_LIST))
        if word in WORD_LIST:
            print(str(word)+" found")
            t.write(word+': ')
            t.write(str(i)[len(str(v))+1:str(i).index('_wordlist')])
            t.write("\n")
            return
    else:
        print(str(word) + " not found")
        t.write(str(word) + " not found\n")
        u.close()


def word_list(x):
    url = ("http://video.google.com/timedtext?lang=en&v=%s" % (x))
    HEADERS = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) '
        'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110'
        'Safari/537.36'
        }
    response = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(response.text, 'lxml')

    g1 = g / "IDs" / ("ID_%s.txt" % x)
    with g1.open("w+") as f:
        f.write(soup.get_text())
        f.close()
    l = []
    m = []
    with g1.open("r") as f:
        for words in f:
            for word in words.split():
                if word.lower() not in l:
                    l.append(word.lower())

        for i in l:
            i = i.replace("&#39;", "'")
            i = i.replace("&quot;", "")
            i = i.replace("&gt;", "")
            i = i.replace(",", "")
            i = i.replace(".", "\n")
            i = i.replace("?", "")
            i = i.replace("!", "")
            m.append(i)
        n = g / "wordlists" / ("ID:%s_wordlist.txt" % x)
        with n.open("w+") as f:
            for i in m:
                f.write(i)
                f.write("\n")
            f.close()


NUM_OF_VID = int(input(
    "How many videos do you want to convert to word lists?: "
    ))
j = g / "pewds.txt"
d = g / "lis.txt"
f = j.open("r")
COUNT = 0
with d.open("w") as t:
    t.close()
if not Path.exists(g / "wordlists"):
    y = g / "wordlists"
    y.mkdir()
    # "wordlists/"
else:
    pass
if not Path.exists(g / "IDs"):
    x = g / "IDs"
    x.mkdir()
    # '/IDs'
else:
    pass

while (COUNT != NUM_OF_VID):
    word_in_line = f.readline()
    word_list(word_in_line.rstrip())
    COUNT += 1
    cls()
    print(
        str(COUNT) + " of " + str(NUM_OF_VID) +
        " videos converted into word lists.")
cls()
print(str(COUNT) + " videos converted into word lists.")

ans = input("Do you want to look for the files that match the lyrics now?: ")

if (ans == "y" or ans == "Y"):
    lyr = list(map(str, input("Enter the text: ").split(" ")))
    for word in lyr:
        find_text(word)
else:
    exit(0)
