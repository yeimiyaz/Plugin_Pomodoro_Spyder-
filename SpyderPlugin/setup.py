# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# Copyright © 2024, Yeimi P
#
# Licensed under the terms of the MIT license
# ----------------------------------------------------------------------------
"""
Spyder Pomodoro Timer setup.
"""
from setuptools import find_packages
from setuptools import setup

from spyder_pomodoro_timer import __version__


setup(
    # See: https://setuptools.readthedocs.io/en/latest/setuptools.html
    name="Spyder Plugin",
    version=__version__,
    author="Yeimi P",
    author_email="yeimiyaz-pomodoro@gmail.com",
    description="Example of plugin",
    license="MIT license",
    url="https://github.com/map0logo/Spyder Plugin",
    python_requires='>= 3.7',
    install_requires=[
        "qtpy",
        "qtawesome",
        "spyder>=5.0.1",
    ],
    packages=find_packages(),
    entry_points={
        "spyder.plugins": [
            "spyder_pomodoro_timer = spyder_pomodoro_timer.spyder.plugin:SpyderPomodoroTimer"
        ],
    },
    classifiers=[
        "Operating System :: MacOS",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Developers",
        "Topic :: Scientific/Engineering",
    ],
)
