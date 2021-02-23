import tweepy, time, sys
import settings
import schedule

from pull_request import get_pull_request

CONSUMER_KEY = settings.ENV['CONSUMER_KEY']
CONSUMER_SECRET = settings.ENV['CONSUMER_SECRET']
ACCESS_KEY = settings.ENV['ACCESS_KEY']
ACCESS_SECRET = settings.ENV['ACCESS_SECRET']

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

def update_twitter():
  api.update_status(get_pull_request())

schedule.every().day.at("23:59").do(update_twitter)

while 1:
  schedule.run_pending()
  time.sleep(1)