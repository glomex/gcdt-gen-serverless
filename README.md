# AWS serverless scaffolding generator for gcdt

author: glomex OPS Team

## Features



## Running tests

If you add a plugin here it is very important to have a good test coverage so we can make sure your plugin runs with the next gcdt version.

Run tests like so:

``` bash
$ python -m pytest -vv --cov-report term-missing plugins/say_hello/tests/test_*
```

If you want to run tests for all plugins (like to prepare for a release)

``` bash
$ python -m pytest -vv --cov-report term-missing --cov plugins plugins/*/tests/test_*
```
