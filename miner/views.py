import urllib2
import time

from bs4 import BeautifulSoup

from .models import GoldMeasure

def getCurrentGold(request):
  url="http://www.reddit.com/"
  page=urllib2.urlopen(url)
  soup = BeautifulSoup(page.read())
  divs = soup.find('div',{'class':'progress'})
  gm = GoldMeasure()
  gm.timestamp = int(time.time())
  gm.value = divs.findChildren()[0].string[:-1]
  gm.save()