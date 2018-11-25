from .models import Match
from rest_framework import serializers 

class MatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match 
        fields = '__all__'