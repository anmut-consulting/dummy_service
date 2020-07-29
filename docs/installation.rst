.. highlight:: shell

.. _installation:

============
Installation
============


Stable release
--------------

To install dummy_service, run this command in your terminal:

.. code-block:: console

    $ pip install git+ssh://git@github.com/anmut-consulting/dummy_service.git@latest

This is the preferred method to install dummy_service, as it will always install the most recent stable release.

If you're using **pipenv** for your virtual environment and you'd like to install from the repo, the command becomes (notice the ``#egg=dummy_service`` section)::

    $ pipenv install git+ssh://git@github.com/anmut-consulting/dummy_service.git@latest#egg=dummy_service


If you don't have `pip`_ installed, this `Python installation guide`_ can guide
you through the process.

.. _pip: https://pip.pypa.io
.. _Python installation guide: http://docs.python-guide.org/en/latest/starting/installation/


From sources
------------

The sources for dummy_service can be downloaded from the `Github repo`_.

You can either clone the public repository:

.. code-block:: console

    $ git clone git://github.com/anmut-consulting/dummy_service

Or download the `tarball`_:

.. code-block:: console

    $ curl  -OL https://github.com/anmut-consulting/dummy_service/tarball/latest

Once you have a copy of the source, you can install it with:

.. code-block:: console

    $ python setup.py install


.. _Github repo: https://github.com/anmut-consulting/dummy_service
.. _tarball: https://github.com/anmut-consulting/dummy_service/tarball/latest
