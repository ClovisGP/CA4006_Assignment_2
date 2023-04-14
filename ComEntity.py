from threading import Thread
import pika

class ComEntity(Thread):

  _id: int

  def __init__(self, id):
    super().__init__()
    self._id = id

  def getId(self):
    return self._id
  
  def setUp(self):
    """To be overrided"""
    pass

  def sendMsg(self, queueName='default', msg =''):
    """Send a message on the queueName"""
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    channel.queue_declare(queue=queueName)
    channel.basic_publish(exchange='',
                      routing_key=queueName,
                      body=msg)
    connection.close()

  def receiveResponse(self):
    """Receive a response from the queueName and quit while returning the body or an empty string"""
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    queueName = str(self._id)

    channel.queue_declare(queue=queueName)
    method_frame, header_frame, body = channel.basic_get(queue=queueName)
    while (method_frame is None):
      method_frame, header_frame, body = channel.basic_get(queue=queueName)         
    channel.basic_ack(delivery_tag=method_frame.delivery_tag)
    connection.close()
    return str(body, encoding="utf-8")
  
  def behaviour(self):
    """"This method aims to contain the behaviour of the class."""
    print("No behaviour programmed for this Entity")

  def run(self) -> None:
    while True:
        self.behaviour()