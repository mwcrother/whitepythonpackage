from setuptools import setup

setup(name='White Python Package',
      version='0.1',
      description='Read a matrix and run BLAST searches',
      url='TBD',
      author='Mary White',
      author_email='mwhite@selu.edu',
      license='MIT',
      packages=['white_pythonpackage'],
      install_requires=[
          'biopython',
          'dendropy',
          'pandas'
      ],
      long_description=open('README.txt').read(),
zip_safe=True)