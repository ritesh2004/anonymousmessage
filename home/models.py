from django.db import models
from datetime import datetime
# Create your models here.
class Message(models.Model):
    message = models.TextField()
    datetime = models.DateField()
    def __str__(self):
        return "someone"+ str(datetime.now())