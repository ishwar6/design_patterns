# lets try to make a basic kafka. 

# Define the Message Model

class Message:
    def __init__(self, topic, data):
        self.topic = topic
        self.data = data

# Broker Class

import threading
import queue

class Broker:
    def __init__(self):
        # Dictionary to store topics and their corresponding queues
        self.topics = {}  
      
    def create_topic(self, topic):
        if topic not in self.topics:
            self.topics[topic] = queue.Queue()

    def publish_message(self, message):
        if message.topic in self.topics:
            self.topics[message.topic].put(message)

    def get_message(self, topic, consumer_id):
        # Here we will add logic to manage consumers and their offsets
        if topic in self.topics:
            return self.topics[topic].get()
        return None


# Produce Class

class Producer:
    def __init__(self, broker):
        self.broker = broker

    def send(self, topic, data):
        message = Message(topic, data)
        self.broker.publish_message(message)




# consumer Class
class Consumer:
    def __init__(self, broker, topic):
        self.broker = broker
        self.topic = topic
        self.consumer_id = self._generate_consumer_id()  

    def consume(self):
        return self.broker.get_message(self.topic, self.consumer_id)

    def _generate_consumer_id(self):
        # we will generate a unique ID for the consumer
        return  random(124312341435234,9921341234232323232)











