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


from rest_framework import routers
from tos_app import tos_api as api_views

router = routers.DefaultRouter()
router.register(r'user_tos', api_views.UserTermsViewset, basename='user_tos')
router.register(r'tos', api_views.TermsOfServiceViewset, basename='tos')
