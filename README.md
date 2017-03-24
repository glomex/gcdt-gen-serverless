# Plugins for gcdt

author: glomex OPS Team


## List of available plugins 

gcdt-plugins is a collection of gcdt plugins we use internally @ glomex.

* say_hello - the friendliest plugin ever
* gcdt_slack_plugin - inform slack channels about deployments on prod
* gcdt_datadog_plugin - collect gcdt usage statistics for the gcdt dashboard
* ...


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
