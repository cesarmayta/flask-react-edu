-- Active: 1678156802741@@127.0.0.1@3306@db_perudemy_g19
insert into tbl_curso_topico(curtop_descripcion,curso_id)
values ('INTRODUCCIÓN A PYTHON',1),
('INTRODUCCIÓN A MYSQL',2),
('INTRODUCCIÓN A FLASK',4);

insert into tbl_curso_topico_clase(curtopcla_descripcion,curtopcla_duracion,curtop_id)
VALUES
('QUE ES PYTHON',10,1),('INSTALACIÓN DE PYTHON',10,1),('HOLA MUNDO CON PYTHON',10,1),
('QUE ES MYSQL',10,2),('INSTALACIÓN DE MYSQL',10,2),('CREANDO PRIMERAS TABLAS',10,2),
('QUE ES FLASK',10,3),('INSTALACIÓN DE FLASK',10,3),('HOLA MUNDO CON FLASK',10,3);
