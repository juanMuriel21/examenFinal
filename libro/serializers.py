from rest_framework import serializers
from .models import Mlibro


class libroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mlibro
        fields = '__all__'
    def validate_isbn(self, value):
        
        if len(value) not in [10, 13] or not value.isdigit():
            raise serializers.ValidationError("debe tener 10 o 13 dígitos numéricos.")
        return value