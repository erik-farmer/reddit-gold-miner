import logging
import datetime

from django.core.management.base import BaseCommand

from miner.views import getCurrentGold


class Command(BaseCommand):
  def handle(self, *args, **options):
    getCurrentGold()
    current_dt_string = datetime.datetime.now().strftime('%b %d %Y - %H:%M')
    logging.info('mine command issued at: {}'.format(current_dt_string))