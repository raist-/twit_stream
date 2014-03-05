import redis
import threading

class StreamClient(threading.Thread):

    def __init__(self, redis_connection, channel):
        threading.Thread.__init__(self)
        self.__redis_connection = redis_connection
        self.pubsub = self.__redis_connection.pubsub()
        self.__channel = channel
        self.pubsub.subscribe(channel)


    def run(self):
        for item in self.pubsub.listen():
            if item['data'] == "END":
                self.pubsub.unsubscribe(channel)

                print 'unsubscribing from channel : ' + self.__channel
                break
            else:
                print 'received message : ' + item['data']




if __name__ == "__main__":
    r = redis.Redis()
    client = StreamClient(redis.Redis(), 'hello')
    client.start()

    r.publish('hello', 'this will reach the listener')
    r.publish('hello', 'this will not')

    r.publish('hello', 'END')

