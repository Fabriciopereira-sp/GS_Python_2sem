Integrantes:
Fabrício Henrique Pereira, RM563237
Leonardo José Pereira, RM563065
Pedro Henrique de Oliveira, RM562312


README – SkillShift AI (CRUD em Python com Oracle)
Sobre o projeto

O SkillShift AI é um sistema em Python voltado para o gerenciamento de profissionais e trilhas de aprendizado. A ideia principal é permitir cadastrar, listar e consultar informações diretamente em um banco de dados Oracle, além de possibilitar a exportação dos dados em formato JSON.

O projeto foi feito para ser simples de usar, rodando pelo terminal, sem interface gráfica, e com foco nas funcionalidades básicas esperadas em um CRUD.

Tecnologias utilizadas

Python 3

Banco de Dados Oracle

Biblioteca oracledb para conexão

Manipulação de arquivos JSON

Dependências necessárias

Antes de rodar o programa, é necessário ter:

Python 3 instalado

Biblioteca oracledb instalada via pip

Oracle Instant Client (caso a máquina exija para a conexão)

Conexão com o banco de dados

As credenciais para acessar o banco Oracle utilizado no projeto não ficam diretamente no código, e sim armazenadas em um arquivo .env, que deve conter as variáveis usadas para o acesso.

Esse arquivo deve incluir informações como usuário, senha, host, porta e service name.

O código já está preparado para ler essas informações automaticamente ao iniciar a conexão.

O que o sistema faz

O programa oferece um menu simples com as seguintes opções:

1. Criar tabelas

Cria as tabelas necessárias no banco (professionals e learning_paths), caso ainda não existam.

2. Cadastrar profissional

Permite inserir nome, e-mail, cargo e nível de habilidade (0 a 100) no banco.

3. Listar profissionais

Exibe todos os profissionais cadastrados e permite exportar os dados para um arquivo JSON.

4. Cadastrar trilha

Registra uma nova trilha de aprendizado com título, descrição e duração.

5. Listar trilhas

Lista todas as trilhas cadastradas, também com opção de exportar para JSON.

6. Consultar profissionais iniciantes

Mostra somente profissionais com nível de habilidade abaixo de um valor escolhido pelo usuário.

Como executar

Instale as dependências necessárias.

Certifique-se de ter o arquivo .env configurado corretamente com as credenciais do banco.

Abra o terminal na pasta do projeto.

Execute o arquivo principal com:

python SkillShift-AI.py


O menu será exibido. Se for a primeira execução, comece pela opção de criar as tabelas.

Exportação de dados

Tanto na listagem de profissionais quanto na de trilhas, o sistema permite exportar os resultados para um arquivo JSON. O próprio programa pergunta se o usuário deseja exportar logo após a exibição dos dados.

Considerações finais

O projeto foi construído para ser direto, funcional e fácil de entender. Todos os inputs recebem validação básica para evitar erros comuns, e o uso do formato JSON facilita a integração com outros sistemas ou a geração de relatórios.