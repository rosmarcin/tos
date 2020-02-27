"""
Terms of Service App, Marcin Roszczyk 2020

"""

__author__ = "Marcin Roszczyk,"
__copyright__ = "Copyright 2020, Marcin Roszczyk"
__license__ = "GPL"
__version__ = "0.0.1-pre-beta"
__maintainer__ = "Marcin Roszczyk"
__email__ = "mr@marcinros.net"
__status__ = "DEV"


from django.http import Http404

from rest_framework import viewsets, response, status
from rest_framework.decorators import action


from tos_app import models
from tos_app import serializers



class TermsOfServiceViewset(viewsets.ModelViewSet):
    queryset = models.TermsOfService.objects.all()
    serializer_class = serializers.TermsOfServiceSerializer 

class UserTermsViewset(viewsets.ModelViewSet):
    """
    User Terms of Service API 
    - CRUD
    - create action (POST) is equivalent to User Terms signof for indicated Terms of Service version

    Functional endpoint : sign_terms allows authenticated user to sign current (latest) version of terms


    """
    queryset = models.UserTerms.objects.all()
    serializer_class = serializers.UserTermsSerializer

    def create(self, request):
        serializer =  serializers.UserTermsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=status.HTTP_201_CREATED)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



