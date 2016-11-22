import os
import sys

try:
    from setuptools import setup
except:
    from distutils.core import setup

readme_note = '''\
.. note::

   For the latest source, issues and discussion, etc, please visit the
   `GitHub repository <https://github.com/samuell/scipype>`_\n\n
'''

with open('README.md') as fobj:
    long_description = readme_note + fobj.read()

setup(
    name='scipype',
    version='0.0.1a1',
    description='Pure python workflow library',
    long_description=long_description,
    author='Samuel Lampa',
    author_email='samuel.lampa@farmbio.uu.se',
    url='https://github.com/samuell/scipype',
    license='MIT',
    keywords='workflows workflow pipeline',
    packages=[
        'scipype',
    ],
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Console',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
        'Topic :: Scientific/Engineering :: Chemistry',
    ],
)
