from django.contrib import admin
from .models import Post, Category, Location


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):

    list_display = ('title', 'pub_date', 'author', 'is_published')
    list_filter = ('is_published', 'pub_date')
    search_fields = ('title', 'text')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

    list_display = ('title', 'slug', 'is_published')
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):

    list_display = ('name', 'is_published')
