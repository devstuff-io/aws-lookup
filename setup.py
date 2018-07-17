import ast
import os
import re
from setuptools import setup


# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

BASEDIR = os.path.dirname(os.path.abspath(__file__))
VERSION = None
REQUIREMENTS = []
DEPENDENCY_LINKS = []
DESCRIPTION = 'A utility that can be used from the command line or plugged into python projects that provides a simple search functionality for AWS objects.'

with open(os.path.join(BASEDIR, 'requirements.txt')) as fp:
    lines = fp.readlines()
    for line in lines:
        line = line.strip()
        if ("http://" in line or "https://" in line or "ssh://" in line) and "#egg=" in line:
            parts = line.split("#egg=")
            REQUIREMENTS.append(parts[-1])
            DEPENDENCY_LINKS.append(line)
        elif len(line) and line[0] != "#" and line[0] != "-":
            REQUIREMENTS.append(line)


_version_re = re.compile(r'__version__\s+=\s+(.*)')
with open('aws_lookup/__init__.py', 'rb') as f:
    VERSION = str(ast.literal_eval(
        _version_re.search(f.read().decode('utf-8')).group(1)
    ))


setup(
    name='aws-lookup',
    version=VERSION,
    license='MIT',
    packages=['aws_lookup'],
    include_package_data=True,
    description=DESCRIPTION,
    long_description=DESCRIPTION,
    url='https://github.com/meganlkm/aws-lookup',
    author='meganlkm',
    author_email='devstuff.io@gmail.com',
    install_requires=REQUIREMENTS,
    dependency_links=DEPENDENCY_LINKS,
    keywords=[
        'aws',
        'lookup'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Topic :: System :: Software Distribution',
        'Topic :: Utilities'
    ]
)
