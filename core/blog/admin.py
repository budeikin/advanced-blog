from django.contrib import admin
from blog.models import Post, Category

# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ("author", "title", "status", "categoy", "created_date")


admin.site.register(Post, PostAdmin)
admin.site.register(Category)
