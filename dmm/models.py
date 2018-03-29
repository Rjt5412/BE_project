from django.db import models


class Posts_data(models.Model):
    site = models.CharField(max_length=400)
    username = models.CharField(max_length=400)
    likes = models.IntegerField()
    shares = models.IntegerField()
    coefficient = models.IntegerField()
    comment = models.IntegerField()
    sub_category = models.CharField(max_length=400)

