# generate random youtube links

from bs4 import BeautifulSoup, SoupStrainer
import requests


url = ("https://www.youtube.com/feed/trending")
page = requests.get(url)
data = page.text
soup = BeautifulSoup(data)
watch = "/watch?"
uniquelink = []
joinurl = "https://www.youtube.com"

for link in soup.find_all('a'):
    ytlink = link.get('href')
    if watch in ytlink:
        ytlinkurl = joinurl + ytlink
        if ytlinkurl in uniquelink:
            pass
        else:
            uniquelink.append(ytlinkurl)

print(uniquelink)
# print(len(uniquelink))
