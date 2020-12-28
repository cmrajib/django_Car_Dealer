from django.contrib import admin
from .models import Contact

# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'firstname', 'lastname', 'email', 'car_title', 'create_date')
    list_display_links = ('id','firstname', 'lastname')
    list_filter = ('create_date',)
    # list_editable = ('is_published',)
    search_fields =('firstname', 'lastname','email', 'car_title', )
    list_per_page = 25

admin.site.register(Contact, ContactAdmin)
