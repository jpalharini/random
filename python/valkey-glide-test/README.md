# Valkey in Python

This project sets up a connection to a Valkey client and allows for interaction with it via REPL.

## Usage

1. Make sure the address of the Valkey server is correct in `valkey_test.py`.
2. Start a REPL by running `python valkey_test.py`.
3. Run any Valkey commands supported by Valkey GLIDE (should be all).

Examples:

```python
client.set("key", "value")

client.get("key")
```
