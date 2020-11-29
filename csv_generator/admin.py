from django.contrib import admin

from csv_generator.models import Schema, User


@admin.register(Schema)
class SchemaAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_by')


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username')
