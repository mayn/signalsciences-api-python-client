from distutils.core import setup
from setuptools import find_packages

setup(
    name='signalsciences-api-python-client',
    version='0.0.1.dev0',
    author='Matthew Aynalem',
    author_email='maynalem@gmail.com',
    packages=find_packages('signalsciencesapiclient'),
    package_dir={'': 'signalsciencesapiclient'},
    url='https://github.com/mayn/signalsciences-api-python-client',
    license='MIT',
    description='signalsciences-api-python-client - a python client for the signalsciences API',
    long_description=open('README.rst').read(),
    install_requires=[
    ],
)
