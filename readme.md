# Screwdriver

Collections for CI deploy utils.

- deploy with github actions.
- Working with github API
- Encrypt and decrypt files (some text variables)

## Quic Start

This is sample, how to collect release changes in github actions.

`.github/workflows/hello_world.yml`:

```yaml
name: Simple Hello world Job

on:
  workflow_dispatch:
  push:

jobs:
  tests:
    name: Collect Release Changes
    runs-on: ubuntu-latest
    steps:
      - uses: klee0kai/screwdriver@master
        with:
          cmd: hello_world -l --summary
```

Install as python lib

    pip3 install .

Install `screwdriver` bash tool to `$HOME/.local/bin`
    
    pip3 install .
    python3 ./install_scripts.py

## Using Env

- SECRETS_GH_API_TOKEN - github api token

## License

```
Copyright (c) 2023 Andrey Kuzubov
```
