# themodelbot

import tweepy as tp
import time
import os


from config import *


# login to twitter account api
auth = tp.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tp.API(auth)


os.chdir('models')


# iterates over pictures in models folder
for model_image in os.listdir('.'):
    api.update_with_media(model_image)
    time.sleep(10)



