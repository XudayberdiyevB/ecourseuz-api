from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from modeltranslation.admin import TabbedTranslationAdmin

from .models import Course, CourseContent, Review
from .resources import CourseResource


@admin.register(Course)
class AdminCourse(ImportExportModelAdmin, TabbedTranslationAdmin):
    resource_classes = [CourseResource]
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(CourseContent)
admin.site.register(Review)
