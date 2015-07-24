---
layout: page
title: Installation
---

The [download](https://github.com/networks-lab/isilib) from Github includes a customized [Vagrant](https://www.vagrantup.com) file that installs [isilib](https://github.com/networks-lab/isilib/archive/master.zip) and other useful Python libraries into a virtual machine. It is currently the easiest way of getting isilib working if you are not already familiar with Python. Alternatively you can run `setup.py install` to install locally

Please note that isilib is under active development and these instructions may be out of date.

## Install with Vagrant
The vagrant method is intended for students and those not familiar with python it creates a virtual machine with isilib installed, also the python scientific stack numpy, scipy and matplotlib as well a series of iPython notebooks for teaching people to use isilib and python.

The instructions for those familiar with the command line use the advanced instructions otherwise use the easy instructions.

###Easy instructions

First you need to install [Vagrant](https://www.vagrantup.com/downloads.html) and [VirtualBox](https://www.virtualbox.org/wiki/Downloads) before you can install isilib.

Once vagrant and virtualBox are installed, download [isilib](https://github.com/mclevey/web_of_science_isi/archive/master.zip). Unzip the file, if you do not have a tool to do this you can download [7-Zip](http://www.7-zip.org/) and use it.

Open the directory isilib then go to the vagrant subdirectory. If you are using windows double click on win\_run or if you are using a Macintosh double click on mac\_run, if you are using Linux you will need to read the advanced instructions.

A window should pop up and say something like:


    Bringing machine 'default' up with 'virtualbox' provider...
    ==> default: Importing base box 'ubuntu/trusty64'...

It will also tell how long it will take, which is usually around 20 minutes. Now you just have to wait for it to finish. Once that is done a bunch of green, and occasionally red, text will appear, it should take another 10 minutes. Then a browser window will appear at the notebooks and everthing is done. If a browser window opens and it is showing `No data received` hit refresh a couple times.

If you see:

    Lesson-0
    Lesson-1
    Lesson-2
    ...

You have installed everything successfully.

To open the page again just double click on which ever of mac\_run and win\_run you used. It should take less than a minute the second time.

###Advanced Instructions
0. Install [Vagrant](https://www.vagrantup.com/downloads.html) and [VirtualBox](https://www.virtualbox.org/wiki/Downloads)
1. Clone the git [repo](https://github.com/networks-lab/isilib.git)
2. Go to the vagrant directory
3. Run `vagrant up`
4. Once vagrant has finished go to [http://localhost:1159/](http://localhost:1159/)

What you are doing by running `vagrant up` is creating an Ubuntu VM and provisioning it with the script bootstrap also in vagrant. If you run`vagrant up` again it only starts the VM. So to access the VM once it is created:

1. Go to the vagrant directory
2. Run `vagrant up`
3. Once vagrant has finished go to [http://localhost:1159/](http://localhost:1159/)

You can also use `vagrant ssh` to ssh into the VM or `vagrant provision` to rerun bootstrap.

## Install without Vagrant

Installing without Vagrant is done with [setuptools](https://pypi.python.org/pypi/setuptools). Go to the isilib directory and run `python3 setup.py install`
