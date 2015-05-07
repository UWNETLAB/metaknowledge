from setuptools import setup, find_packages
setup(name='isilib',
    version='0.0.1',
    author="Reid McIlroy-Young",
    url="https://github.com/mclevey/web_of_science_isi",
    keywords= 'isi wos',
    install_requires= ['networkx'],
    packages=['isilib'],
    scripts=['bin/isilib-test', 'bin/isilib-coauthmaker', 'bin/isilib-cocitemaker'],
    test_suite='tests',
    #data_files= [('/tests', ["testFile.isi", "OnePaper.isi", "ManyAuthors.isi"])]
)
