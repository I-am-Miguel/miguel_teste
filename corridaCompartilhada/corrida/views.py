from django.shortcuts import render, redirect

from .models import Motorista, Passageiro, Corrida
from ..core import views

# Create your views here.

def listagemMotoristas(request):
    template = 'lista.html'
    usuarios = Motorista.objects.all()
    context = {
        'nomeUsuario': 'Motoristas',
        'usuarios': usuarios,
        'genero': 'o',
    }
    return render(request, template, context)


def listagemPassageiros(request):
    template = 'lista.html'
    usuarios = Passageiro.objects.all()
    context = {
        'nomeUsuario': 'Passageiros',
        'usuarios': usuarios,
        'genero': 'o',
    }
    return render(request, template, context)


def listagemCorridas(request):
    template = 'listaCorridas.html'
    usuarios = Corrida.objects.all()
    context = {
        'nomeUsuario': 'Corridas',
        'usuarios': usuarios,
        'genero': 'a',
    }
    return render(request, template, context)


def cadastroMotoristas(request):
    if request.method == 'GET':
        return formCadastro(request)

    elif request.method == 'POST':
        motorista = Motorista.objects.create(
            nome=request.POST.get('nome'),
            data_nascimento=request.POST.get('dataNascimento'),
            cpf=request.POST.get('cpf'),
            sexo=request.POST.get('sexo'),
            modelo_carro=request.POST.get('modeloCarro'),
            ativo=(request.POST.get('modeloCarro') == 'Ativo')
        )

        motorista.save()

        return redirect('corridas:listagemMotoristas')

    return views.not_found(request)


def cadastroPassageiros(request):
    if request.method == 'GET':
        return formCadastro(request, Passageiro(), "Passageiros")

    elif request.method == 'POST':
        passageiro = Passageiro.objects.create(
            nome=request.POST.get('nome'),
            data_nascimento=request.POST.get('dataNascimento'),
            cpf=request.POST.get('cpf'),
            sexo=request.POST.get('sexo')
        )

        passageiro.save()

        return redirect('corridas:listagemPassageiros')

    return views.not_found(request)


def formCadastro(request, user=Motorista(), descricao='Motoristas'):
    template = 'cadastroUsuarios.html'
    context = {
        'nomeUsuario': descricao,
        'user': user,
    }
    return render(request, template, context)


def formCorrida(request):
    template = 'cadastroCorrida.html'

    motoristas = Motorista.objects.all()
    passageiros = Passageiro.objects.all()

    context = {
        'nomeUsuario': 'Corridas',
        'motoristas': motoristas,
        'passageiros': passageiros
    }
    return render(request, template, context)


def cadastroCorridas(request):
    if request.method == 'GET':
        return formCorrida(request)

    elif request.method == 'POST':
        motoristaCPF = str(request.POST.get('motorista')).split(' - ')[1]
        passageiroCPF = str(request.POST.get('passageiro')).split(' - ')[1]
        valor = request.POST.get('preco')

        motorista = Motorista.objects.filter(cpf=motoristaCPF).first()
        passageiro = Passageiro.objects.filter(cpf=passageiroCPF).first()

        corrida = Corrida.objects.create(
            passageiro=passageiro,
            motorista=motorista,
            valor=valor
        )

        corrida.save()

        return redirect('corridas:listagemCorridas')

    return views.not_found(request)
