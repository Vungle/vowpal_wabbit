#!/usr/bin/env python

import os
from setuptools import setup
from setuptools.command.install import install
from distutils.command.build import build
from subprocess import call
from multiprocessing import cpu_count

BASEPATH = os.path.dirname(os.path.abspath(__file__))


class build_pyvw(build):
    def run(self):
        # run original build code
        build.run(self)

        build_path = os.path.abspath(self.build_temp)

        cmd = [
            'make',
            'python'
        ]

        def compile():
            print '*' * 80
            call(cmd, cwd=BASEPATH)
            print '*' * 80

        self.execute(compile, [], 'compiling pyvw')

        # copy resulting tool to library build folder
        self.mkpath(self.build_lib)

        if not self.dry_run:
            for target in ['python/pylibvw.so', 'python/pyvw.py']:
                self.copy_file(target, self.build_lib)


class install_pyvw(install):
    def run(self):
        # run original install code
        install.run(self)

        # install XCSoar executables
        print 'running install_pyvw'
        self.copy_tree(self.build_lib, self.install_lib)


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name='pyvw',
    version='0.4.1',
    description='Python bindings for VW',
    maintainer='Vladimir Magdin',

    cmdclass={
        'build': build_pyvw,
        'install': install_pyvw,
    }
)
