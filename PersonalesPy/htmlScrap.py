from bs4 import BeautifulSoup
import urllib
import re

htmlFile = urllib.urlopen("https://twitter.com/schiob")
soup = BeautifulSoup(htmlFile)

res = soup.find_all("a", class_="js-nav", text="Seguidores")
print res