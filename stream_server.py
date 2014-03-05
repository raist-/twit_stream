from TwitterAPI import TwitterAPI
import concurrent.futures
import redis

class Stream_Server(object):

    def __init__(self, api_credentials_path):
        # read in the api setup credentials from file

        consumer_key = ''
        consumer_secret = ''
        access_token_key = ''
        access_token_secret = ''
        self.__api = TwitterAPI(consumer_key, consumer_secret, access_token_key, access_token_secret)
        self.__redis = redis.StrictRedis(host='localhost', port=6379, db=0)

    def stream_tweets(self, api, method, param_dict, time_to_live):

        response = api.request(method, param_dict)
        
    def handle_stream_requests(self):

        with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
            # Start the load operations and mark each future with its URL
            future_to_url = {executor.submit(stream_tweets, url, 60): url for url in URLS}
            for future in concurrent.futures.as_completed(future_to_url):
                url = future_to_url[future]
                try:
                    data = future.result()
                except Exception as exc:
                    print('%r generated an exception: %s' % (url, exc))
                else:
                    print('%r page is %d bytes' % (url, len(data)))
        