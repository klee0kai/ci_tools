# CI/CD Tools

Collections for CI deploy utils.
 - deploy with github actions. 
 - Working with github API 

## Quic Start 

This is sample, how to collect release changes in github actions.

`.github/workflows/collect_release_changes.yml`:
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
          cmd: hello_world
```

## Using Env

 - SECRETS_GH_API_TOKEN - github api token 

## License

```
Copyright (c) 2023 Andrey Kuzubov
```
