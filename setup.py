from setuptools import setup, find_packages
from codecs import open
import os
from gcdt_gen_serverless import __version__

here = os.path.abspath(os.path.dirname(__file__))
version = __version__


# Get the long description from the README file
with open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# get the dependencies and installs
with open(os.path.join(here, 'requirements.txt'), encoding='utf-8') as f:
    all_reqs = f.read().split('\n')


install_requires = [x.strip() for x in all_reqs if ('git+' not in x) and
                    (not x.startswith('#')) and (not x.startswith('-'))]
dependency_links = [x.strip().replace('git+', '') for x in all_reqs if 'git+' not in x]

setup(
    name='gcdt-gen-serverless',
    version='0.0.8',
    description='Serverless generator for gcdt',
    long_description=long_description,
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 2.7',
    ],
    keywords='',
    packages=find_packages(exclude=['docs', 'tests*']),
    include_package_data=True,
    author='glomex OPS Team',
    install_requires=install_requires,
    dependency_links=dependency_links,
    author_email='mark.fink@glomex.com',
    entry_points={
        'gcdtgen10': [
            'serverless=gcdt_gen_serverless.generator',
        ],
    }
)
