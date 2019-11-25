from django.contrib import admin

# Register your models here.

from .models import OrdemServico,Cliente,Servico,ClienteServicoValor,Fornecedor,Produto,Fatura,FaturaOrdemServico,Situacao,Paciente,GruposKanban


class OrdemServicoAdmin(admin.ModelAdmin):
    list_display = ('id_cliente', 'id_situacao')
    list_filter = ['id_cliente']

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome','endereco','telefone')
    search_fields = ['nome']


class ClienteServicoValorAdmin(admin.ModelAdmin):
    list_display = ('id_cliente','id_servico','valor')
    search_fields = ['id_cliente']

admin.site.register(OrdemServico,OrdemServicoAdmin)
admin.site.register(Cliente,ClienteAdmin)
admin.site.register(Situacao)
admin.site.register(Servico)
admin.site.register(Paciente)
admin.site.register(GruposKanban)
admin.site.register(ClienteServicoValor, ClienteServicoValorAdmin)
admin.site.register(Fatura)
admin.site.register(FaturaOrdemServico)