from rest_framework import routers
from tos_app import tos_api as api_views

router = routers.DefaultRouter()
router.register(r'user_tos', api_views.UserTermsViewset, basename='user_tos')
router.register(r'tos', api_views.TermsOfServiceViewset, basename='tos')
