build:
	poetry build

package-install:
	python3 -m pip install --user dist/*.whl

lint:
	poetry run flake8 gendiff

uninstall:
	pip uninstall hexlet-code

test-coverage:
    poetry run pytest --cov=gendiff --cov-report xml