"""
Django(mini)
====================

**Django(mini)** - Infrastructure for rapid development on Django.


Quick start
-------------

Read `Quick Start <https://github.com/djangomini/djangomini>`_ on GitHub.


Don't forget to star project on
`github.com <https://github.com/djangomini/djangomini>`_
to tell us that you like it.
"""

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


version = '1.0.0b2'


setup(
    name='djangomini',
    version=version,
    url='https://github.com/djangomini/djangomini',
    license='MIT',
    author='Anton Danilchenko',
    author_email='anton@danilchenko.me',
    description='Django(mini) - Infrastructure for rapid development on Django.',
    keywords='django web framework',
    long_description=__doc__,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    packages=[
        'djangomini',
        # in future:
        # 'djangomini.controllers',
        # 'djangomini.models',
        # 'djangomini.views'
    ],
    install_requires=['django'],
    include_package_data=True,
    zip_safe=False,
    platforms='any'
)
