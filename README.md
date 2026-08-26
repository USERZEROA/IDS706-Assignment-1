# IDS706-Assignment-1
[![Python tests](https://github.com/USERZEROA/IDS706-Assignment-1/actions/workflows/test.yml/badge.svg)](https://github.com/USERZEROA/IDS706-Assignment-1/actions/workflows/test.yml)

## Overview

This project is a simple Python application for IDS 706 Data Engineering.

The application asks the user for a name and prints a welcome message. The project also demonstrates a basic software engineering workflow using:

* Python 3.12
* Virtual environments
* Pytest
* Black
* Ruff
* Makefile
* Docker
* GitHub Actions

## Project Structure

```text
IDS706-Assignment-1/
├── .github/
│   └── workflows/
│       └── test.yml
├── src/
│   └── main.py
├── tests/
│   └── test_main.py
├── .dockerignore
├── .gitignore
├── Dockerfile
├── Makefile
├── README.md
└── requirements.txt
```

## Setup

Create a Python virtual environment:

```bash
python -m venv .venv
```

Activate the environment.

### Windows

```powershell
.venv\Scripts\activate
```

### macOS / Linux

```bash
source .venv/bin/activate
```

Install the required dependencies:

```bash
make install
```

## Run the Application

```bash
make run
```

The program will ask for a name and print a welcome message for the Data Engineering course.

## Run Tests

Run the test suite locally:

```bash
make test
```

## Formatting

Format the Python code with Black:

```bash
make format
```

## Linting

Check the code with Ruff:

```bash
make lint
```

## Docker

Build the Docker image:

```bash
make docker-build
```

Run the application inside Docker:

```bash
make docker-run
```

Run the tests inside Docker:

```bash
make docker-test
```

## Continuous Integration

GitHub Actions automatically runs the project checks whenever code is pushed or a pull request is created.

The CI workflow performs:

1. Repository checkout
2. Python 3.12 setup
3. Dependency installation
4. Code formatting
5. Linting
6. Unit tests
7. Docker image build
8. Tests inside Docker

The workflow status is shown by the badge at the top of this README.

## Clean Generated Files

```bash
make clean
```

## Author

Haiwei Yu