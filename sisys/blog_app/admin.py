from django.contrib import admin

from blog_app.models import Post, Tag


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_on', 'updated_on')
    list_filter = ('tags', 'created_on', 'updated_on')
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}
    autocomplete_fields = ('tags',)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    search_fields = ('name',)
