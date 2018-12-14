import os
import re

from setuptools import setup

with open('requirements/base.txt') as f:
    install_requires = [line for line in f if line and not line.startswith('-')]


def get_version(package):
    """
    Return package version as listed in `__version__` in `init.py`.
    """
    with open(os.path.join(package, '__init__.py'), 'rb') as init_py:
        src = init_py.read().decode('utf-8')
        return re.search("__version__ = ['\"]([^'\"]+)['\"]", src).group(1)


setup(
    name='ridi-django-jwt',
    packages=[
        'ridi.django_jwt',
    ],
    version=get_version('ridi/django_jwt'),
    description='JSON Web Token based authentication for RIDI\'s django services',
    url='https://github.com/ridi/django-jwt',
    keywords=['jwt', 'django', 'ridi', 'ridibooks'],
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
    ],
    install_requires=install_requires,
    entry_points={
        'console_scripts': [
            'secret-keeper = ridi.secret_keeper.cmdline:main'
        ]
    },
)
