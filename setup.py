from metaknowledge.journalAbbreviations import abrevDBname

from setuptools import setup, find_packages
setup(name='metaknowledge',
    version='0.2.0',
    author="Reid McIlroy-Young",
    author_email = "rmcilroy@uwaterloo.ca",
    url="https://github.com/networks-lab/metaknowledge",
    keywords= 'isi wos testing',
    install_requires= ['networkx'],
    #extras_require={'visualizer' : ['matplotlib']},
    packages=find_packages(),#['metaknowledge', 'metaknowledge.journalAbbreviations'],
    scripts=['metaknowledge/bin/metaknowledge-CLI'],
    test_suite='metaknowledge.tests',
    include_package_data = True,
    package_data = {'': [abrevDBname + '.*']}
    #data_files= [('/tests', ["testFile.isi", "OnePaper.isi", "ManyAuthors.isi"])]
)
