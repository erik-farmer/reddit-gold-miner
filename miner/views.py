import urllib2
import time
import datetime

from django.core import serializers
from django.http import HttpResponse

from bs4 import BeautifulSoup

from .models import GoldMeasure

def getCurrentGold():
  url="http://www.reddit.com/"
  page=urllib2.urlopen(url)
  soup = BeautifulSoup(page.read())
  divs = soup.find('div',{'class':'progress'})
  gm = GoldMeasure()
  gm.timestamp = int(time.time())
  gm.value = divs.findChildren()[0].string[:-1]
  gm.save()

def get_todays_gold_json(request):
  now = datetime.datetime.now()
  start_of_day = now.replace(hour=0, minute=0, second=0, microsecond=0)
  end_of_day = now.replace(hour=23, minute=59, second=59, microsecond=0)
  start_ts = time.mktime(start_of_day.utctimetuple())
  end_ts = time.mktime(end_of_day.utctimetuple())
  todays_measurements = GoldMeasure.objects.filter(
    timestamp__gte=start_ts, timestamp__lte=end_ts
  )
  data = serializers.serialize("json", todays_measurements)
  return HttpResponse(data, content_type="application/json")