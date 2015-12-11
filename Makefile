all: env test

env:
	@export PYTHONPATH=.

test:
	@find . -name '*.py' | xargs -I file python file && echo 'All tests passed.'
