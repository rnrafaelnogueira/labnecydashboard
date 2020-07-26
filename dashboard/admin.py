from django.contrib import admin


# Register your models here.

from .models import OrdemServico,Cliente,Servico,ClienteServicoValor,Fornecedor,Produto,Fatura,FaturaOrdemServico,Situacao,Paciente,GruposKanban


class OrdemServicoAdmin(admin.ModelAdmin):
    list_display = ('id','id_cliente','id_paciente','data_entrada','quantidade','valor_unitario','valor_total')
    list_filter = ['id_cliente','data_entrada']
    list_per_page = 10 

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('id','nome','endereco','telefone')
    search_fields = ['nome']

class ClienteServicoValorAdmin(admin.ModelAdmin):
    list_display = ('id','id_cliente','id_servico','valor')
    search_fields = ['id_cliente']

class FaturaAdmin(admin.ModelAdmin):
    list_display = ('id','id_cliente','data_geracao','referencia','valor_fatura')
    search_fields = ['id_cliente']

class FaturaOrdemServicoAdmin(admin.ModelAdmin):
    list_display = ('id','id_fatura','id_ordem_servico','valor')
    search_fields = ['id_fatura']

admin.site.register(OrdemServico,OrdemServicoAdmin)
admin.site.register(Cliente,ClienteAdmin)
admin.site.register(Situacao)
admin.site.register(Servico)
admin.site.register(Paciente)
admin.site.register(GruposKanban)
admin.site.register(ClienteServicoValor, ClienteServicoValorAdmin)
admin.site.register(Fatura,FaturaAdmin)
admin.site.register(FaturaOrdemServico,FaturaOrdemServicoAdmin)