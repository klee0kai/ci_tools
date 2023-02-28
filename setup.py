from os.path import join, dirname
from setuptools import setup, find_packages

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(name='screwdriver',
      version='0.01',
      url='https://github.com/klee0kai/screwdriver',
      license='GNU, v3',
      author='Klee0kai',
      author_email='klee0kai@gmail.com',
      description='Collections for CI deploy utils.',
      packages=find_packages(exclude=['tests']),
      long_description=open(join(dirname(__file__), 'readme.md')).read(),
      install_requires=required,
      zip_safe=False)
