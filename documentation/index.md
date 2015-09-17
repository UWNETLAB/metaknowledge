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
   <li><article>
   <a href="#Installing">Installing<span class="excerpt">How to install metaknowledge</span></a>
   </article></li>
   <li><article>
   <a href="#Students">Students Install<span class="excerpt">How to install metaknowledge for class</span></a>
   </article></li>

{% for post in sortedDocs %}
  <li><article><a href="{{ site.baseurl }}{{ post.url }}">{{ post.title }}{% if post.excerpt %} <span class="excerpt">{{ post.excerpt }}</span>{% endif %}</a></article></li>
{% endfor %}

</ul>


##<a name="Installing"></a>Installation

_metaknowledge_ has two distributions the simplest is found under the release branch of the [git repo](https://github.com/networks-lab/metaknowledge/tree/release). This can be installed the usual way with pip

{% highlight bash %}
pip3 install metaknowledge
{% endhighlight %}

The second version is at the master branch on [_Github_](https://github.com/networks-lab/metaknowledge) and comes with extra documents and resources for teaching.

The [download](https://github.com/networks-lab/metaknowledge/archive/master.zip) from _Github_ includes a customized [_Vagrant_](https://www.vagrantup.com) file that installs _metaknowledge_ and other useful _Python_ libraries into a virtual machine. It is the easiest way of getting _metaknowledge_ working if you are not familiar with _Python_.

##Install with Vagrant

The _Vagrant_ method is intended for students and those not familiar with _Python_ it creates a virtual machine with _metaknowledge_ installed, as well as the _Python_ scientific stack _numpy_, _scipy_ and _matplotlib_ as well a series of iPython notebooks for teaching people to use _metaknowledge_ and _Python_.

The instructions for those familiar with the command line use the advanced instructions otherwise use the Student Install.

###<a name="Students">Student Install

First you need to install [_Vagrant_](https://www.vagrantup.com/downloads.html) and [_VirtualBox_](https://www.virtualbox.org/wiki/Downloads) before you can install _metaknowledge_.

Once _Vagrant_ and _VirtualBox_ are installed, download [_metaknowledge_](https://github.com/networks-lab/metaknowledge/archive/master.zip). Unzip the file. If you are unable to, download [_7-Zip_](http://www.7-zip.org/) and use it.

Open the directory _metaknowledge_ then go to the vagrant subdirectory. If you are using windows double click on win\_run or if you are using a Macintosh double click on mac\_run, if you are using Linux use linux\_run.

A window should pop up and say something like:

    Bringing machine 'default' up with 'virtualbox' provider...
    ==> default: Box 'ubuntu/trusty64' could not be found. Attempting to find and in
    stall...
    default: Box Provider: virtualbox
    default: Box Version: >= 0

It will also tell how long it will take, which is usually around 20 minutes. Now you just have to wait for it to finish. Once that is done a bunch of text will appear, it should take another 10 minutes. Then a browser window will appear at the showing the notebooks. If a browser window opens and it is showing `No data received` hit refresh a couple times.

When you see a page with:

    Lesson-1-Getting-Started
    Lesson-2-Reading-Files
    Lesson-3-Objects
    ...

You have installed everything successfully.

To open the page again just double click on which ever of win\_run, mac\_run or linux\_run you used. It should take less than a minute the second time.

###Advanced Instructions
0. Install [Vagrant](https://www.vagrantup.com/downloads.html) and [VirtualBox](https://www.virtualbox.org/wiki/Downloads)
1. Clone the [git repo](https://github.com/networks-lab/metaknowledge.git)
2. Make sure you are on the master branch
3. Go to the vagrant directory
4. Run `vagrant up`
5. Once vagrant has finished go to [http://localhost:1159/](http://localhost:1159/)

What you are doing by running `vagrant up` is creating an Ubuntu VM and provisioning it with the script `bootstrap` also in vagrant. If you run`vagrant up` again it only starts the VM. To access the VM's notebook once it is created:

1. Go to the vagrant directory
2. Run `vagrant up`
3. Once vagrant has finished go to [http://localhost:1159/](http://localhost:1159/)

You can also use `vagrant ssh` to ssh into the VM or `vagrant provision` to rerun bootstrap. If `vagrant ssh` does not work on your machine, you should be able to ssh into it at:

    HostName: 127.0.0.1
    Port: 2222
    Username: vagrant
    Password: vagrant

On Windows [_PuTTY_](http://www.chiark.greenend.org.uk/~sgtatham/putty/) has been tested and works well.

## Install without Vagrant

Installing without _Vagrant_ is done with [setuptools](https://pypi.python.org/pypi/setuptools). Go to the metaknowledge directory and run `python3 setup.py install`. This is the same version as the that on PyPi with some extra development command line tools.

{% include docsFooter.md %}
