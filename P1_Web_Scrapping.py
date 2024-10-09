# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 18:25:57 2024

@author: juanf
"""

import requests
from bs4 import BeautifulSoup as bs

try:
  github_user = input('Input GitHub user: ')
  url = 'https://github.com/' + github_user
  r = requests.get(url)
  soup = bs(r.content, 'html.parser')
  profile_image = soup.find('img', {'class': 'avatar'})['src']
  print(profile_image)
except TypeError:
  print('Image not exist')
except:
  print('Username not found')

