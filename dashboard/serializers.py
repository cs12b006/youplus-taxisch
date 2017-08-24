from .models import Request
from rest_framework import serializers

class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = ('status', 'location', 'req_time', 'raised_by', 'pk', 'picked_by')