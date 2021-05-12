from django.contrib import admin

from .forms import GuideVersionAdminForm
from .models import Element, Guide, GuideVersion


class GuideAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'start_date', 'version')
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('title',)
    empty_value_display = '-пусто-'


admin.site.register(Guide, GuideAdmin)


class GuideVersionAdmin(admin.ModelAdmin):
    form = GuideVersionAdminForm
    list_display = ('name', 'guide', 'date_from')
    list_filter = ('name',)
    empty_value_display = '-пусто-'


admin.site.register(GuideVersion, GuideVersionAdmin)


class ElementAdmin(admin.ModelAdmin):
    list_display = ('code', 'value', 'show_versions')
    list_filter = ('code', )
    empty_value_display = '-пусто-'

    @admin.action(description='версии')
    def show_versions(self, obj):
        return ', '.join([str(a) for a in obj.version.all()])


admin.site.register(Element, ElementAdmin)
