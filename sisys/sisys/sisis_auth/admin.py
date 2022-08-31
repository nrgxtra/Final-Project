from django.contrib import admin

from sisys.sisis_auth.models import SisisUser


@admin.register(SisisUser)
class UserAdmin(admin.ModelAdmin):
    pass

