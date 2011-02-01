# -*- encoding: utf-8 -*-

from django.contrib import admin
from models import WikiPostPlugin as WikiPost

class WikiPostAdmin(admin.ModelAdmin):
    pass


admin.site.register(WikiPost, WikiPostAdmin)
