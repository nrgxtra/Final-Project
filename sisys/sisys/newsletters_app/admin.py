from django.contrib import admin

from sisys.newsletters_app.models import NewsletterUser, Newsletter


@admin.register(NewsletterUser)
class NewsletterUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'time_added',)


@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('title', 'content',)
