from is_wire.core import Channel, Message

# Configuração do broker RabbitMQ
ipbroker = "localhost:5672"  # Endereço correto do broker

# Conecte ao broker RabbitMQ
channel = Channel(f"amqp://guest:guest@{ipbroker}")

while True:
    # Solicitar informações do usuário
    msg = input("Digite a mensagem: ")
    dest = input("Digite o destinatário: ")

    # Criar a mensagem
    message = Message()
    message.body = msg.encode('utf-8')  # Mensagem no corpo
    message.correlation_id = 69  # Apenas um identificador exemplo
    message.reply_to = "resposta.fila"  # Opcional, apenas se esperar resposta

    # Publicar a mensagem no tópico especificado
    topic = f"Aluno.{dest}"
    channel.publish(message, topic=topic)
    print(f"Mensagem enviada para o tópico: {topic}")
