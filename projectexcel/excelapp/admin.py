from django.contrib import admin
from django_celery_beat.models import PeriodicTask, IntervalSchedule
from .models import Product
# Register your models here.
admin.site.register(Product)



# admin.site.register(PeriodicTask)
# admin.site.register(IntervalSchedule)