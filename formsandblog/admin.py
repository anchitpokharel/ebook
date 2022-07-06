from django.contrib import admin
from .models import Contact_us
from django.utils.safestring import mark_safe
# Register your models here.

class Store_contact_us(admin.ModelAdmin):
    readonly_fields = ['your_name', 'your_email', 'your_number', 'subject', 'message', ]
    

admin.site.register(Contact_us, Store_contact_us)