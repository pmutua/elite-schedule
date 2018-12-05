from .models import Match
from rest_framework import serializers,fields

class MatchSerializer(serializers.ModelSerializer):

    class Meta:
        model = Match 
        fields = '__all__'