# https://github.com/kevinzg/facebook-scraper/blob/master/README.md
# https://github.com/kevinzg/facebook-scraper/issues/214

"""
facebook-scraper - collecting corpora in alsatian.

This script allows to collect posts and comments in alsatian with the help of twint
See here: https://github.com/kevinzg/facebook-scraper

Autor: Audrey Deck
Created: 06-2021
"""

from facebook_scraper import write_posts_to_csv

posts = write_posts_to_csv(account = 'olcalsace',	
                    filename = 'facebook_ocla.csv',
                    encoding = 'utf8',
                    # options = {'comments': True},
                    pages = 30)
for post in posts:
    print(post)