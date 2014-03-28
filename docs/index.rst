.. Pacific Project documentation master file, created by
   sphinx-quickstart on Tue Dec  3 17:33:38 2013.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Pacific Project
===============

Contents:

.. toctree::
   :maxdepth: 2


Getting started
---------------

.. code-block:: bash

    $ vagrant up
    $ vagrant ssh
    vagrant@precise64:~$ cd /vagrant
    vagrant@precise64:/vagrant$ source ~/venv/pacific/bin/activate
    (pacific)vagrant@precise64:/vagrant$ python setup.py develop
    (pacific)vagrant@precise64:/vagrant$ pacific run config.yml


Navigate to https://localhost:34443/

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

