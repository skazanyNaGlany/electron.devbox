# nodejs.devbox
Simple development box for Electron apps.

## Run
```
docker-compose up -d
```

## Development
Your ```www/``` directory is mapped to container and is accessible via ```http://localhost:18080/``` (8080 on container)

## Access www shell
```
./devbox_shell.sh
```

NodeJS, NPM and Electron are installed by default.

## Run Hello World example
```
$ ./devbox_shell.sh
# npm install
# npm start
```
