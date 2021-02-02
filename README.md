# BookStore

API Rest para uma livraria online.


# Recursos 
O usuário pode gerenciar livros, reservas de livro e clientes. O tempo padrão para cada reserva são três dias. 
Caso ultrapasse, deverá ser calculada uma multa e juros ao dia sobre o valor da reserva, de acordo com as seguintes regras:
 
| Dias de Atraso  |  Multa  | Juros ao dia
| ------------------- | ------------------- | ------------------- |
| Sem Atraso |  0 |  0%
|  Até 3 dias |  3% | 0.2%
|  Acimca de 3 dias |  5% | 0.4%
|  Acima de 5 dias |  7% | 0.6%

# API v1 Doc

## Livros 

- GET - /api/v1/books/ - obtém uma lista de livros;
- POST - /api/v1/books/ - cadastra um livro;
- GET - /api/v1/books/{id}/ - obtém um livro específico (id);
- DELETE - /api/v1/books/{id}/ - deleta um livro específico.

Exemplo de objeto:

````json
{    
    "id": 1,
    "title": "Fluent Python",
    "author": "Luciano Ramalho",
    "numbers_pages": 800,
    "reserve_price": 200
}
````
## Cliente

- GET - /api/v1/clients/ - obtém uma lista de clientes;
- GET - /api/v1/clients/{id}/books/ - obtém uma lista de reservas para o cliente específico (id) com os atributos de multas se houver.
- POST - /api/v1/clients/ - cadastra um cliente;
- GET - /api/v1/clients/{id}/ - obtém um cliente específico (id);
- DELETE - /api/v1/clients/{id}/ - deleta um cliente específico.

Exemplo de objeto cliente:

````json
{
    "id": 1,
    "name": "Guilherme Peixoto"
}
````

Exemplo de objeto Lista de Reservas:

```json
[    
    {
        "date": "2021-02-01",
        "book_name": "Estrutura de Dados I",
        "days_of_delay": 0,
        "penalty": 0.0,
        "interest_per_day": 0.0,
        "total_price": 200.0
    },
    {
        "date": "2021-01-27",
        "book_name": "Matemática",
        "days_of_delay": 3,
        "penalty": 6.0,
        "interest_per_day": 1.2,
        "total_price": 207.2
    }
]

```

## Reserva de Livro

- POST - /api/v1/books/{id}/reserve/ - reseva o livro específico (id), enviar pelo body da requisição o id do cliente;

Exemplo:

```json
{
  "client": 1
}
```



# Instalação

Clone o projeto repositório:

```bash
git clone https://github.com/peixoto3/book_store
```


Para rodar o projeto com docker, certifique-se que tem o docker e docker-compose instalado na sua máquina:

### Docker

- [Windows](https://docs.docker.com/docker-for-windows/)
- [OS X](https://docs.docker.com/get-started/)
- [Linux](https://docs.docker.com/get-started/)

### Docker-compose

- [Install Docker Compose](https://docs.docker.com/compose/install/)

### Variáveis de ambiente

Para configurar algumas variáveis de ambiente, editar o arquivo ``.env.dev`` na raiz do projeto. 

### Parar rodar todos os containers:

`````dockerfile
docker-compose up --build
`````

Realize as migrações

`````dockerfile
docker-compose exec app python manage.py migrate
`````

Para ter acesso ao admin, crie um super usuário:
`````dockerfile
docker-compose exec app python manage.py createsuperuser
`````
Para executar os testes unitários:
`````dockerfile
docker-compose exec app python manage.py tests
`````


---
Para rodar o projeto sem docker:


Instale as dependências:

```bash
$ pip install -r requirements.txt
```

Realize as migrações:

`````bash
python manage.py migrate
`````

Para ter acesso ao admin, crie um super usuário:
`````dockerfile
python manage.py createsuperuser
`````

Para executar os testes unitários:
```bash
$ python manage.py tests
```


## Dependências

- [Python 3.7+](https://www.python.org/downloads/release/python-374/)
- [Django 3.1.5](https://docs.djangoproject.com/en/3.1/)
- [djangorestframework 3.12.2](https://www.django-rest-framework.org/)


## Postman

Importe o arquivo ``book_store_collection.postman_collection.json`` no [postman](https://www.postman.com/) para obter 
uma coleção de requisições configuradas para API Book Store. 