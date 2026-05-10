install:
	pip install -r requirements.txt

run:
	python main.py

test:
	pytest

doctest:
	python -m doctest -v app/calculator.py

lint:
	flake8 .

format:
	black .

check-format:
	black --check .

security:
	safety check

all:
	make test
	make doctest
	make check-format
	make security