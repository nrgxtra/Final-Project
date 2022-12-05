from django.contrib import admin

from sisis_auth.models import SisisUser


@admin.register(SisisUser)
class UserAdmin(admin.ModelAdmin):
    list_display = ("email", "is_staff")
    list_filter = ("is_staff", "is_superuser", "groups")
    ordering = ("email",)

    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Permissions",
         {
             "fields": (
                 "is_staff",
                 "is_superuser",
                 "groups",
                 "user_permissions",
             ),
         }),
        ("Important dates", {"fields": ("last_login", "date_joined",)}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2"),
            },
        ),
    )

    readonly_fields = ('date_joined',)

