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

This is the documentation for the current version of _metaknowledge_ which is not compatible with the old version. The old version's documentation can be found [here]({{ site.baseurl }}/documentation/metaknowledgeFullOld.html).


{% assign sortedDocs = site.categories.docs | sort:"weight"  %}
<ul class="post-list">
   <li><article>
   <a href="#Installing">Installing<span class="excerpt">How to install metaknowledge</span></a>
   </article></li>
   <li><article>
   <a href="#Students">Students Install<span class="excerpt">How to install metaknowledge for the class</span></a>
   </article></li>
   <li><article>
   <a href="{{ site.baseurl }}/documentation/metaknowledgeFull.html#objlist">Classes and Modules<span class="excerpt">The list of major classes and modules provided by metaknowledge</span></a>
   </article></li>
   <li><article>
   <a href="{{ site.baseurl }}/documentation/metaknowledgeFull.html#fulllist">Functions and Methods<span class="excerpt">The full list of functions and methods provided by metaknowledge</span></a>
   </article></li>


{% for post in sortedDocs %}
  <li><article><a href="{{ site.baseurl }}/documentation/metaknowledgeFull.html#{{ post.title }}">{{ post.title }}{% if post.excerpt %} <span class="excerpt">{{ post.excerpt }}</span>{% endif %}</a></article></li>
{% endfor %}

</ul>


## <a name="Installing"></a>Installation

_metaknowledge_ has two distributions. The simplest is found under the release branch of the [git repo](https://github.com/networks-lab/metaknowledge/tree/release), which can be installed the usual way with pip:

{% highlight bash %}
pip3 install metaknowledge
{% endhighlight %}

The second version is at the master branch on [_Github_](https://github.com/networks-lab/metaknowledge). It comes with extra documents and resources for teaching.

The [download](https://github.com/networks-lab/metaknowledge/archive/master.zip) from _Github_ includes a customized [_Vagrant_](https://www.vagrantup.com) file that installs _metaknowledge_ and other useful _Python_ libraries into a virtual machine. It is the easiest way of getting _metaknowledge_ working if you are not familiar with _Python_.

## Install with Vagrant

The _Vagrant_ method is intended for students and anyone not familiar with _Python_ it creates a [virtual machine](https://en.wikipedia.org/wiki/Virtual_machine) with _metaknowledge_ installed, as well as the _Python_ scientific stack _numpy_, _scipy_ and _matplotlib_ and a series of iPython notebooks for teaching _metaknowledge_ and _Python_. Some notebooks are more complete than others.

The instructions for those familiar with the command line use the advanced instructions. Otherwise, it is probably best to use the student install.

### <a name="Students">Student Install

First, you need to install [_Vagrant_](https://www.vagrantup.com/downloads.html) and [_VirtualBox_](https://www.virtualbox.org/wiki/Downloads). You need to do this before you can install _metaknowledge_.

Once _Vagrant_ and _VirtualBox_ are installed, download [_metaknowledge_](https://github.com/networks-lab/metaknowledge/archive/master.zip). Unzip the file. If you are unable to unzip the file, download [_7-Zip_](http://www.7-zip.org/).

Open the directory _metaknowledge_ and go to the vagrant subdirectory. Depending on your operating system, double click either: `win_run`, `mac_run`, or `linux_run`.

A window should pop up and say something like:

    Bringing machine 'default' up with 'virtualbox' provider...
    ==> default: Box 'ubuntu/trusty64' could not be found. Attempting to find and in
    stall...
    default: Box Provider: virtualbox
    default: Box Version: >= 0

You will also see an estimate of how long the download and installation process will take (typically 20 minutes). All you have to do it wait for it to finish. When it is done, a browser window will appear at the showing the notebooks. If a browser window opens and it is showing `No data received` hit refresh a couple times.

When you see a page with:

    Lesson-1-Getting-Started
    Lesson-2-Reading-Files
    Lesson-3-Objects
    ...

You have installed everything successfully.

To open the page again just double click on which ever of `win_run`, `mac_run`, or `linux_run` you used. It should take less than a minute the second time.

### Advanced Instructions
0. Install [Vagrant](https://www.vagrantup.com/downloads.html) and [VirtualBox](https://www.virtualbox.org/wiki/Downloads)
1. Clone the [git repo](https://github.com/networks-lab/metaknowledge.git)
2. Make sure you are on the master branch
3. Go to the vagrant directory
4. Run `vagrant up`
5. Once vagrant has finished go to [http://localhost:1159/](http://localhost:1159/)

What you are doing by running `vagrant up` is creating an Ubuntu VM and provisioning it with the script `bootstrap`, which is also in the vagrant directory. If you run`vagrant up` again it only starts the VM. To access the VM's notebook once it is created:

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

Installing without _Vagrant_ is done with [setuptools](https://pypi.python.org/pypi/setuptools). Go to the metaknowledge directory and run `python3 setup.py install`. This is the same version that is installed via pip plus some extra development command line tools.

## IF you want to extend MK

do tall this ...

{% include docsFooter.md %}
