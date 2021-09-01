create table libro(
id int not null auto_increment,
nombre varchar(255) not null,
precio double not null,
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
id_libro int not null,
id_vendedor int not null,
primary key (id_venta),
foreign key (id_libro) references libro (id)
foreign key (id_vendedor) references vendedor (id_vendedor)
);