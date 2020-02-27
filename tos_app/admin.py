from django.contrib import admin

from tos_app import models
from django.conf import settings
from django.contrib.auth.models import User


class TermsOfServiceAdmin(admin.ModelAdmin):
    list_display=(
        'id',
        'last_modified',
        'created_at',
        'version',
        'content',
    )
    readonly_fields=('id', 'created_at', 'last_modified', 'users')
    fields=(
        'id',
        'version',
        'last_modified',
        'created_at',
        'content',
        'users',
    )
   


admin.site.register(models.TermsOfService, TermsOfServiceAdmin)

class UserTermsAdmin(admin.ModelAdmin):
    list_display=(
        'id',
        'user',
        'get_user_name',
        'first_name',
        'last_name',
        'street',
        'signed_date',
        'get_terms_version',
        'version_changed',

    )
    
    def get_user_name(self, instance):
        return instance.user.first_name + ' ' + instance.user.last_name

    def get_terms_version(self, instance):
        #here model should have a copy of the last modified date at the time of sigining
        return instance.tos_version.last_modified
    get_terms_version.short_description = 'ToS Version signed'
 

    def version_changed(self, instance):
        #here getting last modified date from ToS
        return instance.tos_version.last_modified
    version_changed.short_description = 'ToS Current Version'
    
    

admin.site.register(models.UserTerms, UserTermsAdmin)
