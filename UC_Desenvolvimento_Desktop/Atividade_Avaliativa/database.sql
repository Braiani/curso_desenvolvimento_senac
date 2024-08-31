-- Remover o banco de dados existente e criar um novo
drop database if exists pythonapps;
create database if not exists pythonapps;
use pythonapps;

-- Criar a tabela users
create table users (
    id int auto_increment primary key,
    username varchar(100) not null,
    name varchar(255) not null,
    password varchar(100) not null
);

insert into users (username, name, password) values 
    ("ederson", "Ederson", "123456"), 
    ("edini", "Edini", "123456"), 
    ("enilda", "Enilda", "123456");

-- Criar a tabela categories
create table categories (
    id int auto_increment primary key,
    description varchar(100) not null
);

-- Criar a tabela products com um campo de imagem em Base64
create table products (
    id int auto_increment primary key,
    description varchar(100) not null,
    price float not null,
    category_id int not null,
    image text,  -- Alterado nome do campo de image_base64 para image
    constraint foreign key (category_id) references categories(id)
);

-- Criar a tabela cart
create table cart (
    id int auto_increment primary key,
    product_id int not null,
    quantity int default(1),
    status enum('open', 'closed') default('open'),
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
INSERT INTO products (description, price, category_id, image) VALUES
    ('Bruschetta', 12.50, (SELECT id FROM categories WHERE description = 'Entradas'), "https://www.marba.com.br/wp-content/uploads/2022/09/bruschetta-de-mortadela-marba-superiore-azeitona.png"),
    ('Crostini', 15.00, (SELECT id FROM categories WHERE description = 'Entradas'), "https://www.marba.com.br/wp-content/uploads/2022/09/bruschetta-de-mortadela-marba-superiore-azeitona.png"),
    ('Azeitonas Temperadas', 8.00, (SELECT id FROM categories WHERE description = 'Entradas'), "https://www.marba.com.br/wp-content/uploads/2022/09/bruschetta-de-mortadela-marba-superiore-azeitona.png"),
    ('Salada Caprese', 14.00, (SELECT id FROM categories WHERE description = 'Entradas'), "https://www.marba.com.br/wp-content/uploads/2022/09/bruschetta-de-mortadela-marba-superiore-azeitona.png"),
    ('Sopa de Tomate', 11.00, (SELECT id FROM categories WHERE description = 'Entradas'), "https://www.marba.com.br/wp-content/uploads/2022/09/bruschetta-de-mortadela-marba-superiore-azeitona.png");

-- Inserir produtos para a categoria 'Pratos Principais'
INSERT INTO products (description, price, category_id, image) VALUES
    ('Filé Mignon', 45.00, (SELECT id FROM categories WHERE description = 'Pratos Principais'), "https://www.marba.com.br/wp-content/uploads/2022/09/bruschetta-de-mortadela-marba-superiore-azeitona.png"),
    ('Risoto de Cogumelos', 38.00, (SELECT id FROM categories WHERE description = 'Pratos Principais'), "https://www.marba.com.br/wp-content/uploads/2022/09/bruschetta-de-mortadela-marba-superiore-azeitona.png"),
    ('Espaguete à Carbonara', 32.00, (SELECT id FROM categories WHERE description = 'Pratos Principais'), "https://www.marba.com.br/wp-content/uploads/2022/09/bruschetta-de-mortadela-marba-superiore-azeitona.png"),
    ('Peito de Frango Grelhado', 28.00, (SELECT id FROM categories WHERE description = 'Pratos Principais'), "https://www.marba.com.br/wp-content/uploads/2022/09/bruschetta-de-mortadela-marba-superiore-azeitona.png"),
    ('Salmão ao Molho de Limão', 42.00, (SELECT id FROM categories WHERE description = 'Pratos Principais'), "https://www.marba.com.br/wp-content/uploads/2022/09/bruschetta-de-mortadela-marba-superiore-azeitona.png");

-- Inserir produtos para a categoria 'Bebidas'
INSERT INTO products (description, price, category_id, image) VALUES
    ('Água Mineral', 5.00, (SELECT id FROM categories WHERE description = 'Bebidas'), "https://www.marba.com.br/wp-content/uploads/2022/09/bruschetta-de-mortadela-marba-superiore-azeitona.png"),
    ('Refrigerante', 6.00, (SELECT id FROM categories WHERE description = 'Bebidas'), "https://www.marba.com.br/wp-content/uploads/2022/09/bruschetta-de-mortadela-marba-superiore-azeitona.png"),
    ('Suco de Laranja', 7.00, (SELECT id FROM categories WHERE description = 'Bebidas'), "https://www.marba.com.br/wp-content/uploads/2022/09/bruschetta-de-mortadela-marba-superiore-azeitona.png"),
    ('Chá Gelado', 6.50, (SELECT id FROM categories WHERE description = 'Bebidas'), "https://www.marba.com.br/wp-content/uploads/2022/09/bruschetta-de-mortadela-marba-superiore-azeitona.png"),
    ('Água de Coco', 8.00, (SELECT id FROM categories WHERE description = 'Bebidas'), "https://www.marba.com.br/wp-content/uploads/2022/09/bruschetta-de-mortadela-marba-superiore-azeitona.png");

-- Inserir produtos para a categoria 'Bebidas Alcoólicas'
INSERT INTO products (description, price, category_id, image) VALUES
    ('Cerveja Artesanal', 10.00, (SELECT id FROM categories WHERE description = 'Bebidas Alcoólicas'), "https://www.marba.com.br/wp-content/uploads/2022/09/bruschetta-de-mortadela-marba-superiore-azeitona.png"),
    ('Vinho Tinto', 45.00, (SELECT id FROM categories WHERE description = 'Bebidas Alcoólicas'), "https://www.marba.com.br/wp-content/uploads/2022/09/bruschetta-de-mortadela-marba-superiore-azeitona.png"),
    ('Vinho Branco', 40.00, (SELECT id FROM categories WHERE description = 'Bebidas Alcoólicas'), "https://www.marba.com.br/wp-content/uploads/2022/09/bruschetta-de-mortadela-marba-superiore-azeitona.png"),
    ('Whisky', 80.00, (SELECT id FROM categories WHERE description = 'Bebidas Alcoólicas'), "https://www.marba.com.br/wp-content/uploads/2022/09/bruschetta-de-mortadela-marba-superiore-azeitona.png"),
    ('Margarita', 15.00, (SELECT id FROM categories WHERE description = 'Bebidas Alcoólicas'), "https://www.marba.com.br/wp-content/uploads/2022/09/bruschetta-de-mortadela-marba-superiore-azeitona.png");

-- Inserir produtos para a categoria 'Sobremesas'
INSERT INTO products (description, price, category_id, image) VALUES
    ('Cheesecake', 12.00, (SELECT id FROM categories WHERE description = 'Sobremesas'), "https://www.marba.com.br/wp-content/uploads/2022/09/bruschetta-de-mortadela-marba-superiore-azeitona.png"),
    ('Tiramisu', 14.00, (SELECT id FROM categories WHERE description = 'Sobremesas'), "https://www.marba.com.br/wp-content/uploads/2022/09/bruschetta-de-mortadela-marba-superiore-azeitona.png"),
    ('Brownie com Sorvete', 13.00, (SELECT id FROM categories WHERE description = 'Sobremesas'), "https://www.marba.com.br/wp-content/uploads/2022/09/bruschetta-de-mortadela-marba-superiore-azeitona.png"),
    ('Mousse de Chocolate', 11.00, (SELECT id FROM categories WHERE description = 'Sobremesas'), "https://www.marba.com.br/wp-content/uploads/2022/09/bruschetta-de-mortadela-marba-superiore-azeitona.png"),
    ('Pavê de Frutas', 10.00, (SELECT id FROM categories WHERE description = 'Sobremesas'), "https://www.marba.com.br/wp-content/uploads/2022/09/bruschetta-de-mortadela-marba-superiore-azeitona.png");

-- Inserir produtos para a categoria 'Menu do Chef'
INSERT INTO products (description, price, category_id, image) VALUES
    ('Prato do Dia', 50.00, (SELECT id FROM categories WHERE description = 'Menu do Chef'), "https://www.marba.com.br/wp-content/uploads/2022/09/bruschetta-de-mortadela-marba-superiore-azeitona.png"),
    ('Menu Degustação', 75.00, (SELECT id FROM categories WHERE description = 'Menu do Chef'), "https://www.marba.com.br/wp-content/uploads/2022/09/bruschetta-de-mortadela-marba-superiore-azeitona.png"),
    ('Especialidade do Chef', 60.00, (SELECT id FROM categories WHERE description = 'Menu do Chef'), "https://www.marba.com.br/wp-content/uploads/2022/09/bruschetta-de-mortadela-marba-superiore-azeitona.png"),
    ('Menu Executivo', 45.00, (SELECT id FROM categories WHERE description = 'Menu do Chef'), "https://www.marba.com.br/wp-content/uploads/2022/09/bruschetta-de-mortadela-marba-superiore-azeitona.png"),
    ('Jantar Romântico', 85.00, (SELECT id FROM categories WHERE description = 'Menu do Chef'), "https://www.marba.com.br/wp-content/uploads/2022/09/bruschetta-de-mortadela-marba-superiore-azeitona.png");
