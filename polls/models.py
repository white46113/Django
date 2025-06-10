from django.db import models

# Create your models here.
class Question(models.Model):
    question = models.CharField(max_length=255)
    added_date = models.DateTimeField()
    class Meta:
        db_table = 'question'

class Choice(models.Model):
    question = models.CharField(max_length=255)
    choice_text = models.CharField(max_length=255)
    votes = models.IntegerField()
    class Meta:
        db_table = 'choice'
    