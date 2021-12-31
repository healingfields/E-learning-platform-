from django.contrib import admin
from django.db import models
from .models import Course, Subject, Module
# Register your models here.

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {"slug":('title',)}

class ModuleInline(admin.StackedInline):
    model = Module

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'subject', 'owner', 'created']
    prepopulated_fields = {'slug':('title',),}
    list_filter = ['owner', 'subject', 'created']
    search_fields = ['title', 'overview']
    inlines = [ModuleInline ]

admin.site.index_template = 'memcache_status/admin_index.html'