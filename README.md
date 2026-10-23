# Aula SOA — API de Cadastro de Veículos

Projeto acadêmico desenvolvido em aula para praticar a criação de uma API utilizando Python, Flask e SQLAlchemy, com separação de responsabilidades em camadas e integração com uma interface HTML externa.

A aplicação permite cadastrar veículos e consultar os registros armazenados em um banco de dados SQLite.

## Tecnologias utilizadas

- **Python:** linguagem de programação utilizada no desenvolvimento.
- **Flask:** framework responsável pela criação da API e das rotas HTTP.
- **Flask-CORS:** permite a comunicação entre a API e uma interface web de outra origem.
- **SQLAlchemy:** ORM utilizado para mapear as classes Python para tabelas do banco de dados.
- **SQLite:** banco de dados utilizado para persistir os veículos.

## Estrutura do projeto

```text
aula-soa/
├── main.py
├── database.py
├── controller/
│   └── veiculo_controller.py
├── model/
│   └── veiculo.py
├── repository/
│   └── veiculo_repository.py
└── service/
    └── veiculo_service.py
```

## Organização em camadas

O projeto utiliza uma estrutura que separa as responsabilidades da aplicação, facilitando a manutenção e a compreensão do código.

- **Controller:** recebe as requisições HTTP, identifica o método utilizado e retorna as respostas em JSON.
- **Service:** implementa as regras de negócio e valida os dados antes do cadastro.
- **Model:** define a entidade `Veiculo`, com os atributos `id`, `placa` e `modelo`.
- **Repository:** realiza as operações de consulta e gravação no banco de dados.
- **Database:** configura a conexão com o SQLite e os recursos do SQLAlchemy.
- **Main:** inicializa a aplicação Flask, habilita o CORS, registra as rotas e cria as tabelas necessárias.

## Funcionalidades

### 1. Cadastro de veículos

Permite cadastrar veículos informando placa e modelo.

A API valida os campos obrigatórios e verifica os limites de caracteres definidos no serviço.

### 2. Consulta de veículos

Retorna os veículos cadastrados no banco de dados em formato JSON.

### 3. Persistência de dados

Os registros são armazenados em um banco SQLite, utilizando o SQLAlchemy para executar as operações de persistência.

## Endpoints da API

A API disponibiliza a rota `/veiculo`, com dois métodos HTTP.

| Método | Endpoint | Descrição |
|---|---|---|
| GET | `/veiculo` | Lista os veículos cadastrados. |
| POST | `/veiculo` | Cadastra um novo veículo. |

### Exemplo de cadastro

**Requisição POST**

```http
POST /veiculo
Content-Type: application/json
```

Corpo da requisição:

```json
{
  "placa": "ABC1234",
  "modelo": "Sedan"
}
```

Resposta esperada:

```json
{
  "mensagem": "Veículo cadastrado!"
}
```

### Exemplo de consulta

Uma requisição GET para `/veiculo` retorna uma lista de veículos, semelhante a:

```json
[
  {
    "id": 1,
    "placa": "ABC1234",
    "modelo": "Sedan"
  }
]
```

Os dados retornados dependem dos registros existentes no banco.

## Como executar o projeto

### 1. Pré-requisitos

- Python instalado.
- Git instalado, caso queira clonar o repositório.

### 2. Clonar o repositório

```bash
git clone https://github.com/lukasfreitax/aula-soa.git
cd aula-soa
```

### 3. Instalar as dependências

```bash
python -m pip install Flask Flask-Cors SQLAlchemy
```

### 4. Executar a aplicação

```bash
python main.py
```

A API será iniciada na porta `9000`.

Endereço local:

```text
http://127.0.0.1:9000
```

Para consultar os veículos, acesse:

```text
http://127.0.0.1:9000/veiculo
```

A aplicação cria as tabelas necessárias na inicialização, utilizando o banco SQLite configurado no projeto.

## Integração com uma página HTML externa

O projeto também pode ser utilizado em conjunto com uma página HTML mantida em um arquivo separado.

Essa página atua como interface de usuário e se comunica com a API por meio de requisições HTTP.

- **GET:** consulta os veículos cadastrados.
- **POST:** envia os dados de um veículo para cadastro.
- **JSON:** formato utilizado para transmitir os dados entre a interface e a API.

O Flask-CORS está habilitado para permitir requisições entre origens diferentes. A API deve estar em execução para que a interface consiga consumir seus endpoints.

Em ambiente local, a interface pode utilizar o endereço `http://127.0.0.1:9000/veiculo`. Se a API estiver em outro computador, será necessário ajustar o endereço para o ambiente correspondente.

## Objetivo acadêmico

O objetivo do projeto é aplicar conceitos de desenvolvimento de APIs, organização em camadas, regras de negócio, persistência de dados e integração entre aplicações.

A implementação permite compreender como uma interface pode consumir serviços disponibilizados por uma aplicação Python, mantendo separadas as responsabilidades de apresentação, processamento e acesso aos dados.

---

Projeto desenvolvido para fins educacionais na disciplina relacionada a Web Services e SOA.
