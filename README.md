# nodejs.devbox
Simple development box for Electron apps.

## Prerequirement
In order to allow Docker to connect to your host DISPLAY, please type in the terminal:
```
/usr/bin/xhost +local:root
```

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

## Run Electron Hello World example
```
$ ./devbox_shell.sh
# cd electron-app
# npm install
# npm start
```

## Run Electron Hello World example using Vue, Vuetify and TypeScript
```
$ ./devbox_shell.sh
# cd vue-electron-app
# npm install
# npm run electron:serve
```
