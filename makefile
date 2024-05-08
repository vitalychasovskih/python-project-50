install:
	poetry install

build:
	poetry build

package-install:
	python3 -m pip install --user dist/*.whl

lint:
	poetry run flake8 gendiff
	poetry run flake8 tests

uninstall:
	pip uninstall hexlet-code

test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml