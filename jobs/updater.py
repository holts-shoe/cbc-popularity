from apscheduler.schedulers.background import BackgroundScheduler
from .jobs import scheduler_api
from pytz import utc

def start():
    scheduler = BackgroundScheduler(timezone=utc)
    #scheduler.add_job(scheduler_api, 'interval', seconds=15)
    scheduler.add_job(scheduler_api, 'cron', hour='5', minute='1')
    scheduler.start()
