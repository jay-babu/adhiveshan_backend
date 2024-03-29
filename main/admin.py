from django.contrib import admin

from . import models


@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    search_fields = ('id',)


@admin.register(models.MukhpathItem)
class MukhpathItemAdmin(admin.ModelAdmin):
    search_fields = ('title',)


@admin.register(models.ModuleInstance)
class ModuleInstanceAdmin(admin.ModelAdmin):
    search_fields = ('module__title',)


admin.site.register(models.Pledge)
admin.site.register(models.PledgedModule)
admin.site.register(models.Module)
admin.site.register(models.MukhpathItemInstance)
