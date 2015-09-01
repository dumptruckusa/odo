#!/usr/bin/env python

import os
from fnmatch import fnmatch
from setuptools import setup

import versioneer


def find_packages(path):
    for root, _, _ in filter(lambda x: '__init__.py' in x[2], os.walk(path)):
        yield os.path.relpath(root).replace(os.sep, '.')


def find_data_files(where, exts):
    exts = tuple(exts)
    for root, dirs, files in os.walk(where):
        for f in files:
            if any(fnmatch(f, pat) for pat in exts):
                yield os.path.join(root, f)


exts = ('*.h5', '*.csv', '*.xls', '*.xlsx', '*.db', '*.json', '*.gz', '*.hdf5',
        '*.sas7bdat')
package_data = [x.replace('odo' + os.sep, '') for x in
                find_data_files('odo', exts)]


def read(filename):
    with open(filename, 'r') as f:
        return f.read()


packages = list(find_packages(os.path.abspath('odo')))


setup(name='odo',
      version=versioneer.get_version(),
      cmdclass=versioneer.get_cmdclass(),
      description='Data migration utilities',
      url='https://github.com/blaze/odo',
      author='Blaze development team',
      author_email='blaze-dev@continuum.io',
      license='BSD',
      keywords='odo data conversion hdf5 sql blaze',
      packages=packages,
      install_requires=read('requirements.txt').strip().split('\n'),
      long_description=read('README.rst'),
      package_data={'odo': package_data},
      zip_safe=False,
      scripts=[os.path.join('bin', 'odo')])
