import urllib.request,ssl
ssl._create_default_https_context = ssl._create_unverified_context


site = urllib.request.urlopen('http://user.it.uu.se/~joachim/').read().decode('utf-8')
names = ['elaf','salam']
for name in names:
    if name in site:
       print(name, 'found word')
    else:
       print(name, 'not found')
