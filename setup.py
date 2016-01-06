#Written by Reid McIlroy-Young for Dr. John McLevey, University of Waterloo 2015
import os.path
from setuptools import setup, find_packages

versionNumber = open("versionNum.md").readline().strip()

long_descriptionLOC = "README.rst"
if os.path.isfile(long_descriptionLOC):
    long_description = open(long_descriptionLOC).read()
else:
    long_description = ''

setup(name='metaknowledge',
    version=versionNumber,
    description = "A library for handling Web of science files",
    long_description = long_description,
    author="Reid McIlroy-Young, John McLevey",
    author_email = "rmcilroy@uwaterloo.ca, john.mclevey@uwaterloo.ca",
    license = 'GPL',
    url="https://github.com/networks-lab/metaknowledge",
    download_url = "https://github.com/networks-lab/metaknowledge/archive/.tar.gz".format(versionNumber),
    keywords= 'WOS',
    classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Environment :: Console',
    'Environment :: MacOS X',
    'Intended Audience :: Science/Research',
    'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
    'Operating System :: MacOS :: MacOS X',
    'Operating System :: POSIX',
    'Operating System :: Microsoft :: Windows',
    'Programming Language :: Python :: 3 :: Only',
    'Topic :: Education',
    'Topic :: Scientific/Engineering :: Information Analysis',
    'Topic :: Sociology',
    'Topic :: Text Processing',
    ],
    install_requires= ['networkx'],
    extras_require={'contour' : ['matplotlib', 'scipy', 'numpy']},
    packages=['metaknowledge', 'metaknowledge.journalAbbreviations', 'metaknowledge.visual', 'metaknowledge.tagProcessing'],
    entry_points={'console_scripts': [
              'metaknowledge = metaknowledge.bin:mkCLI',
              'metaknowledge-mdToNb = metaknowledge.bin:mkMdToNb',
              'metaknowledge-DocsGen = metaknowledge.bin:mkDocs',
          ]},
    test_suite='metaknowledge.tests',
    include_package_data = True,
    package_data = {'': ['manualj9Abbreviations.*']}
)

try:
    import metaknowledge.journalAbbreviations
except ImportError:
    print("Setup did not work, metaknowledge cannot be imported")
else:
    try:
        print("journal abbreviations database being downloaded\nPress ctr-C to cancel")
        metaknowledge.journalAbbreviations.updatej9DB()
    except:
        print("journal abbreviations database could not be downloaded. Try again when you have a connection if you wish to use them. The function to updated them is metaknowledge.journalAbbreviations.updatej9DB().")
    else:
        print("journal abbreviations database downloaded")
