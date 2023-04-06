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

  def sendMsg(self, queueName='default', msg=''):
    """Send a message on the queueName"""
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    channel.queue_declare(queue=queueName)
    print("before message posted")
    channel.basic_publish(exchange='',
                      routing_key=queueName,
                      body=msg)
    print("message posted")
    connection.close()

  def callback(self, ch, method, properties, body):
          print(" [x] Received %r" % body)

  def receiveMsg(self, queueName='default'):
    """Receive a message from the queueName"""
    try:
      connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
      channel = connection.channel()

      channel.queue_declare(queue=queueName)      

      channel.basic_consume(queue=queueName, on_message_callback=self.callback, auto_ack=True)
      print(' [*] Waiting for messages. To exit press CTRL+C')
      channel.start_consuming()
    except KeyboardInterrupt:
        os.exit()
  
  def run(self) -> None:
     return super().run()