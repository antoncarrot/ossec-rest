from rest_framework import serializers

from .models import Alert, Category, Location, RuleView, CategoryView


class AlertSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alert
        fields = '__all__'
        depth = 1


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'


class RuleViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = RuleView
        fields = '__all__'


class CategoryViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryView
        fields = '__all__'
