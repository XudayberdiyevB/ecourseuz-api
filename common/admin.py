from django.contrib import admin
from django.contrib.sites.models import Site

from common.models import Blog, SocialMedia, AboutUs, Banner, ContactUs, ContactForm

from common.models.category import Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'position']
    ordering = ['-id']
    search_fields = ['name']


class BlogAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'author', 'created_at', 'views_count']
    ordering = ['-created_at']
    search_fields = ['title']


class BannerAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "description", "position", ]
    ordering = ['-id']
    search_fields = ['title']


class SocialMediaAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "type", "urls", ]
    ordering = ['-id']
    search_fields = ['name']


class AboutUsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', ]
    ordering = ['-id']
    search_fields = ['title']


class ContactUsAdmin(admin.ModelAdmin):
    list_display = ['id', 'country', 'city', 'street', 'location', 'email', 'phone']
    search_fields = ['title']


class ContactFormAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'phone', 'message']
    list_display_links = ['name']
    ordering = ['-created_at']
    search_fields = ['email']


# Register your models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register(Blog, BlogAdmin)
admin.site.register(Banner, BannerAdmin)
admin.site.register(SocialMedia, SocialMediaAdmin)
admin.site.register(AboutUs, AboutUsAdmin)
admin.site.register(ContactUs, ContactUsAdmin)
admin.site.register(ContactForm, ContactFormAdmin)
