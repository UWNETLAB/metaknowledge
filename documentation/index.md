---
layout: page
title: Documentation
excerpt: "Instructions on how to install and use metaknowledge."
modified: 2015-09-14
image:
  feature:
  credit:
  creditlink:
---

{% assign sortedDocs = site.categories.docs | sort:"weight"  %}
<ul class="post-list">
   <li><article><a href="#Installing">Installing<span class="excerpt">How to install metaknowledge</span></a></article></li>

{% for post in sortedDocs %}
  <li><article><a href="{{ site.baseurl }}{{ post.url }}">{{ post.title }}{% if post.excerpt %} <span class="excerpt">{{ post.excerpt }}</span>{% endif %}</a></article></li>
{% endfor %}

</ul>


##<a name="Installing"></a>Installation

metaknowledge has two distributions the simplest is found under the release branch of the [git repo](https://github.com/networks-lab/metaknowledge/tree/release). This can be installed the usual way with pip

{% highlight bash %}
pip3 install metaknowledge
{% endhighlight %}

The second version is at the master branch on [github](https://github.com/networks-lab/metaknowledge) and comes with extra documents and resources for teaching.

The [download](https://github.com/networks-lab/metaknowledge/archive/master.zip) from Github includes a customized [Vagrant](https://www.vagrantup.com) file that installs metaknowledge and other useful Python libraries into a virtual machine. It is the easiest way of getting metaknowledge working if you are not familiar with Python.

##Install with Vagrant

The vagrant method is intended for students and those not familiar with python it creates a virtual machine with metaknowledge installed, as well as the python scientific stack numpy, scipy and matplotlib as well a series of iPython notebooks for teaching people to use metaknowledge and python.

The instructions for those familiar with the command line use the advanced instructions otherwise use the easy instructions.

###Easy instructions

First you need to install [Vagrant](https://www.vagrantup.com/downloads.html) and [VirtualBox](https://www.virtualbox.org/wiki/Downloads) before you can install metaknowledge.

Once vagrant and virtualBox are installed, download [metaknowledge](https://github.com/networks-lab/metaknowledge/archive/master.zip). Unzip the file. If you are unable to, download [7-Zip](http://www.7-zip.org/) and use it.

Open the directory metaknowledge then go to the vagrant subdirectory. If you are using windows double click on win\_run or if you are using a Macintosh double click on mac\_run, if you are using Linux use linux\_run.

A window should pop up and say something like:

    Bringing machine 'default' up with 'virtualbox' provider...
    ==> default: Box 'ubuntu/trusty64' could not be found. Attempting to find and in
    stall...
    default: Box Provider: virtualbox
    default: Box Version: >= 0

It will also tell how long it will take, which is usually around 20 minutes. Now you just have to wait for it to finish. Once that is done a bunch of text will appear, it should take another 10 minutes. Then a browser window will appear at the notebooks and everything is done. If a browser window opens and it is showing `No data received` hit refresh a couple times.

Then if you a page with see:

    Lesson-0
    Lesson-1
    ...

You have installed everything successfully.

To open the page again just double click on which ever of mac\_run and win\_run you used. It should take less than a minute the second time.

###Advanced Instructions
0. Install [Vagrant](https://www.vagrantup.com/downloads.html) and [VirtualBox](https://www.virtualbox.org/wiki/Downloads)
1. Clone the [git repo](https://github.com/networks-lab/metaknowledge.git)
2. Make sure you are on the master branch
3. Go to the vagrant directory
4. Run `vagrant up`
5. Once vagrant has finished go to [http://localhost:1159/](http://localhost:1159/)

What you are doing by running `vagrant up` is creating an Ubuntu VM and provisioning it with the script `bootstrap` also in vagrant. If you run`vagrant up` again it only starts the VM. To access the VM]s notebook once it is created:

1. Go to the vagrant directory
2. Run `vagrant up`
3. Once vagrant has finished go to [http://localhost:1159/](http://localhost:1159/)

You can also use `vagrant ssh` to ssh into the VM or `vagrant provision` to rerun bootstrap.

## Install without Vagrant

Installing without Vagrant is done with [setuptools](https://pypi.python.org/pypi/setuptools). Go to the metaknowledge directory and run `python3 setup.py install`. This is the same version as the that on PyPi with some extra development command line tools.

{% include docsFooter.md %}
