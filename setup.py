from setuptools import setup, find_packages
import os

version = '1.1.3'

setup(name='medialog.controlpanel',
      version=version,
      description="A pluggable control panel.",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='',
      author='Espen Moe-Nilssen',
      author_email='espen@medialog.no',
      url='https://github.com/espenmn/medialog.controlpanel',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['medialog'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
           'plone.app.registry',
           'plone.directives.form',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      setup_requires=[
      
      ],
      )
