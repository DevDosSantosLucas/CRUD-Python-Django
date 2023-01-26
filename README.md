no CMD:
C:\www\django\crud> python -m venv cliente1  ==> cliente1 pode ser nome qualquer

C:\www\django\crud>cd client1\Scripts

C:\www\django\crud\client1\Scripts>activate
irá ativar o servidor:
(client1) C:\www\django\crud\client1\Scripts>

agora instala o django:
pip install django
(client1) C:\www\django\crud\client1\Scripts>cd ../../
(client1) C:\www\django\crud>pip install django

instalar projeto django:
(client1) C:\www\django\crud>django-admin startproject app .   => o ponto (.) serve para não criar subpasta app

(client1) C:\www\django\crud>python manage.py runserver 
    ctrl+c para sair no cmd

config do banco:
(client1) C:\www\django\crud>python manage.py migrate 
(client1) C:\www\django\crud>python manage.py createsuperuser admin 
(client1) C:\www\django\crud>python manage.py createsuperuser
digitar user e senha

(client1) C:\www\django\crud>python manage.py runserver 
Ao entrar no http://localhost:8001/admin/
podera logar com o user criado

(client1) C:\www\django\crud>python manage.py startapp crud 
em app/urls.py: path('crud/', include('crud.urls'))
- criar urls.py em core

criar arquivos na pasta migrations atraves dos models criados
(client1) C:\www\django\crud>python manage.py makemigrations 
cria tabela no banco :
(client1) C:\www\django\crud>python manage.py migrate



