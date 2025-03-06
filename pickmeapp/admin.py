from django.contrib import admin
from .models import Vehicle, VehicleImage

class VehicleImageInline(admin.TabularInline):
    model = VehicleImage
    extra = 1

class VehicleAdmin(admin.ModelAdmin):
    inlines = [VehicleImageInline]
    list_display = ('name', 'per_day_rate', 'seating_capacity', 'additional_km_rate', 'allow_daily')

admin.site.register(Vehicle, VehicleAdmin)
