from rest_framework import serializers

from .models import TechNews

class MathsNewsSerializer(serializers.ModelSerializer):
  class Meta:
    model= TechNews
    fields= '__all__'