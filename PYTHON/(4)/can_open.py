#förberedande övning 2

import urllib.request,ssl
ssl._create_default_https_context = ssl._create_unverified_context

def can_open(url):
    try:
        urllib.request.urlopen(url)
        print(url, 'kan öppnas')
        success = True
    except OSError:
        print(url, 'kan inte öppnas')
        success = False
    return 
