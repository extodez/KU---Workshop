# KU-Workshop 2022

### Start DVWA lab on the docker:
> docker run --rm -it -p 80:80 vulnerables/web-dvwa

### Restart Docker server:
```
Get contianer id:
docker container ls
docker exec <CONTAINER ID> /etc/init.d/apache2 reload
```

### Docker stop container:
> docker stop [OPTIONS] CONTAINER [CONTAINER...]

## LFI Lab enabled:
```
docker exec <CONTAINER ID>  sed -i 's/allow_url_include = Off/allow_url_include = On/g' /etc/php/7.0/apache2/php.ini
docker exec <CONTAINER ID> /etc/init.d/apache2 reload
```

## Get into a Docker container's shell.
> docker exec -it <CONTAINER ID> bash

## Kill docker process
> docker kill $(docker ps -q)
