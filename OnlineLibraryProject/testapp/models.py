from django.db import models


class Book(models.Model):
    title=models.CharField(max_length=30)
    author=models.CharField(max_length=30)
    pages=models.IntegerField()
    price=models.FloatField()

class Magagin(models.Model):
    title=models.CharField(max_length=30)
    author=models.CharField(max_length=30)
    publish_date=models.DateField()
    article=models.CharField(max_length=30)

    
class NewsPaper(models.Model):
    Name=models.CharField(max_length=30)
    headline=models.TextField(max_length=30)
    publish_date=models.DateField()
# Create your models here.
