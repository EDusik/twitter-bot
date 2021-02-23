import time
import settings
import schedule
from github import Github
from pull_request import get_pull_request

def update_twitter():
  get_pull_request()

g = Github(settings.ENV['USER_GITHUB'], settings.ENV['PSWD_GITHUB'])
repo = g.get_repo(settings.ENV['REPO_GITHUB'])
pulls = repo.get_pulls(state='open', sort='created', base='master')

if pulls:
  for pr in pulls:
    # schedule.every().day.at("23:59").do(update_twitter)
    schedule.every(1).minutes.do(update_twitter)
else:
  print('No pull requests today')

while 1:
  schedule.run_pending()
  time.sleep(1)