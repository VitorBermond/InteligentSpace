## É necessário um broker RabbitMQ em funcionamento em sua rede

amqp://guest:guest@localhost:5672

## Baixe os arquivos 

git clone https://github.com/VitorBermond/InteligentSpace/tree/master/aula2

## Use os algoritmos para publicar uma imagem ou uma mensagem

cd pasta/onde/os/arquivos/estao

python3 publish.py

- ou

python3 publish_img.py

## Use os algoritmos para consumir a imagem ou mensagem publicada

python3 subscribe.py

- ou

python3 subscribe_img.py

## Confirme

Se tudo der certo, uma imagem será baixada ou uma mensagem aparecerá no prompt de comando
