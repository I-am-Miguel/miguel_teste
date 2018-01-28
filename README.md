# Miguel_teste 

## App-Corrida-Compartilhada

Este projeto foi gerado com [Django](https://github.com/django/django) version 1.8.5.

#### Set Up
Clone esse projeto:

`$ git clone https://github.com/I-am-Miguel/miguel_teste.git`

`$ cd miguel_teste`

Crie um ambiente virtual e instale as dependências:
`$ virtualenv venv`

`(venv)$ source /venv/bin/activate`

`(venv)$ pip install -r requeriments.txt`

## Servidor de desenvolvimento

`(venv)$ python manage.py makemigrations && python manage.py migrate` para rodar o sincronizar os models ecriar o banco de desenvolvimento`. 

`(venv)$ python manage.py runserver` para rodar o servidor de desenvolvimento. Navegar para `http://localhost:8000/`.

### Help

Para obter mais ajuda sobre o uso do django `python manage.py help` ou acesse [DJANGO README](https://github.com/django/django/blob/master/README.rst).
