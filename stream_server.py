from TwitterAPI import TwitterAPI
import redis
import json
import time
import pprint

class Stream_Server(object):

    def __init__(self, api_credentials_path):
        # read in the api setup credentials from file

        consumer_key = 'ise3iDCoHcrXyMSYbLZKA'
        consumer_secret = 'fg6FfGeuvlU8XQwjS7SWdnQ7jvT2t8hFloEJkCEGw'
        access_token_key = '2371236566-ubGrPfBPHNvVtpOwQqgGwf6UOtN4Ab0KxSPzOVf'
        access_token_secret = '5MHnzoHGNx3vk3oixCLBaz49ZdlJDRWWbbmVwEigjlQjy'
        self.__api = TwitterAPI(consumer_key, consumer_secret, access_token_key, access_token_secret)
        self.__redis = redis.StrictRedis(host='localhost', port=6379, db=0)

        self.__pubsub = self.__redis.pubsub()

    def stream_tweets(self, twitter_request, time_to_live):

        response = self.__api.request(twitter_request['method'], {"locations":"-74,40,-73,41"})

        start = time.time()
        elapsed = 0
        
        for item in response.get_iterator():
            if (elapsed > time_to_live):
                self.__redis.publish(twitter_request['channel'], 'END')
                break
            
            self.__redis.publish(twitter_request['channel'], item)

            elapsed = time.time() - start
        
        
    def handle_stream_requests(self):

        serialized_request = self.__redis.brpop(['twitter_requests'], 1)

        if serialized_request is not None:
            pprint.pprint(serialized_request)
            msg = serialized_request[1].decode("utf-8")
            pprint.pprint(msg)
            deserialized_request = json.loads(msg)

            self.stream_tweets(deserialized_request, 15)
        