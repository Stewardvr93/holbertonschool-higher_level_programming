-- Creamos la bd, la usamos, y generamos una tabla con un id que autoincremente con el pasar de
-- las inserciones, el cual es una llave primaria.
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states (id INT UNIQUE NOT NULL AUTO_INCREMENT, name VARCHAR(256) NOT NULL, PRIMARY KEY(id));
