from django.contrib import admin

from . import models


class Admin(admin.ModelAdmin):
    list_display = ('Email',)


admin.site.register(models.Amazon, Admin)
admin.site.register(models.Flipkart, Admin)
admin.site.register(models.Snapdeal, Admin)
