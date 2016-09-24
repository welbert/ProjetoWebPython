# Projeto LabWeb
## Linguagem: Python ; Framework: django

python manage.py runserver

[http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

User: admin
Pass: virtualbox



# TODO 
_
- [x] Login/Logout
- [x] Menu de opções
- [x] **Tela(Simples)** Usuário (nome completo, login, senha, email);
- [x] **Tela(Simples)** Reserva (sigla, descrição);
- [x] **Tela(Simples)** Munição (calibre, descrição);
- [x] **Tela(Simples)** Militar (posto/graduação, nome de guerra);
- [ ] **Tela(Integração)** ReservaMaterial (cadastro de armamento, munição e acessórios com suas respectivas quantidades na reserva de armamento)
- [ ] **Tela Cautela(Integração)** (controle da retirada do armamento pelos militares, com: militar, armamentos e munições)
- [ ] **Regra(Negócio)** Um militar da reserva de armamento cadastra todos os armamentos, munições e acessórios (lanterna, mascara de gás,coldre, bandoleira, etc) e em seguida (em Manter Reserva Material) informa quanto ele tem de cada equipamento na reserva.
- [ ] **Regra(Negócio)** Um outro militar pode se dirigir a reserva de armamento para cautelar armamento(s), munição e/ou acessórios. Nesse momento o militar da reserva registra essa retirada (Manter Cautela) informando o militar e tudo que ele está retirando, nesse momento é feito um registro com data, hora, militar responsável e todo o material retirado.
- [ ] **Regra(Negócio)** Quando o militar retorna a reserva de armamento para devolver o material, é dado a baixa no equipamento. Esse material pode ser devolvido aos poucos.

