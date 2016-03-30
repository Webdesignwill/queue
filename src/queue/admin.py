from django.contrib import admin

from queue import models


class QueueAdmin(admin.ModelAdmin):
    list_display = ('created', 'uuid')

admin.site.register(models.Queue, QueueAdmin)
