from django.db import models

# Create your models here.


class Rooms(models.Model):
    roomname = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True)
    datecreated = models.DateTimeField(auto_now_add=True)
