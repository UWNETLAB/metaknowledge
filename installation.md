---
layout: page
title: Installation
---

The [download](https://github.com/mclevey/web_of_science_isi) from Github includes a customized [Vagrant](https://www.vagrantup.com) file that installs [isilib](https://github.com/mclevey/web_of_science_isi) and other useful Python libraries into a virtual machine. It is currently the easiest way of getting isilib working if you are not already using Python. Alternatively you can run `setup.py install` to install locally

Please note that isilib is under active development and these instructions may be out of date.

## Install with Vagrant
The vagrant method is intended for students and those not familiar with python it creates a virtual machine with isilib installed. It also contains the python scientific stack numpy, scipy and matplotlib as well a series of iPython notebooks for teaching people to use isilib and python.

Once vagrant and a hypervisor([virtualBox](https://www.virtualbox.org/) is the default) are installed, download isilib, click [here](https://github.com/mclevey/web_of_science_isi/archive/master.zip) to download it as a zip file. Go to the vagrant subdirectory and run `vagrant up` or if you are using OS X double click the file mac_run. This will initialize the virtual machine and install all the required software on it.

Now the virtual machine is hosting a iPython notebook on port 8888 you can access it by going to [http://localhost:8888/](http://localhost:8888/) or if you used mac_run a window will appear at it. You can also use `vagrant ssh` to access the virtual machine.

## Install without Vagrant

Installing without Vagrant is done with [setuptools](https://pypi.python.org/pypi/setuptools). Go to the isilib directory and run `python3 setup.py install`
