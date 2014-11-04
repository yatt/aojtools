from setuptools import setup
import glob

desc  = "api client library and scripts for aizu online judge system."
ldesc = """aojtools is a toolset written in Python for aoj, aizu online judge system(http://judge.u-aizu.ac.jp/onlinejudge/) , including transparently API acccess, problem submit library and CLI script.
"""

setup(
    name='aojtools'
    , version='0.2.4'
    , description=desc
    , long_description=ldesc
    , classifiers = [
        'Programming Language :: Python'
        , 'Topic :: Internet :: WWW/HTTP'
        , 'Topic :: Software Development :: Libraries :: Python Modules'
    ]
    , author='yatt'
    , keywords=['competitive programming']
    , author_email='darknesssharp@gmail.com'
    , packages=['aojtools']
    , scripts=[
        'scripts/aojcategories',
        'scripts/aojprepare',
        'scripts/aojrun',
        'scripts/aojsolvedlist',
        'scripts/aojsubmit',
    ]
    , license='MIT'
    , url='https://github.com/yatt/aojtools'
)
