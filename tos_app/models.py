from django.db import models
from django.conf import settings

class TermsOfService(models.Model):
    """
    Terms of Service Dictionary
    
    """
    content = models.TextField(null=True, blank=True)
    created_at=models.DateField(auto_now_add=True)
    last_modified=models.DateTimeField(auto_now=True)
    version = models.CharField(max_length=3, default='1.0')

    class Meta:
        verbose_name ='Terms of Service'
        verbose_name_plural ='Terms of Service'
