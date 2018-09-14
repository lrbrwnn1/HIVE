from django.contrib import admin
from .models import Investigator, Grant, Publication, grant_documents

class InvestigatorAdmin(admin.ModelAdmin):
    list_display = ('id', 'email','Fname', 'Lname','MI', 'picture', 'investigator_tag')
    list_editable = ()

class GrantAdmin(admin.ModelAdmin):
    list_displayGrant = ('grant_id', 'investigator_id', 'title', 'agency', 'guidelink', 'expiryDate')
    list_editableGrant = ()

class PublicationAdmin(admin.ModelAdmin):
    list_displayPublication = ('publication_id', 'title', 'medline', 'guidelink')
    list_editablePublication = ()  

class GrantDocumentAdmin(admin.ModelAdmin):
    list_displayGrantdocuments = ('grantTitle', 'grantID', 'grantText', 'grantLink')
    list_editableGrant = () 

admin.site.register(Investigator, InvestigatorAdmin)
admin.site.register(Grant, GrantAdmin)
admin.site.register(Publication, PublicationAdmin)
admin.site.register(grant_documents, GrantDocumentAdmin)