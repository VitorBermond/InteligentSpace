## Baixe os arquivos

cd pasta/destino

git clone https://github.com/VitorBermond/InteligentSpace/tree/master/aula1

## Construa a imagem Docker

cd pasta/onde/o/dockerfile/esta

docker build --tag=flaskboasvindas .

## Execute a imagem Docker

sudo docker run -it --rm --name flaskboasvindasContainer -p 8080:8000 flaskboasvindas python3 serverFlask.py

## Confirme

Se tudo der certo uma pagina web irá abrir com um texto escrito "Bem vindo ao curso do IS"
