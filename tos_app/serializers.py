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

from rest_framework import serializers
from tos_app import models


class TermsOfServiceSerializer(serializers.ModelSerializer):

    class Meta:
        model=models.TermsOfService
        fields="__all__"


class UserTermsSerializer(serializers.ModelSerializer):
   
    class Meta:
        model=models.UserTerms
        fields="__all__"