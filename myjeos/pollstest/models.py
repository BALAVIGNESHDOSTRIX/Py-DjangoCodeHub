from django.db import models

# Create your models here.
class Questions(models.Model):
    question_txt = models.CharField(max_length=200)
    publish_date = models.DateTimeField('Date Published')

class Choice(models.Model):
    question_id = models.ForeignKey(Questions, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
