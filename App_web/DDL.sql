create table libro(
id int auto_increment,
nombre varchar(255),
precio double,
primary key (id)
);
create table vendedor(
id_vendedor int not null auto_increment,
dpi decimal(13,0) not null,
nombre varchar(50),
apellido varchar(50),
direccion varchar(250),
telefono varchar(10),
primary key (id_vendedor)
);
create table venta(
id_venta int not null auto_increment,
fecha timestamp not null,
id_libro varchar(255),
id_vendedor int not null,
primary key (id_venta),
foreign key (id_vendedor) references libro (id)
);