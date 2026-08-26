# IDS706-Assignment-1

[![Python tests](https://github.com/USERZEROA/IDS706-Assignment-1/actions/workflows/test.yml/badge.svg)](https://github.com/USERZEROA/IDS706-Assignment-1/actions/workflows/test.yml)

## Overview

This project is a simple Python application for IDS 706 Data Engineering.

The application asks the user for a name and prints a welcome message. It also demonstrates professional software development practices including automated testing, code formatting, linting, containerization, and continuous integration.

The project uses:

* Python
* Virtual environments
* Pytest
* Black
* Ruff
* Makefile
* Docker
* GitHub Actions

## Bonus Enhancements

The project includes several enhancements beyond the basic example:

* Updated the welcome message to reference IDS 706 Data Engineering.
* Improved input handling by removing leading and trailing whitespace from user input.
* Added a default `Guest` name when the user provides empty input.
* Added a reusable `normalize_name()` helper function.
* Added additional unit tests for name normalization, whitespace handling, and empty input.
* Added automated code formatting with Black.
* Added automated linting with Ruff.
* Integrated formatting, linting, testing, and Docker testing into the project workflow.

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

The `.venv/` directory is used locally and is excluded from version control.

## Setup

Create a Python virtual environment:

```bash
python -m venv .venv
```

Activate the environment.

### Windows PowerShell

```powershell
.venv\Scripts\Activate.ps1
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

Run the application with:

```bash
make run
```

The program asks for a name and prints a welcome message for IDS 706 Data Engineering.

### Usage Example

```text
$ make run
Enter your name: Haiwei
Haiwei, welcome to IDS 706 Data Engineering!
```

The application also handles extra whitespace:

```text
$ make run
Enter your name:   Haiwei
Haiwei, welcome to IDS 706 Data Engineering!
```

If no name is provided, the application uses `Guest` as the default:

```text
$ make run
Enter your name:
Guest, welcome to IDS 706 Data Engineering!
```

## Run Tests

Run the test suite locally:

```bash
make test
```

The tests verify:

* Standard welcome message generation
* Whitespace handling
* Empty input handling
* Name normalization

## Formatting

Format the Python code with Black:

```bash
make format
```

## Linting

Check the Python code with Ruff:

```bash
make lint
```

## Run All Checks

Run dependency installation, formatting, linting, and testing together:

```bash
make all
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

Run the test suite inside Docker:

```bash
make docker-test
```

## Continuous Integration

GitHub Actions automatically runs project checks whenever code is pushed or a pull request is created.

The CI workflow performs:

1. Repository checkout
2. Python environment setup
3. Dependency installation
4. Code formatting
5. Linting
6. Unit tests
7. Docker image build
8. Tests inside Docker

The current workflow status is displayed by the badge at the top of this README.

## Clean Generated Files

Remove generated Python and testing cache files with:

```bash
make clean
```

## AI Assistance

AI tools were used for debugging and development assistance. All submitted code was reviewed and tested by the author.

## Author

Haiwei Yu
