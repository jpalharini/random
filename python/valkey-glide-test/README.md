# Valkey in Python

This project sets up a connection to a Valkey client and allows for interaction with it via REPL.

## Setup

The project is managed using [uv](https://github.com/astral-sh/uv). If you have it installed, just use `uv venv` followed by `source .venv/bin/activate` to use a virtualenv containing all dependencies.

## Usage

1. Make sure the address of the Valkey server is correct in `valkey_test.py`.
2. Start a REPL by running `python valkey_test.py`.
3. Run any Valkey commands supported by Valkey GLIDE (should be all).

Examples:

```python
client.set("key", "value")

client.get("key")
```
