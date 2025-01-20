# ChatBot for website

## Setup

Create virtual environment.

```bash
$ pyenv shell 3.12.0
$ poetry self update 1.8.3
$ poetry install
```

Install pre-commit.

```bash
$ poetry run pre-commit install
$ poetry run pre-commit install --hook-type commit-msg
```

## Prerequisites

Create **.env** file from **.env.example** and replace values if necessary.

```bash
$ cp .env.example .env
```

### LLM client

Create [access token](https://huggingface.co/docs/hub/en/security-tokens) in hugginface website and put in **.env** file.

## Populate data into vector database

Run the script:

```bash
$ python -m data.populate
```

## Run application

Run application and open localhost with provided port for UI.

```bash
$ python -m app.main
```
