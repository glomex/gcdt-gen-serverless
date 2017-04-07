# -*- coding: utf-8 -*-
"""Implement scaffolding for AWS serverless."""
from __future__ import unicode_literals, print_function
import os
import json

from .swagger import SwaggerGenerator
import ruamel.yaml as yaml


SWAGGER_FILE = 'swagger.yaml'
CONFIG_BASENAME = 'gcdt'


def load_app(project_dir):
    app_py = os.path.join(project_dir, 'app.py')
    with open(app_py) as f:
        g = {}
        contents = f.read()
        exec contents in g
        return g['app']


def scaffold(answers):
    envs = answers.pop('envs')
    app = load_app('./')
    app_name = app.app_name
    if answers['api_gateway']:
        sg = SwaggerGenerator('eu-west-1', '%sUri' % app_name)
        with open(SWAGGER_FILE, 'w') as sfile:
            sfile.write(yaml.dump(sg.generate_swagger(app),
                                  Dumper=yaml.RoundTripDumper))
    for env in envs:
        with open('%s_%s.json' % (CONFIG_BASENAME, env), 'w') as jfile:
            json.dump(generate_config(env=env, app_name=app_name, **answers),
                      jfile, indent=4, sort_keys=True)


def generate_config(**kwargs):
    account = kwargs['account']
    env = kwargs['env']
    region = kwargs['region']
    app_name = kwargs['app_name']

    config = {
        "ramuda": {
            "lambda": {
                "name": "%s-%s-%s" % (account, env, app_name),
                "description": "Lambda function for %s" % app_name,
                "role": kwargs.get('role', 300),
                "handlerFunction": "app.app",
                "handlerFile": "app.py",
                "timeout": kwargs.get('timeout', 300),
                "memorySize": kwargs.get('memory_size', 128),
                "events": {},
                "vpc": {}
            },
            "bundling": {
                "zip": "bundle.zip",
                "folders": [
                    {
                        "source": "./vendored",
                        "target": "."
                    }
                ]
            }
        }
    }
    
    if kwargs.get('artifact_bucket', False):
        config['ramuda']['deployment'] = {
            "region": region,
            "artifactBucket": kwargs.get('artifact_bucket', '')
        }
    
    if kwargs.get('api_gateway', False):
        config['yugen'] = {
            "api": {
                "name": "%s-%s-%s-api" % (account, env, app_name),
                "description": "API Gateway for %s" % app_name,
                "targetStage": env,
                "apiKey": kwargs.get('api_key', '')
            },
            "lambda": {
                "entries": [
                    {
                        "name": "%s-%s-%s" % (account, env, app_name),
                        "swaggerRef": "%sUri" % app_name,
                        "alias": "ACTIVE"
                    }
                ]
            }
        }
    return config
