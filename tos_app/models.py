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


from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied

class TermsOfService(models.Model):
    """
    Terms of Service Dictionary
    - multiple versions 
    - linked to to User's - this is auxiliary
    
    """
    content = models.TextField(null=True, blank=True)
    created_at=models.DateField(auto_now_add=True)
    last_modified=models.DateTimeField(auto_now=True)
    version = models.CharField(max_length=3, default='1.0')
    users = models.ManyToManyField(User, through='UserTerms', blank=False)

    def save(self, *args, **kwargs):
        if self.id:
            raise PermissionDenied
        super(TermsOfService, self).save(*args, **kwargs)

    class Meta:
        verbose_name ='Terms of Service'
        verbose_name_plural ='Terms of Service'


class UserTerms(models.Model):
    """
    User signed Terms 
    Each user can have multiple version of Terms signed

    - user's first and last name is stored in the model as part of a signature independently from User's model
    - when an agreement was signed 
    - what the user data was at that point (first_name, last_name, street, post_code).

    """
    user=models.ForeignKey(User , related_name='user_terms', on_delete=models.CASCADE)
    first_name=models.CharField(max_length=50, null=False, blank=False)
    last_name=models.CharField(max_length=50, null=False, blank=False)
    street=models.CharField(max_length=50, null=False, blank=False)
    post_code=models.CharField(max_length=10, null=False, blank=False)
    created_at=models.DateField(auto_now_add=True)
    signed_date=models.DateTimeField(auto_now=True)
    tos_version = models.ForeignKey(TermsOfService, related_name='user_terms', on_delete=models.DO_NOTHING)

    class Meta:
        unique_together=('tos_version', 'user',)
        verbose_name ='User Terms'
        verbose_name_plural ='User Terms'
        
