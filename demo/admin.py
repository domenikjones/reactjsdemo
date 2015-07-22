from adminsortable2.admin import SortableInlineAdminMixin
from django.contrib import admin
from demo.models import Appartement, AppartementType, AppartementImage


class AppartementImagesInlines(SortableInlineAdminMixin, admin.TabularInline):
    model = AppartementImage

class AppartementAdmin(admin.ModelAdmin):
    list_display = ('title', 'active', 'is_visible', 'created', 'modified', )
    list_filter = ('active', 'modified', 'created', )
    readonly_fields = ('uuid', )
    inlines = [AppartementImagesInlines, ]

admin.site.register(Appartement, AppartementAdmin)

class AppartementTypeAdmin(admin.ModelAdmin):
    pass

admin.site.register(AppartementType, AppartementTypeAdmin)