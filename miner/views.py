import datetime
import json
import pytz
import time
import urllib2

from django.http import HttpResponse
from django.views.generic.base import TemplateView

from bs4 import BeautifulSoup

from .models import GoldMeasure

class MinerHomeTemplateView(TemplateView):
  template_name = 'home.html'


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
  output = []
  pac_tz = pytz.timezone('US/Pacific')
  now = datetime.datetime.now(tz=pac_tz)
  start_of_day = now.replace(hour=0, minute=0, second=0, microsecond=0)
  end_of_day = now.replace(hour=23, minute=59, second=59, microsecond=0)
  start_ts = time.mktime(start_of_day.utctimetuple())
  end_ts = time.mktime(end_of_day.utctimetuple())
  todays_measurements = GoldMeasure.objects.filter(
    timestamp__gte=start_ts, timestamp__lte=end_ts
  ).order_by('timestamp')
  for tm in todays_measurements:
    output.append([tm.timestamp * 1000, tm.value])
  data = json.dumps(output)
  return HttpResponse(data, content_type="application/json")
