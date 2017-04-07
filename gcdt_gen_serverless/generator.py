# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals
from scaffold import scaffold
from whaaaaat import style_from_dict, Token


DOC = """\
Speed up your serverless AWS Lambda development by using gcdt scaffolds!

Usage:
  gcdt generate serverless [options]

Options:
  --help          # Print this info and generator's options and usage
  --version       # Print version
  -f, --force     # Overwrite files that already exist
  --no-color      # Disable colors
  --generators	  # Print available generators
  --verbose       # Talk till death
"""


style = style_from_dict({
    Token.Separator: '#6C6C6C',
    Token.QuestionMark: '#FF9D00 bold',
    Token.Selected: '#5F819D',
    Token.Pointer: '#FF9D00 bold',
    Token.Instruction: '',
    Token.Answer: '#5F819D bold',
    Token.Question: '',
})


def initializing():
    pass


def prompting(prompt):
    """AWS serverless generator prompting phase"""
    questions = [
        {
            'type': 'input',
            'name': 'account',
            'message': 'Which account do you want to use?',
            'default': 'infra',
            'store': True
        },
        {
            'type': 'input',
            'name': 'envs',
            'message': 'Environments [dev, stage, prod]?',
            'store': True
        },
        {
            'type': 'input',
            'name': 'region',
            'message': 'AWS region you want to deploy to.',
            'store': True,
            'default': 'eu-west-1'
        },
        {
            'type': 'input',
            'name': 'role',
            'message': 'AWS Lambda role you want to assign.',
            'store': True
        },
        {
            'type': 'confirm',
            'name': 'use_artifact_bucket',
            'message': 'Do you want to use an s3 bucket for AWS Lambda deployment?',
            'store': True,
            'default': False
        },
        {
            'type': 'input',
            'name': 'artifact_bucket',
            'message': 'S3 bucket used for AWS Lambda deployment.',
            'store': False,
            'when': lambda answers: answers['use_artifact_bucket']
        },
        {
            'type': 'input',
            'name': 'timeout',
            'message': 'The function execution time(s) at which Lambda should terminate the function',
            'store': True,
            'default': '300',
        },
        {
            'type': 'input',
            'name': 'memory_size',
            'message': 'The amount of memory(MB) for the function (must be multiple of 64).',
            'store': True,
            'default': '128'
        },
        {
            'type': 'confirm',
            'name': 'api_gateway',
            'message': 'Do you want scaffolding for API Gateway?',
            'store': True,
            'default': True
        },
        {
            'type': 'input',
            'name': 'api_key',
            'message': 'API Gateway API key.',
            'store': False,
            'when': lambda answers: answers['api_gateway']
        },
    ]

    answers = prompt(questions, style=style)
    return answers


def configuring(answers):
    answers['envs'] = answers['envs'].replace(' ', '').split(',')


def writing(answers):
    scaffold(answers)