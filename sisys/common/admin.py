from django.contrib import admin

from common.models import Service, Category


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    fields = ('name', 'price', 'image', 'description', 'category', 'pic1', 'pic2')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    fields = ('name',)
