# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.models import User
import logging
from django.utils.timezone import now
from datetime import datetime, timedelta

class Categoria(models.Model):
    nome = models.TextField()
    detalhes = models.TextField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.nome

    class Meta:
        managed = True
        db_table = 'categoria'


class Cliente(models.Model):
    nome = models.TextField()
    endereco = models.TextField()
    telefone = models.TextField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    def __str__(self):
        return self.nome

    def save(self, *args, **kwargs):
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        super().save(*args, **kwargs)

    class Meta:
        managed = True
        db_table = 'cliente'

class Despesa(models.Model):
    nome = models.TextField()
    id_categoria = models.ForeignKey(Categoria, models.DO_NOTHING, db_column='id_categoria')
    id_user = models.ForeignKey('Users', models.DO_NOTHING, db_column='id_user')
    valor_fixo = models.FloatField()
    data_recibo = models.DateTimeField()
    mes = models.IntegerField(blank=True, null=True)
    ano = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.nome
        

    class Meta:
        managed = True
        db_table = 'despesa'


class Fornecedor(models.Model):
    nome = models.TextField()
    endereco = models.TextField(blank=True, null=True)
    telefone = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.nome

    class Meta:
        managed = True
        db_table = 'fornecedor'


class GruposKanban(models.Model):
    nome = models.TextField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.nome

    class Meta:
        managed = True
        db_table = 'grupos_kanban'


class Mes(models.Model):
    descricao = models.TextField()
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.descricao

    class Meta:
        managed = True
        db_table = 'mes'

class OrdemCompra(models.Model):
    descricao = models.TextField()
    id_fornecedor = models.IntegerField()
    id_situacao = models.IntegerField()
    id_grupo_kanban = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.descricao

    def save(self, *args, **kwargs):
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        super().save(*args, **kwargs)

    class Meta:
        managed = True
        db_table = 'ordem_compra'

class OrdemCompraParcelas(models.Model):
    parcela = models.IntegerField()
    valor = models.IntegerField()
    data_vencimento = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    id_ordem_compra = models.TextField()

    def save(self, *args, **kwargs):
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.parcela

    class Meta:
        managed = True
        db_table = 'ordem_compra_parcelas'

class OrdemCompraProdutos(models.Model):
    id_ordem_compra = models.IntegerField()
    id_produto = models.IntegerField()
    quantidade = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    def save(self, *args, **kwargs):
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        super().save(*args, **kwargs)

    class Meta:
        managed = True
        db_table = 'ordem_compra_produtos'

class Paciente(models.Model):
    nome = models.TextField()
    observacao = models.TextField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.nome

    def save(self, *args, **kwargs):
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        super().save(*args, **kwargs)

    class Meta:
        managed = True
        db_table = 'paciente'

class Pagamento(models.Model):
    valor = models.FloatField()
    descricao = models.TextField(blank=True, null=True)
    data_recibo = models.DateTimeField()
    recibo = models.TextField(blank=True, null=True)
    id_despesa = models.ForeignKey(Despesa, models.DO_NOTHING, db_column='id_despesa', blank=True, null=True)
    mes = models.ForeignKey(Mes, models.DO_NOTHING, db_column='mes', blank=True, null=True)
    ano = models.IntegerField(blank=True, null=True)
    data_cadastro = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    def save(self, *args, **kwargs):
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        super().save(*args, **kwargs)

    class Meta:
        managed = True
        db_table = 'pagamento'

class Produto(models.Model):
    nome = models.TextField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    def save(self, *args, **kwargs):
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        super().save(*args, **kwargs)

    class Meta:
        managed = True
        db_table = 'produto'


class Receita(models.Model):
    valor = models.FloatField()
    tipo_receita = models.ForeignKey('TipoReceita', models.DO_NOTHING, db_column='tipo_receita')
    mes = models.ForeignKey(Mes, models.DO_NOTHING, db_column='mes')
    data_cadastro = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    id_user = models.ForeignKey('Users', models.DO_NOTHING, db_column='id_user')
    ano = models.IntegerField(blank=True, null=True)
    nome = models.TextField(blank=True, null=True)
    data_recibo = models.DateTimeField(blank=True, null=True)

    def save(self, *args, **kwargs):
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        super().save(*args, **kwargs)

    class Meta:
        managed = True
        db_table = 'receita'


