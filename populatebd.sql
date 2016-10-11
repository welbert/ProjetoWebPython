INSERT INTO registro_acessorio
(descricao)
VALUES ('Mochila');
INSERT INTO registro_acessorio 
(descricao)
VALUES ('Cantil');
INSERT INTO registro_acessorio 
(descricao)
VALUES ('Sacola para dormir');
INSERT INTO registro_acessorio 
(descricao)
VALUES ('Lanterna');
INSERT INTO registro_acessorio 
(descricao)
VALUES ('Barraca');


INSERT INTO registro_armamento
(modelo,fabricante,numero_de_serie)
VALUES ('PT101','Taurus S.A.',79234);
INSERT INTO registro_armamento
(modelo,fabricante,numero_de_serie)
VALUES ('PT101','Amadeo Rossi S.A.',79234);
INSERT INTO registro_armamento
(modelo,fabricante,numero_de_serie)
VALUES ('PT101','CBC',79234);


INSERT INTO registro_municao
(calibre,descricao)
VALUES (12,'gáugio 12');
INSERT INTO registro_municao
(calibre,descricao)
VALUES (7.62,'7,62 mm NATO');
INSERT INTO registro_municao
(calibre,descricao)
VALUES (9,'9 mm Parabellum');
INSERT INTO registro_municao
(calibre,descricao)
VALUES (0.50,'.50 AE');


INSERT INTO registro_reserva
(sigla,descricao)
VALUES ('RS1','Reserva n1');
INSERT INTO registro_reserva
(sigla,descricao)
VALUES ('RS2','Reserva n2');
INSERT INTO registro_reserva
(sigla,descricao)
VALUES ('RS3','Reserva n3');


INSERT INTO registro_militar
(posto,nome_de_guerra,reserva_id)
VALUES ('Marechal','Serra',1);
INSERT INTO registro_militar
(posto,nome_de_guerra,reserva_id)
VALUES ('Cabo','Novaes',2);
INSERT INTO registro_militar
(posto,nome_de_guerra,reserva_id)
VALUES ('Soldado','Cezar',null);
INSERT INTO registro_militar
(posto,nome_de_guerra,reserva_id)
VALUES ('Coronel','Azevedo',1);
INSERT INTO registro_militar
(posto,nome_de_guerra,reserva_id)
VALUES ('Primeiro-Sargento','Camera',3);
INSERT INTO registro_militar
(posto,nome_de_guerra,reserva_id)
VALUES ('Aspirante','Souza',null);
INSERT INTO registro_militar
(posto,nome_de_guerra,reserva_id)
VALUES ('Terceiro-Sargento','Queiroz',3);