from django.contrib import admin
from .models import Enquiry

class EnquiryAdmin(admin.ModelAdmin):
    list_display=('first_name','email','created')

admin.site.register(Enquiry,EnquiryAdmin)
