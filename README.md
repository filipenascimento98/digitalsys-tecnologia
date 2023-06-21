# Sistema de Gestão de Propostas de Empréstimo Pessoal 

O objetivo deste desafio é criar um sistema onde os usuários possam cadastrar propostas de empréstimo pessoal e realizar sua avaliação através de uma fila RabbitMQ utilizando o Django Celery.

# Tecnologias
- [Python](https://www.python.org/)
- [Django](https://www.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)
- [Celery](https://docs.celeryq.dev/en/stable/)
- [RabbitMQ](https://www.rabbitmq.com/)
- Testes Unitários

# Instalação

Para acessar a API basta clonar o seguinte respositório.
```bash
git clone https://github.com/filipenascimento98/digitalsys-tecnologia.git
```

# Como executar
Esse projeto depende do [Docker](https://www.docker.com/) e do [Docker Compose](https://docs.docker.com/compose/). Com essas dependências resolvidas, navegue até o diretório do projeto que contém o arquivo __docker_compose.yml__ e execute os seguintes comandos que irão construir e executar a aplicação:
```bash
docker-compose build
docker-compose -f docker-compose.yml run --rm api python manage.py makemigrations
docker-compose -f docker-compose.yml run --rm api python manage.py migrate
docker-compose up -d
```
A aplicação irá rodar em containers Docker juntamente com a instância do RabbitMQ e o banco de dados PostgreSQL.

# Criação de usuário
Para criar um super usuário com acesso ao django-admin basta executar o seguinte comando.
```bash
docker-compose -f docker-compose.yml run --rm api python manage.py createsuperuser --noinput --username <seu-username> --email <seu-email>
```

# Criação do arquivo .env
É necessário a criação de uma arquivo __.env__ para a execução correta da aplicação. O arquivo pode conter os seguintes valores:
```bash
SECRET_KEY='sua-secret-key'
DB_USER='postgres'
DB_PASSWORD='postgres'
DB_NAME='postgres'
DJANGO_SUPERUSER_PASSWORD='sua-senha-do-usuario-criado-na-secao-anterior'
```

# Rotas
Temos o seguinte endpoint nessa API:

* POST: /api/proposta-emprestimo/


# Project structure
Breve explicação de alguns elementos da estrutura desse projeto.
* api: Único app desse projeto.
    * views: Contém os arquivos das views que são chamadas nas rotas definidas.
    * domain: Camada responsável pela regra do negócio e manipulação dos dados que são passados para view.
    * serializers: Diretório que armazena os serializers que são responsáveis por validar a entrada de cada rota.
    * data_access: Camada responsável pelo acesso aos os dados no banco de dados.
    * tests: Diretório que armazena os testes.

# Testes unitários
Para executar os testes unitários certifique-se que a aplicação esteja rodando e execute o seguindo comando
```bash
docker-compose -f docker-compose.yml run --rm api python manage.py test -b
```