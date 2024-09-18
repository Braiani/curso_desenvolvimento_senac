-- INSERT INTO `atividade_bd`.`cliente` (
--     `nome_usuario`, `regime_tributacao`, `email`, `email_danfe`, `email_cobranca`, `email_loja_virtual`,
--     `telefone_comercial`, `ramal`, `telefone_resid`, `telefone_celular`, `cpf`, `rg`, `situacao_icms`,
--     `insc_estadual`, `insc_suframa`, `sexo`, `data_nasc`, `transportadora1`, `tabela_preco`, `mod_frete_padrao`,
--     `sit_cadastro`, `aliquota`, `icms_carga_trib_media`, `cliente_fornecedor`, `confirmacao_cadastro_email`, `email_informacao`,
--     `estado`, `cidade`, `bairro`, `rua`, `numero`, `instagram`, `linkedin`, `estado_civil`, `cor`, `ensino_medio`,
--     `ensino_superior`, `nome_indicacao`, `contato_funcionario`, `nome_vendedor`, `whatsapp_usuario`, `cartao_nome`,
--     `cartao_numero`, `cartao_venc`, `cvv`, `salario`, `cnpj`
-- ) VALUES 
-- ('teste', 'Pessoa Física', 'teste.subteste@meusistemacompleto.com.br', 'teste.subteste@meusistemacompleto.com.br',
-- 'teste.subteste@meusistemacompleto.com.br', 'teste.subteste@meusistemacompleto.com.br',
-- '67999998888', '023', '6733334444', '67999998877', '12345678900', '123456', 'Aguardando',
-- '456', NULL, 'Masculino', '1990-01-01', 'Azul Cargo', 'Tabela Padrão', 'Padrão', 'Ativo', '2',
-- '0', '1', '1', '0', 'MS', 'Campo Grande', 'Nhanhá', 'Teste', '12', '@teste', 'teste', 'Viúvio',
-- 'branco', 'Sim', 'Não', 'Vend', '2222222', 'Vendedor', '987987', 'TEste da Silva', '123456789', '12/2025', '999', '1500', '0');

-- INSERT INTO `atividade_bd`.`EstruturaDeProdutos` (
--     `descricao`, `variante`, `PS`, `codigo`, `qtd_base`, `qtde`, `um`, `custo_un`, `custo_total`, `qt_fixa`, `ordem`, `origem`, `status_pedido`, `armazem`
-- ) VALUES ('Banco de Bike', 'Azul', 'Produto', '12345', '2', '3', '1', '25', '26', '3', '1', '0', 'Aguardando Pagamento', 'Padrão');

-- INSERT INTO `atividade_bd`.`NF` (
--     `documento`, `sequencia`, `emissao`, `vencimento`,`previsaoFatura`, `aprov_cliente`, `hora_aprovacao`, `embarques`,
--     `prazo`, `numPedido`, `vendedor`, `cliente`, `enderecoEntrega`, `tabela_preco`, `transportadora1`, `valorFrete`
-- ) VALUES 
-- (
-- 	'123', '12', '2024-09-16','2024-10-16','2024-10-25','2024-09-14','16:25','1','15','1','Vendedor','1','Teste','Padrão','Azul Cargo','120'
-- );
-- INSERT INTO `atividade_bd`.`OrdemDeServico` (
--     `documento`, `Emissao`, `cliente`, `previsao`, `descricao`, `execucao`, `servico`, `variante`, `qtd`, `valor`
-- ) VALUES 
-- (
-- 	'12', '2024-09-16', '1', '2024-10-01', 'Envio', 'Local', '1', 'Azul', '1', '30'
-- );

-- -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
-- Começando os ajustes da database

RENAME TABLE cliente to Clientes;
RENAME TABLE OrdemDeServico to OrdensDeServico;
RENAME TABLE NF to NFs;

CREATE TABLE RegimeTributacao (
    id_regime_tributacao int auto_increment primary key,
    descricao varchar(100)
);

INSERT INTO RegimeTributacao (id_regime_tributacao, descricao) VALUES 
(1, 'Pessoa Física'),
(2, 'Pessoa Jurídica');

ALTER TABLE Clientes RENAME COLUMN id TO id_cliente;
ALTER TABLE Clientes RENAME COLUMN nome_usuario TO nome;
ALTER TABLE Clientes RENAME COLUMN regime_tributacao TO id_regime_tributacao;

UPDATE Clientes set id_regime_tributacao = 1 WHERE id_regime_tributacao = "Pessoa Física";
UPDATE Clientes set id_regime_tributacao = 2 WHERE id_regime_tributacao = "Pessoa Jurídica";

