drop database pythonapps;
create database pythonapps;
use pythonapps;

create table users(
	id int auto_increment primary key,
    username varchar(100) not null,
    name varchar(255) not null,
    password varchar(100) not null
);

insert into users (username, name, password) values ("ederson", "Ederson", "123456"), ("edini", "Édini", "123456"), ("enilda", "Enilda", "123456");

create table categories (
	id int auto_increment primary key,
    description varchar(100) not null
);

create table products (
	id int auto_increment primary key,
    description varchar(100) not null,
    price float not null,
    category_id int not null,
    constraint foreign key (category_id) references categories(id)
);

create table cart (
	id int auto_increment primary key,
    product_id int not null,
    constraint foreign key (product_id) references products(id)
);

-- Inserir categorias
INSERT INTO categories (description) VALUES
('Entradas'),
('Pratos Principais'),
('Bebidas'),
('Bebidas Alcoólicas'),
('Sobremesas'),
('Menu do Chef');

-- Inserir produtos para a categoria 'Entradas'
INSERT INTO products (description, price, category_id) VALUES
('Bruschetta', 12.50, (SELECT id FROM categories WHERE description = 'Entradas')),
('Crostini', 15.00, (SELECT id FROM categories WHERE description = 'Entradas')),
('Azeitonas Temperadas', 8.00, (SELECT id FROM categories WHERE description = 'Entradas')),
('Salada Caprese', 14.00, (SELECT id FROM categories WHERE description = 'Entradas')),
('Sopa de Tomate', 11.00, (SELECT id FROM categories WHERE description = 'Entradas'));

-- Inserir produtos para a categoria 'Pratos Principais'
INSERT INTO products (description, price, category_id) VALUES
('Filé Mignon', 45.00, (SELECT id FROM categories WHERE description = 'Pratos Principais')),
('Risoto de Cogumelos', 38.00, (SELECT id FROM categories WHERE description = 'Pratos Principais')),
('Espaguete à Carbonara', 32.00, (SELECT id FROM categories WHERE description = 'Pratos Principais')),
('Peito de Frango Grelhado', 28.00, (SELECT id FROM categories WHERE description = 'Pratos Principais')),
('Salmão ao Molho de Limão', 42.00, (SELECT id FROM categories WHERE description = 'Pratos Principais'));

-- Inserir produtos para a categoria 'Bebidas'
INSERT INTO products (description, price, category_id) VALUES
('Água Mineral', 5.00, (SELECT id FROM categories WHERE description = 'Bebidas')),
('Refrigerante', 6.00, (SELECT id FROM categories WHERE description = 'Bebidas')),
('Suco de Laranja', 7.00, (SELECT id FROM categories WHERE description = 'Bebidas')),
('Chá Gelado', 6.50, (SELECT id FROM categories WHERE description = 'Bebidas')),
('Água de Coco', 8.00, (SELECT id FROM categories WHERE description = 'Bebidas'));

-- Inserir produtos para a categoria 'Bebidas Alcoólicas'
INSERT INTO products (description, price, category_id) VALUES
('Cerveja Artesanal', 10.00, (SELECT id FROM categories WHERE description = 'Bebidas Alcoólicas')),
('Vinho Tinto', 45.00, (SELECT id FROM categories WHERE description = 'Bebidas Alcoólicas')),
('Vinho Branco', 40.00, (SELECT id FROM categories WHERE description = 'Bebidas Alcoólicas')),
('Whisky', 80.00, (SELECT id FROM categories WHERE description = 'Bebidas Alcoólicas')),
('Margarita', 15.00, (SELECT id FROM categories WHERE description = 'Bebidas Alcoólicas'));

-- Inserir produtos para a categoria 'Sobremesas'
INSERT INTO products (description, price, category_id) VALUES
('Cheesecake', 12.00, (SELECT id FROM categories WHERE description = 'Sobremesas')),
('Tiramisu', 14.00, (SELECT id FROM categories WHERE description = 'Sobremesas')),
('Brownie com Sorvete', 13.00, (SELECT id FROM categories WHERE description = 'Sobremesas')),
('Mousse de Chocolate', 11.00, (SELECT id FROM categories WHERE description = 'Sobremesas')),
('Pavê de Frutas', 10.00, (SELECT id FROM categories WHERE description = 'Sobremesas'));

-- Inserir produtos para a categoria 'Menu do Chef'
INSERT INTO products (description, price, category_id) VALUES
('Prato do Dia', 50.00, (SELECT id FROM categories WHERE description = 'Menu do Chef')),
('Menu Degustação', 75.00, (SELECT id FROM categories WHERE description = 'Menu do Chef')),
('Especialidade do Chef', 60.00, (SELECT id FROM categories WHERE description = 'Menu do Chef')),
('Menu Executivo', 45.00, (SELECT id FROM categories WHERE description = 'Menu do Chef')),
('Jantar Romântico', 85.00, (SELECT id FROM categories WHERE description = 'Menu do Chef'));
