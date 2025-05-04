import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE','Redzone_Safety_Warehouse.settings')
app = Celery('Redzone_Safety_Warehouse', broker='redis://localhost:6379/0')
app.autodiscover_tasks()
