# Stack Docker Django 1.11 / Python 2.7 avec MSSQL Express

Cette stack s'inspire du principe de [jolicode/docker-starter](https://github.com/jolicode/docker-starter) : une séparation claire des services, un `.env` pour la configuration et un lancement simple via `docker-compose`.

## Structure

```
.
├── docker
│   ├── nginx
│   │   ├── Dockerfile
│   │   └── default.conf
│   └── python
│       ├── Dockerfile
│       └── entrypoint.sh
├── src
│   ├── manage.py
│   └── stackbb
│       ├── __init__.py
│       ├── settings.py
│       ├── urls.py
│       └── wsgi.py
├── .env.example
├── docker-compose.yml
└── requirements.txt
```

Le code source de l'application Django vit dans le dossier `src/`, qui est monté dans le conteneur `app` (volume `./src:/app`). Cela permet de développer localement avec rechargement direct dans le conteneur.

## Pré-requis

- Docker Desktop (Windows/Mac) ou Docker Engine (Linux)
- Docker Compose

## Démarrage rapide

1. Copier la configuration d'environnement :

```bash
cp .env.example .env
```

2. Construire et lancer la stack :

```bash
docker-compose up --build
```

3. Accéder à l'application via le serveur web :

- http://localhost:8080/health/

## Services

- **app** : conteneur Django 1.11 / Python 2.7 + Gunicorn.
- **nginx** : serveur web reverse proxy sur le port `8080`.
- **mssql** : SQL Server Express pour Linux (port `1433`).

## Base de données MSSQL

Le backend Django est configuré pour `sql_server.pyodbc` (package `django-pyodbc-azure`).
Les variables d'environnement par défaut sont dans `.env.example`. Ajustez `DB_PASSWORD` avant usage.

## Notes Windows

- Assurez-vous que Docker Desktop expose le port `8080`.
- Le montage du dossier `src` est compatible Windows/Mac/Linux.

## Commandes utiles

- Exécuter les migrations :

```bash
docker-compose exec app python manage.py migrate
```

- Ouvrir un shell Django :

```bash
docker-compose exec app python manage.py shell
```
