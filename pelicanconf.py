#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = "Daniele D'Avino"
SITENAME = "Daniele D'Avino"
SITEURL = ''

PATH = 'content'

THEME = 'tema/pelican-themes/pelican-hyde'

TIMEZONE = 'Europe/Berlin'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Biography
BIO = "Decision Intelligence Data Scientist @ Virtual B"
PROFILE_IMAGE = 'avatar.png'


# # Blogroll
# LINKS = (('Pelican', 'http://getpelican.com/'),
#          ('Python.org', 'http://python.org/'),
#          ('Jinja2', 'http://jinja.pocoo.org/'),
#          ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('email','daniele.davino@live.it'),
          ('linkedin', 'https://www.linkedin.com/in/daniele-d-avino-a2678354'),
          ('twitter','https://twitter.com/DAvinoDaniele'),
          ('github', 'https://github.com/davins90'))


DEFAULT_PAGINATION = 3

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# URL settings
ARTICLE_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'
PAGE_URL = 'pages/{slug}/'
PAGE_SAVE_AS = 'pages/{slug}/index.html'

# Plugins
PLUGIN_PATHS = [ 'plugins/pelican-plugins' ]
PLUGINS = [ 'summary' ]

# altro 
DIRECT_TEMPLATES = ['blog']
PAGINATED_DIRECT_TEMPLATES = ['blog']

# Static files
STATIC_PATHS = ['extra','images','pdf']
EXTRA_PATH_METADATA = {'extra/favicon.ico': {'path': 'favicon.ico'},
                              'extra/robots.txt':{'path': 'robots.txt'}}

