from rest_framework import serializers
from .models import SpyCat
from .services import is_valid_breed 

class SpyCatSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpyCat
        fields = "__all__"

    def validate_breed(self, value):
        if not is_valid_breed(value):
            raise serializers.ValidationError("Breed does not exist in TheCatAPI")
        return value
