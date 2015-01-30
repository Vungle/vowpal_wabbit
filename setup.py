#!/usr/bin/env python

import os
from setuptools import setup, Extension
from setuptools.command.install import install
from setuptools.command.build_ext import build_ext
from distutils.command.build import build
from subprocess import call
from multiprocessing import cpu_count

BASEPATH = os.path.dirname(os.path.abspath(__file__))


class build_pyvw(build_ext):
    def run(self):
        cmd = [
            'make',
            'python'
        ]

        call(cmd, cwd=BASEPATH)
        self.copy_file('python/pylibvw.so', self.get_ext_fullpath("pylibvw"))


setup(
    name='pyvw',
    version='0.0.1',
    description='Python bindings for VW',
    maintainer='Vladimir Magdin',
    ext_modules = [Extension('pylibvw', sources=[])],
    py_modules = ['python/pyvw'],
    cmdclass={
        'build_ext': build_pyvw
    }
)
