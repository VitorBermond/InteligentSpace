from is_wire.rpc import ServiceProvider, LogInterceptor
from is_wire.core import Channel, StatusCode, Status
from google.protobuf.empty_pb2 import Empty
from is_msgs.common_pb2 import Position
import time
import random

class Robot():
    def __init__(self, id, x, y):
        self.id = id
        self.pos_x = x
        self.pos_y = y

    def get_id(self):
        return self.id

    def set_position(self, x, y):
        self.pos_x = x
        self.pos_y = y

    def get_position(self):

        return self.pos_x, self.pos_y


def get_position(Empty, ctx):
    position = Position()
    position.x, position.y = robot.get_position()
    return position

def set_position(Position, ctx):
    if Position.x < 0 or Position.y < 0:
        return Status(StatusCode.OUT_OF_RANGE, "The number must be positive")

    robot.set_position(x=Position.x, y=Position.y)
    return Empty()

def get_id(Empty, ctx):
    id = get_id()
    return id

robot1 = Robot(id=1, x=random.randint(1, 9), y=random.randint(1, 9))
robot2 = Robot(id=2, x=random.randint(1, 9), y=random.randint(1, 9))
robot3 = Robot(id=3, x=random.randint(1, 9), y=random.randint(1, 9))
robot4 = Robot(id=4, x=random.randint(1, 9), y=random.randint(1, 9))
robot5 = Robot(id=5, x=random.randint(1, 9), y=random.randint(1, 9))

channel = Channel("amqp://guest:guest@localhost:5672")
provider = ServiceProvider(channel)
logging = LogInterceptor() # Log requests to console
provider.add_interceptor(logging)

# Os tipos das mensagens devem ser passados, tanto no request como no reply

provider.delegate(
    topic="Get.Id",
    function=get_id,
    request_type=Empty,
    reply_type=id)

provider.delegate(
    topic="Get.Position",
    function=get_position,
    request_type=Empty,
    reply_type=Position) 

provider.delegate(
    topic="Set.Position",
    function=set_position,
    request_type=Position,
    reply_type=Empty)

provider.run()
