from rest_framework import serializers
from .models import *

class DigimonListSerializer(serializers.ModelSerializer):

    class Meta:

        model=Digimon
        fields="__all__"

        




