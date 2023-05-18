from django.contrib import admin

from common.models import Blog, Category, SocialMedia, ContactUs, AboutUs, ApplicationForm, ContactForm


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'position']
    ordering = ['-id']
    search_fields = ['name']


class BlogAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'author', 'created_at', 'views_count']
    ordering = ['-created_at']
    search_fields = ['title']


# Register your models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register(Blog, BlogAdmin)
admin.site.register(SocialMedia)
admin.site.register(ContactUs)
admin.site.register(ContactForm)
admin.site.register(AboutUs)
admin.site.register(ApplicationForm)
