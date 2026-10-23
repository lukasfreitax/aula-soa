# Aula SOA — API de Cadastro de Veículos

Projeto acadêmico desenvolvido em aula para praticar a criação de uma API utilizando Python, Flask e SQLAlchemy, com separação de responsabilidades em camadas e integração com um cliente HTML/JavaScript.

A aplicação permite cadastrar veículos e consultar os registros armazenados em um banco de dados SQLite. O cliente HTML envia os dados do formulário para a API por meio de requisições HTTP.

## Tecnologias utilizadas

- **Python:** linguagem utilizada no desenvolvimento do servidor.
- **Flask:** framework responsável pela API e pelas rotas HTTP.
- **Flask-CORS:** permite a comunicação entre a API e uma interface web de outra origem.
- **SQLAlchemy:** ORM utilizado para mapear classes Python para tabelas do banco.
- **SQLite:** banco de dados utilizado para armazenar os veículos.
- **HTML:** estrutura da interface de cadastro.
- **JavaScript:** captura os dados do formulário e realiza requisições à API utilizando `fetch()`.

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
├── service/
│   └── veiculo_service.py
└── client/
    └── veiculo.html
```

## Organização em camadas

O projeto separa as responsabilidades da aplicação, facilitando a compreensão e a manutenção do código.

- **Cliente (`client/veiculo.html`):** apresenta o formulário para cadastro de veículos.
- **JavaScript:** captura os valores informados, envia uma requisição HTTP e exibe a resposta da API.
- **Controller:** recebe as requisições HTTP, encaminha os dados ao serviço e retorna respostas em JSON.
- **Service:** implementa as regras de negócio e valida os dados antes do cadastro.
- **Model:** define a entidade `Veiculo`, com os atributos `id`, `placa` e `modelo`.
- **Repository:** realiza as operações de consulta e gravação no banco de dados.
- **Database:** configura a conexão com o SQLite e os recursos do SQLAlchemy.
- **Main:** inicializa a aplicação Flask, habilita o CORS, registra as rotas e cria as tabelas necessárias.

## Funcionalidades

### 1. Cadastro de veículos

Permite cadastrar veículos informando placa e modelo. O serviço verifica os campos obrigatórios e aplica os limites de caracteres definidos no código.

### 2. Consulta de veículos

Retorna os veículos cadastrados no banco de dados em formato JSON.

### 3. Persistência de dados

Os registros são armazenados em um banco SQLite, utilizando o SQLAlchemy para executar as operações de persistência.

## Endpoints da API

A API disponibiliza a rota `/veiculo` com dois métodos HTTP.

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
- Navegador web para abrir o cliente HTML.

### 2. Clonar o repositório

```bash
git clone https://github.com/lukasfreitax/aula-soa.git
cd aula-soa
```

### 3. Instalar as dependências

```bash
python -m pip install Flask Flask-Cors SQLAlchemy
```

### 4. Iniciar a API

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

### 5. Abrir o cliente HTML

Com a API em execução:

1. Abra a pasta do projeto no computador.
2. Entre na pasta `client`.
3. Abra o arquivo `veiculo.html` em um navegador.
4. Preencha os campos de placa e modelo.
5. Clique em **Cadastrar**.

O JavaScript enviará os dados para `http://localhost:9000/veiculo` e exibirá a mensagem retornada pela API.

O endereço `localhost` aponta para o próprio computador. Por isso, a API deve estar em execução na mesma máquina durante o teste, ou o endereço do endpoint deverá ser ajustado.

## Como ocorre a comunicação

1. O usuário preenche o formulário HTML.
2. O JavaScript captura os valores dos campos.
3. A função `fetch()` envia uma requisição HTTP `POST` com os dados em JSON.
4. O Controller Flask recebe os dados e chama o Service.
5. O Service valida as informações e utiliza o Repository para persistir o veículo no SQLite.
6. A API retorna uma resposta JSON, e o cliente exibe a mensagem ao usuário.

Essa comunicação demonstra o modelo **cliente-servidor**: o HTML/JavaScript atua como cliente, a API Flask atua como servidor e o SQLite armazena os dados.

## Objetivo acadêmico

O objetivo do projeto é aplicar conceitos de desenvolvimento de APIs, arquitetura em camadas, regras de negócio, persistência de dados e integração entre aplicações por meio de requisições HTTP.

A implementação permite compreender como uma interface web pode consumir serviços disponibilizados por uma aplicação Python, mantendo separadas as responsabilidades de apresentação, processamento e acesso aos dados.

---

Projeto desenvolvido para fins educacionais na disciplina relacionada a Web Services e SOA.
