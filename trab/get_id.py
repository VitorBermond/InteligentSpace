from __future__ import print_function
from is_wire.core import Channel, Message, Subscription, Logger
from google.protobuf.empty_pb2 import Empty
import socket
from is_msgs.common_pb2 import Position

# Programa para fazer o "get position"

log = Logger(name='get_id')

empty = Empty()

channel = Channel("amqp://guest:guest@localhost:5672")
subscription = Subscription(channel)
request = Message(content=empty, reply_to=subscription)
channel.publish(request, topic="Get.Id")

try:
    reply = channel.consume(timeout=1.0)
    log.info(f'id = {id}')

except socket.timeout:
    print('No reply :(')



