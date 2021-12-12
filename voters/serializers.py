from .models import Voter
from rest_framework import serializers


class VoterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Voter
        fields = '__all__'
