from django.contrib import admin
from .models import *


class CorridaAdmin(admin.ModelAdmin):
    list_display = ['motorista', 'passageiro', 'valor']
    search_fields = ['motorista', 'passageiro', 'valor']
    fieldsets = [
        ('Motorista', {'fields': ['motorista']}),
        ('Passageiro', {'fields': ['passageiro']}),
        ('Valor', {'fields': ['valor']}),

    ]

    def user_id(self, obj):
        obj.user_id.admin_order_field = 'user__id'
        return obj.user.id


# '''

admin.site.register(Corrida, CorridaAdmin)
admin.site.register(Motorista)
admin.site.register(Passageiro)