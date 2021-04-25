from django.contrib import admin

from .models import Guide


class GuideAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'start_date', 'version')
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('title',)
    empty_value_display = '-пусто-'


admin.site.register(Guide, GuideAdmin)
