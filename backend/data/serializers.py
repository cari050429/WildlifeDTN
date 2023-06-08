from rest_framework import serializers
from .models import Data


class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model=Data
        fields=('picture','node_origination', 'date_created','file_type')