.. highlight:: shell

.. _contributing:

============
Contributing
============

Contributions are welcome, and they are greatly appreciated! Every little bit
helps, and credit will always be given.

You can contribute in many ways:

Types of Contributions
----------------------

Report Bugs
~~~~~~~~~~~

Report bugs at https://github.com/anmut-consulting/dummy_service/issues.

If you are reporting a bug, please include:

* Your operating system name and version.
* Any details about your local setup that might be helpful in troubleshooting.
* Detailed steps to reproduce the bug.

Fix Bugs
~~~~~~~~

Look through the GitHub issues for bugs. Anything tagged with "bug" and "help
wanted" is open to whoever wants to implement it.

Implement Features
~~~~~~~~~~~~~~~~~~

Look through the GitHub issues for features. Anything tagged with "enhancement"
and "help wanted" is open to whoever wants to implement it.

Write Documentation
~~~~~~~~~~~~~~~~~~~

dummy_service could always use more documentation, whether as part of the
official dummy_service docs and in docstrings.

Submit Feedback
~~~~~~~~~~~~~~~

The best way to send feedback is to file an issue at https://github.com/anmut-consulting/dummy_service/issues.

If you are proposing a feature:

* Explain in detail how it would work.
* Keep the scope as narrow as possible, to make it easier to implement.

Get Started!
------------

Ready to contribute? Here's how to set up `dummy_service` for local development.

1. Clone the `dummy_service` repo on GitHub.::

    $ git clone git@github.com:anmut-consulting/dummy_service.git

2. Create a pipenv environment (assuming you have the `basics <https://github.com/anmut-consulting/pipenv-cookiecutter/blob/master/the_basics.md>`_ covered) ::

    $ cd dummy_service
    $ pipenv run init

3. Activate your environment shell. ::

    $ pipenv shell

4. Create a branch for local development::

    $ git checkout -b name-of-your-bugfix-or-feature

Now you can make your changes locally.

5. When you're done making changes, check that your changes pass all the tests by running::

    # to run the pre-commit hooks only, run:
    $ pipenv run tests
    # or
    $ pipenv run commit_test

    # to run coverage test only, run:
    $ pipenv run coverage

    # to run the pre-commit PUSH hooks, run:
    $ pipenv run push_test

    # to make the documentation, run:
    $ pipenv run make_docs

6. Commit your changes and push your branch to GitHub::

    $ git add .
    $ git commit -m "Your detailed description of your changes."
    $ git push origin name-of-your-bugfix-or-feature

7. Submit a pull request through the GitHub website.

Pull Request Guidelines
-----------------------

Before you submit a pull request, check that it meets these guidelines:

1. The pull request should include tests.
2. If the pull request adds functionality, the docs should be updated. Put
   your new functionality into a function with a docstring, and add the
   feature to the list in README.rst.
3. The pull request should work for Python 3.6+

Tips
----

You can check the command next to each of the **entry:** lines in :file:`.pre-commit-config.yaml` to understand what each of the individual pre-commit hooks runs.

Check the [scripts] section in :file:`Pipfile` to see the shortcuts you can run with ``$ pipenv run ..``, i.e. ``$ pipenv run coverage``.

Deploying
---------

A reminder for the maintainers on how to deploy.
Make sure all your changes are committed (including an entry in :file:`HISTORY.rst`).
Then run::

  $ pipenv run release [major/minor/patch]