ALTER TABLE Clientes MODIFY id_regime_tributacao int NOT NULL default(1);

CREATE TABLE Usuarios (
    id_usuario int auto_increment primary key,
    usuario varchar(200) NOT null,
    senha varchar(200) NOT NULL,
    cliente_id int,
    foreign key fk_cliente(cliente_id) references Clientes(id_cliente)
);

ALTER TABLE Clientes
ADD FOREIGN KEY fk_regime_tributacao(id_regime_tributacao) REFERENCES RegimeTributacao(id_regime_tributacao);

ALTER TABLE Clientes MODIFY email varchar(200);
ALTER TABLE Clientes MODIFY email_danfe varchar(200);
ALTER TABLE Clientes MODIFY email_cobranca varchar(200);
ALTER TABLE Clientes MODIFY email_loja_virtual varchar(200);

ALTER TABLE Clientes RENAME COLUMN telefone_resid TO telefone_residencial;

ALTER TABLE Clientes MODIFY cpf varchar(11) NULL unique;
ALTER TABLE Clientes MODIFY cnpj varchar(15) NULL unique;

ALTER TABLE Clientes MODIFY rg varchar(20) NULL;

CREATE TABLE Sexo (
    id_sexo int auto_increment primary key,
    descricao varchar(50)
);

INSERT INTO Sexo (id_sexo, descricao) VALUES
(1, "Masculino"),
(2, "Feminino");

UPDATE Clientes set sexo = 1 WHERE sexo = "Masculino";
UPDATE Clientes set sexo = 1 WHERE sexo = "Masculina";
UPDATE Clientes set sexo = 2 WHERE sexo = "Feminino";
UPDATE Clientes set sexo = 2 WHERE sexo = "Feminina";

ALTER TABLE Clientes RENAME COLUMN sexo TO id_sexo;
ALTER TABLE Clientes MODIFY id_sexo int NULL;

ALTER TABLE Clientes ADD FOREIGN KEY fk_sexo(id_sexo) REFERENCES Sexo(id_sexo);

ALTER TABLE Clientes MODIFY data_nasc date NULL;

CREATE TABLE SituacaoICMS (
    id_situacao_icms int auto_increment primary key,
    codigo varchar(2),
    descricao varchar(200)
);

INSERT INTO SituacaoICMS (id_situacao_icms, codigo, descricao) VALUES
(1, '00', 'Tributada integralmente'),
(2, '10', 'Tributada e com cobrança do ICMS por substituição tributária'),
(3, '20', 'Com redução de base de cálculo'),
(4, '30', 'Isenta ou não tributada e com cobrança do ICMS por substituição tributária'),
(5, '40', 'Isenta'),
(6, '41', 'Não tributada'),
(7, '50', 'Suspensão'),
(8, '51', 'Diferimento'),
(9, '60', 'ICMS cobrado anteriormente por substituição tributária'),
(10, '70', 'Com redução de base de cálculo e cobrança do ICMS por substituição tributária'),
(11, '90', 'Outras');


UPDATE Clientes set situacao_icms = 11;

ALTER TABLE Clientes RENAME COLUMN situacao_icms TO id_situacao_icms;
ALTER TABLE Clientes MODIFY id_situacao_icms int NOT NULL DEFAULT 11;

ALTER TABLE Clientes ADD FOREIGN KEY fk_situacao_icms(id_situacao_icms) REFERENCES SituacaoICMS(id_situacao_icms);

ALTER TABLE Clientes MODIFY aliquota float not null default 0;

CREATE TABLE SituacaoCadastro (
    id_situacao_cadastro int auto_increment primary key,
    descricao varchar(200)
);

INSERT INTO SituacaoCadastro (id_situacao_cadastro, descricao) VALUES
(1, 'Ativo'),
(2, 'Inativo'),
(3, 'Pendente'),
(4, 'Suspenso'),
(5, 'Cancelado'),
(6, 'Finalizado'),
(7, 'Aguardando documentação'),
(8, 'Em análise'),
(9, 'Aprovado'),
(10, 'Rejeitado'),
(11, 'Em atualização');

UPDATE Clientes set sit_cadastro = 1 WHERE sit_cadastro = "Ativo";
UPDATE Clientes SET sit_cadastro = 2 WHERE sit_cadastro = 'Inativo';
UPDATE Clientes SET sit_cadastro = 3 WHERE sit_cadastro = 'Pendente';
UPDATE Clientes SET sit_cadastro = 4 WHERE sit_cadastro = 'Suspenso';
UPDATE Clientes SET sit_cadastro = 5 WHERE sit_cadastro = 'Cancelado';
UPDATE Clientes SET sit_cadastro = 6 WHERE sit_cadastro = 'Finalizado';
UPDATE Clientes SET sit_cadastro = 7 WHERE sit_cadastro = 'Aguardando documentação';
UPDATE Clientes SET sit_cadastro = 8 WHERE sit_cadastro = 'Em análise';
UPDATE Clientes SET sit_cadastro = 9 WHERE sit_cadastro = 'Aprovado';
UPDATE Clientes SET sit_cadastro = 10 WHERE sit_cadastro = 'Rejeitado';
UPDATE Clientes SET sit_cadastro = 11 WHERE sit_cadastro = 'Em atualização';

