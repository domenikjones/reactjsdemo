from django.contrib import admin
from demo.models import Appartement, AppartementType

# Register your models here.
class AppartementAdmin(admin.ModelAdmin):
    list_display = ('title', 'active', 'is_visible', 'created', 'modified', )
    list_filter = ('active', 'modified', 'created', )
    readonly_fields = ('uuid', )

admin.site.register(Appartement, AppartementAdmin)

class AppartementTypeAdmin(admin.ModelAdmin):
    pass

admin.site.register(AppartementType, AppartementTypeAdmin)