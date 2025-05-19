from rest_framework import serializers
from Plate_Api.models import Plate


class PlateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plate
        fields = ['id', 'image', 'image_name', 'plate_number']
        read_only_fields = [ 'image_name', 'plate_number']