from __future__ import print_function
from is_wire.core import Channel, Subscription
import time

print("ip default 10.10.1.24 ")
ipbroker = input("Digite o ip do broker a ser utilizado:")

# Connect to the broker
channel = Channel(f"amqp://guest:guest@{ipbroker}:5672")

aluno = input("Digite o topico do aluno")
# Subscribe to the desired topic(s)
subscription = Subscription(channel)
subscription.subscribe(topic=f"Aluno.{aluno}")
# ... subscription.subscribe(topic="Other.Topic")

while True:
    message = channel.consume()
    print(message.reply_to,":",message.body.decode('latin1') )
#   print(message.body.decode('latin1'))
    time.sleep(1)
