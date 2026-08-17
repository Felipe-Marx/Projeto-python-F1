# F1 Data Analyzer

Uma aplicação web para gerenciamento e análise de dados de pilotos de Fórmula 1, desenvolvida como projeto prático de aprendizado em **Python, FastAPI e desenvolvimento de APIs REST**.

O projeto está sendo construído de forma incremental, com foco em praticar programação Python, desenvolvimento backend, organização de código, validação de dados, manipulação de coleções e, posteriormente, análise de dados e desenvolvimento de um frontend.

> 🚧 **Status:** Em desenvolvimento

---

## 🎯 Objetivo

O principal objetivo do projeto é aprender e praticar desenvolvimento de software através de um domínio de interesse: **Fórmula 1**.

O projeto busca evoluir gradualmente de uma API CRUD simples para uma aplicação capaz de realizar análises sobre dados de pilotos e equipes.

Durante o desenvolvimento serão praticados conceitos como:

- Python
- Programação orientada a objetos
- Manipulação de listas e dicionários
- Funções
- List comprehensions
- `lambda`
- `sorted()`
- `enumerate()`
- Slicing
- APIs REST
- FastAPI
- Pydantic
- Validação de dados
- CRUD
- JSON
- Persistência de dados
- Tratamento de erros
- Separação de responsabilidades
- Arquitetura em camadas
- Query parameters
- HTML, CSS e JavaScript
- Consumo de APIs
- Análise de dados
- Visualização de dados

---

## 🛠️ Tecnologias

### Backend

- **Python**
- **FastAPI**
- **Pydantic**
- **Uvicorn**
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
- Dados reais de Fórmula 1

---

## 📂 Estrutura do projeto

Atualmente, o backend está organizado separando responsabilidades entre modelos, serviços e rotas:

```text
f1-data-analyzer/
│
├── backend/
│   │
│   ├── main.py
│   ├── models.py
│   ├── services.py
│   │
│   ├── routers/
│   │   └── drivers.py
│   │
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

### Responsabilidade dos arquivos

**`main.py`**

Responsável por inicializar a aplicação FastAPI e registrar os routers.

**`models.py`**

Contém os modelos Pydantic utilizados para validação dos dados recebidos pela API.

**`services.py`**

Contém a lógica de negócio e manipulação dos dados, como:

- carregar pilotos;
- salvar pilotos;
- buscar pilotos;
- criar pilotos;
- atualizar pilotos;
- remover pilotos;
- gerar rankings.

**`routers/drivers.py`**

Contém as rotas HTTP relacionadas aos pilotos.

**`data/drivers.json`**

Responsável pela persistência dos dados enquanto o projeto utiliza JSON.

---

# 🚀 API

A API atualmente possui operações CRUD para pilotos e um endpoint de classificação.

## Página inicial

```http
GET /
```

Retorna uma mensagem indicando que a API está funcionando.

Exemplo:

```json
{
    "message": "F1 Data Analyzer API"
}
```

---

## Listar pilotos

```http
GET /drivers
```

Retorna todos os pilotos cadastrados.

---

## Buscar piloto

```http
GET /drivers/{driver_id}
```

Busca um piloto específico através do seu ID.

Exemplo:

```http
GET /drivers/1
```

Caso o piloto não exista:

```http
404 Driver not found
```

---

## Criar piloto

```http
POST /drivers
```

Recebe os dados de um novo piloto.

Exemplo:

```json
{
    "name": "Oscar Piastri",
    "team": "McLaren",
    "points": 150
}
```

O ID é gerado automaticamente pela aplicação.

---

## Atualizar piloto

```http
PUT /drivers/{driver_id}
```

Permite atualizar os dados de um piloto existente.

Exemplo:

```json
{
    "name": "Oscar Piastri",
    "team": "McLaren",
    "points": 175
}
```

Caso o piloto não exista:

```http
404 Driver not found
```

---

## Remover piloto

```http
DELETE /drivers/{driver_id}
```

Remove um piloto pelo seu ID.

Caso o piloto não exista:

```http
404 Driver not found
```

---

# 🏆 Ranking de pilotos

O projeto possui um endpoint dedicado para gerar a classificação dos pilotos de acordo com a pontuação.

```http
GET /drivers/ranking
```

Por padrão, o endpoint retorna os **5 primeiros pilotos**.

Também é possível definir a quantidade através do parâmetro `limit`:

```http
GET /drivers/ranking?limit=3
```

Exemplo de resposta:

```json
[
    {
        "id": 2,
        "name": "Kimi Antonelli",
        "team": "Mercedes",
        "points": 219,
        "position": 1
    },
    {
        "id": 3,
        "name": "Lewis Hamilton",
        "team": "Ferrari",
        "points": 169,
        "position": 2
    }
]
```

O parâmetro `limit` possui validação:

```text
1 <= limit <= 22
```

Valores fora desse intervalo resultam em erro de validação HTTP `422`.

---

# 🧪 Validação de dados

Os dados recebidos pela API são validados através do **Pydantic**.

Atualmente:

- `name` não pode ser vazio;
- `team` não pode ser vazio;
- espaços extras no início e no final são removidos;
- `points` deve ser maior ou igual a zero.

Exemplo:

```python
class DriverCreate(BaseModel):
    name: str = Field(min_length=1)
    team: str = Field(min_length=1)
    points: int = Field(ge=0)
