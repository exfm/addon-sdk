#!/usr/bin/env python
import os
def _include_dir(source):
    paths={}

    pathnames = os.listdir(source)
    for pathname in pathnames:
        full_path = os.path.join(source, pathname)
        if os.path.isdir(full_path):
            for k, v in _include_dir(full_path).iteritems():
                if paths.has_key(k):
                    paths[k].extend(v)
                else:
                    paths[k] = v

        elif os.path.isfile(full_path):
            d = os.path.dirname(full_path)
            if not paths.has_key(d):
                paths[d] = []
            paths[d].append(full_path)

    return paths

data_files = []
data_files.extend([(_dir, _files)for _dir, _files in _include_dir('packages').iteritems()])
data_files.extend([(_dir.replace('python-lib/', ''), _files)for _dir, _files in _include_dir('python-lib/cuddlefish').iteritems()])


from setuptools import setup
setup(
    name='addon-sdk',
    version='1.0',
    url='http://ex.fm/',
    license='BSD',
    author='Lucas Hrabovsky',
    author_email='lucas@ex.fm',
    description='Tools for Chrome Extensions',
    zip_safe=False,
    install_requires=[
        'mozrunner',
        'simplejson',
        'markdown'
    ],
    packages=['cuddlefish'],
    package_dir = {'': 'python-lib'},
    data_files=data_files,
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License'
    ],
    entry_points = {
        'console_scripts': [
            'cfx = cuddlefish:run'
        ],
    }
)