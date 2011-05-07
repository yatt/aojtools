from setuptools import setup
import glob

desc = 'aojtools is a toolset written in Python for aoj, aizu online judge system(http://rose.u-aizu.ac.jp/onlinejudge/) , including transparently API acccess, problem submit library and CLI script.'
ldesc = desc

setup(
    name='aojtools'
    , version='0.1.4'
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
    , scripts=glob.glob('scripts/*')
    , license='MIT'
)

