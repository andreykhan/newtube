from django.contrib import admin

from . import models


@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('pk', 'post_name', 'text', 'pub_date', 'author', 'group')
    search_fields = ('post_name', 'text', 'author')
    list_display_links = ('post_name',)
    list_filter = ('author',)
    list_editable = ('group',)


@admin.register(models.Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'description')
    search_fields = ('title',)
