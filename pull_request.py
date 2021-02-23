import settings
import random
from github import Github
import tweepy

CONSUMER_KEY = settings.ENV['CONSUMER_KEY']
CONSUMER_SECRET = settings.ENV['CONSUMER_SECRET']
ACCESS_KEY = settings.ENV['ACCESS_KEY']
ACCESS_SECRET = settings.ENV['ACCESS_SECRET']

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
tweepy = tweepy.API(auth)

def get_pull_request():

  greetings = ['Hi, ', 'Hello, ', 'Hey, ', 'Hi there, ', 'Hello there, ', 'Hey there, ']
  subject = ['see my new post ', 'take a look to my new post ', 'read my new post ', 'see my new article ', 'read my new article ', 'take a look to my new article ']
  preposition = ' in '

  g = Github(settings.ENV['USER_GITHUB'], settings.ENV['PSWD_GITHUB'])
  repo = g.get_repo(settings.ENV['REPO_GITHUB'])
  pulls = repo.get_pulls(state='open', sort='created', base='master')
  
  for pr in pulls:
    tweepy.update_status(random.choice(greetings) + random.choice(subject) + pr.title + preposition + settings.ENV['URL'] + '.')

