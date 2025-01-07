from is_wire.core import Channel, Subscription

ipbroker = "localhost:5672" #Substitua pelo IP do broker

# Conecte ao broker
channel = Channel(f"amqp://guest:guest@{ipbroker}")

# Subscreva ao tópico específico
subscription = Subscription(channel)
subscription.subscribe(topic="Aluno.vitor")  # Substitua pelo tópico correto

print("Aguardando mensagens...")
while True:
    message = channel.consume()  # Aguarda mensagem
    print(f"Mensagem recebida: {message.body.decode('utf-8')}")

