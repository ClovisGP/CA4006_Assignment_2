import pika

class ComEntity:
  _connectionTarget: str
  
  
  def __init__(self, connectionTarget):
    """aims"""
    self._connectionTarget = connectionTarget

  def sendMsg(self, dest, msg):
    connection = pika.BlockingConnection(pika.ConnectionParameters(self._connectionTarget))
    channel = connection.channel()
    channel.queue_declare(queue=dest)
    channel.basic_publish(exchange='',
                      routing_key=dest,
                      body=msg)
    connection.close()