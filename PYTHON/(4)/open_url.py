#förberedande övning 1

import urllib.request,ssl
ssl._create_default_https_context = ssl._create_unverified_context

def open(url):
    file = urllib.request.urlopen(url)
    content = file.read()
    text = content.decode('utf-8')
    return text
    print(text)

 
