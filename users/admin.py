from django.contrib import admin

from .models import User, VerificationCode


# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'first_name', 'last_name']
    ordering = ['-date_joined']


@admin.register(VerificationCode)
class VerificationCodeAdmin(admin.ModelAdmin):
    list_display = ["email", "code", "last_sent_time", "expired_at", "is_verified"]
    ordering = ["-last_sent_time"]