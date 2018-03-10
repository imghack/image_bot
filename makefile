

install:
	pip install -r requirements.txt & pip install pytest

run:
	python main.py & mongod

test:
	python -m pytest