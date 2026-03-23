.PHONY: install test run

install:
	python3 -m pip install -e '.[dev]'

test:
	pytest

run:
	python3 -m package_dispatcher 50 40 30 10
