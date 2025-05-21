from rest_framework import serializers
from Plate_Api.models import Plate


class PlateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plate
        fields = ['id', 'image', 'image_name', 'plate_number']
        read_only_fields = [ 'image_name', 'plate_number']

class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    password = serializers.CharField(max_length=128, write_only=True)
    password2 = serializers.CharField(max_length=128, write_only=True)

    # def validate(self, attrs):
    #     if attrs['password'] != attrs['password2']:
    #         raise serializers.ValidationError("Passwords do not match")
    #     return attrs

    # def create(self, validated_data):
    #     from django.contrib.auth.models import User
    #     user = User.objects.create_user(
    #         username=validated_data['username'],
    #         password=validated_data['password']
    #     )
    #     return user