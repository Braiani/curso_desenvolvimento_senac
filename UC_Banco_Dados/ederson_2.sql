-- Se a letra da cidade começar de A até M, Mudar o nome da cidade para “Abaixo de M”, e de M até o final do alfabeto mudar o nome para “Acima de M”;
UPDATE cidade SET cidade = "Abaixo de M" where cidade < "M%";
UPDATE cidade SET cidade = "Acima de M" where cidade > "M%";

-- Os estados, deixaremos de utilizar seu nome, e sim sua região, então verifique a região do estado e altere, ex.: se o estado for Mato Grosso do Sul, você irá alterar o nome para “Centro Oeste”;
UPDATE estado SET estado = "Centro-Oeste" WHERE estado in ("Mato Grosso do Sul", "Mato Grosso", "Goias", "Distrito Federal");
UPDATE estado SET estado = "Nordeste" WHERE estado in ("Bahia", "Sergipe", "Alagoas", "Pernambuco", "Paraíba", "Rio Grande do Norte", "Ceará", "Maranhão", "Piauí");
UPDATE estado SET estado = "Norte" WHERE estado in ("Acre", "Amazonas", "Pará", "Rondônia", "Roraima", "Tocantins", "Amapá");
UPDATE estado SET estado = "Sul" WHERE estado in ("Paraná", "Santa Catarina", "Rio Grande do Sul");
UPDATE estado SET estado = "Sudeste" WHERE estado in ("São Paulo", "Rio de Janeiro", "Minas Gerais", "Espírito Santo");

-- Na nacionalidade, alterar estrangeiro para “Fora do Brasil”;
UPDATE nacionalidade SET nacionalidade = "Fora do Brasil" WHERE nacionalidade = "Estrangeira";

-- Nas raças, alterar para “seres humanos”;
UPDATE raca SET raca = "Seres Humanos";

-- Na escolaridade mudaremos o padrão, tudo que for ensino fundamental ou médio, será alterado para “ensino básico”, e o que for de graduação para cima, será alterado para “ensino avançado”.
UPDATE escolaridade SET escolaridade = "Ensino Básico" WHERE escolaridade LIKE "%Fundamental%" OR escolaridade LIKE "%Médio%";
UPDATE escolaridade SET escolaridade = "Ensino Avançado" WHERE escolaridade <> "Ensino Básico";


-- 
-- Apresentar um select apenas com o nome e a cidade.
--

SELECT c.nome, ci.cidade
FROM clientes c
JOIN cidade ci ON c.id_cidade = ci.id_cidade;

-- 
-- Apresentar um select apenas com o nome e o estado.
--

SELECT c.nome, e.estado
FROM clientes c
JOIN cidade ci ON c.id_cidade = ci.id_cidade
JOIN estado e ON ci.id_estado = e.id_estado;

-- 
-- Apresentar um select apenas com o nome, cpf e a raça.
--

SELECT c.nome, c.cpf, r.raca
FROM clientes c
JOIN raca r ON c.id_raca = r.id_raca;

-- 
-- Apresentar um select apenas com o nome e a nacionalidade.
--

SELECT c.nome, n.nacionalidade
FROM clientes c
JOIN nacionalidade n ON c.id_nacionalidade = n.id_nacionalidade;

-- 
-- Apresentar um select apenas com o nome e a escolaridade.
--

SELECT c.nome, e.escolaridade
FROM clientes c
JOIN escolaridade e ON c.id_escolaridade = e.id_escolaridade;

-- 
-- Apresentar um select com nome, cidade e estado.
--

SELECT c.nome, ci.cidade, e.estado
FROM clientes c
JOIN cidade ci ON c.id_cidade = ci.id_cidade
JOIN estado e ON ci.id_estado = e.id_estado;

-- 
-- Apresentar um select com nome, cidade, estado, fone, rg, sexo, nacionalidade, raça, escolaridade.
--

SELECT 
    c.nome, 
    ci.cidade, 
    e.estado, 
    c.fone, 
    c.rg, 
    s.sexo, 
    n.nacionalidade, 
    r.raca, 
    es.escolaridade,
    civil.estado_civil
FROM clientes c
JOIN cidade ci ON c.id_cidade = ci.id_cidade
JOIN estado e ON ci.id_estado = e.id_estado
JOIN sexo s ON c.id_sexo = s.id_sexo
JOIN nacionalidade n ON c.id_nacionalidade = n.id_nacionalidade
JOIN raca r ON c.id_raca = r.id_raca
JOIN escolaridade es ON c.id_escolaridade = es.id_escolaridade
JOIN estado_civil civil ON c.id_estado_civil = civil.id_estado_civil;