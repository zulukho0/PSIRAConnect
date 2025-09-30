from django.contrib import admin
from .models import Student

# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'second_name','last_name', 'id_number', 'contact_number', 'created_at')
    search_fields = ('first_name', 'last_name', 'id_number')
