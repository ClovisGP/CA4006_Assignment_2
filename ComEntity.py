from threading import Thread
import pika
import os


class ComEntity(Thread):

  _id = 0

  def __init__(self, id):
    super().__init__()
    self._id = id

  def getId(self):
     return self._id

  def sendMsg(self, queueName='default', msg: bytearray=''):
    """Send a message on the queueName"""
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    channel.queue_declare(queue=queueName)
    channel.basic_publish(exchange='',
                      routing_key=queueName,
                      body=msg)
    connection.close()

  def callback(self, ch, method, properties, body):
          print(" [x] Received %r" % body)

  def receiveMsg(self, queueName='default'):
    """Receive a message from the queueName"""
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.queue_declare(queue=queueName)      

    channel.basic_consume(queue=queueName, on_message_callback=self.callback, auto_ack=True)
    channel.start_consuming()

  def receiveResponse(self, queueName='default'):
    """Receive a response from the queueName and quit while returning the body or an empty string"""
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    channel.queue_declare(queue=queueName)      
    method_frame, header_frame, body = channel.basic_get(queue=queueName)        
    if method_frame is None:
        connection.close()
        return ''
    else:          
        channel.basic_ack(delivery_tag=method_frame.delivery_tag)
        connection.close()
        return body
  
  def behaviour():
     """"This method aims to contain the behaviour of the class."""
     print("No behaviour programmed for this Entity")

  def run(self) -> None:
     self.behaviour()