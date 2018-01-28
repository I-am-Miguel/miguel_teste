from django.db import models


class Passageiro(models.Model):
    nome = models.CharField('Nome', max_length=40, null=False)
    data_nascimento = models.DateField('DataNascimento', null=False)
    cpf = models.CharField('CPF', max_length=11, null=False)
    sexo = models.CharField('Sexo', max_length=1, null=False)

    def __str__(self):
        return "{} - {}".format(self.nome, self.cpf)

    @models.permalink
    def cadastroUsuario(self):
        return ('corridas:cadastroPassageiros', (), {})


class Motorista(models.Model):
    nome = models.CharField('Nome', max_length=40, null=False)
    data_nascimento = models.DateField('DataNascimento', null=False)
    cpf = models.CharField('CPF', max_length=11, null=False)
    sexo = models.CharField('Sexo', max_length=1, null=False)
    ativo = models.BooleanField('Ativo', default=True)
    modelo_carro = models.CharField('ModeloCarro', max_length=40)

    def __str__(self):
        return "{} - {} - {}".format(self.nome, self.cpf, self.modelo_carro)

    @models.permalink
    def cadastroUsuario(self):
        return ('corridas:cadastroMotoristas', (), {})


class Corrida(models.Model):
    motorista = models.ForeignKey(Motorista)
    passageiro = models.ForeignKey(Passageiro)
    valor = models.DecimalField('Valor', decimal_places=2, max_digits=10)

    def __str__(self):
        return "Motorista: {} Passageiro: {} Preço: {}".format(self.motorista.nome, self.passageiro.nome, self.valor)

    @models.permalink
    def cadastro(self):
        return ('corridas:cadastroCorridas', (), {})
