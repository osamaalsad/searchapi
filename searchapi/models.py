from django.db import models


class Category(models.Model):
    ID = models.IntegerField(primary_key=True)
    Name = models.CharField(max_length=64)
    def __str__(self):
        return self.Name

class SearchingData(models.Model):
    ID = models.ForeignKey(Category, default=0, verbose_name="Category", on_delete=models.SET_DEFAULT)
    Name = models.CharField(max_length=128)
    URL = models.CharField(max_length=400)
    Description = models.TextField()

    def __str__(self):
        return self.Name
# Create your models here.

class UnknownSearch(models.Model):
    Name = models.CharField(max_length=256)
    num = models.IntegerField(default=0)

    def __str__(self):
        return self.Name


class CommentAnalysis(models.Model):
    Name = models.CharField(max_length=30)
    Email = models.EmailField(max_length=200)
    comment = models.TextField(max_length=400)
    status = models.CharField(max_length=8)

    def __str__(self):
        return self.Name
