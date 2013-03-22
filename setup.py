# -*- coding: utf-8 -*-
import os
from setuptools import setup, find_packages
from version import get_version

version = get_version()

setup(name='gs.group.messages.ratelimit',
    version=version,
    description="Limit the rate of message posting in a GroupServer group",
    long_description=open("README.txt").read() + "\n" +
                      open(os.path.join("docs", "HISTORY.txt")).read(),
    classifiers=[
      "Development Status :: 4 - Beta",
      "Environment :: Web Environment",
      "Framework :: Zope2",
      "Intended Audience :: Developers",
      "License :: Other/Proprietary License",
      "Natural Language :: English",
      "Operating System :: POSIX :: Linux"
      "Programming Language :: Python",
      "Topic :: Software Development :: Libraries :: Python Modules",
      ],
    keywords='groupserver message rate limit',
    author='Richard Waid',
    author_email='richard@onlinegroups.net',
    url='http://groupserver.org/',
    license='other',
    packages=find_packages(exclude=['ez_setup']),
    namespace_packages=['gs', 'gs.group', 'gs.group.messages'],
    include_package_data=True,
    zip_safe=True,
    install_requires=[
        'setuptools',
        'zope.cachedescriptors',
        'zope.component',
        'zope.formlib',
        'zope.interface',
        'zope.schema',
        'Zope2',
        'gs.content.form',
        'gs.group.base',
        'gs.group.properties',
        'gs.group.messages.viewlet',
        'gs.help',
    ],
    entry_points="""
    # -*- Entry points: -*-
    """,)
