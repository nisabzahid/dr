from rest_framework import serializers
from .models import Cars

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cars
        fields = ('id', 'owner_name', 'email', 'document', 'number', 'registrationDate')