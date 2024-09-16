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
ALTER TABLE Clientes MODIFY rg varchar(20) NULL;