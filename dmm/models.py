from django.db import models


class Posts_data(models.Model):
    auto_increment_id = models.AutoField(primary_key=True)
    site = models.CharField(max_length=400)
    username = models.CharField(max_length=400)
    likes = models.IntegerField()
    shares = models.IntegerField()
    coefficient = models.FloatField()
    #sub_category = models.CharField(max_length=400)
    #main_category = models.CharField(max_length=400)
    ml_out = models.IntegerField()
    url = models.TextField()
    user_url = models.TextField()


class Sub_Category(models.Model):
    main_category_model = models.ForeignKey('Main_Category')
    sub_category_model = models.CharField(max_length=100, verbose_name=('Sub-Category'))

    def __unicode__(self, ):
        return str(self.sub_category_model)


class Main_Category(models.Model):
    main_category_model = models.CharField(max_length= 100,  verbose_name = ('Main Category'))
    def __unicode__(self):
        return str(self.main_category_model)
