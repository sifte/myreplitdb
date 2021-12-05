from setuptools import setup

setup(
    name='MyDB',
    author="kaylebetter",
    version='1.0',
    description='The most simplistic and easiest wrapper to use for replit\'s database system.',
    packages=['myreplitdb'],
    include_package_data=True,
    license="MIT",
    keywords="myreplitdb",
    install_requires=[
        'replit',
        'db',
    ],
)