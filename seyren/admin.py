from django.contrib import admin
from .models import Alert


@admin.register(Alert)
class AlertAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'bot_token', 'chat_id')
    search_fields = ('name', 'url', 'bot_token', 'chat_id')
