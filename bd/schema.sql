CREATE TABLE rol (
    id_rol INT PRIMARY KEY AUTO_INCREMENT,
    nombre_rol VARCHAR(255)
);
CREATE TABLE usuario (
    id_usuario INT PRIMARY KEY AUTO_INCREMENT,
    rut VARCHAR(255) UNIQUE,
    nombre VARCHAR(255),
    password VARCHAR(255),
    id_rol INT
);
CREATE TABLE bodega (
    id_bodega INT PRIMARY KEY AUTO_INCREMENT,
    nombre_bodega VARCHAR(255),
    direccion VARCHAR(255)
);
CREATE TABLE autor (
    id_autor INT PRIMARY KEY AUTO_INCREMENT,
    nombre_autor VARCHAR(255)
);
CREATE TABLE editorial (
    id_editorial INT PRIMARY KEY AUTO_INCREMENT,
    nombre_editorial VARCHAR(255)
);
CREATE TABLE producto (
    id_producto INT PRIMARY KEY AUTO_INCREMENT,
    titulo VARCHAR(255),
    tipo VARCHAR(255),
    descripcion TEXT,
    stock_total INT,
    stock_minimo INT,
    id_autor INT,
    id_editorial INT,
    id_bodega INT
);
CREATE TABLE movimiento (
    id_movimiento INT PRIMARY KEY AUTO_INCREMENT,
    fecha DATETIME,
    cantidad INT,
    id_usuario INT,
    id_producto INT,
    id_bodega_origen INT,
    id_bodega_destino INT
);
CREATE TABLE log_accion (
    id_log INT PRIMARY KEY AUTO_INCREMENT,
    fecha DATETIME,
    accion VARCHAR(255),
    id_usuario INT
);
ALTER TABLE usuario
ADD FOREIGN KEY (id_rol) REFERENCES rol (id_rol);
ALTER TABLE producto
ADD FOREIGN KEY (id_autor) REFERENCES autor (id_autor);
ALTER TABLE producto
ADD FOREIGN KEY (id_editorial) REFERENCES editorial (id_editorial);
ALTER TABLE producto
ADD FOREIGN KEY (id_bodega) REFERENCES bodega (id_bodega);
ALTER TABLE movimiento
ADD FOREIGN KEY (id_usuario) REFERENCES usuario (id_usuario);
ALTER TABLE movimiento
ADD FOREIGN KEY (id_producto) REFERENCES producto (id_producto);
ALTER TABLE movimiento
ADD FOREIGN KEY (id_bodega_origen) REFERENCES bodega (id_bodega);
ALTER TABLE movimiento
ADD FOREIGN KEY (id_bodega_destino) REFERENCES bodega (id_bodega);
ALTER TABLE log_accion
ADD FOREIGN KEY (id_usuario) REFERENCES usuario (id_usuario);