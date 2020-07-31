from django.contrib import admin
from .models import Port, System, Client


class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'link', 'port', 'system', 'version', 'status')


class PortAdmin(admin.ModelAdmin):
    list_display = ('id', 'connector', 'shutdown')


class SystemAdmin(admin.ModelAdmin):
    list_display = ('id', 'initials', 'name')


admin.site.register(Port, PortAdmin)
admin.site.register(System, SystemAdmin)
admin.site.register(Client, ClientAdmin)
