from .models import Match
from rest_framework import serializers,fields

class MatchSerializer(serializers.ModelSerializer):
    country = serializers.CharField(source='get_country_display')
    class Meta:
        model = Match 
        fields = '__all__'