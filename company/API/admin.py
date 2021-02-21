from django.contrib import admin
from company.API.models import Employee, Sector, Project


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('employee_id', 'first_name', 'last_name', 'salary')
    list_filter = ('first_name', 'salary')
    ordering = ('first_name', 'salary')


@admin.register(Sector)
class SectorAdmin(admin.ModelAdmin):
    list_display = ('sector_id', 'name', 'location')
    list_filter = ('name', 'location')
    ordering = ('name', 'location')


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('project_id', 'name', 'location')
    list_filter = ('name', 'location')
    ordering = ('name', 'location')
