This is the sourcecode for the queue website.

Prerequisites
=============

Production
----------

- Python 2.7.10 (noted in runtime.txt)
- PostgreSQL 9.4 (or higher)
- Python packages found in requirements.txt

Development
-----------
- Git
- Python 3.5.1  (noted in runtime.txt)
- PostgreSQL 9.4 (or higher)
- Virtualenvwrapper (https://virtualenvwrapper.readthedocs.org/en/latest/)
  This is a tool that lets you install python packages in a virtualenv, meaning
  you can have multiple projects on your computer with different versions
  of packages without them interfering with eachother.
- Python packages found in requirements.txt


Installation
============

Installation (local)
--------------------

::

    $ git clone git@github.com:Webdesignwill/queue.git queue
    $ cd queue
    $ pip install -r requirements.txt

    Now copy queue/local_example.py to queue/local.py and fill in the database credentials.

::

    $ python manage.py migrate
    $ python manage.py createsuperuser
    $ python manage.py runserver


Commands
========

Celery (local)
--------------

To start celery locally run

::

    $ celery -A queue worker -l info
