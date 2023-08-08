CREATE TABLE registro_usuarios (
	id serial PRIMARY KEY,
	usuario VARCHAR ( 50 ) NOT NULL,
	contrasena VARCHAR ( 255 ) NOT NULL,
	nombrecompleto VARCHAR ( 100 ) NOT NULL,
	email VARCHAR ( 50 ) NOT NULL
);