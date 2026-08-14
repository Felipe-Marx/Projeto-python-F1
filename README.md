
# F1 Data Analyzer

Uma aplicação web para gerenciamento e análise de dados de pilotos de Fórmula 1, desenvolvida como projeto prático de aprendizado em **Python, FastAPI e desenvolvimento de APIs REST**.

O projeto está sendo construído de forma incremental, começando por uma API simples e evoluindo posteriormente para uma aplicação completa com frontend, persistência de dados e ferramentas de análise.

> 🚧 &#x2A;*Status:** Em desenvolvimento

---

## 🎯 Objetivo

O principal objetivo do projeto é colocar em prática conceitos de programação e desenvolvimento backend através de um domínio de interesse: **Fórmula 1**.

Durante o desenvolvimento, serão praticados conceitos como:

- Python
- APIs REST
- FastAPI
- Pydantic
- CRUD
- JSON
- Persistência de dados
- Validação de dados
- Tratamento de erros
- HTML, CSS e JavaScript
- Consumo de APIs
- Análise de dados
- Estruturação de projetos

---

## 🛠️ Tecnologias

### Backend

- **Python**
- **FastAPI**
- **Pydantic**
- **JSON**

### Frontend

Planejado:

- HTML
- CSS
- JavaScript

### Futuro

- SQLite
- Pandas
- NumPy
- Matplotlib

---

## 📂 Estrutura do projeto

A estrutura será desenvolvida gradualmente. Atualmente, a organização segue aproximadamente:

```text
f1-data-analyzer/
│
├── backend/
│   ├── main.py
│   └── data/
│       └── drivers.json
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
└── README.md
```

> A estrutura do frontend ainda está em desenvolvimento.

---

## 🚀 API

Atualmente, a API possui endpoints para consulta e criação de pilotos.

### Página inicial

```http
GET /
```

Retorna uma mensagem indicando que a API está funcionando.

### Listar pilotos

```http
GET /drivers
```

Retorna todos os pilotos cadastrados.

### Buscar piloto

```http
GET /drivers/{driver_id}
```

Busca um piloto específico através do seu ID.

Exemplo:

```http
GET /drivers/1
```

### Criar piloto

```http
POST /drivers
```

Recebe os dados de um novo piloto:

```json
{
    "name": "Oscar Piastri",
    "team": "McLaren",
    "points": 150
}
```

O ID é gerado automaticamente pela aplicação.

### Atualizar piloto

```http
PUT /drivers/{driver_id}
```

Permite atualizar os dados de um piloto existente.

> 🚧 Endpoint em desenvolvimento.

---

## 📊 Modelo de dados

Cada piloto é armazenado inicialmente como um objeto JSON:

```json
{
    "id": 1,
    "name": "Kimi Antonelli",
    "team": "Mercedes",
    "points": 219
}
```

Os dados são atualmente persistidos em:

```text
data/drivers.json
```

---

## ▶️ Como executar

Clone o repositório:

```bash
git clone <URL_DO_REPOSITORIO>
```

Entre no diretório:

```bash
cd f1-data-analyzer
```

Crie um ambiente virtual:

```bash
python -m venv venv
```

Ative o ambiente virtual no Windows:

```bash
venv\Scripts\activate
```

Instale as dependências:

```bash
pip install fastapi uvicorn pydantic
```

Execute a aplicação:

```bash
uvicorn main:app --reload
```

A API estará disponível em:

```text
http://127.0.0.1:8000
```

A documentação interativa do FastAPI pode ser acessada em:

```text
http://127.0.0.1:8000/docs
```

---

## 🗺️ Roadmap

### Backend

- [x] Criar API com FastAPI
- [x] Criar modelo `DriverCreate`
- [x] Carregar pilotos do JSON
- [x] Listar pilotos
- [x] Buscar piloto por ID
- [x] Criar piloto
- [ ] Atualizar piloto
- [ ] Remover piloto
- [ ] Melhorar validações
- [ ] Separar o projeto em módulos
- [ ] Migrar persistência de JSON para SQLite

### Frontend

- [ ] Criar interface inicial
- [ ] Exibir classificação
- [ ] Criar formulário para adicionar piloto
- [ ] Editar pilotos
- [ ] Remover pilotos
- [ ] Consumir API através de JavaScript
- [ ] Criar dashboard

### Análise de dados

- [ ] Estatísticas dos pilotos
- [ ] Estatísticas das equipes
- [ ] Classificação automática
- [ ] Gráficos
- [ ] Integração com Pandas
- [ ] Integração com NumPy
- [ ] Visualizações com Matplotlib
- [ ] Integração com dados reais de Fórmula 1

---

## 📚 Objetivo de aprendizado

Este projeto está sendo desenvolvido principalmente como uma forma de **aprender através da prática**.

A aplicação será evoluída gradualmente, começando com conceitos básicos de Python e APIs e posteriormente incorporando conceitos mais avançados de backend, frontend e análise de dados.

---

## 🏁 Próximos passos

O próximo objetivo do desenvolvimento é finalizar o CRUD de pilotos, implementando corretamente:

```text
GET    /drivers
GET    /drivers/{id}
POST   /drivers
PUT    /drivers/{id}
DELETE /drivers/{id}
```

Depois disso, o projeto será conectado a um frontend desenvolvido com **HTML, CSS e JavaScript**, permitindo interagir com a API através de uma interface gráfica.

---

## 👨‍💻 Projeto em desenvolvimento

Projeto criado para fins de estudo e prática de desenvolvimento de software, com foco em **Python, backend, APIs e análise de dados aplicados à Fórmula 1**.
