install:
	pip install --upgrade pip &&\
	pip install -r requirements.txt
format:
	black *.py mylib/*.py
lint:
	pylint *.py mylib/*.py
	# or pylint --disable=R,C *.py mylib/*.py if you want to disable some of their feature
test:
	python -m pytest -vv --cov=mylib --cov=main test_*.py
build:
	# build docker image
	docker build -t deploy-fastapi .
deploy:
	# run docker container (should be run by docker-compose instead of directly run like this)
	docker run -d -p 127.0.0.1:8080:8080 deploy-fastapi
	# after this, we can deploy this on aws ecs and using aws codebuild to automation deploy

all: install lint test build deploy
