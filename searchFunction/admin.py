from django.contrib import admin

from .models import Investigator
from .models import Publication
from .models import Grant
from .models import ClinicalTrial
from .models import terms_list
from .models import similarity_matrix

class PubAdmin(admin.ModelAdmin):
    model = Publication
    list_display = ['title', 'investigator_tag', ]



admin.site.register(Investigator)
admin.site.register(Publication, PubAdmin)
admin.site.register(Grant)
admin.site.register(ClinicalTrial)


