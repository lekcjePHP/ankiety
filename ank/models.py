#models.py
from django.db import models

# Create your models here.
class Poll (models.Model):
    question=models.CharField(max_length=500)
    pubdate=models.DateTimeField("data publikacji")
    
    def __unicode__(self):
         return self.question

class Choice (models.Model):

    poll = models.ForeignKey(Poll)
    choice = models.CharField(max_length = 200)
    votes = models.IntegerField();

    def __unicode__(self):
        return self.choice













