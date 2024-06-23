from django.contrib import admin
from .models import *

admin.site.register(Advertisement)


class AdvertisementAdmin(admin.ModelAdmin):

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.author = request.user
        super().save_model(request, obj, form, change)



# Register your models here.
