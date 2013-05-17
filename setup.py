from setuptools import setup
import glob

desc = """aojtools is a toolset written in Python for aoj, aizu online judge system(http://judge.u-aizu.ac.jp/onlinejudge/) , including transparently API acccess, problem submit library and CLI script.
"""
ldesc = desc

setup(
    name='aojtools'
    , version='0.2'
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
        'scripts/aojsubmit',
        'scripts/aojwhatis',
        'scripts/aojwhois',
        'scripts/diff.py',
        'scripts/aojrun',
        'scripts/aojprepare',
    ]
    , license='MIT'
)
