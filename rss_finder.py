"""Script to find RSS feed paths on a webpage from a given URL."""

import bs4 as bs
import requests
import sys
import warnings

keywords = ['feed', 'rss', 'xml', 'atom', 'asp', 'application/rss']
warnings.filterwarnings('ignore', message='Unverified HTTPS request')

url = sys.argv[1]

# download webpage then isolate all links
response = requests.get(url, timeout=30, verify=False)
links = bs.BeautifulSoup(response.text, 'html.parser').find_all(href=True)

# search for expressions containing keywords
for link in links:
    for word in keywords:
        if word in link.get('href'):
            print(link.get('href'))