```

Também são utilizados `field_validator` para validar e normalizar os campos de texto.

---

# 📊 Modelo de dados

Cada piloto é inicialmente armazenado como um objeto JSON:

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
backend/data/drivers.json
```

O campo `position` utilizado no ranking é gerado dinamicamente e não faz parte dos dados persistidos.

---

# 🏗️ Arquitetura

O projeto utiliza uma separação simples de responsabilidades:

```text
                    ┌──────────────┐
                    │   Frontend   │
                    └──────┬───────┘
                           │
                           │ HTTP
                           ▼
                    ┌──────────────┐
                    │    Router    │
                    └──────┬───────┘
                           │
                           ▼
                    ┌──────────────┐
                    │   Services   │
                    └──────┬───────┘
                           │
                           ▼
                    ┌──────────────┐
                    │    JSON      │
                    │   Storage    │
                    └──────────────┘
```

A ideia é manter as rotas responsáveis principalmente por lidar com HTTP, enquanto a lógica de negócio permanece nos services.

---

# ▶️ Como executar

Clone o repositório:

```bash
git clone https://github.com/Felipe-Marx/Projeto-python-F1
```

Entre no diretório:

```bash
cd Projeto-python-F1
```

Crie um ambiente virtual:

```bash
python -m venv venv
```

Ative o ambiente virtual no Windows:

```bash
venv\Scripts\activate
```

No Linux ou macOS:

```bash
source venv/bin/activate
```

Instale as dependências:

```bash
pip install fastapi uvicorn pydantic
```

Entre na pasta do backend:

```bash
cd backend
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

# 🗺️ Roadmap

## Backend

- [x] Criar API com FastAPI
- [x] Criar modelo `DriverCreate`
- [x] Criar validação com Pydantic
- [x] Carregar pilotos do JSON
- [x] Salvar pilotos no JSON
- [x] Listar pilotos
- [x] Buscar piloto por ID
- [x] Criar piloto
- [x] Atualizar piloto
- [x] Remover piloto
- [x] Separar models e services
- [x] Separar rotas em routers
- [x] Criar ranking de pilotos
- [x] Adicionar posições ao ranking
- [x] Implementar `limit` no ranking
- [x] Validar query parameters
- [ ] Criar estatísticas dos pilotos
- [ ] Criar estatísticas das equipes
- [ ] Melhorar tratamento de erros
- [ ] Criar testes automatizados
- [ ] Criar schemas de resposta
- [ ] Migrar persistência de JSON para SQLite

## Frontend

- [ ] Criar interface inicial
- [ ] Conectar frontend à API
- [ ] Exibir classificação
- [ ] Exibir informações dos pilotos
- [ ] Criar formulário para adicionar piloto
- [ ] Editar pilotos
- [ ] Remover pilotos
- [ ] Criar dashboard
- [ ] Criar gráficos
- [ ] Criar filtros e ordenação

## Análise de dados

- [ ] Estatísticas dos pilotos
- [ ] Estatísticas das equipes
- [x] Classificação automática
- [ ] Média de pontos
- [ ] Pontuação total
- [ ] Maior pontuação
- [ ] Menor pontuação
- [ ] Gráficos
- [ ] Integração com Pandas
- [ ] Integração com NumPy
- [ ] Visualizações com Matplotlib
- [ ] Integração com dados reais de Fórmula 1

---

# 📚 Objetivo de aprendizado

Este projeto está sendo desenvolvido principalmente como uma forma de **aprender Python através da prática**.

A ideia não é apenas construir uma API funcional, mas utilizar o projeto como um laboratório para praticar conceitos de programação e desenvolvimento de software.

O projeto será evoluído gradualmente, introduzindo novos conceitos conforme a aplicação cresce.

Entre os principais conceitos que serão praticados estão:

- Estruturas de dados
- Funções
- Modularização
- Programação orientada a objetos
- Manipulação de arquivos
- APIs REST
- Validação
- Tratamento de exceções
- Arquitetura de software
- Algoritmos
- Análise de dados
- Desenvolvimento frontend
- Integração entre frontend e backend

---

# 🏁 Próximos passos

O próximo objetivo é transformar o F1 Data Analyzer de uma API CRUD em uma aplicação de análise de dados.

Os próximos recursos planejados incluem:

```text
GET /drivers/statistics
```

para fornecer estatísticas gerais do campeonato, seguido pela criação do frontend e de um dashboard interativo.

Posteriormente, o projeto será evoluído para utilizar dados reais de Fórmula 1 e ferramentas de análise de dados como **Pandas, NumPy e Matplotlib**.

---

## 👨‍💻 Projeto em desenvolvimento

Projeto criado para fins de estudo e prática de desenvolvimento de software, com foco em **Python, backend, APIs REST e análise de dados aplicados à Fórmula 1**.
