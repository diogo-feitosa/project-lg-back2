from django.contrib import admin
from project_lg.models import Project

# Register your models here.
class Projects(admin.ModelAdmin):
    list_display = ('id','name', 'startDate', 'endDate', 'value', 'risk')

    list_display_links = ('id','name')
    search_fields = ('name',)
    list_per_page = 20

admin.site.register(Project, Projects)