-- Criar a tabela alunos
CREATE TABLE alunos (
    aluno_id character varying(5) NOT NULL,
    nome character varying(40) NOT NULL,
    endereco character varying(60),
    cidade character varying(15),
    estado character varying(15),
    cep character varying(10),
    pais character varying(15),
    telefone character varying(24)
);

-- Inserir pelo menos 10 alunos
INSERT INTO alunos (aluno_id, nome, endereco, cidade, estado, cep, pais, telefone) VALUES
('A001', 'João Silva', 'Rua das Flores, 123', 'São Paulo', 'SP', '12345-678', 'Brasil', '11987654321'),
('A002', 'Maria Santos', 'Avenida Central, 456', 'Rio de Janeiro', 'RJ', '23456-789', 'Brasil', '21987654322'),
('A003', 'Pedro Almeida', 'Travessa do Sol, 789', 'Curitiba', 'PR', '34567-890', 'Brasil', '41987654323'),
('A004', 'Ana Souza', 'Rua Primavera, 101', 'Belo Horizonte', 'MG', '45678-901', 'Brasil', '31987654324'),
('A005', 'Carlos Lima', 'Rua do Campo, 202', 'Porto Alegre', 'RS', '56789-012', 'Brasil', '51987654325'),
('A006', 'Fernanda Costa', 'Alameda das Rosas, 303', 'Fortaleza', 'CE', '67890-123', 'Brasil', '85987654326'),
('A007', 'Ricardo Gomes', 'Rua da Paz, 404', 'Recife', 'PE', '78901-234', 'Brasil', '81987654327'),
('A008', 'Patrícia Oliveira', 'Rua Horizonte, 505', 'Manaus', 'AM', '89012-345', 'Brasil', '92987654328'),
('A009', 'Lucas Ferreira', 'Avenida Brasil, 606', 'Brasília', 'DF', '90123-456', 'Brasil', '61987654329'),
('A010', 'Beatriz Rocha', 'Rua do Sol, 707', 'Salvador', 'BA', '01234-567', 'Brasil', '71987654330');
