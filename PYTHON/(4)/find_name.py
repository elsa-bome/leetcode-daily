#förberedande övning 3

import urllib.request,ssl
ssl._create_default_https_context = ssl._create_unverified_context
names = ['elaf','salam']

def find_name(url):
    site = urllib.request.urlopen(url).read().decode('utf-8')
    for name in names:
        if name in site:
           print('found name', name)
           return True
        else:
           print('name not found')
           return False
