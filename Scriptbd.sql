CREATE DATABASE tienda_online;

USE tienda_online;

CREATE TABLE Producto (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    descripcion TEXT,
    precio DECIMAL(10, 2) NOT NULL
);

CREATE TABLE Carrito (
    id INT AUTO_INCREMENT PRIMARY KEY
);

CREATE TABLE ItemCarrito (
    id INT AUTO_INCREMENT PRIMARY KEY,
    producto_id INT NOT NULL,
    carrito_id INT NOT NULL,
    cantidad INT NOT NULL,
    FOREIGN KEY (producto_id) REFERENCES Producto(id),
    FOREIGN KEY (carrito_id) REFERENCES Carrito(id)
);

CREATE TABLE Pedido (
    id INT AUTO_INCREMENT PRIMARY KEY,
    carrito_id INT NOT NULL,
    direccion_entrega TEXT NOT NULL,
    total DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (carrito_id) REFERENCES Carrito(id)
);



show tables;