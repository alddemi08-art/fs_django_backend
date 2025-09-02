from django.contrib import admin
from .models import Contact

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'created_at')  # Show phone in admin list
    search_fields = ('name', 'email', 'phone')
    list_filter = ('created_at',)
