from github import Github
import settings
import random

# breakpoint()
def get_pull_request():

  greetings = ['Hi, ', 'Hello, ', 'Hey, ', 'Hi there, ', 'Hello there, ', 'Hey there, ']
  subject = ['see my new post ', 'take a look to my new post ', 'read my new post ', 'see my new article ', 'read my new article ', 'take a look to my new article ']
  preposition = ' in '

  g = Github(settings.ENV['USER_GITHUB'], settings.ENV['PSWD_GITHUB'])
  repo = g.get_repo(settings.ENV['REPO_GITHUB'])

  try:
    pulls = repo.get_pulls(state='open', sort='created', base='master')
    for pr in pulls:
      return random.choice(greetings) + random.choice(subject) + pr.title + preposition + settings.ENV['URL'] + '.'
  except:
    return null

