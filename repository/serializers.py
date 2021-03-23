
from rest_framework import serializers


class RepositoryInfoSerializer(serializers.Serializer):
    full_name = serializers.CharField()
    description = serializers.CharField()
    clone_url = serializers.CharField()
    owner_id = serializers.DecimalField(max_digits=99, decimal_places=0)
    language = serializers.CharField(allow_null=True)
