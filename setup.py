from distutils.core import setup
from setuptools import find_packages

setup(
    name='morphrater',
    version='0.1',
    description="Quick image classifier for morphology classification",
    long_description=open('README.md', encoding="utf-8").read(),
    author="Colin Jacobs",
    author_email="colin@coljac.net",
    url="https://github.com/coljac/morphrater",
    data_files=[('morphrater', ['icon.png'])],
    include_package_data=True,
    scripts=['bin/morphrater'],
    packages=['morphrater'],
    license='MIT License')
