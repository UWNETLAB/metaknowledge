from setuptools import setup
setup(name='isilib',
    version='0.2.0',
    author="Reid McIlroy-Young",
    url="https://github.com/networks-lab/isilib",
    keywords= 'isi wos testing',
    install_requires= ['networkx'],
    #extras_require={'visualizer' : ['matplotlib']},
    packages=['isilib'],
    scripts=['isilib/bin/isilib-test', 'isilib/bin/isilib-coauthmaker', 'isilib/bin/isilib-cocitemaker', 'isilib/bin/isilib-makeListofcitations', 'isilib/bin/isilib-citemaker', 'isilib/bin/isilib-collectRecords', 'isilib/bin/isilib-cociteAuthsMaker', 'isilib/bin/isilib-CLI'],
    test_suite='isilib.tests',
    #data_files= [('/tests', ["testFile.isi", "OnePaper.isi", "ManyAuthors.isi"])]
)
