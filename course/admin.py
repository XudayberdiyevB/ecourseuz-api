from django.contrib import admin
from modeltranslation.admin import TranslationAdmin, TabbedTranslationAdmin

from .models import Course, CourseContent, Review


@admin.register(Course)
class AdminCourse(TabbedTranslationAdmin):
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(CourseContent)
admin.site.register(Review)
