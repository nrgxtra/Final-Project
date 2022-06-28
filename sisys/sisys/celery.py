from celery import Celery
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sisys.settings')
app = Celery('sisys')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

