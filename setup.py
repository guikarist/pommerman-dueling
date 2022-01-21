from setuptools import setup

setup(name='pommerman_dueling',
      version='0.0.1',
      install_requires=[
          'gym',
          'pommerman @ git+https://github.com/MultiAgentLearning/playground.git@master#egg=pommerman'
      ]
      )
