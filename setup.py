from distutils.core import setup
import os

def _get_version():
    version_file = os.path.normpath(os.path.join(os.path.dirname(__file__), 'colabxterm', 'VERSION'))
    with open(version_file) as fh:
        version = fh.read().strip()
        return version

setup(
        name='colabxterm',
        # version=_get_version(),
        packages=['colabxterm']
        )
