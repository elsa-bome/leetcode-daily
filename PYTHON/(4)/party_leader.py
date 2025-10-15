#förberedande övning 4

import random,urllib.request,ssl
ssl._create_default_https_context = ssl._create_unverified_context

def count_mentions(text):

    file = urllib.request.urlopen(url)
    content = file.read()
    textx = content.decode('utf-8')
    return textx.count(text)

text = ['Trump','Macron','Löfven','Dejan']

url = 'https://www.expressen.se/'

print(url)
for leader in text:
    print(leader, 'är omnämnd', count_mentions(leader), 'gånger')
