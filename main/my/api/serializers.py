from rest_framework import serializers
from my.models import studentform

class studentserializer(serializers.ModelSerializer):
    class Meta:
        model=studentform
        fields=["id","name","email","password"]