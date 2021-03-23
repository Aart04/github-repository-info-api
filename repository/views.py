from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .services import get_repository_info
from .serializers import RepositoryInfoSerializer
class RepositoryDetail(APIView):

    def get(self, request, owner, repository_name):
        api_status, api_response = get_repository_info(owner, repository_name)
        if api_status == status.HTTP_200_OK:
            response_data = {
                'full_name': api_response['full_name'],
                'description': api_response['description'],
                'clone_url': api_response['clone_url'],
                'owner_id': api_response['owner']['id'],
                'language': api_response['language']
            }
            serializer = RepositoryInfoSerializer(data=response_data)
            if serializer.is_valid():
                return Response(data=serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(data=None, status=status.HTTP_501_NOT_IMPLEMENTED)