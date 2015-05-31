from setuptools import setup
setup(name='isilib',
    version='0.2',
    author="Reid McIlroy-Young",
    url="https://github.com/mclevey/web_of_science_isi",
    keywords= 'isi wos',
    install_requires= ['networkx'],
    packages=['isilib'],
    scripts=['bin/isilib-test', 'bin/isilib-coauthmaker', 'bin/isilib-cocitemaker', 'bin/isilib-makeListofcitations', 'bin/isilib-citemaker', 'bin/isilib-collectRecords', 'bin/isilib-cociteAuthsMaker'],
    test_suite='tests',
    #data_files= [('/tests', ["testFile.isi", "OnePaper.isi", "ManyAuthors.isi"])]
)
