from celery import Celery
import os

from celery.schedules import crontab

from sisys import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sisys.settings')
app = Celery('sisys')
app.conf.enable_utc = False
app.conf.update(timezone='Europe/Madrid')
app.config_from_object(settings, namespace='CELERY')

app.conf.beat_schedule = {
    'Send_mail_to_Clients': {
        'task': 'newsletters_app.tasks.send_scheduled_mails',
        # uncomment the row below and comment the next one for testing
        # 'schedule': 30.0,
        'schedule': crontab(hour=7, minute=30, day_of_week=1),
    }
}
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
