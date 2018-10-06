import bs4 as bs
import urllib.request

sauce = urllib.request.urlopen('https://thewire.in/161600/civilian-vigilante-groups-nigeria-reshaping-conflict-boko-haram/').read()
soup = bs.BeautifulSoup(sauce,'lxml')



for mul_tags in soup.find_all(['p','h1','h3']):
     print(mul_tags.string)