from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from accounts.models import User,Profile

# Register your models here.

class CostomUserAdmin(UserAdmin):
    model = User
    list_display = ['email','is_staff','is_active','is_verified']
    list_filter = ("email", "is_staff", "is_active","is_verified")
    searching_fields = ('email',)
    ordering = ('created_date',)
    fieldsets = (
        ('Authentication', {
            "fields": (
                'email','password'
            ),
        }),
        ('Permission', {
            "fields": (
                'is_staff','is_active','is_superuser','is_verified'
            ),
        }),
        ('Group Permission', {
            "fields": (
                'groups','user_permissions'
            ),
        }),
        ('Important Date', {
            "fields": (
                'last_login',
            ),
        }),
    )

    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "email", "password1","password2","is_staff",
                "is_active", "is_superuser","is_verified"
            )}
        ),
    )
    

admin.site.register(User,CostomUserAdmin)
admin.site.register(Profile)
