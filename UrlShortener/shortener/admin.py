from django.contrib import admin
from .models import Link

@admin.register(Link)  # Optional: You can use this decorator
class LinkAdmin(admin.ModelAdmin):
    list_display = ('slug', 'original_url', 'created_at', 'access_count', 'last_accessed', 'expires_at')
    search_fields = ('slug', 'original_url')
    list_filter = ('created_at',)