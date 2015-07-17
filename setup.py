from setuptools import setup
setup(name='isilib',
    version='0.1.0',
    author="Reid McIlroy-Young",
    url="https://github.com/mclevey/web_of_science_isi",
    keywords= 'isi wos',
    install_requires= ['networkx'],
    packages=['isilib'],
    scripts=['isilib/bin/isilib-test', 'isilib/bin/isilib-coauthmaker', 'isilib/bin/isilib-cocitemaker', 'isilib/bin/isilib-makeListofcitations', 'isilib/bin/isilib-citemaker', 'isilib/bin/isilib-collectRecords', 'isilib/bin/isilib-cociteAuthsMaker', 'isilib/bin/isilib-CLI'],
    test_suite='isilib.tests',
    #data_files= [('/tests', ["testFile.isi", "OnePaper.isi", "ManyAuthors.isi"])]
)
