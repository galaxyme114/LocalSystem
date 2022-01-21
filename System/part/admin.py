from django.contrib import admin
from System.part.models import User
from import_export.admin import ImportExportModelAdmin

# Register your models here.

@admin.register(User)
class UserAdmin(ImportExportModelAdmin):
	pass