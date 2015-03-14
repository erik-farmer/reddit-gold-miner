from django.conf.urls import patterns
from django.conf.urls import url

from .views import get_todays_gold_json
from .views import MinerHomeTemplateView

urlpatterns = patterns('',
    url(r'$', MinerHomeTemplateView.as_view()),
    url(r'^data', get_todays_gold_json),
)
