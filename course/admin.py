from django.contrib import admin

from .models import Course, CourseContent, Review


@admin.register(Course)
class AdminCourse(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(CourseContent)
admin.site.register(Review)
