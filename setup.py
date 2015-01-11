import os
from setuptools import setup, find_packages

f = open(os.path.join(os.path.dirname(__file__), 'README.md'))
readme = f.read()
f.close()

test_requires = []

name='ENML2HTML'

setup(
    name=name,
    version='0.0.1',
    description='This is a python library for converting ENML (Evernote Markup Language, http://dev.evernote.com/start/core/enml.php) to/from HTML.',
    long_description=readme,
    author='Carl Lee',
    author_email='ljbha007@gmail.com',
    url='https://github.com/CarlLee/ENML_PY/tree/master',
    packages=find_packages(),
    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
    test_suite='test',
)
