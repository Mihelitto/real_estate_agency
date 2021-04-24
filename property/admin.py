from django.contrib import admin
from .models import Flat, Complaint, Owner


class OwnerInline(admin.TabularInline):
    model = Owner.flats.through
    raw_id_fields = ['owner',]
    verbose_name = 'Собственники'


class FlatAdmin(admin.ModelAdmin):
    search_fields = ['town',]
    readonly_fields = ['created_at',]
    list_display = ['address', 'price', 'new_building', 'construction_year', 'town']
    list_editable = ['new_building',]
    list_filter = ['new_building',]
    raw_id_fields = ['likes',]
    inlines = [OwnerInline,]


class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ['flat', 'user']


class OwnerAdmin(admin.ModelAdmin):
    raw_id_fields = ['flats']


admin.site.register(Flat, FlatAdmin)
admin.site.register(Complaint, ComplaintAdmin)
admin.site.register(Owner, OwnerAdmin)
