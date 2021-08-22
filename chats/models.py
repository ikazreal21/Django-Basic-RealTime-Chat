from django.db import models

# Create your models here.


class Rooms(models.Model):
    roomname = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True)
    datecreated = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('datecreated',)


class Message(models.Model):
    username = models.CharField(max_length=255)
    room = models.CharField(max_length=255)
    content = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('date_added',)
