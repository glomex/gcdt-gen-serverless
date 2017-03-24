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
    ]

    answers = prompt(questions, style=style)
    return answers


def configuring(answers):
    answers['envs'] = answers['envs'].replace(' ', '').split(',')


def writing(answers):
    scaffold(answers)