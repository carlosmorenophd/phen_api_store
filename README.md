# DataWarehouse para datos fenotipicos

## Enpoint para obtener informacion de las variables fenotipicas

Ejemplo:
```
https://cropontology.org/brapi/v1/variables/CO_321:0001235
```

## Install

First install venv

```py
python3 -m venv .venv

```

Actiavte source

```shell
sourcer .venv/bin/activate

```

Install requiremntes

```py
pip install -r requirements.txt
```

# To run don docker

## Run on production
Command to build image

```
docker build --tag phen/api_store:24.06 .
```

To run the container

```
docker run --name api_store -p 8081:8000 -d --network=net-phenotypic -e DATABASE_USERNAME=admin -e DATABASE_PASSWORD=Fantasy24 -e DATABASE=phenotypic_db -e DATABASE_HOST=mariadb_phenotypic -e DATABASE_SOCKET=3306 -e FTP_HOSTNAME=ftp_phenotypic -e FTP_PORT=21 -e FTP_USERNAME=user -e FTP_PASSWORD=ftp1221Wheat phen/api_store:24.05
```

## Run on dev

Create image to dev project

```
docker build --tag phen/api_store:00.dev -f Dockerfile.dev .
```

Run image in a container

```
docker run -it -d --name dev_api_store -p 8091:8000 --network=net-phenotypic -v ${PWD}:/develop  phen/api_store:00.dev
```%