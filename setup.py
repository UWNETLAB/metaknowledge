#Written by Reid McIlroy-Young for Dr. John McLevey, University of Waterloo 2015
import os.path
import re
from setuptools import setup, find_packages

with open('metaknowledge/constants.py') as f:
    versionString = re.search(r"__version__ = '(.+)'", f.read()).group(1)

long_descriptionLOC = "README.md"
if os.path.isfile(long_descriptionLOC):
    long_description = open(long_descriptionLOC).read()
else:
    long_description = ''

if __name__ == '__main__':

    setup(name='metaknowledge',
        version = versionString,
        description = "A library for handling Web of science files",
        long_description = long_description,
        long_description_content_type = 'text/markdown',
        author="Reid McIlroy-Young, John McLevey",
        author_email = "rmcilroy@uwaterloo.ca, john.mclevey@uwaterloo.ca",
        license = 'GPL',
        url="https://github.com/networks-lab/metaknowledge",
        download_url = "https://github.com/networks-lab/metaknowledge/archive/{}.tar.gz".format(versionString),
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
        packages = find_packages(),
        entry_points={'console_scripts': [
                  'metaknowledge = metaknowledge.bin:mkCLI',
                  'metaknowledge-mdToNb = metaknowledge.bin:mkMdToNb',
                  'metaknowledge-DocsGen = metaknowledge.bin:mkDocs',
              ]},
        test_suite='metaknowledge.tests',
    )
    print("metaknowledge installed\nIf you intend to use the gender name data or journal abbreviations facilities it is\nadvisable to download and setup the required files now.\nRunning following line in your interpreter will do it:\nimport metaknowledge;metaknowledge.downloadExtras()")
