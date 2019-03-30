from rest_framework import serializers


class HelloSerializer(serializers.Serializer):
    """serailizes a name field for testing api"""

    name = serializers.CharField(max_length=10)
