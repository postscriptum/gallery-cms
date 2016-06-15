from django.contrib import admin
from front.models import General, Theme


class GeneralAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(General, GeneralAdmin)
admin.site.register(Theme)
