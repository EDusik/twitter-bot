#!/usr/bin/env python
# -*- coding: utf-8 -*-

from github import Github
import settings

def get_pull_request():
  g = Github(settings.ENV['USER_GITHUB'], settings.ENV['PSWD_GITHUB'])
  repo = g.get_repo('EDusik/my-blog')
  try:
    pulls = repo.get_pulls(state='open', sort='created', base='master')
    # breakpoint()
    for pr in pulls:
      return 'Hello, see my new post ' + pr.title + ' in ' + settings.ENV['URL'] + '.'
  except:
    return null
  # breakpoint()
