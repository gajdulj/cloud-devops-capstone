## The Makefile includes instructions on environment setup and lint tests
# setup: Create and activate a virtual environment
# install: Install dependencies from requirements.txt
# test: ...
# lint: ...

setup:
	# Creates python virtualenv
	# When it's done run command below manually to activate:
	# source venv/bin/activate
	# Note: On Mac Big sur you cannot name them starting with a dot
	python3 -m venv venv

install:
	# This should be run from inside a virtualenv
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	# Additional, optional, tests could go here
	# python -m pytest -vv --cov=myrepolib tests/*.py

lint:
	# See local hadolint install instructions:   https://github.com/hadolint/hadolint
	# This is linter for Dockerfiles
	hadolint Dockerfile
	# This is a linter for Python source code linter: https://www.pylint.org/
	# This should be run from inside a virtualenv
	pylint --disable=R,C,W1203 app.py

all: install lint test
