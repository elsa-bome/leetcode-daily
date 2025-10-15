#basuppgift 3

import random,urllib.request,ssl
ssl._create_default_https_context = ssl._create_unverified_context
from email_from_string import email_from_string
from both import find_first_email
from find_all_emails import split_text, find_all_emails

url = 'http://www.it.uu.se/katalog/bylastname'
def find_emails_url(url):
    file = urllib.request.urlopen(url)
    content = file.read()
    textx = content.decode('utf-8')
    email_list = find_all_emails(textx)

    email_set = set()
    email_set.update(email_list)
    if len(email_set) == 0:
        print('No emails found in url')
    for email in email_set:
        print(email)
