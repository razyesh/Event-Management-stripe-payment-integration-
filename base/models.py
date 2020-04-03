from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.

class EventCategory(models.Model):
    category_name = models.CharField(max_length=255)

    def __str__(self):
        return self.category_name 

    class Meta:
        verbose_name_plural = 'Category'


class FutureEventManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(start_date__gt = datetime.date.today())

class PastEventManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(end_date__lt = datetime.date.today())

class PresentEventManager(models.Manager):
    def get_queryset(self):
        
        return super().get_queryset().filter(start_date__lte = datetime.date.today(), end_date__gte = datetime.date.today())


class Event(models.Model):
    user = models.ForeignKey(User, related_name='event_user', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    type = models.ForeignKey(EventCategory, related_name='event_category', on_delete=models.PROTECT)
    description = models.TextField()
    image_url = models.URLField(blank=True, null=True)
    image = models.ImageField(upload_to='images', blank=True, null=True)
    start_date = models.DateField()
    start_time = models.TimeField()
    total_seat = models.IntegerField(blank=True, null=True)
    location = models.CharField(max_length=255)
    end_date = models.DateField()
    creation = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()
    future_events = FutureEventManager()
    past_events = PastEventManager()
    ongoing_events = PresentEventManager()
    entry_fee = models.FloatField()

    def __str__(self):
        return self.title 

    class Meta:
        ordering = ['-creation']
        verbose_name_plural = 'Events'
        verbose_name = 'Event'


    def get_absolute_url(self):
        from django.urls import reverse 
        return reverse('event-detail-view', args=[str(self.id)])
