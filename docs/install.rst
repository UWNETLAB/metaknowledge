###############
Installation
###############

**Note:** For a more recent guide to getting started, please visit `the NetLab blog <https://uwaterloo.ca/networks-lab/blog/post/getting-started-metaknowledge>`_.

*metaknowledge* has two distributions. The simplest is found under the release branch of the `git repo <https://github.com/networks-lab/metaknowledge/tree/release>`_, which can be installed the usual way with pip: ::

  pip3 install metaknowledge

The second version is at the master branch on |Github|_. It comes with extra documents and resources for teaching.

The |download|_ from *Github* includes a customized |VG|_ file that installs *metaknowledge* and other useful *Python* libraries into a virtual machine. It is the easiest way of getting *metaknowledge* working if you are not familiar with *Python*.

Install with Vagrant
^^^^^^^^^^^^^^^^^^^^
The *Vagrant* method is intended for students and anyone not familiar with *Python*. It creates a `virtual machine <https://en.wikipedia.org/wiki/Virtual_machine>`_ with *metaknowledge* installed, as well as the *Python* scientific stack *numpy*, *scipy*, and *matplotlib*, as well as a series of iPython notebooks for teaching *metaknowledge* and *Python*. Some notebooks are more complete than others.

The instructions for those familiar with the command line use the advanced instructions. Otherwise, it is probably best to use the student install.

Student Install
^^^^^^^^^^^^^^^
First, you need to install |VagrantDownload|_ and |VirtualBox|_. You need to do this before you can install *metaknowledge*.

Once *Vagrant* and *VirtualBox* are installed, download |mk_download|_. Unzip the file. If you are unable to unzip the file, download |7zip|_.

Open the directory *metaknowledge* and go to the vagrant subdirectory. Depending on your operating system, double click either: :code:`win_run`, :code:`mac_run`, or :code:`linux_run`.

A window should pop up and say something like: ::

  Bringing machine 'default' up with 'virtualbox' provider...
  ==> default: Box 'ubuntu/trusty64' could not be found. Attempting to find and install...
  default: Box Provider: virtualbox
  default: Box Version: >= 0

You will also see an estimate of how long the download and installation process will take (typically 20 minutes). All you have to do it wait for it to finish. When it is done, a browser window will appear at the showing the notebooks. If a browser window opens and it is showing :code:`No data received`, hit refresh a couple times.

When you see a page with the following, you have installed everything successfully: ::

  Lesson-1-Getting-Started
  Lesson-2-Reading-Files
  Lesson-3-Objects
  ...

To open the page again, just double click on which ever of :code:`win_run`, :code:`mac_run`, or :code:`linux_run` you used. It should take less than a minute the second time.

Advanced Instructions
^^^^^^^^^^^^^^^^^^^^^

1. Install `Vagrant <https://www.vagrantup.com/downloads.html>`_ and `VirtualBox <https://www.virtualbox.org/wiki/Downloads>`_.
2. Clone the `git repo <https://github.com/networks-lab/metaknowledge.git>`.
3. Make sure you are on the master branch.
4. Go to the vagrant directory.
5. Run :code:`vagrant up`
6. Once vagrant has finished go to http://localhost:1159/

What you are doing by running :code:`vagrant up` is creating an Ubuntu VM and provisioning it with the script :code:`bootstrap`, which is also in the vagrant directory. If you run :code:`vagrant up` again it only starts the VM. To access the VM’s notebook once it is created:

1. Go to the vagrant directory.
2. Run :code:`vagrant up`
3. Once vagrant has finished go to http://localhost:1159/

You can also use :code:`vagrant ssh` to ssh into the VM or :code:`vagrant provision` to rerun bootstrap. If :code:`vagrant ssh` does not work on your machine, you should be able to ssh into it at: ::

  HostName: 127.0.0.1
  Port: 2222
  Username: vagrant
  Password: vagrant

On Windows |Putty|_ has been tested and works well.</p>

Install without Vagrant
^^^^^^^^^^^^^^^^^^^^^^^
Installing without *Vagrant* is done with setuptools_. Go to the metaknowledge directory and run :code:`python3 setup.py install`. This is the same version that is installed via :code:`pip` plus some extra development command line tools.

Extending MK
^^^^^^^^^^^^
Coming soon

Questions?
^^^^^^^^^^
If you find bugs, or have questions, please write to:

| Reid McIlroy-Young `reid@reidmcy.com <mailto:reid@reidmcy.com>`_
| John McLevey `john.mclevey@uwaterloo.ca <mailto:john.mclevey@uwaterloo.ca>`_

License
^^^^^^^
*metaknowledge* is free and open source software, distributed under the GPL License.

.. toctree::
   :maxdepth: 2
   :caption: Installation:

.. _Github: https://github.com/networks-lab/metaknowledge
.. |Github| replace:: *Github*
.. _download: https://github.com/networks-lab/metaknowledge/archive/master.zip
.. |download| replace:: *download*
.. _VG: https://www.vagrantup.com/
.. |VG| replace:: *Vagrant*
.. _VagrantDownload: https://www.vagrantup.com/downloads.html
.. |VagrantDownload| replace:: *Vagrant*
.. _VirtualBox: https://www.virtualbox.org/wiki/Downloads
.. |VirtualBox| replace:: *VirtualBox*
.. _mk_download: https://github.com/networks-lab/metaknowledge/archive/master.zip
.. |mk_download| replace:: *metaknowledge*
.. _7zip: http://www.7-zip.org/
.. |7zip| replace:: *7-zip*
.. _Putty: http://www.chiark.greenend.org.uk/~sgtatham/putty/
.. |Putty| replace:: *PuTTY*
.. _setuptools: https://pypi.python.org/pypi/setuptools
