from rest_framework import serializers
from .models import *

class BmbcChecksheetSerializer(serializers.ModelSerializer):
    class Meta:
        model = BmbcChecksheet
        fields = '__all__'

class BogieChecksheetSerializer(serializers.ModelSerializer):
    class Meta:
        model = BogieChecksheet
        fields = '__all__'

class BogieDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BogieDetails
        fields = '__all__'

class BogieChecksheetFormSerializer(serializers.ModelSerializer):
    bmbcChecksheet = BmbcChecksheetSerializer(source='bmbc_checksheet')
    bogieChecksheet = BogieChecksheetSerializer(source='bogie_checksheet')
    bogieDetails = BogieDetailsSerializer(source='bogie_details')

    class Meta:
        model = BogieChecksheetForm
        fields = [
            'form_number', 'inspection_by', 'inspection_date',
            'bmbcChecksheet', 'bogieChecksheet', 'bogieDetails'
        ]

    def create(self, validated_data):
        bmbc_data = validated_data.pop('bmbc_checksheet')
        bogie_data = validated_data.pop('bogie_checksheet')
        details_data = validated_data.pop('bogie_details')

        bmbc = BmbcChecksheet.objects.create(**bmbc_data)
        bogie = BogieChecksheet.objects.create(**bogie_data)
        details = BogieDetails.objects.create(**details_data)

        return BogieChecksheetForm.objects.create(
            bmbc_checksheet=bmbc,
            bogie_checksheet=bogie,
            bogie_details=details,
            **validated_data
        )


class WheelSpecificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = WheelSpecification
        fields = '__all__'
