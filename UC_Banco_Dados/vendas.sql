-- Quantas cidades tem cadastradas no banco? 
SELECT 
    count(*) as total_cidades
FROM
    CIDADE;
-- Quantos Clientes tem cadastrado no banco? 
SELECT 
    count(*) as total_clientes
FROM
    CLIENTE;

-- Quantos produtos tem no banco? 
SELECT 
    count(*) as total_produtos
FROM
    PRODUTO;
-- Quantos setores tem no banco? 
SELECT 
    count(*) as total_setores
FROM
    SETOR;

-- Quantos pedidos tem no banco? 
SELECT 
    count(*) as total_pedidos
FROM
    PEDIDO;
-- Qual o maior salário dos vendedores? 
SELECT 
    max(SALARIO) as maior_salario
FROM
    VENDEDOR;

-- Quem possui o maior salário? 
SELECT 
    NOMEVEND
FROM
    VENDEDOR
WHERE 
    SALARIO = (SELECT max(salario) FROM VENDEDOR);

-- Qual o menor salário dos vendedores? 
SELECT 
    min(SALARIO) as menor_salario
FROM
    VENDEDOR;
-- Quem possui o menor salário? 
SELECT 
    NOMEVEND
FROM
    VENDEDOR
WHERE 
    SALARIO = (SELECT min(salario) FROM VENDEDOR);



-- Qual pedido teve a maior venda em quantidade? 
SELECT 
	p.NUMPED,
    sum(ip.QTDADE) as soma
FROM
    PEDIDO p
JOIN
    ITEMPEDIDO ip ON p.NUMPED = ip.NUMPED
GROUP BY p.NUMPED
ORDER BY soma DESC
LIMIT 1;

-- Qual pedido teve a menor venda em quantidade? 
SELECT 
	p.NUMPED,
    sum(ip.QTDADE) as soma
FROM
    PEDIDO p
JOIN
    ITEMPEDIDO ip ON p.NUMPED = ip.NUMPED
GROUP BY p.NUMPED
ORDER BY soma ASC
LIMIT 1;

-- Qual o produto mais barato? 
SELECT 
	CODPROD,
    DESCRICAO
FROM
    PRODUTO
ORDER BY VALOR_UN ASC
LIMIT 1;

-- Qual o produto mais caro? 
SELECT 
	CODPROD,
    DESCRICAO
FROM
    PRODUTO
ORDER BY VALOR_UN DESC
LIMIT 1;

-- Quantos vendedores existem no setor de ferramentas? 
SELECT 
	count(*)
FROM
    VENDEDOR v
JOIN
    SETOR s ON v.CODSETOR = s.CODSETOR
WHERE
    s.NOMESETOR = 'FERRAMENTAS';

-- Quantos pedidos o cliente Estevan Pereira Cardoso fez? 
SELECT 
	count(*)
FROM
    PEDIDO P
JOIN
    CLIENTE C ON C.CODCLI = P.CODCLI
WHERE
    C.NOME = 'Estevan Pereira Cardoso';