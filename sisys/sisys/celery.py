from celery import Celery
import os
from sisys import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sisys.settings')
app = Celery('sisys')
app.conf.enable_utc = False
app.conf.update(timezone='Europe/Madrid')
app.config_from_object(settings, namespace='CELERY')

app.conf.beat_schedule = {
    'Send_mail_to_Clients': {
        'task': 'newsletters_app.tasks.send_scheduled_mails',
        'schedule': 30.0,  # every 60 seconds it will be called
    }
}
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
