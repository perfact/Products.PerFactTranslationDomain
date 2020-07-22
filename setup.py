from setuptools import setup, find_packages

version = '2.1.dev0'

setup(
    name='Products.PerFactTranslationDomain',
    version=version,
    description="",
    long_description="""\
    """,
    # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Zope",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v2 or later"
        " (GPLv2+)",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: Implementation :: CPython",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
    ],
    keywords='',
    author='perfact',
    author_email='',
    url='',
    license='',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    package_data={
    },
    include_package_data=True,
    zip_safe=False,
    namespace_packages=['Products'],
    install_requires=[
        'zope.component',
        'zope.interface',
        'zope.i18n',
    ],
    entry_points="""
# -*- Entry points: -*-
    """,
)
