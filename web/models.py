from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Request(models.Model):
    title = models.CharField(max_length=256)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    description = models.CharField(max_length=256)
    status = models.CharField(max_length=256)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Category(models.Model):
    title = models.CharField(max_length=256)
    description = models.CharField(max_length=256)
    request = models.ManyToManyField(Request)


class Comment(models.Model):
    text = models.CharField(max_length=1024)
    date = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    request = models.ManyToManyField(Request)


class Rate(models.Model):
    rate = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    request = models.ForeignKey(Request, on_delete=models.CASCADE)
