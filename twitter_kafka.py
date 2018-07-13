"""
Created on Fri Jun 22 06:53:12 2018

@author: lalbrijesh 
"""

from kafka import KafkaClient, SimpleProducer
import configparser
import tweepy

class TwitterStream(tweepy.StreamListener):

    def __init__(self, api):
        self.api = api
        super(tweepy.StreamListener, self).__init__()
        client = KafkaClient("localhost:9092")
        self.producer = SimpleProducer(client, async = True, batch_send_every_n = 2500, batch_send_every_t = 5)

    def on_status(self, status):
        msg =  status.text.encode('utf-8')
        try:
            self.producer.send_messages('first-topic', msg)
        except Exception as e:
            print(e)
            return False
        return True

    def on_error(self, status_code):
        print("Error")
        return True

    def on_timeout(self):
        return True

if __name__ == '__main__':

    config = configparser.ConfigParser()
    config.read('twitter_credentials.txt')
    c_key = config['KEYS']['consumerKey']
    c_secret = config['KEYS']['consumerSecret']
    a_key = config['KEYS']['accessToken']
    a_secret = config['KEYS']['accessTokenSecret']

    auth = tweepy.OAuthHandler(c_key, c_secret)
    auth.set_access_token(a_key, a_secret)
    api = tweepy.API(auth)

    stream = tweepy.Stream(auth, listener = TwitterStream(api))

    stream.filter(track = ['trump', 'president'])
