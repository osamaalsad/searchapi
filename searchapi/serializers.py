from rest_framework import serializers
from .models import Category, SearchingData

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'

class SearchSerializer(serializers.ModelSerializer):

    class Meta:
        model = SearchingData
        fields = '__all__'