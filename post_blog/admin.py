from django.contrib import admin
from .models import post_model

class post_admin(admin.ModelAdmin):
    list_display = ('title', 'publish_date', 'slug', )
    readonly_fields = ('slug', )

admin.site.register(post_model, post_admin)
