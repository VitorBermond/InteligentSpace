from is_wire.core import Channel, Message

print("ip default 10.10.1.24 ")
ipbroker = input("Digite o ip do broker a ser utilizado:")

#Conncet to the broker
channel = Channel(f"amqp://guest:guest@{ipbroker}")

message = Message()
#message.body = "Arthur@abacaxi na pizza é crime".encode('latin1')
message.reply_to = "Arthur"
message.correlation_id = 69

while True:
    #Broadcast message to anyone interested (subscribed)
    msg = input("Digite a mensagem:")
    dest = input("Digite o destinatário:")
    message.body = msg.encode('utf-8')
    channel.publish(message, topic=f"Aluno.{dest}")
