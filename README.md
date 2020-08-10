# clientes-web-acom

Uma ferramenta desenvolvida para gerenciar o uso de um servidor de aplicação.
A ferramenta permite o cadastro das portas do servidor (porta de acesso e shutdown), cadastro dos sistemas, e dos clientes (qual sistema, e qual porta está utilizando).

![Home](https://i.imgur.com/nzLvPId.png)
![Gerenciar](https://i.imgur.com/pVi86ga.png)

Neste projeto, foram utilizados:
Python 3.8
Django 3.0.8
Gunicorn 20.0.4
WhiteNoise 5.1.0

Para ser executado, o projeto necessita de duas variáveis de ambiente:
* CLIENTESWEBACOM_SECRET_KEY -> Chave para execução do projeto.
* DJANGO_DEBUG -> Usada para definir se o projeto será executado em modo debug ou não.
