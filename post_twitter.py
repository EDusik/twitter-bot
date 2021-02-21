#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tweepy, time, sys
import settings
from pull_request import get_pull_request

CONSUMER_KEY = settings.ENV['CONSUMER_KEY']
CONSUMER_SECRET = settings.ENV['CONSUMER_SECRET']
ACCESS_KEY = settings.ENV['ACCESS_KEY']
ACCESS_SECRET = settings.ENV['ACCESS_SECRET']

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

# time.sleep(900) #Tweet every 15 minutes

api.update_status(get_pull_request())