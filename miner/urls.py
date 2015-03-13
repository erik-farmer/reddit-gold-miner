from django.conf.urls import patterns
from django.conf.urls import url

from .views import get_todays_gold_json

urlpatterns = patterns('',
    url(r'^data', get_todays_gold_json),
)
