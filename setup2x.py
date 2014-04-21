# See the reasoning of presence of this file in the project at
# http://stackoverflow.com/a/15331209/458106

import os
from setuptools import setup, find_packages


here = lambda path: os.path.join(os.path.abspath(os.path.dirname(__file__)), path)

with open(here('requirements.txt')) as f:
    rows = f.read().strip().split('\n')
    requires = []
    for row in rows:
        row = row.strip()
        if row and not (row.startswith('#') or row.startswith('http')):
            requires.append(row)

requires.extend([
    'Babel==1.3',
    'lingua==1.5',
    'Mako==0.9.0',
    'Plim>=0.8.9'
])

entry_points = """
[paste.app_factory]
main = pacific:main
[console_scripts]

[babel.extractors]
plim = plim.adapters.babelplugin:extract
"""

setup(name='Pacific',
      version='0.0.2',
      packages=find_packages(),
      install_requires=requires,
      entry_points=entry_points,
      message_extractors = {'pacific': [
          ('**.py', 'lingua_python', None),
          ('**.pt', 'lingua_xml', None),
          ('**.plim', 'plim', None),
          ('**.mako', 'mako', None),
          ('static/**', 'ignore', None)
      ]},
      )
