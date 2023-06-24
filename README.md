# SafarbaziProject

## project setup

1- compelete cookiecutter workflow (recommendation: leave project_slug empty) and go inside the project
```
cd SafarbaziTestProject
```

2- SetUp venv
```
virtualenv -p python3.10 venv
source venv/bin/activate
```

3- install Dependencies
```
pip install -r requirements/local.txt
```

4- edit your env
```
cp .env.development .env.production
```

5- spin off docker compose
```
docker compose -f docker-compose.dev.yml build

docker compose -f docker-compose.dev.yml up
```