ALTER TABLE Clientes RENAME COLUMN sit_cadastro TO id_situacao_cadastro;
ALTER TABLE Clientes MODIFY id_situacao_cadastro int NOT NULL DEFAULT 3;

ALTER TABLE Clientes ADD FOREIGN KEY fk_id_situacao_cadastro(id_situacao_cadastro) REFERENCES SituacaoCadastro(id_situacao_cadastro);

ALTER TABLE Clientes ADD escolaridade varchar(200) null after cor;
UPDATE Clientes set escolaridade = "Ensino médio" WHERE ensino_medio = "Sim"; 
UPDATE Clientes set escolaridade = "Ensino superior" WHERE ensino_superior = "Sim"; 

ALTER TABLE Clientes DROP COLUMN ensino_medio;
ALTER TABLE Clientes DROP COLUMN ensino_superior;

-- -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

ALTER TABLE EstruturaDeProdutos RENAME COLUMN idPedido TO id_produto;
ALTER TABLE EstruturaDeProdutos MODIFY codigo varchar(100);
ALTER TABLE EstruturaDeProdutos MODIFY ordem int not null default 0;
ALTER TABLE EstruturaDeProdutos MODIFY um varchar(100);

CREATE TABLE StatusPedido (
    id_status_pedido int primary key auto_increment,
    descricao varchar(100)
);

INSERT INTO StatusPedido (id_status_pedido, descricao) VALUES
(1, 'Pendente'),
(2, 'Processando'),
(3, 'Enviado'),
(4, 'Entregue'),
(5, 'Cancelado'),
(6, 'Devolvido'),
(7, 'Em espera'),
(8, 'Aguardando pagamento'),
(9, 'Pago'),
(10, 'Finalizado');

UPDATE EstruturaDeProdutos SET status_pedido = 1 WHERE status_pedido = 'Pendente';
UPDATE EstruturaDeProdutos SET status_pedido = 2 WHERE status_pedido = 'Processando';
UPDATE EstruturaDeProdutos SET status_pedido = 3 WHERE status_pedido = 'Enviado';
UPDATE EstruturaDeProdutos SET status_pedido = 4 WHERE status_pedido = 'Entregue';
UPDATE EstruturaDeProdutos SET status_pedido = 5 WHERE status_pedido = 'Cancelado';
UPDATE EstruturaDeProdutos SET status_pedido = 6 WHERE status_pedido = 'Devolvido';
UPDATE EstruturaDeProdutos SET status_pedido = 7 WHERE status_pedido = 'Em espera';
UPDATE EstruturaDeProdutos SET status_pedido = 8 WHERE status_pedido = 'Aguardando pagamento';
UPDATE EstruturaDeProdutos SET status_pedido = 9 WHERE status_pedido = 'Pago';
UPDATE EstruturaDeProdutos SET status_pedido = 10 WHERE status_pedido = 'Finalizado';

ALTER TABLE EstruturaDeProdutos RENAME COLUMN status_pedido TO id_status_pedido;
ALTER TABLE EstruturaDeProdutos MODIFY id_status_pedido int NOT NULL DEFAULT 1;

ALTER TABLE EstruturaDeProdutos ADD FOREIGN KEY fk_status_pedido(id_status_pedido) REFERENCES StatusPedido(id_status_pedido);

-- -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

ALTER TABLE NFs ADD id_nfs int auto_increment primary key;
ALTER TABLE NFs auto_increment = 2;

UPDATE NFs set id_nfs = 1 where documento = '123';

-- -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

ALTER TABLE OrdensDeServico ADD id_ordem_servico int auto_increment primary key;
ALTER TABLE OrdensDeServico auto_increment = 2;

UPDATE OrdensDeServico set id_ordem_servico = 1 where documento = '12';

ALTER TABLE OrdensDeServico RENAME COLUMN servico to id_servico;
ALTER TABLE OrdensDeServico MODIFY id_servico int;

ALTER TABLE OrdensDeServico ADD FOREIGN KEY fk_servico(id_servico) REFERENCES EstruturaDeProdutos(id_produto);

-- -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=