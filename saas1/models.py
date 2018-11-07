from django.db import models

# Create your models here.
class BigBang(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    sex = models.CharField(max_length=20)
    score = models.IntegerField()

class movieInfo(models.Model):
    title = models.CharField(max_length=64)
    content = models.CharField(max_length=255)

    def __unicode__(self):
        return self.title

class MessageBox(models.Model):
    title = models.CharField(max_length=64)
    content = models.CharField(max_length=255)
    msgFrom = models.CharField(max_length=64)
    msgTo = models.CharField(max_length=64)
    time = models.CharField(max_length=64)

    class Meta:
        ordering = ['id']
