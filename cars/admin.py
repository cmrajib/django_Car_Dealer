from django.contrib import admin
from .models import Car
from django.utils.html import format_html


# Register your models here.

class CarAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" style="border-radius: 50px;"/>'.format(object.car_photo.url))

    thumbnail.short_description = 'Photo'

    list_display = ('id', 'thumbnail','is_featured','car_title', 'color', 'model', 'body_style', 'fuel_type', 'city')
    list_display_links = ('id','thumbnail', 'car_title', 'color')
    list_filter = ('model','condition')
    list_editable = ('is_featured',)
    search_fields =('model', 'color','price')
    list_per_page = 10


admin.site.register(Car, CarAdmin)
