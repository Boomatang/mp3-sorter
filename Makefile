.PHONY: playground/create
playground/create: 
	unzip playground.zip

.PHONY: playground/clean
playground/clean:
	rm -R playground

.PHONY: playground/reset
playground/reset: playground/clean playground/create

.PHONY: setup/python
setup/python:
	python -m venv venv --prompt mp3sorter

.PHONY: activate
activate:
	echo -e "Run command:\nsource venv/bin/activate"
