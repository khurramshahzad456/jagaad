from rest_framework import serializers
from .models import StatsMessage


class StatsMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = StatsMessage
        fields = '__all__'
