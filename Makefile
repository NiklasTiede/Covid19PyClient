

# ------------- Installation  ------------------------------------
.Phony: install

install: clean ## install the package to the active Python's site-packages
	python setup.py install

dev-install: ## install the package to the active Python's site-packages for development
	pip install -e .[dev]

# ------------- Test/Lint  ------------------------------------

.PHONY: pre-commit pre-commit-update lint test test-all

pre-commit: ## apply pre-commit to all files
	pre-commit run --all-files

pre-commit-update: ## update pre-commit
	pre-commit autoupdate

lint: ## check style with flake8
	flake8 covid19pyclient tests

test: ## run tests quickly with the default Python
	pytest -s -vvv

test-all: ## test across Python 3.6 - 3.9
	tox

coverage: ## check code coverage quickly with the default Python
	coverage run --source src/covid19pyclient -m pytest
	coverage report -m
	coverage html
	$(BROWSER) htmlcov/index.html



# ------------- Clean Artifacts (Test/Lint/Build) ---------------------

.PHONY: clean clean-pyc clean-test clean-build

clean: clean-pyc clean-test clean-build clean-coverage ## remove all build, test and Python artifacts

clean-pyc: ## remove Python file artifacts
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-test: ## remove test and coverage artifacts
	rm -fr .tox/
	rm -fr .mypy_cache
	rm -fr .pytest_cache

clean-build: ## remove build artifacts
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +

clean-coverage: ## remove coverage report
	rm -fr .coverage
	rm -fr htmlcov


# ------------  Documentation  -----------------------------------

docs: ## generate Sphinx HTML documentation, including API docs
	# rm -f docs/covid19pyclient.rst
	# rm -f docs/modules.rst
	# sphinx-apidoc -o docs/ covid19pyclient
	# $(MAKE) -C docs clean
	# $(MAKE) -C docs html
	$(BROWSER) docs/build/html/index.html

servedocs: docs ## compile the docs watching for changes
	watchmedo shell-command -p '*.rst' -c '$(MAKE) -C docs html' -R -D .



# ------------  Deployment  -----------------------------------

.PHONY: dist release

dist: clean ## builds source and wheel package
	python setup.py sdist
	python setup.py bdist_wheel
	ls -l dist

release: dist ## package and upload a release
	twine upload dist/*



# ------------  Help  --------------------------------------

.PHONY: help

help: ## This help.
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

.DEFAULT_GOAL := help

define BROWSER_PYSCRIPT
import os, webbrowser, sys

from urllib.request import pathname2url

webbrowser.open("file://" + pathname2url(os.path.abspath(sys.argv[1])))
endef
export BROWSER_PYSCRIPT

BROWSER := python -c "$$BROWSER_PYSCRIPT"
