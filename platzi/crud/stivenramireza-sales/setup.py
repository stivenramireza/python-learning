from importlib.metadata import entry_points
from setuptools import setup

setup(
    name='ss',
    version='0.1',
    py_modules=['ss'],
    install_requires=['Click'],
    entry_points='''
        [console_scripts]
        ss=ss:cli
    ''',
)
