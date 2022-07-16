# KU-Workshop 2022

### Start DVWA lab on the docker:
> docker run --rm -it -p 80:80 vulnerables/web-dvwa

### Restart Docker server:
```
docker container ls
docker exec d441fd0e7f56 /etc/init.d/apache2 reload
```

## LFI Lab enabled:
```
docker exec db127edf2d93  sed -i 's/allow_url_include = Off/allow_url_include = On/g' /etc/php/7.0/apache2/php.ini
docker exec db127edf2d93 /etc/init.d/apache2 reload
```

## Get into a Docker container's shell.
> docker exec -it db127edf2d93 bash
