from setuptools import setup, find_packages

setup(
    name='attune-log-audit-tool',
    version='0.0.0.1',
    packages=find_packages(),
    install_requires=[
      'click',
    ],
    entry_points='''
      [console_scripts]
      iqs-logs=iqs_logs.logtool:cli
    ''',
)