class Servico(models.Model):
    nome = models.TextField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    def __str__(self):
        return self.nome

    def save(self, *args, **kwargs):
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        super().save(*args, **kwargs)

    class Meta:
        managed = True
        db_table = 'servico'


class Situacao(models.Model):
    nome = models.TextField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.nome

    def save(self, *args, **kwargs):
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        super().save(*args, **kwargs)

    class Meta:
        managed = True
        db_table = 'situacao'


class TipoReceita(models.Model):
    descricao = models.TextField()
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    def save(self, *args, **kwargs):
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        super().save(*args, **kwargs)

    class Meta:
        managed = True
        db_table = 'tipo_receita'


class Users(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(unique=True, max_length=255)
    password = models.CharField(max_length=255)
    remember_token = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    cpf = models.TextField(blank=True, null=True)

    def save(self, *args, **kwargs):
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        super().save(*args, **kwargs)

    class Meta:
        managed = True
        db_table = 'users'
        
class ClienteServicoValor(models.Model):
    id_cliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='id_cliente')
    id_servico = models.ForeignKey(Servico, models.DO_NOTHING, db_column='id_servico')
    valor = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.id

    def save(self, *args, **kwargs):
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        super().save(*args, **kwargs)

    class Meta:
        db_table = 'cliente_servico_valor'

class OrdemServico(models.Model):

    BOOL_CHOICES = (('S', 'Sim'), ('N', 'Não'))

    id_cliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='id_cliente')
    id_paciente = models.ForeignKey(Paciente, models.DO_NOTHING, db_column='id_paciente')
    id_servico = models.ForeignKey(Servico, models.DO_NOTHING, db_column='id_servico')
    id_situacao = models.ForeignKey(Situacao, models.DO_NOTHING, db_column='id_situacao',default='5')
    id_grupo_kanban = models.ForeignKey(GruposKanban, models.DO_NOTHING, db_column='id_grupo_kanban',default='11')
    data_entrada = models.DateTimeField(blank=True, null=True)
    data_previsao_entrega = models.DateTimeField(blank=True, null=True)
    quantidade = models.IntegerField()
    hora_previsao_entrega = models.TextField(blank=True, null=True)
    cor = models.TextField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    valor_padrao = models.CharField(max_length=1,choices=BOOL_CHOICES)
    valor_total = models.IntegerField(blank=True, null=True)
    valor_unitario = models.IntegerField(blank=True, null=True)

    def __int__(self):
        return self.id

    def save(self, *args, **kwargs):

        if (self.valor_padrao == 'S'):
            for e in ClienteServicoValor.objects.filter(id_cliente = self.id_cliente, id_servico=self.id_servico):
                self.valor_unitario = e.valor
        
        self.data_entrada = datetime.now()
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.data_previsao_entrega = datetime.now() + timedelta(days=3)
        self.valor_total = self.quantidade * self.valor_unitario
        super().save(*args, **kwargs)

    class Meta:
        db_table = 'ordem_servico'

class Fatura(models.Model):
    id_cliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='id_cliente')
    data_geracao = models.DateTimeField(blank=True, null=True)
    referencia = models.TextField()
    enviada = models.CharField(max_length=1)
    baixada = models.CharField(max_length=1)
    valor_fatura = models.FloatField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    def __int__(self):
        return self.id

    def save(self, *args, **kwargs):
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        super().save(*args, **kwargs)

    class Meta:
        db_table = 'fatura'

class FaturaOrdemServico(models.Model):
    id_fatura = models.ForeignKey(Fatura, models.DO_NOTHING, db_column='id_fatura')
    id_ordem_servico = models.ForeignKey(OrdemServico, models.DO_NOTHING, db_column='id_ordem_servico')
    valor = models.FloatField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    def __int__(self):
        return self.id

    def save(self, *args, **kwargs):
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        super().save(*args, **kwargs)
        
    class Meta:
        db_table = 'fatura_ordem_servico'
