from setuptools import setup, find_packages
setup(name='isilib',
    version='0.01',
    author="Reid McIlroy-Young",
    url="https://github.com/mclevey/web_of_science_isi",
    keywords= 'isi wos',
    install_requires= ['networkx'],
    packages=['isilib'],
    #scripts=['bin/isilib-test'],
    test_suite='tests',
)
