-- Utilizando o Banco de Dados do IBGE, efetua as seguintes consultas:
use ibge;

-- 1.Faça uma consulta selecionando somente o estado de Mato Grosso do Sul;

select * from senso where estado = 'Mato Grosso do Sul';

-- 2.Faça uma consulta selecionando somente cidades com menos de 1000 habitantes;

select * from senso where populacao < 1000;

-- 3.Faça uma consulta selecionando somente as cidades de Terenos e Campo Grande;

select * from senso where estado = 'Mato Grosso do Sul' and (nome_mun = 'Terenos' or nome_mun = 'Campo Grande');

-- 4.Faça uma consulta selecionando somente as cidades com mais de 100 mil habitantes do estado de Mato Grosso do Sul;

select * from senso where estado = 'Mato Grosso do Sul' and populacao > 100000;

-- 5.Faça uma consulta apenas dos campos estado e nome_mun ordenando a coluna nome_mun;

select estado, nome_mun from senso order by nome_mun;

-- 6.Faça uma consulta da cidade com maior PIB;

select * from senso order by pib desc limit 1;

-- 7.Faça uma consulta da cidade com maior PIB_PER_CAP;

select * from senso order by pib_per_cap desc limit 1;

-- 8.Faça uma consulta da cidade com maior População;

select * from senso order by populacao desc limit 1;

-- 9.Faça uma consulta da cidade com menor População;

select * from senso order by populacao asc limit 1;

-- 10.Efetue uma consulta qualquer e informe.

select * from senso where pib > 100000 and nome_mun LIKE "C%m%";

-- 11.Faça uma contagem de todos os registros;

select count(*) from senso;

-- 12.Faça uma média do PIB;

select avg(pib) from senso;

-- 13.Faça uma consulta das cidades que começam com a letra C;

select * from senso where nome_mun LIKE "C%";

-- 14.Efetue 5 consultas de sua escolha

select * from senso where pib > 100000 and nome_mun LIKE "C%m%";
select * from senso where estado LIKE 'M%' and nome_mun LIKE "C%m%";
select * from senso where populacao > 10000 and pib <= 50000;
select * from senso where pib_per_cap < 20000 or pib_per_cap > 60000;
select * from senso where pib < (select avg(pib) from senso);