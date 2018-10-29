from django.db import models

# Create your models here.
class BigBang(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField(max_length=11)
    sex = models.CharField(max_length=20)
    score = models.IntegerField(max_length=11)