from django.db import models

# Create your models here.
class Topic(models.Model):
    topic=models.CharField(max_length=50)
    subject=models.TextField()