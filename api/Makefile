# define the name of the virtual environment directory
VENV := venv
APP_DIR := app

# default target, when make executed without arguments
all: venv

#
$(VENV)/bin/activate:
	python3 -m venv $(VENV)
	./$(VENV)/bin/pip install -r ./requirements/requirements.txt -r ./requirements/requirements-dev.txt

venv: $(VENV)/bin/activate

# Test in normal mode
test: venv
	./$(VENV)/bin/python3 -m pytest

# Test in verbose mode
testv: venv
	./$(VENV)/bin/python3 -m pytest -v


run: venv
	./$(VENV)/bin/python3 $(APP_DIR)/main.py

clean:
	rm -rf $(VENV)
	find . -type f -name '*.pyc' -delete
	tree -if | grep -E '\.pyc|__pycache__' | xargs rm -r

lint:
	python -m black app tests
	python -m flake8 app tests

.PHONY: all venv run clean

