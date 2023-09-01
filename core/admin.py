from django.contrib import admin
from .models import Project, Directory, File

class DirectoryInline(admin.TabularInline):
    model = Directory

class FileInline(admin.TabularInline):
    model = File

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', 'created_at')
    inlines = [DirectoryInline]

class DirectoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'project', 'parent_dir', 'created_at')
    inlines = [FileInline]

class FileAdmin(admin.ModelAdmin):
    list_display = ('name', 'directory', 'created_at', 'updated_at')
    search_fields = ('name', 'directory__name', 'directory__project__name')

admin.site.register(Project, ProjectAdmin)
admin.site.register(Directory, DirectoryAdmin)
admin.site.register(File, FileAdmin)
