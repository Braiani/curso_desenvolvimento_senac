CREATE DATABASE IF NOT EXISTS titanic_base;
use titanic_base;

CREATE TABLE titanic_base (
	PassengerId int primary key,
    Survived tinyint,
    Pclass int,
    Nome varchar(100),
    Sex varchar(20),
    Age int,
    SibSp int,
    Parch int,
    Ticket varchar(30),
    Fare float,
    Cabin varchar(20),
    Embarked varchar(10)
);

select count(*) from titanic;
-- Quantas pessoas sobreviveram?
select count(*) from titanic where Survived = 1;

-- Quantas crianças menores de 12 anos sobreviveram?
select count(*) from titanic where Survived = 1 and (Age < 12  and Age <> "");

-- Quantas mulheres sobreviveram?
select count(*) from titanic where Survived = 1 and Sex = "female";

-- Quantos Homens sobreviveram?
select count(*) from titanic where Survived = 1 and Sex = "male";