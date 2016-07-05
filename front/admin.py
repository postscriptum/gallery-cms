from django.contrib import admin
from front.models import General, Theme


class GeneralAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


class ThemeAdmin(admin.ModelAdmin):
    fields = (
        'name',
        'header',
        'jumbotron',
        'footer',
        'layout',
        ('bg_color', 'text_color'),
        ('panel_bg_color', 'panel_text_color')
    )


admin.site.register(General, GeneralAdmin)
admin.site.register(Theme, ThemeAdmin)
