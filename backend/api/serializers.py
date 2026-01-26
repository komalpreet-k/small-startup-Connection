from rest_framework import serializers
from .models import SavedBusiness, Country, State, City, Category, Business

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'

class SavedBusinessSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavedBusiness
        fields = ["id", "business", "saved_at"]
        read_only_fields = ["saved_at"]


class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = '__all__'


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class BusinessSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    country = CountrySerializer(read_only=True)
    state = StateSerializer(read_only=True)
    city = CitySerializer(read_only=True)

    class Meta:
        model = Business
        fields = "__all__"


class BusinessCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Business
        exclude = [
            'owner',
            'verification_status',
            'created_at',
            'updated_at'
        ]

