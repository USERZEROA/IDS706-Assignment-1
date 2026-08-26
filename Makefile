.PHONY: all install format lint test run docker-build docker-run docker-test clean

IMAGE_NAME := data-engineering-demo

# Run the main project checks
all: install format lint test

# Install dependencies
install:
	python -m pip install -r requirements.txt

# Format Python code
format:
	python -m black src tests

# Lint Python code
lint:
	python -m ruff check src tests

# Run tests
test:
	python -m pytest -q

# Run the application
run:
	python src/main.py

# Build the Docker image
docker-build:
	docker build -t $(IMAGE_NAME) .

# Run the application inside Docker
docker-run:
	docker run -it --rm $(IMAGE_NAME)

# Run the test suite inside Docker
docker-test:
	docker run --rm $(IMAGE_NAME) python -m pytest -q

# Clean generated Python cache files
clean:
	python -c "import shutil; from pathlib import Path; [shutil.rmtree(p, ignore_errors=True) for root in ('src', 'tests') for p in Path(root).rglob('__pycache__')]; shutil.rmtree('.pytest_cache', ignore_errors=True); shutil.rmtree('.ruff_cache', ignore_errors=True)"