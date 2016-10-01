> # Projeto LabWeb
## Linguagem: Python ; Framework: [Django](https://www.djangoproject.com/)

### Equipe:
  * Bruno Novaes
  * Diego Novaes
  * Iran Cezar
  * Welbert Serra

### Instalando
1. Descompacte o arquivo  django.tar.gz

ou

1. pip install Django==1.10.1

ou

1. git clone https://github.com/django/django.git
2. mv django/django/ ProjectFolder

### Executando

python manage.py runserver

[http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

User: admin
Pass: virtualbox



> # TODO 

- [ ] Cronograma
- [ ] Material Escrito
  - [ ] Capa
  - [ ] Contracapa com tema, equipe, dados da disciplina e demais informações pertinentes ao tema. 
  - [ ] Diagrama de Classes
  - [x] Entidade e Relacionamento 
- [ ] Slides
- [x] *Login/Logout*
- [x] *Menu de opções*
- [ ] **Tela(Simples)** *Usuário* (nome completo, login, senha, email);
- [ ] **Tela(Simples)** *Armamento* (nº de série, modelo, fabricante);
- [ ] **Tela(Simples)** *Acessórios* (descrição);
- [ ] **Tela(Simples)** *Munição* (calibre, descrição);
- [ ] **Tela(Simples)** *Produto* ('Armamento/Acessórios/Munição'[Classe Genérica]);
- [ ] **Tela(Simples)** *Reserva* (sigla, descrição);
- [ ] **Tela(Simples)** *Militar* (posto/graduação, nome de guerra);
- [ ] **Tela(Integração)** *ReservaMaterial* (cadastro de armamento, munição e acessórios com suas respectivas quantidades na reserva de armamento)
- [ ] **Tela(Integração)** *Cautela* (controle da retirada do armamento pelos militares, com: militar, armamentos e munições)
- [ ] **Regra(Negócio)** Um militar da reserva de armamento cadastra todos os armamentos, munições e acessórios (lanterna, mascara de gás,coldre, bandoleira, etc) e em seguida (em Manter Reserva Material) informa quanto ele tem de cada equipamento na reserva.
- [ ] **Regra(Negócio)** Um outro militar pode se dirigir a reserva de armamento para cautelar armamento(s), munição e/ou acessórios. Nesse momento o militar da reserva registra essa retirada (Manter Cautela) informando o militar e tudo que ele está retirando, nesse momento é feito um registro com data, hora, militar responsável e todo o material retirado.
- [ ] **Regra(Negócio)** Quando o militar retorna a reserva de armamento para devolver o material, é dado a baixa no equipamento. Esse material pode ser devolvido aos poucos.

