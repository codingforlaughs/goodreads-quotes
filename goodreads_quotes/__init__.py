# -*- coding: utf-8 -*-
"""
    goodreads_quotes
    ~~~~~~~~~~~~~~~~

    goodreads_quotes module
"""

import requests
from requests.exceptions import RequestException, Timeout
from lxml import html
from six import u
import json

__version__ = '0.1.0'

class GoodreadsException(Exception):
    """Goodreads exception
    """
    
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        """ Try to pretty-print the exception, if this is going on screen. """

        def red(words):
            return u("\033[31m\033[49m%s\033[0m") % words

        def blue(words):
            return u("\033[34m\033[49m%s\033[0m") % words

        msg = (
                "\n{red_error}"
                "\n\n{message}\n".format(
                    red_error=red("Error occured"),
                    message=blue(str(self.msg))
                ))
        return msg

class Goodreads:

    @staticmethod
    def get_recent_quotes():
        from random import randint
        i = randint(1,100)
        try:
            quotes_page = requests.get(f'https://www.goodreads.com/quotes/recently_added?page={i}')
        except Timeout as e:
            raise GoodreadsException(e)
        except RequestException as e:
            raise GoodreadsException(e)

        tree = html.fromstring(quotes_page.content)

        quotes = []
        for quote_div in tree.xpath('//div[@class="quoteText"]'):
            quote_text = quote_div.xpath('text()')[0].strip().replace('“', '').replace('”', '')
            # author = quote_div.xpath('a/text()')[0].strip()
        for quote_div in tree.xpath('//span[@class="authorOrTitle"]'):
            author = quote_div.xpath('text()')[0].strip().replace('“', '').replace('”', '')
            # author = quote_div.xpath('a/text()')[0].strip()
              
            quote = {
                'quote': quote_text,
                'author': author
            }

            quotes.append(quote)

        return quotes

    @staticmethod
    def get_popular_quotes():
        from random import randint
        i = randint(1,100)
        try:
            quotes_page = requests.get(f'https://www.goodreads.com/quotes?page={i}')
        except Timeout as e:
            raise GoodreadsException(e)
        except RequestException as e:
            raise GoodreadsException(e)

        tree = html.fromstring(quotes_page.content)

        quotes = []
        for quote_div in tree.xpath('//div[@class="quoteText"]'):
            quote_text = quote_div.xpath('text()')[0].strip().replace('“', '').replace('”', '')
            # author = quote_div.xpath('a/text()')[0].strip()
        for quote_div in tree.xpath('//span[@class="authorOrTitle"]'):
            author = quote_div.xpath('text()')[0].strip().replace('“', '').replace('”', '')
            # author = quote_div.xpath('a/text()')[0].strip()
              
            quote = {
                'quote': quote_text,
                'author': author
            }

            quotes.append(quote)

        return quotes

    @staticmethod
    def get_daily_quote_as_json():
        return json.dumps(Goodreads.get_recent_quote())

    @staticmethod
    def get_popular_quotes_as_json():
        return json.dumps(Goodreads.get_popular_quotes())
