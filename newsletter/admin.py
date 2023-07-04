from django.contrib import admin
from newsletter.models import Newsletter, Subscriber


@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'confirmed']
    list_filter = ['confirmed', 'receive_emails', 'created']
    search_fields = ['name', 'email']


@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ['title', 'created', 'updated']
    list_filter = ['created', 'updated']
    search_fields = ['title', 'content']

