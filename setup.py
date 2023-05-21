from distutils.core import setup
import os

# exec(open("colabxterm/_version.py").read())
setup(
        name='colabxterm',
        packages=['colabxterm'],
        version="0.0.0",
        package_data={
            'colabxterm': ['client/dist/*','VERSION']
        },
        include_package_data=False,
        install_requires=['ptyprocess~=0.7.0', 'tornado>5.1'],
        extras_require={
            'dev': [
                'jupyter',
                'twine'
            ],

        }
        )
