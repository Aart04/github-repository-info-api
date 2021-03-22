from typing import ClassVar
from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class RepositoryDetail(APIView):

    def get(self,request, owner, repository_name):
        return Response(data=None, status=status.HTTP_501_NOT_IMPLEMENTED)