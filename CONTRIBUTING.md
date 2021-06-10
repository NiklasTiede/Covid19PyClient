
# Contributing

Contributions are welcome, and they are greatly appreciated! Every little bit
helps, and credit will always be given.

You can contribute in many ways:

# Types of Contributions


## Report Bugs


Report bugs at https://github.com/NiklasTiede/covid19pyclient/issues.

If you are reporting a bug, please include:

* Your operating system name and version.
* Any details about your local setup that might be helpful in troubleshooting.
* Detailed steps to reproduce the bug.

## Fix Bugs


Look through the GitHub issues for bugs. Anything tagged with "bug" and "help
wanted" is open to whoever wants to implement it.

## Implement Features

Look through the GitHub issues for features. Anything tagged with "enhancement" and "help wanted" is open to whoever wants to implement it.

## Write Documentation

COVID-19 API Python Client could always use more documentation, whether as part of the official COVID-19 API Python Client docs, in docstrings, or even on the web in blog posts, articles, and such.

## Submit Feedback

The best way to send feedback is to file an issue at https://github.com/NiklasTiede/covid19pyclient/issues.

If you are proposing a feature:

* Explain in detail how it would work.
* Keep the scope as narrow as possible, to make it easier to implement.
* Remember that this is a volunteer-driven project, and that contributions
  are welcome :)

# Get Started!

Ready to contribute? Here's how to set up `covid19pyclient` for local development.

1. Fork the `covid19pyclient` repo on GitHub.
2. Clone your fork locally:

```
$ git clone git@github.com:your_name_here/covid19pyclient.git
```

3. Install your local copy into a virtualenv. Assuming you have `pipenv` installed, this is how you set up your fork for local development:

```
    $ cd covid19pyclient/
    $ pipenv --python 3.9
    $ pipenv shell
    $ pip install -e .[dev]
```

4. Create a branch for local development:

```
$ git checkout -b name-of-your-bugfix-or-feature
```

   Now you can make your changes locally.

5. When you're done making changes, check that your changes pass linting (pre-commit) and the
   tests (pytest), including testing other Python versions with tox. Each of these can be called via the `Makefile`::

```
$ make pre-commit
$ make test
$ make test-all
```

The Makefile gives a nice overview about the workflows commonly used when working on the project as a developer.

6. Commit your changes and push your branch to GitHub::

```
$ git add .
$ git commit -m "Your detailed description of your changes."
$ git push origin name-of-your-bugfix-or-feature
```

7. Submit a pull request through the GitHub website.

# Pull Request Guidelines

Before you submit a pull request, check that it meets these guidelines:

1. The pull request should include tests.
2. If the pull request adds functionality, the docs should be updated. Put
   your new functionality into a function with a docstring, and add the
   feature to the list in README.md.
3. The pull request should work for Python 3.6, 3.7, 3.8 and 3.9. Check
   https://github.com/NiklasTiede/covid19pyclient/tree/main/.github/workflows
   and make sure that the tests pass for all supported Python versions.

# Tips

To run a subset of tests:

```
$ pytest tests/covid19pyclient_test.py
```

To lint a single file or enforce type checking for a particular file.

```
$ flake8 filename
$ mypy filename
```

# Deploying

A reminder for the maintainers on how to deploy. Make sure all your changes are committed (including an entry in CHANGELOG.md). Create the tag, release it on Github and the workflow for publishing at PyPI will kick in.
