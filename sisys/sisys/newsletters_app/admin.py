from django.contrib import admin

from sisys.newsletters_app.models import NewsletterUser


@admin.register(NewsletterUser)
class NewsletterUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'time_added',)

