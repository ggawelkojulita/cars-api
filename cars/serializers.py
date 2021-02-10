from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from cars.models import Car, Rate
from cars.services import VehiclesService


class CarSerializer(serializers.ModelSerializer):
    avg_rate = serializers.IntegerField(read_only=True)

    class Meta:
        model = Car
        fields = '__all__'
        read_only_fields = ('id', 'avg_rate')

    def validate(self, attrs):
        make_name = attrs.get('make_name')
        model_name = attrs.get('model_name')

        is_correct_make_name = VehiclesService.is_correct_make_name(make_name)
        if not is_correct_make_name:
            raise ValidationError({'make_name': 'Invalid value'})

        is_correct_model_name = VehiclesService.is_correct_model_name(make_name, model_name)
        if not is_correct_model_name:
            raise ValidationError({'model_name': 'Invalid value'})

        return attrs


class RateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rate
        fields = "__all__"


class PopularCarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = "__all__"
