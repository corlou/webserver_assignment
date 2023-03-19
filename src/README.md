# Pole Calendar API

## Requirements

- Docker
- Python 3
- Pip

## Setup & Installation

1. Activate virtual environment.

This application runs inside a virtual environment, which ensures that dependencies can be managed independently of the global environment.
`source venv/bin/activate`

2. Run installation script.

Run this Makefile script to install the necessary dependencies.
`make install`

3. Setup postgres database.

A local instance of a Postgres database can be started and stopped with the scripts `make db:start` and `make db:stop`.

## Running

The API server can be started up using the following Makefile command:
`make start`

## Testing

The unit tests can be run using the following command:
`make test`
