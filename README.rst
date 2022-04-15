goodreads-quotes
================

A Python module to fetch popular quotes and quote of the day from `Goodreads <https://goodreads.com/quotes>`_ page.

Dependencies
------------

This package depends on the following packages:

- requests
- lxml
- u

They can be installed using ``pip``.

::

    sudo pip install -r requirements.txt


Installation
------------

- You will need [Python 3](https://www.python.org/download/).
- [pip](http://pip.readthedocs.org/en/latest/installing.html) is recommended for installing dependencies.

::

    sudo pip install goodreads_quotes

Getting Started
---------------

.. code:: python

    from goodreads_quotes import Goodreads

    print(Goodreads.get_popular_quotes())
    print(Goodreads.get_popular_quotes_as_json())
    print(Goodreads.get_daily_quote())
    print(Goodreads.get_daily_quote_json())
    
Example
-------------

.. code:: python

    from goodreads_quotes import Goodreads
    from random import randint

    qtxt = Goodreads.get_daily_quote() ## dict stored in list var

    ubnd = len(qtxt) ## get upper bound of list
    i = randint(0, ubnd-1) ## create var to hold random number based on ubound of list
    quote = qtxt[i]['quote'] ## access quote text var
    author = qtxt[i]['author'] ## access author text var
    print(quote + '\n' +  author.strip(',')) ## example of clean quote w/ author on next line

Features
--------

- Popular quote: pulls from popular quote page
- Daily quote: pulls from recent quote page

Contribution
------------

Feel free to create a Github issue. Also, you are more than welcome to submit
a pull request for a bug fix or additional feature.

License
-------

`MIT License <http://opensource.org/licenses/mit-license.php>`_
