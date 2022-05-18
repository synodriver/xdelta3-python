from importlib.machinery import SourceFileLoader
from pathlib import Path
from setuptools import setup, Extension

THIS_DIR = Path(__file__).resolve().parent
long_description = THIS_DIR.joinpath('README.rst').read_text()

# avoid loading the package before requirements are installed:
version = SourceFileLoader('version', 'xdelta3/version.py').load_module()

package = THIS_DIR.joinpath('xdelta3')
package_data = ['_xdelta3.c']
if package.joinpath('lib').exists():
    package_data += [f'lib/{f.name}' for f in package.joinpath('lib').iterdir()]

setup(
    name='xdelta3',
    version=str(version.VERSION),
    description='Fast delta encoding using xdelta3',
    long_description=long_description,
    author='Samuel Colvin',
    author_email='s@muelcolvin.com',
    url='https://github.com/samuelcolvin/xdelta3-python',
    license='Apache License, Version 2.0',
    packages=['xdelta3'],
    package_data={
        'xdelta3': package_data
    },
    zip_safe=True,
    ext_modules=[
        Extension(
            '_xdelta3',
            sources=['xdelta3/_xdelta3.c'],
            include_dirs=['./xdelta/xdelta3'],
            # use with SECONDARY_LZMA to enabled secondary compression with lzma
            # libraries=['lzma'],
            define_macros=[
                ('SIZEOF_SIZE_T', '8'),
                ('SIZEOF_UNSIGNED_LONG_LONG', '8'),
                ('XD3_USE_LARGEFILE64', '1'),
                # ('SECONDARY_LZMA', '1'),
                # adds verbose debug output to xdelta3
                # ('XD3_DEBUG', '3'),
            ]
        )
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: Unix',
        'Operating System :: POSIX :: Linux',
        'Topic :: System :: Archiving :: Compression',
    ],
)
