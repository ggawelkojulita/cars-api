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

    def create(self, validated_data):
        make_name = validated_data.pop('make_name')
        model_name = validated_data.pop('model_name')

        is_correct_make_name = VehiclesService.is_correct_make_name(make_name)
        if not is_correct_make_name:
            raise ValidationError('Provided make name is invalid')

        is_correct_model_name = VehiclesService.is_correct_model_name(make_name, model_name)
        if not is_correct_model_name:
            raise ValidationError('Provided model name is invalid')

        return super().create(validated_data)


class RateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rate
        fields = "__all__"


class PopularCarSerializer(serializers.ModelSerializer):

    class Meta:
        model = Car
        fields = "__all__"
