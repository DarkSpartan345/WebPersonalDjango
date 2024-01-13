from django.contrib import admin
from .models import Project
class ProjectAdmin(admin.ModelAdmin):
    readonly_fields=('created','update')
admin.site.register(Project,ProjectAdmin)
