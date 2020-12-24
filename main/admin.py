from django.contrib import admin

from . import models

admin.site.register(models.User)
admin.site.register(models.Pledge)
admin.site.register(models.Module)
admin.site.register(models.ModuleInstance)
admin.site.register(models.MukhpathItem)
admin.site.register(models.MukhpathItemInstance)
