from django.contrib import admin

from csv_generator.models import Schema, User, SchemaColumn, GeneratedFile


@admin.register(Schema)
class SchemaAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_by')


@admin.register(SchemaColumn)
class SchemaColumnAdmin(admin.ModelAdmin):
    list_display = ('id', 'schema', 'name', 'type', 'from_field', 'to_field', 'order', 'created_by')


@admin.register(GeneratedFile)
class GeneratedFileAdmin(admin.ModelAdmin):
    list_display = ('id', 'schema')


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username')
