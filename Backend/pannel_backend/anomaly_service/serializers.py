from rest_framework import serializers

'''
Serializer for representing unsuccessful buy per days data.

Attributes:
    days (List[float]): List of floats representing the unsuccessful buy values per day.
'''


class UnSuccessfulBuyPerDaysSerializer(serializers.Serializer):
    days = serializers.ListField(
        child=serializers.FloatField()
    )

'''
Serializer for representing successful buy per days data.

Attributes:
    days (List[float]): List of floats representing the successful buy values per day.
'''
class SuccessfulBuyPerDaysSerializer(serializers.Serializer):
    days = serializers.ListField(
        child=serializers.FloatField()
    )