

install:
	pip install -r requirements.txt & pip install pytest

run:
	python main.py & mongod

test:
    @echo "[RUN]: run flask app and mongod"
	python -m pytest

#TODO :
kill:
	kill -9 $(ps aux | grep python | awk '{print $2}')
