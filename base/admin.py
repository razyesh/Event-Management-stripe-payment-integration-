from django.contrib import admin

# Register your models here.
from .models import EventCategory, Event 

admin.site.register(Event)
admin.site.register(EventCategory)