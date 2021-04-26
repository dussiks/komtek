from django.contrib import admin

from .models import Element, Guide, GuideVersion


class GuideAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'start_date', 'version')
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('title',)
    empty_value_display = '-пусто-'


admin.site.register(Guide, GuideAdmin)


class GuideVersionAdmin(admin.ModelAdmin):
    list_display = ('name', 'guide', 'date_from')
    list_filter = ('name',)
    empty_value_display = '-пусто-'


admin.site.register(GuideVersion, GuideVersionAdmin)


class ElementAdmin(admin.ModelAdmin):
    list_display = ('code', 'value')
    list_filter = ('code', )
    empty_value_display = '-пусто-'


admin.site.register(Element, ElementAdmin)
