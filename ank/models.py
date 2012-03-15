from django.db import models

# Create your models here.
class Poll (models.Model):
    question=models.CharField(max_length=500)
    pubdate=models.DateTimeField("data publikacji")

class Choice (models.Model):
    pass















