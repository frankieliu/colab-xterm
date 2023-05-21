from distutils.core import setup
import os

exec(open("colabxterm/_version.py").read())
setup(
        name='colabxterm',
        version=__version__,
        packages=['colabxterm']
        )
