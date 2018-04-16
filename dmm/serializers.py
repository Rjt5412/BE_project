from rest_framework import serializers
from . import models

class MainCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Main_Category
        fields= '__all__'

    class SubCategorySerializer(serializers.ModelSerializer):
        class Meta:
            model = models.Sub_Category
            fields = '__all__'