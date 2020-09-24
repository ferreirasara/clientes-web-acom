from django.contrib import admin
from .models import Port, System, Client, Note, Server


class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'link', 'port', 'system', 'version', 'status')


class PortAdmin(admin.ModelAdmin):
    list_display = ('id', 'connector', 'shutdown', 'server')


class SystemAdmin(admin.ModelAdmin):
    list_display = ('id', 'initials', 'name')


class NoteAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'text')


class ServerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'acomServer')


admin.site.register(Port, PortAdmin)
admin.site.register(System, SystemAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Note, NoteAdmin)
admin.site.register(Server, ServerAdmin)
