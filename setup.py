from distutils.core import setup

setup(
    name='PylintPlugin',
    version='0.1.0',
    description='A plugin make Pylint more Django-Friendly',
    author='akun',
    license='WTFPL',
    package_dir={'PylintPlugin': 'src'},
    packages=['PylintPlugin'],
)
