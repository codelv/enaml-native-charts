"""
Copyright (c) 2017, Jairus Martin.

Distributed under the terms of the MIT License.

The full license is in the file COPYING.txt, distributed with this software.

Created on Oct 30, 2017

@author: jrm
"""
import os
import fnmatch
from setuptools import setup


def find_data_files(dest, *folders):
    matches = {}
    #: Want to install outside the venv volder in the packages folder
    dest = os.path.join('packages', dest)

    excluded_types = ['.pyc', '.enamlc', '*.apk', '*.iml']
    excluded_dirs = ['android/build']
    for folder in folders:
        for dirpath, dirnames, files in os.walk(folder):
            #: Skip build folders and exclude hidden dirs
            if ([d for d in dirpath.split("/") if d.startswith(".")] or
                    [pattern for pattern in excluded_dirs if fnmatch.fnmatch(dirpath,pattern)]):
                continue
            k = os.path.join(dest,dirpath)
            if k not in matches:
                matches[k] = []
            for f in fnmatch.filter(files, '*'):
                if [p for p in excluded_types if f.endswith(p)]:
                    continue
                m = os.path.join(dirpath, f)
                matches[k].append(m)
    return matches.items()


setup(
    name="enaml-native-charts",
    version="1.0.3",
    author="jrm",
    author_email="",
    license='MIT',
    url="",
    description="enaml-native-charts package for enaml-native-cli",
    long_description=open("README.md").read(),
    py_modules=['enamlnative_charts'],
    data_files=find_data_files("enaml-native-charts", 'android', 'ios', 'src'),
    install_requires=['enaml-native>=3.0.0'],
    entry_points={
        'p4a_recipe': [
            'enaml_native_charts = enamlnative_charts:get_recipe'
        ]
    },
)
