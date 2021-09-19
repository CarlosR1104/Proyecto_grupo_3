create database muebles_valencia;
use Muebles_Valencia;
create table Productos
(codigoProd int primary key auto_increment not null,
nombreProd varchar(50),
precio DECIMAL(9,2) NOT NULL
descripcionProd varchar(255),
fotoProd varchar(255)
);
create table Administrador
(codigoAdmin int primary key auto_increment not null,
username varchar(255),
correo varchar(255),
password int
);

create table Clientes
(codigoCli int primary key auto_increment not null,
cedula int unique,
nombreCli varchar(55),
apellidoCli varchar(55),
fechaNaciminCli date,
celular int
);

create table Usuarios
(codigoUsua int primary key auto_increment not null,
correoUsua varchar(255),
username varchar(255),
password int
);

