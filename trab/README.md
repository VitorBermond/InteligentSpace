# Trabalho_IS

Foi requisitada a criação de uma aplicação que recebe comandos de Set e Get positions para um robô.
É necessário executar cada parte da aplicação para o seu funcionamento adequado. 
E também é necessário um broker RabbitMQ em funcionamento

### Broker
```
docker run -d --rm -p 5672:5672 -p 15672:15672 rabbitmq:3.7.6-management
```

### Executar Parte 1

No diretório da parte 1 execute o comando:

```
python3 Parte1.py
```

### Executar  Parte 2

No diretório da parte 2 execute o comando:

```
python3 Parte2.py
```

### Executar parte 3

No diretório da parte 3 execute o comando:

```
python3 Parte3.py
```
