#!/usr/bin/env python
# -*- coding: utf-8 -*-

from github import Github
import settings

def get_pull_request():
  g = Github(settings.ENV['USER_GITHUB'], settings.ENV['PSWD_GITHUB'])
  repo = g.get_repo('my-blog')
  try:
    pull_request = repo.get_pulls('all')
    return pull_request.name
  except:
    return null
  # breakpoint()