# Trabalho_IS

Simulação de Set e Get positions em um robo. 
É necessário executar cada parte em sequência.
Também é necessário um Broker RabbitMQ em funcionamento.

### Broker

```
docker run -d --rm -p 5672:5672 -p 15672:15672 rabbitmq:3.7.6-management
```

### Parte 1

```
docker run --rm -it --network=host vitor/parte1 python3 Parte1.py
```

### Parte 2

```
docker run --rm -it --network=host vitor/parte2 python3 Parte2.py
```

### Parte 3

```
docker run --rm -it --network=host vitor/parte3 python3 Parte3.py
```
