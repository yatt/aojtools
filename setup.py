from setuptools import setup

desc = 'aojtools is a toolset written in Python for aoj, aizu online judge system(http://rose.u-aizu.ac.jp/onlinejudge/) , including transparently API acccess library, problem submit library and CLI script.'
ldesc = desc

setup(
    name='aojtools'
    , version='0.1.0'
    , description=desc
    , long_description=ldesc
    , classifiers = [
        'Programming Language :: Python'
        , 'Topic :: Internet :: WWW/HTTP'
        , 'Topic :: Software Development :: Libraries :: Python Modules'
    ]
    , author='yatt'
    , author_email='darknesssharp@gmail.com'
    , packages=['aojtools']
    , scripts=['scripts']
    , license='MIT'
)

