
from rest_framework import serializers


class RepositoryInfoSerializer(serializers.Serializer):
    full_name = serializers.CharField()
    description = serializers.CharField()
    clone_url = serializers.CharField()
    owner_id = serializers.IntegerField()
    language = serializers.CharField()
