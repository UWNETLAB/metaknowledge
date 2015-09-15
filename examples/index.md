---
layout: page
title: Examples
excerpt: "Examples showing how to use metaknowledge to analyze data."
search_omit: true
---

<ul class="post-list">

  <li><article>
  <a href="{{ site.baseurl }}/examples/#Getting-Started">Getting Started</a>
  </article></li>
  <li><article>
  <a href="{{ site.baseurl }}/examples/#Reading-Files">Reading Files</a>
  </article></li>
  <li><article>
  <a href="{{ site.baseurl }}/examples/#The-RecordCollection-Object">The RecordCollection Object</a>
  </article></li>
  <li><article>
  <a href="{{ site.baseurl }}/examples/#Filtering">Filtering</a>
  </article></li>
  <li><article>
  <a href="{{ site.baseurl }}/examples/#Exporting-RecordCollections">Exporting RecordCollections</a>
  </article></li>
  <li><article>
  <a href="{{ site.baseurl }}/examples/#Making-a-co-citation-network">Making a co-citation network</a>
  </article></li>
  <li><article>
  <a href="{{ site.baseurl }}/examples/#Making-a-citation-network">Making a citation network</a>
  </article></li>
  <li><article>
  <a href="{{ site.baseurl }}/examples/#Making-a-co-author-network">Making a co-author network</a>
  </article></li>
  <li><article>
  <a href="{{ site.baseurl }}/examples/#Making-a-one-mode-network">Making a one-mode network</a>
  </article></li>
  <li><article>
  <a href="{{ site.baseurl }}/examples/#Making-a-two-mode-network">Making a two-mode network</a>
  </article></li>
  <li><article>
  <a href="{{ site.baseurl }}/examples/#Making-a-multi-mode-network">Making a multi-mode network</a>
  </article></li>
  <li><article>
  <a href="{{ site.baseurl }}/examples/#Post-processing-graphs">Post processing graphs</a>
  </article></li>
  <li><article>
  <a href="{{ site.baseurl }}/examples/#Exporting-graphs">Exporting graphs</a>
  </article></li>
</ul>

<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="Getting-Started">Getting Started<a class="anchor-link" href="#Getting-Started">&#182;</a></h1><p>{% comment %}</p>
<h1 id="Notes-for-those-who-downloaded-the-notebook">Notes for those who downloaded the notebook<a class="anchor-link" href="#Notes-for-those-who-downloaded-the-notebook">&#182;</a></h1><p>The notebook should just work as long as you put the sample file (<code>savedrecs.txt</code>) in the same directory as this file.</p>
<p>The one issue you will have is that the urls will not work. To make them work you will need to replace <code>{{ site.baseurl }}</code> with <code>http://networkslab.org/metaknowledge</code>, sorry about that.</p>
<p>{% endcomment %}</p>
<p>metaknowledge is a python library for creating and analyzing scientific metadata. It uses records obtained from Web of Science (WOS) and mostly produces graphs. This will be a short overview of its capabilities, for complete coverage of the package and install institutions read full the documentation <a href="{{ site.baseurl }}/documentation">here</a>.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>This document was made from a <a href="https://jupyter.org">jupyter</a> notebook you can download the notebook <a href="{{ site.baseurl }}/examples/metaknowledgeExamples.ipynb">here</a> and the sample file is <a href="{{ site.baseurl }}/examples/savedrecs.txt">here</a> if you wish to see an interactive version of these examples.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>First you need to import the metaknowledge package:</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[1]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span class="kn">import</span> <span class="nn">metaknowledge</span> <span class="k">as</span> <span class="nn">mk</span>
</pre></div>

</div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>You will often need the <a href="https://networkx.github.io/documentation/networkx-1.9.1/">networkx</a> package as well:</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[2]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span class="kn">import</span> <span class="nn">networkx</span> <span class="k">as</span> <span class="nn">nx</span>
</pre></div>

</div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>I am using <a href="http://matplotlib.org/">matplotlib</a> to display the graphs and to make them look nice when displayed:</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[3]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span class="kn">import</span> <span class="nn">matplotlib.pyplot</span> <span class="k">as</span> <span class="nn">plt</span>
<span class="o">%</span><span class="k">matplotlib</span> inline
</pre></div>

</div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>metaknowledge also has a matplotlib based graph <a href="{{ site.baseurl }}/docs/visual#quickGraph">visualizer</a>.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[4]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span class="kn">import</span> <span class="nn">metaknowledge.visual</span> <span class="k">as</span> <span class="nn">mkv</span>
</pre></div>

</div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p><a href="http://pandas.pydata.org/">pandas</a> is also used in one example</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[5]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span class="kn">import</span> <span class="nn">pandas</span>
</pre></div>

</div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="Reading-Files"><a href="{{ site.baseurl }}/docs/RecordCollection#RecordCollection">Reading Files</a><a class="anchor-link" href="#Reading-Files">&#182;</a></h1><p>The files from the Web of Science (WOS) can be loaded into <a href="{{ site.baseurl }}/docs/RecordCollection#RecordCollection">RecordCollections</a> by creating a RecordCollection object with the path to the files given to the initializer as a string.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[6]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span class="n">RC</span> <span class="o">=</span> <span class="n">mk</span><span class="o">.</span><span class="n">RecordCollection</span><span class="p">(</span><span class="s">&quot;savedrecs.txt&quot;</span><span class="p">)</span>
<span class="nb">repr</span><span class="p">(</span><span class="n">RC</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt output_prompt">Out[6]:</div>


<div class="output_text output_subarea output_execute_result">
<pre>&apos;savedrecs&apos;</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>You can also read a whole directory</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[7]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span class="n">RC</span> <span class="o">=</span> <span class="n">mk</span><span class="o">.</span><span class="n">RecordCollection</span><span class="p">(</span><span class="s">&quot;.&quot;</span><span class="p">)</span>
<span class="nb">repr</span><span class="p">(</span><span class="n">RC</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt output_prompt">Out[7]:</div>


<div class="output_text output_subarea output_execute_result">
<pre>&apos;files-from-.&apos;</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>metaknowledge can detect if a file is a valid WOS file or not and will read the entire directory and load only those that have the right header. You can also tell it to only read a certain type of file, by using the extension argument.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[8]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span class="n">RC</span> <span class="o">=</span> <span class="n">mk</span><span class="o">.</span><span class="n">RecordCollection</span><span class="p">(</span><span class="s">&quot;.&quot;</span><span class="p">,</span> <span class="n">extension</span> <span class="o">=</span> <span class="s">&quot;txt&quot;</span><span class="p">)</span>
<span class="nb">repr</span><span class="p">(</span><span class="n">RC</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt output_prompt">Out[8]:</div>


<div class="output_text output_subarea output_execute_result">
<pre>&apos;txt-files-from-.&apos;</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>Now you have a RecordCollection object composed of all the WOS records in the selected file(s).</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[9]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span class="nb">print</span><span class="p">(</span><span class="s">&quot;RC is a &quot;</span> <span class="o">+</span> <span class="nb">str</span><span class="p">(</span><span class="n">RC</span><span class="p">))</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt"></div>
<div class="output_subarea output_stream output_stdout output_text">
<pre>RC is a Collection of 32 records
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="The-RecordCollection-Object"><a href="{{ site.baseurl }}/docs/RecordCollection#RecordCollection">The RecordCollection Object</a><a class="anchor-link" href="#The-RecordCollection-Object">&#182;</a></h1><p>The RecordCollection is the object that metaknowledge uses the most. It is your interface with the data you want.</p>
<p>To see an individual <a href="{{ site.baseurl }}/docs/Record#Record">Record</a> at random you can use <code>peak()</code></p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[10]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span class="nb">print</span><span class="p">(</span><span class="n">RC</span><span class="o">.</span><span class="n">peak</span><span class="p">())</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt"></div>
<div class="output_subarea output_stream output_stdout output_text">
<pre>EXPERIMENTS IN PHENOMENOLOGICAL ELECTRODYNAMICS AND THE ELECTROMAGNETIC ENERGY-MOMENTUM TENSOR
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>Or to iterate over all of them you can use a for loop</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[11]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span class="k">for</span> <span class="n">R</span> <span class="ow">in</span> <span class="n">RC</span><span class="p">:</span>
    <span class="nb">print</span><span class="p">(</span><span class="n">R</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt"></div>
<div class="output_subarea output_stream output_stdout output_text">
<pre>EXPERIMENTS IN PHENOMENOLOGICAL ELECTRODYNAMICS AND THE ELECTROMAGNETIC ENERGY-MOMENTUM TENSOR
Transverse displacement at total reflection near the grazing angle: a way to discriminate between theories
RESONANCE EFFECTS ON TOTAL INTERNAL-REFLECTION AND LATERAL (GOOS-HANCHEN) BEAM DISPLACEMENT AT THE INTERFACE BETWEEN NONLOCAL AND LOCAL DIELECTRIC
PREDICTION OF A RESONANCE-ENHANCED LASER-BEAM DISPLACEMENT AT TOTAL INTERNAL-REFLECTION IN SEMICONDUCTORS
OBSERVATION OF SHIFTS IN TOTAL REFLECTION OF A LIGHT-BEAM BY A MULTILAYERED STRUCTURE
Optical properties of nanostructured thin films
Longitudinal and transverse effects of nonspecular reflection
ASYMMETRICAL MOMENTUM-ENERGY TENSORS AND 6-COMPONENT ANGULAR-MOMENTUM IN PROBLEM CONCERNING 2 PHOTON MOMENTA AND MAGNETODYNAMIC EFFECT PROBLEM
CALCULATION AND MEASUREMENT OF FORCES AND TORQUES APPLIED TO UNIAXIAL CRYSTAL BY EXTRAORDINARY WAVE
Simple technique for measuring the Goos-Hanchen effect with polarization modulation and a position-sensitive detector
ANGULAR SPECTRUM AS AN ELECTRICAL NETWORK
EXCHANGED MOMENTUM BETWEEN MOVING ATOMS AND A SURFACE-WAVE - THEORY AND EXPERIMENT
Experimental observation of the Imbert-Fedorov transverse displacement after a single total reflection
LONGITUDINAL AND TRANSVERSE DISPLACEMENTS OF A BOUNDED MICROWAVE BEAM AT TOTAL INTERNAL-REFLECTION
MECHANICAL INTERPRETATION OF SHIFTS IN TOTAL REFLECTION OF SPINNING PARTICLES
SPIN ANGULAR-MOMENTUM OF A FIELD INTERACTING WITH A PLANE INTERFACE
A Novel Method for Enhancing Goos-Hanchen Shift in Total Internal Reflection
Goos-Hanchen and Imbert-Fedorov shifts for leaky guided modes
Numerical study of the displacement of a three-dimensional Gaussian beam transmitted at total internal reflection. Near-field applications
NONLINEAR TOTALLY REFLECTING PRISM COUPLER - THERMOMECHANIC EFFECTS AND INTENSITY-DEPENDENT REFRACTIVE-INDEX OF THIN-FILMS
GENERAL STUDY OF DISPLACEMENTS AT TOTAL REFLECTION
TRANSVERSE DISPLACEMENT OF A TOTALLY REFLECTED LIGHT-BEAM AND PHASE-SHIFT METHOD
DISPLACEMENT OF A TOTALLY REFLECTED LIGHT-BEAM - FILTERING OF POLARIZATION STATES AND AMPLIFICATION
DISCUSSIONS OF PROBLEM OF PONDEROMOTIVE FORCES
SPIN ANGULAR-MOMENTUM OF A FIELD INTERACTING WITH A PLANE INTERFACE
WHY ENERGY FLUX AND ABRAHAMS PHOTON MOMENTUM ARE MACROSCOPICALLY SUBSTITUTED FOR MOMENTUM DENSITY AND MINKOWSKIS PHOTON MOMENTUM
INTERFERENCE THEORY OF REFLECTION FROM MULTILAYERED MEDIA
INTERNAL PHOTON IMPULSE OF DIELECTRIC AND ON COUPLE APPLIED TO ANISOTROPIC CRYSTAL
THEORETICAL NOTES ON AMPLIFICATION OF TRANSVERSE SHIFT BY TOTAL REFLECTION ON MULTILAYERED SYSTEM
Goos-Hanchen shift as a probe in evanescent slab waveguide sensors
SHIFTS OF COHERENT-LIGHT BEAMS ON REFLECTION AT PLANE INTERFACES BETWEEN ISOTROPIC MEDIA
CONSERVATION OF ANGULAR MOMENT WITH SIX COMPONENTS AND ASYMMETRICAL IMPULSE ENERGY TENSORS
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>The individual Records are index by their WOS numbers so you can access a specific one in the collection if you know its number.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[12]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span class="n">RC</span><span class="o">.</span><span class="n">getWOS</span><span class="p">(</span><span class="s">&quot;WOS:A1979GV55600001&quot;</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt output_prompt">Out[12]:</div>


<div class="output_text output_subarea output_execute_result">
<pre>&lt;metaknowledge.record.Record at 0x10a7b5ba8&gt;</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="Filtering"><a href="{{ site.baseurl }}/docs/RecordCollection#yearSplit">Filtering</a><a class="anchor-link" href="#Filtering">&#182;</a></h1><p>The for loop shown above is the main way to filter a RecordCollection, there are a few builtin filters, e.g. <a href="{{ site.baseurl }}/docs/RecordCollection#yearSplit"><code>yearSplit()</code></a>, but the for loop is an easily generalized way of filtering that is relatively simple to read so it the main way you should filter. An example of the workflow is as follows:</p>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>First create a new RecordCollection</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[13]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span class="n">RCfiltered</span> <span class="o">=</span> <span class="n">mk</span><span class="o">.</span><span class="n">RecordCollection</span><span class="p">()</span>
</pre></div>

</div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>Then add the records that meet your condition, in this case that their title's start with <code>'A'</code></p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[14]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span class="k">for</span> <span class="n">R</span> <span class="ow">in</span> <span class="n">RC</span><span class="p">:</span>
    <span class="k">if</span> <span class="n">R</span><span class="o">.</span><span class="n">title</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span> <span class="o">==</span> <span class="s">&#39;A&#39;</span><span class="p">:</span>
        <span class="n">RCfiltered</span><span class="o">.</span><span class="n">addRec</span><span class="p">(</span><span class="n">R</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[15]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span class="nb">print</span><span class="p">(</span><span class="n">RCfiltered</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt"></div>
<div class="output_subarea output_stream output_stdout output_text">
<pre>Collection of 3 records
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>Now you have a RecordCollection <code>RCfiltered</code> of all the <code>Records</code> whose titles begin with <code>'A'</code>.</p>
<p>One note about implementing this, the above code does not handle the case in which the title is missing i.e. <code>R.title</code> is <code>None</code>. You will have to deal with this in some way.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>Two builtin functions to filter collections are <a href="{{ site.baseurl }}/docs/RecordCollection#yearSplit"><code>yearSplit()</code></a> and <a href="{{ site.baseurl }}/docs/RecordCollection#localCitesOf"><code>localCitesOf()</code></a>. To get a RecordCollection of all Records between 1970 and 1979:</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[16]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span class="n">RC70</span> <span class="o">=</span> <span class="n">RC</span><span class="o">.</span><span class="n">yearSplit</span><span class="p">(</span><span class="mi">1970</span><span class="p">,</span> <span class="mi">1979</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">RC70</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt"></div>
<div class="output_subarea output_stream output_stdout output_text">
<pre>Collection of 19 records
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>The second function <a href="{{ site.baseurl }}/docs/RecordCollection#localCitesOf"><code>localCitesOf()</code></a> takes in an object that a <a href="{{ site.baseurl }}/docs/Citation#Citation">Citation</a> can be created from and returns a RecordCollection of all the Records that cite it. So to see all the records that cite <code>"Yariv A., 1971, INTRO OPTICAL ELECTR"</code>.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[17]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span class="n">RCintroOpt</span> <span class="o">=</span> <span class="n">RC</span><span class="o">.</span><span class="n">localCitesOf</span><span class="p">(</span><span class="s">&quot;Yariv A., 1971, INTRO OPTICAL ELECTR&quot;</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">RCintroOpt</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt"></div>
<div class="output_subarea output_stream output_stdout output_text">
<pre>Collection of 1 records
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="Exporting-RecordCollections">Exporting RecordCollections<a class="anchor-link" href="#Exporting-RecordCollections">&#182;</a></h1>
</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>Now you have a filtered RecordCollection you can write it as a file with <a href="{{ site.baseurl }}/docs/RecordCollection#writeFile"><code>writeFile()</code></a></p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[18]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre> <span class="n">RCfiltered</span><span class="o">.</span><span class="n">writeFile</span><span class="p">(</span><span class="s">&quot;Records_Starting_with_A.txt&quot;</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>The written file is identical to one of those produced by WOS.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>If you wish to have a more useful file use <a href="{{ site.baseurl }}/docs/RecordCollection#writeCSV"><code>writeCSV()</code></a> which creates a CSV file of all the tags as columns and the Records as rows. IF you only care about a few tags the <code>onlyTheseTags</code> argument allows you to control the tags.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[19]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span class="n">selectedTags</span> <span class="o">=</span> <span class="p">[</span><span class="s">&#39;TI&#39;</span><span class="p">,</span> <span class="s">&#39;UT&#39;</span><span class="p">,</span> <span class="s">&#39;CR&#39;</span><span class="p">,</span> <span class="s">&#39;AU&#39;</span><span class="p">]</span>
</pre></div>

</div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>This will give the title, WOS number, citations, and authors.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[20]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span class="n">RCfiltered</span><span class="o">.</span><span class="n">writeCSV</span><span class="p">(</span><span class="s">&quot;Records_Starting_with_A.csv&quot;</span><span class="p">,</span> <span class="n">onlyTheseTags</span> <span class="o">=</span> <span class="n">selectedTags</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>The last export feature is for using metaknowledge with other packages, in particular <a href="http://pandas.pydata.org/">pandas</a> but other should also work. [<code>makeDict()</code>] creates a dictionary with tags as keys and lists a values with each element of a list corresponding to a Record. pandas can accept these directly to make DataFrames.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[21]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span class="n">recDataFrame</span> <span class="o">=</span> <span class="n">pandas</span><span class="o">.</span><span class="n">DataFrame</span><span class="p">(</span><span class="n">RC</span><span class="o">.</span><span class="n">makeDict</span><span class="p">())</span>
</pre></div>

</div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="Making-a-co-citation-network">Making a co-citation network<a class="anchor-link" href="#Making-a-co-citation-network">&#182;</a></h1>
</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>To make a basic co-citation network of some collection of Records use the <a href="{{ site.baseurl }}/docs/RecordCollection#coCiteNetwork"><code>coCiteNetwork()</code></a> method.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[22]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span class="n">coCites</span> <span class="o">=</span> <span class="n">RC</span><span class="o">.</span><span class="n">coCiteNetwork</span><span class="p">()</span>
<span class="nb">print</span><span class="p">(</span><span class="n">mk</span><span class="o">.</span><span class="n">graphStats</span><span class="p">(</span><span class="n">coCites</span><span class="p">,</span> <span class="n">makeString</span> <span class="o">=</span> <span class="k">True</span><span class="p">))</span> <span class="c">#makestring by default is True so it is not strictly necessary to include</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt"></div>
<div class="output_subarea output_stream output_stdout output_text">
<pre>The graph has 601 nodes, 19492 edges, 0 isolates, 4 self loops, a density of 0.108109 and a transitivity of 0.691662
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p><a href="{{ site.baseurl }}/docs/metaknowledge#graphStats"><code>graphStats()</code></a> is a function to extract some of the statists of a graph and make a nice string to display them as a sentence.</p>
<p><code>coCites</code> is now <a href="https://networkx.github.io/documentation/networkx-1.9.1/">networkx</a> graph of the co-citation network. All the graphs metaknowledge use are networkx graphs, few functions to trim them are implemented in metaknowledge, <a href="#filtering-graphs">here</a> is the example section, but many useful functions are implemented by it. Read the documentation <a href="https://networkx.github.io/documentation/networkx-1.9.1/">here</a> for more information.</p>
<p>The <code>coCiteNetwork()</code> function has many options for filtering and determining the nodes. The default is to use the citations themselves. If you wanted to make a network of co-citations of journals you would have to make the node type <code>'journal'</code> and remove the non-journals.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[23]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span class="n">coCiteJournals</span> <span class="o">=</span> <span class="n">RC</span><span class="o">.</span><span class="n">coCiteNetwork</span><span class="p">(</span><span class="n">nodeType</span> <span class="o">=</span> <span class="s">&#39;journal&#39;</span><span class="p">,</span> <span class="n">dropNonJournals</span> <span class="o">=</span> <span class="k">True</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">mk</span><span class="o">.</span><span class="n">graphStats</span><span class="p">(</span><span class="n">coCiteJournals</span><span class="p">))</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt"></div>
<div class="output_subarea output_stream output_stdout output_text">
<pre>The graph has 89 nodes, 1383 edges, 0 isolates, 40 self loops, a density of 0.353166 and a transitivity of 0.640306
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>Lets take a look at the graph after a quick spring layout</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[24]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span class="n">nx</span><span class="o">.</span><span class="n">draw_spring</span><span class="p">(</span><span class="n">coCiteJournals</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt"></div>


<div class="output_png output_subarea ">
<img src="data:image/png;base64,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
AElFTkSuQmCC
"
>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>A bit basic but gives a general idea. If you want to make a much better looking and more informative visualization you could try <a href="https://gephi.github.io/">gephi</a> or <a href="http://visone.info/">visone</a>. Exporting to them is coverd <a href="#exporting-graphs">below</a>.</p>
<h1 id="Making-a-citation-network">Making a citation network<a class="anchor-link" href="#Making-a-citation-network">&#182;</a></h1>
</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>The <a href="{{ site.baseurl }}/docs/RecordCollection#citationNetwork"><code>citationNetwork()</code></a> method is nearly identical to <code>coCiteNetwork()</code> in its parameters. It has one additional keyword argument <code>directed</code> which controls wether it produces a directed network, but the rest is the same. So read <a href="{{ site.baseurl }}/examples/#Making-a-co-citation-network"><strong>Making a co-citation network</strong></a> to learn more about <code>citationNetwork()</code>.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>One small example is still worth providing. If you wanted to make a network of the citations of years by other years and have the letter <code>'A'</code> in them then you would write:</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[25]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span class="n">citationsA</span> <span class="o">=</span> <span class="n">RC</span><span class="o">.</span><span class="n">citationNetwork</span><span class="p">(</span><span class="n">nodeType</span> <span class="o">=</span> <span class="s">&#39;year&#39;</span><span class="p">,</span> <span class="n">keyWords</span> <span class="o">=</span> <span class="p">[</span><span class="s">&#39;A&#39;</span><span class="p">])</span>
<span class="nb">print</span><span class="p">(</span><span class="n">mk</span><span class="o">.</span><span class="n">graphStats</span><span class="p">(</span><span class="n">citationsA</span><span class="p">))</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt"></div>
<div class="output_subarea output_stream output_stdout output_text">
<pre>The graph has 18 nodes, 24 edges, 0 isolates, 1 self loops, a density of 0.0784314 and a transitivity of 0.0344828
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[26]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span class="n">nx</span><span class="o">.</span><span class="n">draw_spring</span><span class="p">(</span><span class="n">citationsA</span><span class="p">,</span> <span class="n">with_labels</span> <span class="o">=</span> <span class="k">True</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt"></div>


<div class="output_png output_subarea ">
<img src="data:image/png;base64,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
cdyECaRlZhIcEYE/MBktgUbhfxQGtMFVc11dOWZlxZz58xk0eHC5ys7JyWHUqFH8+uuv/PLLLzRu
3BjQBoD961//YvXq1ezcuZOmTZve0bMLcT+R4CvEA+C7775jyZIl7NmzB0dHx79U1vkLF8gB9qEl
0jBYWVHbSZtYdDUvj7YtWhA+eTJhYWHlbmo+c+YMYWFhNG/enN27d+Ps7AzA9evXefHFF0lLS2PP
nj3FUl4K8SCTAVdC3Od27dpFv3792LZtGy1blpyVWzEFBQX4+Phw6dIl877ly5fTvn17AGrWrFnh
lI6bNm3i5ZdfZsqUKfzjH/8wzwG+ePEivXv3plWrVsyvYJ+xEPc7Cb5C3McSEhLo1KkTixYtonv3
7pVSZlZWFoGBgdja2pKSksK5c+fuKJVjYZrIefPmsXz5coKCgszHDh06RJ8+fRgzZgyTJ0+WNXjF
Q0eanYW4T6WlpREaGsq0adMqLfCCNgUoJSWFixcvkpube0eBNy0tjZdeeonU1FQOHDhQLEHGmjVr
eO2115g3bx79+/evtOcW4n4i4/iFuA8ZDAYGDBjAc889R3h4eKWWvXTpUoYOHYqdnR2urq4Vvv7I
kSO0b98eX19ftm3bZg68SimioqIIDw9nw4YNEnjFQ02anYW4zyilGDlyJJcuXWLNmjVUq1at0so2
Go088sgjxMXF0aZNm3Jdk5GRQU5ODrVr10an0zFu3Dj+85//8Le//c18jsFgYMyYMezdu5e1a9fi
4+NzixKFePBJs7MQ95nZs2ezd+9e4uPjKzXwAuzYsQN3d3cCAgLKdf7x48fp168fHh4etGvXjo0b
N/LTTz/RunVr8znXrl1j4MCBODg4EB8ff0e1aSEeNBJ8hbiPrF69mtmzZ7N79+4qCWKLFy9m2LBh
5RoAtWLFCl555RWuX78OwKVLl/j111+pUaMGR44cwd/fn9OnT9OzZ0+6d+/OrFmzKv3LghD3K2l2
FuI+cejQIbp168aGDRvMU38qU2ZmJg0aNODkyZPUqlXrpufl5+fzr3/9i6ioqFLH4uLiOHbsGFOn
TmXy5MksXryY6dOnM3r06Ep/XiHuZxJ8hbgPXLx4kSeeeII5c+YQFhZWJfdYtGgRq1evZs2aNTc9
JykpiUGDBrF9+/ZSx1566SXy8/OJjo4274uMjOStt96qiscV4r4mo52FuMdlZWXRq1cvxo4dW2WB
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
dX6qg0B3Z2eSz58v9vVFROR3Ct9yKCUlJX/mqtq1a//hEn9FVZZLGIqIyO802rkccnFxKbHALSiw
Xz/OnT2LTxEWVuhVyD5mEREpPLV8K6GS7mMWEZGiUfhWUqXdxywiIn9M4Sul1scsIiK3pvAVERGx
Mk2yISIiYmUKXxEREStT+IqIiFiZwldERMTKFL4iIiJWpvAVERGxMoWviIiIlSl8RURErEzhKyIi
YmUKXxEREStT+IqIiFiZwldERMTKFL4iIiJWpvAVERGxMoWviIiIlSl8RURErEzhKyIiYmUKXxER
EStT+IqIiFiZwldERMTKFL4iIiJWpvAVERGxMoWviIiIlSl8RURErEzhKyIiYmUKXxEREStT+IqI
iFiZwldERMTKFL4iIiJWpvAVERGxMoWviIiIlSl8RURErEzhKyIiYmUKXxEREStT+IqIiFiZwldE
RMTKFL4iIiJWpvAVERGxMoWviIiIlSl8RURErEzhKyIiYmUKXxEREStT+IqIiFiZwldERMTKFL4i
IiJWpvAVERGxMoWviIiIlSl8RURErOz/A31sCHPZyE9OAAAAAElFTkSuQmCC
"
>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="Making-a-co-author-network">Making a co-author network<a class="anchor-link" href="#Making-a-co-author-network">&#182;</a></h1><p>The <a href="{{ site.baseurl }}/docs/RecordCollection#coAuthNetwork"><code>coAuthNetwork()</code></a> function produces the co-authorship network of the RecordCollection as is used as shown</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[27]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span class="n">coAuths</span> <span class="o">=</span> <span class="n">RC</span><span class="o">.</span><span class="n">coAuthNetwork</span><span class="p">()</span>
<span class="nb">print</span><span class="p">(</span><span class="n">mk</span><span class="o">.</span><span class="n">graphStats</span><span class="p">(</span><span class="n">coAuths</span><span class="p">))</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt"></div>
<div class="output_subarea output_stream output_stdout output_text">
<pre>The graph has 45 nodes, 46 edges, 9 isolates, 0 self loops, a density of 0.0464646 and a transitivity of 0.822581
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="Making-a-one-mode-network">Making a one-mode network<a class="anchor-link" href="#Making-a-one-mode-network">&#182;</a></h1><p>In addition to the specialized network generators metaknowledge lets you make a one-mode co-occurence network of any of the WOS tags, with the <a href="{{ site.baseurl }}/docs/RecordCollection#oneModeNetwork">oneModeNetwork()</a> function. For examples the WOS subject tag <code>'WC'</code> can be examined.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[28]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span class="n">wcCoOccurs</span> <span class="o">=</span> <span class="n">RC</span><span class="o">.</span><span class="n">oneModeNetwork</span><span class="p">(</span><span class="s">&#39;WC&#39;</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">mk</span><span class="o">.</span><span class="n">graphStats</span><span class="p">(</span><span class="n">wcCoOccurs</span><span class="p">))</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt"></div>
<div class="output_subarea output_stream output_stdout output_text">
<pre>The graph has 9 nodes, 3 edges, 3 isolates, 0 self loops, a density of 0.0833333 and a transitivity of 0
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[29]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span class="n">nx</span><span class="o">.</span><span class="n">draw_spring</span><span class="p">(</span><span class="n">wcCoOccurs</span><span class="p">,</span> <span class="n">with_labels</span> <span class="o">=</span> <span class="k">True</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt"></div>


<div class="output_png output_subarea ">
<img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAd8AAAFBCAYAAAA2bKVrAAAABHNCSVQICAgIfAhkiAAAAAlwSFlz
AAALEgAACxIB0t1+/AAAIABJREFUeJzs3XmcjXX/x/HXmc2sZ3YzZo8pQii7LJM2CVmyG0QhiiiJ
rFFuFdoXkTVj6ZY93FHh/t01qUw1QoOZYUbMWGYxY9bP748zczVnFlQ6qM/z8TiPmXOu7XtdZ3lf
1/f7va7LJCKCUkoppWzG7loXQCmllPqn0fBVSimlbEzDVymllLIxDV+llFLKxjR8lVJKKRvT8FVK
KaVsTMNXKaWUsjENX6WUUsrGNHyVUkopG9PwVUoppWxMw1cppZSyMQ1fpZRSysY0fJVSSikb0/BV
SimlbEzDVymllLIxDV+llFLKxjR8lVJKKRvT8FVKKaVsTMNXKaWUsjENX6WUUsrGNHyVUkopG9Pw
VUoppWxMw1cppZSyMQ1fpZRSysY0fJVSSikb0/BVSimlbEzDVymllLIxDV+llFLKxjR8lVJKKRvT
8FVKKaVsTMNXKaWUsjENX6WUUsrGNHyVUkopG9PwVUoppWxMw1cppZSyMQ1fpZRSysY0fJVSSikb
0/BVSimlbEzDVymllLIxDV+llFLKxjR8lVJKKRvT8FVKKaVsTMNXKaWUsjENX6WUUsrGNHyVUkop
G9PwVUoppWxMw1cppZSyMQ1fpZRSysY0fJVSSikbc7jWBVBKXVpGRgZnzpwBwNfXF09Pz2tcIqXU
n6VHvkpdh/Ly8oiJiaFNo0YE+/tzd8OG3N2wIcH+/rRp1IiYmBjy8/OvdTGVUn+QSUTkWhdCKfWb
1atWMWb4cG4TYWRWFp35rYqqANgEvOPuzk92drz+/vv07tPn2hVWKfWHaPgqdR15Y948Xp08mU9y
c2l8mXG/Bbq5uvLMzJmMHjfOFsVTSl0lWu2srgtRUVEsWrToqs7z8ccfZ9asWVd1nn+l1atW8erk
yeytJHi/AELLvdYY2JuTw6tTprB61SqblLGsiIgIdu7cafPlKvV3oOGrbCYiIgJXV1c8PDwIDAzk
kUce4cKFCwCYTCZMJtNVXd67777L5MmTr+o8y9u+fTtt27bFbDZTvXp1oqKi2LRp0++eT15eHmOG
D2d9bi5hv2O6MOCTnBzGDB9u8zbgS71ngwcPxs7Ojo0bN1q9PnbsWOzs7Fi6dOkVLSMiIoJdu3YZ
zxMTE7Gzs6O4uPiPF1yp64CGr7IZk8nE5s2bycrK4rvvvmPfvn031JFpeR9//DG9evVi8ODBpKSk
cPr0aV544YU/FL7r1q2jfnExd/yBcjQG6hUXs27duj8w9V/DZDJxyy23sGzZMuO1wsJC1qxZQ2Rk
5BXvaJlMJiprGfujrWWFhYV/aDqlrjYNX3VNBAUF0aFDB+Lj443XEhMTad26NWazmfvvv984vebB
Bx/krbfespq+QYMGbNiwAbAcTQUEBODp6UmDBg04cOAAYDn6mjJlijHNhg0baNSoEZ6enkRGRrJ9
+3YAlixZQq1atTCbzdSsWZOVK1detvwiwrhx45g6dSpDhgzBw8MDgLZt27JgwQJjnFmzZhEREUFA
QACDBg0iMzPTWFc7OzuWLVtGeHg4A6OjCcjONuafCwwGfIB6wDfllp8K9ACqAzWBiOxs3pkzB4Dp
06fTq1cvBg0ahNlspn79+nz77bfGtHPmzCEkJASz2UydOnWMI0sR4V//+heRkZH4+fnRu3dvzp07
Z0y3fPlywsPD8fPz46WXXrrsNurcuTN79+7l/PnzAGzbto2GDRsSEBBghOeRI0do3749fn5++Pv7
M2DAADIyMgCIjo4mOTmZzp074+HhwSuvvEK7du0A8PLywsPDg6+//hqADz/8kLp16+Lj40OHDh1I
Tk42ymFnZ8c777zDzTffTO3atS9bbqVsQpSykYiICPnss89ERCQ5OVnq1asnU6dOFRGRdu3aSa1a
teSXX36R3NxciYqKkueee05ERNasWSPNmzc35rN//37x9fWVgoIC2bZtmzRu3FgyMjJEROTgwYNy
8uRJEREZPHiwTJkyRUREvv76a/H09DSWn5KSIgcPHpTs7Gwxm81y+PBhERH59ddfJT4+/rLr8vPP
P4vJZJLExMQqx1m0aJFERkbKsWPHJDs7W7p37y7R0dEiInLs2DExmUwybNgwOXXqlLg4OEg1kIMg
AjIBpC3IOZDjIPVAQkuGFYHcATITpADkKEhNkGr29nL+/HmZNm2aODs7y6effirFxcUyceJEadGi
hbF9QkNDjW2UlJQkR44cERGR1157TVq2bCkpKSmSn58vw4cPl759+4qISHx8vLi7u8uePXskLy9P
xo0bJw4ODrJz585K133w4MEyefJkGTZsmLz77rsiItKzZ0+JiYmR1q1by9KlS0VEJCEhQT777DPJ
z8+XtLQ0adu2rTz11FPGfCIiIqyWkZiYKCaTSYqKiozX1q9fL5GRkXLw4EEpKiqSWbNmSatWrYzh
JpNJ7rvvPjl37pxcvHjxsu+tUrag4atsJjw8XNzd3cXLy0vCw8Nl1KhRxo9hVFSUvPjii8a477zz
jnTo0EFERHJzc8Xb21sSEhJEROTpp5+WUaNGiYjIzp075ZZbbpGvvvrK6gdZxDp8hw0bJuPGjatQ
puzsbPHy8pJ///vfkpOTc8XrsnfvXjGZTJKXl1flOO3btzeCR0Tk0KFD4ujoKEVFRUb4pqSkyJEj
RyTC3V2agawuCdiaINtL/heQBSAhJf9/BRJWZpiAvATi5uAgR48elWnTpsm9995rLDc+Pl5cXFxE
ROSXX36R6tWrG4FX1q233moVdKmpqeLo6CiFhYUyY8YMI4hFRC5cuCBOTk6XDd+9e/dKy5Yt5fz5
8xIQECC5ublW4VveJ598IrfffrvxvHz4lm63su91hw4dZNGiRcbzoqIicXV1leTkZBGxhO/nn39e
6fKUula02lnZjMlkYsOGDZw7d47ExETeeustqlWrZgwPDAw0/ndxcSG7pBrW2dmZXr16sXz5ckSE
VatWER0dDUD79u154oknGDVqFAEBAQwfPpysrKwKyz5x4gS1atWq8LqbmxurV6/mvffeIygoiE6d
OnHo0KHLrouvry8AJ0+erHKckydPEh4ebjwPCwujsLCQU6dOVbrOrkBpxXMq1r2by3bCSioZ7l3m
MRsoLtMOGhAQ8Nt8XV25ePEixcXFREZG8tprrzF9+nQCAgLo27evsQ6JiYl069YNb29vvL29qVu3
Lg4ODpw6dYqTJ08SEhJiNc/SbVAVk8nEnXfeSVpaGrNmzaJz5844OztbjXPq1Cn69OlDSEgInp6e
REdHG80NVyopKYkxY8YY5S4tV0pKijFOaGj5vuJKXVsavuqGMGjQID766CM+++wzXF1dad68uTHs
ySefZN++fRw4cIDDhw/zyiuvVJg+NDSUhISESud93333sWPHDn799Vfq1KnDY489dtny1K5dm9DQ
UD7++OMqxwkKCiIxMdF4npycjIODg1UwgiXI0/LyKNuFqAaQXOZ52f9DgZuAc2UeZ7C0bfr4+Fy2
M1Pfvn3Zs2cPSUlJmEwmJkyYAFh2DrZt28a5c+eMR05ODkFBQdSoUYPjx48b88jJybnikBwwYADz
5s1j4MCBFYZNmjQJe3t7fvrpJzIyMli+fLlVT+by61LZuoWFhbFgwQKrcl+4cIEWLVpccjqlriUN
X3XdkEv0YG3ZsiUmk4lnnnnG6kd83759fP311xQUFODq6oqzszP29vbG/ErnOXToUBYvXsyuXbso
Li4mJSWFQ4cOcfr0aTZs2MCFCxdwdHTEzc3NmL60U1TZzjulTCYT8+bNY+bMmSxZsoTMzEyKi4vZ
u3cvw4cPBywhN3/+fBITE8nOzmbSpEn06dMHOzvrr52npye3161LepnXemE5mj0PnADeLDOsGeAB
vIylY1YR8BZw80034enpecntePjwYXbt2kVeXh7VqlWz2l4jRoxg0qRJxvqmpaUZpwo9/PDDbN68
mf/+97/k5+czderUS57uU3bbjx49ms8++4w2bdpUGC87Oxs3NzfMZjMpKSkVdpwCAgI4cuSI8dzf
3x87Ozur10aMGMFLL71kdLTLyMhg7dq1VZZNqeuBhq+6bpQ9OqnsHNKBAwfy448/MmDAAOO1zMxM
hg0bho+PDxEREfj5+TF+/PgK82jatCmLFy9m7NixeHl5ERUVRXJyMsXFxcyfP5/g4GB8fX3Zs2cP
7777LgDHjx8nIiKC4ODgSsvbo0cPVq9ezYcffkhwcDCBgYFMnTqVrl27AjBkyBCio6Np27YtNWvW
xNXVlTff/C1Gy67fyAkTSCkJQYBpQDiWI9wOwECgdGx7YDOwH0tPZ39gup0dD/bsWeW2K32el5fH
xIkT8ff3p0aNGqSnpzN79mwAxowZQ5cuXbjvvvswm820bNmS2NhYAOrWrcvbb79Nv379CAoKwsfH
55JVuWXL4O3tzV133VXpeNOmTeO7777D09OTzp0706NHD6uyT5w4kVmzZuHt7c28efNwdXXl+eef
584778Tb25vY2Fi6du3KhAkT6NOnD56entx2221GT/by21mp64VeXlLdMJYvX84HH3zA7t27bbK8
F198kerVq19RNfSflZeXR3j16mzNzPzd5/p+CzxoNpOcloaTk9NfUTyl1FWm4atuCDk5OUbnqrJH
vn8nq1etYvyQIez9HVe5SgZau7ryyqJFeoMFpW4gWu2srnvbt2+nevXq1KhRg379+l3r4vxlevfp
wzOzZtHaxYVvLz8632IJ3mdmztTgVeoGo0e+Sl1nSm8pWL+4mJHZ2XTB+paCG4F3PDyIN5n0loLq
L5ORkWH0aPf19cXT0/Mal+jvRcNXqetQfn4+69at4505c/guPh6/krbc9Px87qhXj5ETJtC9e3dt
41VXVV5envG5+/7AAfxLzsNPy8vj9rp1GTlhAj169NDP3VWg4avUdS4jI4OzZ88C4OPjo0cg6i9R
WuNymwgjs7LojHWNyybgHXd3frKz0xqXq0DDVyml/uHemDePVydP5pNK7iVd3rdAt5K+BqPHjbNF
8f6WtMOVUkr9ha73exCvXrWKVydPZu8VBC9YbmG5NyeHV6dMYfWqVZcdv379+n/J6YEdO3Zk+fLl
V32+tqJHvko7Vih1hdzd3Y2Ldly4cMHqCmELFiygb9++FaZJTEykZs2aFBYWVri62bV2o5xfPn36
dI4cOXJDh21519cnQdlMXl4eMTExtGnUiGB/f+5u2JC7GzYk2N+fNo0aERMTQ35+/rUuplLXlezs
bLKyssjKyiI8PJzNmzcbzysL3uvdunXrqF9c/LuDFyxHwPWKi1m3bt3VLtY/g03voaSuC6tiYiTA
bJZ7PDxkXck9YUtvTZcP8m+Qu93dJcBsllUxMde6uEpdl8re7rCoqEhmz54ttWrVEl9fX+nVq5ec
PXtWRCreBvH8+fMyZMgQqVGjhgQHB8vkyZOtbpG4YMECufXWW8XDw0Pq1q0r3333nYiIHDhwQNq1
aydeXl5Sr1492bhxozFN3759pX///tKuXTtxd3eX1q1by8mTJ2X06NHi5eUlderUke+//94YPzw8
XF555RVxdXYWZ5AhIL+CdAAxg9xTci9pAfm8zO0sSx/hIDtBPgYJCwiQnj17ysCBA8XDw0Pq1asn
+/bts1pW6X20CwsL5cUXX5RatWqJh4eHNG7cWE6cOCEiIqNHj5bQ0FAxm83SuHFj2bNnj4iIfPrp
p+Lk5CSOjo7i7u4ujRo1EhHLPcAXLlwoIiLFxcUyc+ZMCQ8Pl+rVq8vAgQONe3yXbv+lS5dKWFiY
+Pn5Wd2+9Ouvv5bGjRuL2WyWgICASm89+lfQ8L0CJpPJuOF4ZerVqydffvllpcM+//xzCQkJuaJx
r8SIESNk5syZVzTuoEGDZPLkySIisnv3bqldu7a8PneuhLq4yL5yX6bKHvtAQl1d5fW5c/9wea+m
Bx54QJYtW3ati6GUiFiH72uvvSYtW7aUlJQUyc/Pl+HDhxv3Py4fvl27dpURI0ZITk6OnD59Wpo1
aybvv/++iIisWbNGgoODjfBKSEiQpKQkyc/Pl1q1asns2bOloKBAdu3aJR4eHjJ37lxp3bChOJhM
YgdSw8VFXB0cxNPdXfz8/GTx4sVSXFwskydPlrvuusuq7M2aNRNXBwdJAqkOcjvIfpCLIO1BZlwi
fCNKwjcfxNHOTpydneXTTz+V4uJimThxorRo0aLS7fTyyy/LbbfdJocPHxYRkR9++EHOnDkjIiIr
VqyQs2fPSlFRkcydO1cCAwON+2VPnz5doqOjrbZ/VFSUcR/nRYsWSWRkpBw7dkyys7Ole/fuxvil
23/YsGFy8eJFiYuLk2rVqsnBgwdFRKRFixayYsUKEbHcp/qrr7768x+OK/C3Dt/w8HBxcnKS9PR0
q9cbNWokJpNJkpKSrmg+ZcO3bKBdifLha0tlbyYvYjniDXVxkaQrCN7SR1JJAF/NI+CffvpJ7r33
XvHx8REvLy9p3LixbN269arNXylbKBsqt956q/G/iEhqaqo4OjpKUVGRVfj++uuvUq1aNcnNzTXG
XblypRGM9913n7zxxhsVlrV7924JDAw0nq+KiRFnBwep6eQk60CiQYaVqb0aCuJmZ2fUXv3www/i
5eVlVfb58+dLhLu7CEgPkJFlvvdvgnS9gvAVEE9HR2ndurUx7/j4eHFxcal0O91yyy1WR+yX4u3t
LT/88IOIiEybNk0GDBhgNbxs+LZv317effddY9ihQ4cqbP+UlBRjeLNmzWT16tUiItK2bVuZNm2a
pKWlXVG5rpa/dZuvyWSiZs2axMTEGK/9+OOP5Obm/mPudCIl/eny8vIYM3w463/HdYPBchP3T3Jy
GDN8eKVtwFLm1nFXqnPnztx///2cOnWK06dP88Ybb2A2m3/XPNTfS3JyMh4eHr/7s3Q1fPTRR9x/
//1/ah6JiYl069YNb29vvL29qVu3Lg4ODpw6dcpqvKSkJAoKCqhRo4Yx7ogRI0hLS2Pw4MF89913
1KpVq8L8U1NTjbtIvTFvHuOHDKFPYSH35OfTDcudrqqXjOsItACaFhezJTOT8UOHsiYmhuzsbGN+
Z86cYe/evcZzF6DsXaadgWwubT+We0sD+Pn5Ga+7urpy8eLFSnt3nzhxotL1A3j11VepW7cuXl5e
eHt7k5GRQXr6bzfa/PXXX6u8k9bJkycJDw83noeFhVFYWGi1/QMDA63KWLo9Fi1axOHDh7n11ltp
1qwZW7ZsucyaXx1/6/AFy428ly1bZjxfunQpAwcOtPqSR0VFsWjRIuP5kiVLKr336IIFC1i5ciUv
v/wyHh4ePPTQQwBERESwc+dOAHJzcxk8eDA+Pj7Uq1ePb775xmoeERER7Nq1C4DY2FiaNGmCp6cn
gYGBPP3008Z4e/fupVWrVnh7exMWFmasw+DBg5kyZQoAX3zxBSEhIcyePRt/f39uuukmVq5cWel2
mDVrFuezsoyOFRHAXKAh4AX0AfJKhp0HOmH5MvsA04HIwkKjY0VUVBSTJ0/mzjvvxM3Njblz59Kk
SROr5c2bN8+4tV5Z6enpJCYm8thjj+Hg4ICjoyOtWrXizjvvNMbZsGEDjRo1wtPTk8jISHbs2GEs
t+z79OGHH1K3bl18fHzo0KGD1X137ezseP/997nlllvw9vbmiSeesCrHBx98QN26dTGbzdSrV4/v
v/8esPzI9ejRg+rVq1OzZk2rWwBe6v36p4iIiMDV1RUPDw/jMXr06D8937CwMLKysq7JTnH//v2t
bkH4R4SFhbFt2zbOnTtnPHJycqhRo4YxTmJiIi1atKC4uJjCwkLjsXDhQn788UdMJhNms5mEhIQK
8w8KCuL48eOsiokxTgvKA8rf7HIJUPaXq/S0oIXz51v95vn6+jJw4EDS8vIoKHmtqt0eNyCnzPMi
IK3M85yioip7Oz/99NMkJyfTrVs3evbsSWhoaKXrt2fPHl555RXc3NzIy8ujsLCQ4uJiHnzwQR56
6KHLfi6CgoJITEw0nicnJ+Pg4EBAQECFce3s7MjNzTWeR0ZGsnLlStLS0pgwYQIPP/yw1fC/yt8+
fFu0aEFmZiYHDx6kqKiI1atXV7grTmX3P63MsGHD6N+/PxMmTCArK4sNGzZUmH7GjBkcO3aMo0eP
sn37dpYuXVrhPrWlxowZw9ixY8nIyODo0aP06tULsOwdd+zYkTFjxpCens7+/ftp2LBhpWU9deoU
Z86cITU1laVLlzJs2DB++eWXCmVfHxODe5kvnwlYC2wHjgE/YPniAhQDQ7HcMScZy15xQU4O78yZ
Y0y/YsUKFi5cSHZ2NqNHj+bYsWMcPHjQGL58+XIGDRpUoRy+vr5ERkbSv39/NmzYUOHIIDY2lkGD
BjF37lwyMjLYvXu3sUdbdt03bNjA7Nmz+eSTT0hPT6dNmzYVeptu2bKFffv28cMPP7BmzRrjB3bt
2rXMmDGD5cuXk5mZycaNG/H19aW4uJjOnTtz++23k5qays6dO3nttdeM8K/q/fonMZlMVj18s7Ky
eOONN651sf6woqKiqzKfESNGMGnSJGMHMC0tjY0bN1Y6bpcuXRg6dCipqalkZGRwxx13GOfB3n77
7bz66qt89913iAgJCQkkJyfTokULXFxceOyRR1ibm8tRLPd0Lr3G1KXqC8KAdy9epKioiPz8fIqK
iigoKGDjxo24Ozqy6TLrdgtwEdiK5UpXs/htRz0XqOHvX2n4bt++nY8++oigoCDWrFnDiBEjePTR
R5kyZQoJCQmICD/88ANnz54lOzsbBwcHnJyceP311xk/fjz29vZs3ryZDRs2EBgYyK+//lplGfv2
7cv8+fNJTEwkOzubSZMm0adPnys6tWvFihWkpVl2J0pPs7TFKWF/+/AFiI6OZtmyZfznP/+hbt26
Vd4c/Updqmps7dq1PP/883h5eRESEsKYMWOqHN/JyYlffvmF9PR0XF1dad68OQArV67k3nvvpXfv
3tjb2+Pj42OEb2XLnzlzJo6OjrRt25YHH3yQ1atXWw3PyMggITERl3LLHw0EAt5AZyzVSGA52u2G
perJHZgE/AJ8Fx9PRkYGJpOJwYMHc+utt2JnZ4eTkxO9evVixYoVAMTHx5OUlESnTp0qrLPJZOLz
zz8nIiKCp59+mqCgINq1a2fsDS9atIihQ4dy9913A5Y92tq1a1eYz3vvvcfEiROpXbs2dnZ2TJw4
kf3793P8+HFjnOeeew6z2UxoaCh33XUXcXFxACxcuJAJEybQuLHlkgK1atUiLCyMb775hvT0dCZP
noyDgwM33XQTjz76KKtKLiRQ1fulLJYsWULr1q0ZP348Pj4+1KxZk23bthnDjx07Rtu2bTGbzdx7
772MGjWK6OhooOKFKKKiopg6dSqtW7fGbDZz//33G+eiA3z11VdGzVCjRo348ssvjWEZGRkMHTqU
oKAgQkJCmDJlijHfJUuWcOeddzJu3Dj8/PyYPn16hZquS9WaFBcX8/TTT+Pv78+JEydYv349dnZ2
PPnkk3Tp0oX77rsPs9lMy5YtiY2NNaYru8O8dOlS8vPzjVqbnj17GsFy66238vzzz9OvXz9cXV25
7bbbqF+/PlFRUXTt2hWHggLuB4YD9YDWgB/wNXAGGAH8D3gCKK1UHgysKfnf1dWVsLAwUlNT2bNn
D0PGjOEdd3eOA+8BnkAkEI9lB30x0BLLDnkXwBfLb0Jp5W+2yUTT1q0rHLyYTCacnJxwcXHB3t4e
R0dH7r77bsaNG0evXr2477778PT05LHHHuPixYvcf//9dOjQga+//ppnn30WFxcXwsJ+ayDr2bMn
ACkpKUYtW15eHm+//TbVq1fnxRdf5Oabb6Zt27bUrFkTFxcXIiIiiIyM5LbbbkNEOHHiBG3btgXg
m2++YeTIkaxdu5alS5cSGBhItWrVeOCBB2jZsiUmk4mnnnqK4OBggoODGTt2rNHsVlrjOG/ePAIC
AggKCuKP+NuHr8lkIjo6mo8++qjSKuerrWzbDGD1ASqvqraGEydOULNmzStanre3Ny4uv8VqeHg4
J0+etBrnzJkzeDo6Vpg2sMz/LvzWxpOD5csdgeXL2A7IAHwdHY1rDJdvexk0aJBR5b18+XJ69+6N
YyXLBAgODubNN98kISGBpKQk3NzcGDhwIHDpNqGykpKSGDNmjNFu5uvrC1i+nMb6VdHGU9UykpKS
SE1NNebp7e3N7NmzOX36NHDt2oauN5f6/sTGxlKnTh3OnDnDs88+y9ChQ41h/fr1o0WLFpw9e5bp
06ezYsWKS9Y4xcTEsGTJEk6fPk1+fj6vvvoqYHmPO3XqxNSpUzl37hyvvvoqPXr0MMJ58ODBODk5
ceTIEb7//nt27NjBwoULrcpYq1YtTp8+zfPPP1/psquqNVmwYAHbtm0jLi6OtLQ0Dhw4YNTIjB07
loMHD5KZmUlCQgKzZs0CLFX1RUVFxtGUh4cH77zzDsePH+f8+fN89913VrUow4cPJyYmBrPZzO7d
u8nIyGD48OG88/bbvF9czBksO8atgCQgBVgEvAO8jyUsL4JRnQyWo9YXgZp+fqxbt45BgwbRu3dv
pk2bxvcifAuswPI9340lxHdgaQfeguUIdxeWKuf2wFEs1dEFWA4Wyjbtla7vrbfeytmzZ7nrrru4
6667AMuOzfPPP8/Ro0fJzMzk66+/JigoCDs7OxYtWkSbNm2YO3cu48eP5+jRo7Rv3x6wXNP8zTff
JDg4mH379lFcXExeXh7dunUzaqkOHjzIwoULOX36NA0aNGD9+vV8+umnZGVlERcXh7u7u1HD8Msv
v3Dx4kV69uzJ888/j52dHePGjSMnJ4etW7cya9YsYmNjiYuLIy4ujtjYWOP9BEuNY2ZmJqmpqVZN
Yb/H3z58wRKANWvW5NNPP6V79+4Vhru5uXHhwgXj+aWqNy5XPV2jRg2rtsey/5dXWVtDTk4OoaGh
HDly5Irv25tZAAAgAElEQVTKUNq2VCopKclqT+yPtKHNBQ4DsVi+jF9SsVqr/HxbtGiBk5MTu3fv
JiYmxjiiuZyQkBBGjhzJTz/9BFBlm1B5YWFhLFiwwKqN7cKFC7Ro0eKy01a1jLCwMG666SareWZm
ZrJ582bg2rUNXU9EhK5du1rtoJT98QkPD2fo0KGYTCYGDhzIyZMnOX36NMnJyezbt48XXngBBwcH
7rzzTrp06VJlkJtMJh555BEiIyNxdnamV69e7N9vqZtZsWIFHTt2pEOHDgDcc889NGnShC1btnDq
1Ck+/fRT5s+fj4uLC/7+/jz11FNG7QVYalNGjRqFnZ0dzs7OlS6/qlqTNWvW8NRTTxEUFISXlxcT
J0783Tvzfn5+Vtvv0KFDVusNlpAfPnw4TZs2xWQy8dBDD5Gfn48/lu/lSeAVLDvN1bAEMVRe/WwC
ugLjgdSzZ6lTp44xrFq1atzeogU4OHBz6fYBSuuaOgI3lfzfFrgP2IOlOWpKtWp4eXtXWuVcUFDA
/fffz1tvvUV6ejqPPvqosZ1at25d5Y6riDB69Gir7TNt2rQK412ulmrhwoXG0TBAgwYN8PHxqXSZ
YNkpmDFjBo6Ojjg7O7Ny5UqmTp2Kn58ffn5+TJs2zerqWo6OjkydOhV7e3seeOCBKud7Kf+I8AXL
UcuuXbusjhJLNWrUiHXr1pGbm0tCQsIl92QCAgI4evRolcN79erF7NmzOX/+PCdOnLDqsFNe+bYG
k8mEvb09/fr147PPPmPt2rUUFhZy5swZ48tfWe/iadOmUVBQwJ49e9iyZYtRRVM6rq+vLxkFBVyp
bCxfak/gLDCj5PX0/HzjA1zZD050dDRPPPEETk5OtGrVqsJwgPPnzzNt2jSOHDlCcXEx6enpfPjh
h7Rs2RKAoUOHsnjxYnbt2kVxcTEpKSlWP06lRowYwUsvvcSBAwcAS1Xj2rVrq1ynstvt0UcfrbRd
rVmzZnh4ePDyyy+Tm5tLUVERP/30E/v27QMqf7+ut8sF/tVMJhMbNmyw2kEpe3RbvrYBLFeFSk1N
xcfHxyrsquq5Wtm8XFxcjJqLpKQk1q5da/UD/d///pdff/2V5OTkKnsTX+lyK1uP0mWfPHnSavqQ
kJDLzqu8M2fOWG2/yppVkpKSmDt3rrEOpTVop4HjQDi/78c7FEsvaD8nJ6P2qlS1atXo0KULrV1c
+LbcdJ9i6Tnti6V5aivwE9Da1ZXeQ4YY73F5u3btoqCggOjoaNauXcuRI0d49NFHyczM5NChQ7Ru
3brS6UwmE2+++abV9pkxY0aF8S5XS3WlNWil/Mu1W6emplboPZ2ammo89/X1/dPf/X/ML0fNmjW5
447fLqJW9sht7NixODk5ERAQwCOPPMKAAQOq7CQ1dOhQDhw4gLe3d6VH0dOmTSM8PJybbrqJDh06
MHDgwCqPPrdv3079+vXx8PBg7NixrFq1imrVqhEWFsbWrVuZO3cuvr6+3H777fzwww9GWcrOLzAw
EG9vb4KCgoiOjjbaqsqO6+npSWREBBcvsX1MJQ+Ap7BUM/lh2aN+oGTYHfXqGR0SKlun6Oho4uPj
K3RoK8vJyYmkpCTuuecePD09ue2223BxcWHJkiUANG3alMWLFzN27Fi8vLyIioqqtPaga9euTJgw
gT59+hjzKdtjtbI2qNLXHn74YaNdzWw20717d86dO4ednR2bN29m//791KxZE39/f4YNG0ZmZiZQ
9fulLq9GjRqcPXvWqqbgUrVClxIWFkZ0dLTVD3RWVhbPPvssISEhVKtWzSrgMjIy+PHHH43p/0yP
6ho1alj1Kyj7/9UUFhbG888/b6zD999/T7i7O72xBGkylirg8v7ImoWGhhIaHs4rH37Ig2Yz97i7
sw64APQAnsVStb0QMDs4sNLJiVcWLaLHJTocFhYWUlCyw+/s7MymTZuIi4ujadOm9O3b909fPz40
NPSStVRXWoNWqvxnorLe03+0bbdKNjqfWP0Ffs8FPFauXCl3l5xQ/0ce7T08JOYyF9rIyckRDw8P
SUhIuBqrp65DERERxqUCy1u8eLHVxRZErC9Q06JFC3n22WclPz9f/u///k88PT0rXIWo9CpQUVFR
xqUDy8/7+PHjEhgYKNu3b5fCwkLJzc2Vzz//3LhM4UMPPSRjxoyRzMxMKSoqkoSEBOOqcpWVsfxr
5a9oV/bCOu+++67Uq1dPUlJS5Ny5c3LPPfeInZ2dUe5p06ZJVFRUpdundB0LCwsrHV52Ofv27ZPQ
0FD5+uuvpbi4WFJSUqSavb2cBSkCaQjyDMgFkFyQ/5Z8Tz8tuQBGfpnv7iCQySWvuTk6yvnz562W
FRsbK15eXrJz507Jzc2Vt99+WxrXqSOuDg4CSICzs7g6OEi9mjWlWrVqMmnSJBG59O9PRkaGBAUF
ydSpUyU3N1fOnz8vTz/9tJhMJnn22WcrnUak4vteVtnlFRYWyh133CFz5syRnJwcKSwslB9//FG+
+eYbERF55ZVXpEGDBvLLL79IcXGxxMXFGVfSCgwMlB07dlQ631KTJ0+WVq1aSVpamqSlpcmdd95p
XLDoal046R9z5PtP1717d36ys+O7PzDtt0C8yVTpkX5Z7777Ls2aNftd1T3qxtO5c2er83x79OgB
VH7KXtnnH330Ef/73//w9fVlypQp9O7d26qq71LTlp13SEgIGzZs4KWXXqJ69eqEhYUxd+5co0fz
smXLquxNXFUZq6rpKj/8scce47777qNBgwY0btyYBx98EHt7e6MK8vjx41VWqZby8vKy2n6vvfZa
heU0btyYDz74gCeeeAIfHx+aNGmCh7s7W7FUV24CErCcRhTKb72Z78bSCzqQ3y66UVqrtZHfaq/K
LqtsbVP16tWZP38+s994g9T0dGbMmEGRuzuObm7cceeddO/e3biLU2XbqpTZbGbHjh189dVXBAUF
ERkZyfnz54mNjWXx4sWXbNp74oknrLZP06ZNKyyv9DSkqmqpqupVDZY7JA0aNAhvb28+/vjjSj8T
kydPpkmTJjRo0IAGDRrQpEkTJk+efNn1/l3+dHyra+bzzz+X0NDQKx7/r7y8ZHh4uERERMj+/fv/
7Gqpf4hevXrJ9OnTr3Ux/pStW7dKeHi48bxRo0bGDRWuNlvUXinb0fD9h7mRb6ygbmzffPONJCQk
SFFRkWzdulWcnZ1vuJ213Nxc2bJlixQUFMiJEyekefPmMnbsWJss++LFixJgNsu3fyB494EEmM3G
jQrUtafh+w9UekvBu93d5d9UvKXgxyV7yXpLQXU1bdq0SUJDQ8XV1VVq164tS5YsudZF+t1ycnKk
adOm4uHhIdWrV5chQ4ZIVlaWzZZ/vdwcRf15JpFrcCVzdc3l5+ezbt063pkzh+/i4/EraXtLz8/n
jnr1GDlhAt27d6/ymq1KqWvjjXnzeHXyZD7JzaXxZcb9Fujm6sozM2cyetw4WxRPXSENX0VGRoZx
7p+Pj8+fPg1AKfXXWr1qFWOGD6d+cTEjs7PpAjiUDCvA0rnqHQ8P4k0mXn//fXr36VP1zNQ1oeGr
lFI3IK29urFp+Cql1A1Oa69uPBq+SimllI3pRTaUUkopG9PwVUoppWxMw1cppZSyMQ1fpZRSysY0
fJVSSikb0/BVSimlbEzDVymllLIxDV+llFLKxjR8lVJKKRvT8FVKKaVsTMNXKaWUsjENX6WUUsrG
NHyVUkopG9PwVUoppWxMw1cppZSyMQ1fpZRSysY0fJVSSikb0/BVSimlbEzDVymllLIxDV+llFLK
xjR8lVJKKRvT8FVKKaVsTMNXKaWUsjENX6WUUsrGNHyVUkopG9PwVUoppWxMw1cppZSyMQ1fpZRS
ysY0fJVSSikb0/BVSimlbEzDVymllLIxDV+llFLKxjR8lVJKKRvT8FVKKaVsTMNXKaWUsjENX6WU
UsrGNHyVUkopG9PwVUoppWxMw1cppZSyMQ1fpZRSysY0fJVSSikb0/BVSimlbEzDVymllLIxDV+l
lFLKxjR8lVJKKRvT8FVKKaVsTMNXKaWUsjENX6WUUsrGNHyVUkopG9PwVUoppWxMw1cppZSyMQ1f
pZRSysY0fJVSSikb0/BVSimlbEzDVymllLIxDV+llFLKxjR8lVJKKRvT8FVKKaVsTMNXKaWUsjEN
X6WUUsrGNHyVUkopG9PwVUoppWxMw1cppZSyMQ1fpZRSysY0fJVSSikb0/BVSimlbEzDVymllLIx
DV+llFLKxjR8lVJKKRvT8FVKKaVsTMNXKaWUsjENX6WUUsrGNHyVUkopG9PwVUoppWxMw1cppZSy
MQ1fpZRSysY0fJVSSikb0/BVSimlbEzDVymllLIxDV+llFLKxjR8lVJKKRvT8FVKKaVsTMNXKaWU
sjENX6WUUsrGHK51AZRSSv01MjIyOHPmDAC+vr54enpe4xKpUnrkq5RSfyN5eXnExMTQplEjgv39
ubthQ+5u2JBgf3/aNGpETEwM+fn517qY/3gmEZFrXQillFJ/3upVqxgzfDi3iTAyK4vO/Fa9WQBs
At5xd+cnOztef/99evfpc+0K+w+n4auUUn8Db8ybx6uTJ/NJbi6NLzPut0A3V1eemTmT0ePG2aJ4
qhytdv4by8jI4OjRoxw9epSMjIxrXRylbCoqKopFixZd1Xk+/vjjzJo166rO82pYvWoVr06ezN6S
4I0Adl5i/CnAuJwcXp0yhdWrVlkNS0xMxM7OjuLiYgA6duzI8uXL/3DZZs+ezWOPPXZF406fPp3o
6GgAkpOT8fDw4G97fCjqb+XixYuycuVKad2wobg5OkqEu7tEuLuLm6OjtG7YUFauXCl5eXnXuphK
XRXh4eHi4uIi7u7uEhAQIIMHD5bs7GwREYmKipJFixZd4xL+Pu3atROTySRxcXFWr3ft2lVMJpN8
+eWXFaa5ePGiBJjN8i2IlDwiQHaW/D8NZECZYWUf+0ACzGar34Rjx46JyWSSoqKiv3x9y5s+fboM
GDDA5su9FvTI929k9apVhFevzofDhzMuLo7zBQUcy87mWHY25woKGBsXx6Jhwwjz96+wt6vUjchk
MrF582aysrL47rvv2Ldv33V5ZHqlTCYTtWvXZtmyZcZrZ86c4X//+x/Vq1evdJp169ZRv7iYO/7A
8hoD9YqLWbdu3R8r8FUmNjrKLT2qv5Y0fP8m3pg3j/FDhrAlM5P/ZGXRDevzyByB7sBn2dlsycxk
/NChvDFv3rUprFJ/gaCgIDp06EB8fLzxWmJiIq1bt8ZsNnP//fcbp908+OCDvPXWW1bTN2jQgA0b
NgAwduxYAgIC8PT0pEGDBhw4cACAwYMHM2XKFGOaDRs20KhRIzw9PYmMjGT79u0ALFmyhFq1amE2
m6lZsyYrV6684vXo168fq1evNoIoJiaG7t274+joaIxTthzvzJlD2+xsQiuZ1zZgNrAa8ABuL3k9
CiitkB+enc0zo0fj7+9PrVq12LJli9U8ylbfJyQk0K5dO7y8vPD396dPmQ5b8fHx3Hvvvfj6+hIY
GMjs2bMB66rk0irtDz74gODgYIKCgpg7d26l26F89XdUVBRTp06t9P0E6NmzJzVq1MDLy4t27doZ
71np9nr88cfp2LEj7u7uzJs3j8DAQKsQXrduHY0aNaq0LH8FDd+/gfLtPZfTGNhbRXvPtVb+x+1q
+D1tTurGUxpSx48f59NPP+X22283Xl+5ciVLlizh9OnT5Ofn8+qrrwKWz9mKFSuMecTFxZGamsqD
Dz7I9u3b2bNnD7/88gsZGRmsXbsWHx8fwHJkajKZAIiNjWXQoEHMnTuXjIwMdu/eTUREBBcuXGDM
mDFs27aNzMxM/ve///2uH/WgoCDq1q1rBPny5csZOHCg1Til5cjIyOD7Awe4s4p5dQAmAX2ALOD7
0ulLHgBpQGpaGrt372bfvn18/PHHxjqWX+cpU6bQoUMHzp8/T0pKCqNHjwYgKyuLe+65h44dO3Ly
5EkSEhK4++67jenL++KLL0hISGDHjh3MmTOHnTsv1UL9m5iYmErfT7DsUCUkJJCWlsYdd9xB//79
K0w7ZcoUsrOzefLJJ/H19WXHjh3G8OXLlzNo0KArKsfVcEOGb1RUFD4+Pld8rtoXX3xBaGhl+4U3
vry8PB4dPJjc3FwaAu2Bi1cwXRjQISeHPn378t///veKl2dnZ8fRo0f/YGkvr+wX/WqZOHEiH3zw
wVWdp7o+iAhdu3bF29ubNm3aEBUVxaRJkwDLZ2nIkCFERkbi7OxMr1692L9/PwCdO3fm8OHDHDly
BLD88Pbp0wcHBwccHR3Jysri559/pri4mNq1axMYGFhh2YsWLWLo0KFGyAQFBVG7dm3A8j358ccf
yc3NJSAggLp16/6u9Ro4cCDLli3j4MGDnD9/nhYtWlS67mfOnMG/WjXsL7WNSh5V+Tfg7eSEs7Mz
3t7eTJo0qcrqXycnJxITE0lJScHJyYlWrVoBsHnzZoKCghg7dixOTk64u7vTrFkzo5zlTZs2DRcX
F+rXr88jjzxCTEzMJUpoYTKZeOSRRyp9P8GyQ+Xm5oajoyPTpk0jLi6OrKwsY3jXrl1p2bIlANWq
VWPgwIHGDtjZs2fZsWMH/fr1u2w5rpYbLnwTExOJjY2levXqbNy48arNt6io6KrN60pdjd7Ib775
Jjl5eXwBpAPTubI3VYDPAHc7O1544YXftcxLtcsUFhb+rnkp9WeYTCY2bNjAuXPnSExM5K233qJa
tWrG8LKh6eLiQnZ2NoDx4718+XJEhFWrVhlVo+3bt+eJJ55g1KhRBAQEMHz4cKsf8VInTpygVq1a
FV53c3Nj9erVvPfeewQFBdGpUycOHTr0u9ape/fu7Nq1i7fffrvCUe/VdhJwKLPDGxYWVuW4L7/8
MiJCs2bNqF+/PosXLwYstQ41a9a84mWWPRgKCwsjNTX1iqar6v0sKiriueeeIzIyEk9PT2666SYA
0tPTAcs2LX8A1r9/fzZt2kROTg5r1qyhbdu2BAQEXPE6/Fk3XPguW7aMe+65h+joaJYuXWo1bOvW
rdSrVw+z2UxISAjz5s0jJyeHBx54gNTUVDw8PDCbzZw8eZLp06fz8MMPEx0djaenJ0uXLiU1NZUu
Xbrg6+vLzTffzMKFC415T58+nV69ejFo0CDMZjP169fn22+/NYb//PPPREVF4e3tTf369dm0aZMx
bPDgwYwcOZKOHTvi4eFBnTp1aF6vHn4+PtxcqxZ1IiMJ9POjTaNG9OvXj+7du1ut1+jRo3nqqacq
3R6rFi3CCcuRrD3QFnC6gu24B8gEnikuZtfOnRQUFBjDyrfr9O3bF4C2bdsC0LBhQzw8PFi7di1f
fPEFISEhvPzyy9SoUYOhQ4eSn5/PU089RXBwMMHBwYwdO9aopSgdf/bs2fj7+3PTTTdVaA87e/Ys
nTp1wmw206JFC+NIe9SoUTzzzDNW43bp0oXXX38dgDlz5hASEoLZbKZOnTrs2rULsG5zAti7dy+t
WrXC29ubsLAw43NU/vNTVVuU+nsYNGgQH330EZ999hmurq40b97cGPbkk0+yb98+Dhw4wOHDh3nl
lVcqTB8aGkpCQkKl877vvvvYsWMHv/76K3Xq1PndzR4uLi488MADvPfee1af3VJubm7k5OTg6+tL
Wl4eJy4xr8vVIwUC5wsKjKr15OTkKscNCAhgwYIFpKSk8P777zNy5EiOHDlCWFhYlTVildVklV1G
cnIywcHBlynlpa1cuZKNGzeyc+dOMjIyOHbsGHDpA4WQkBBatGjBunXrWLFiRaXb+a90Q4Zv7969
6dWrF9u3b+f06dPGsKFDh7JgwQIyMzOJj4/nrrvuwtXVlW3bthEUFERWVhaZmZnUqFEDgI0bN9Kz
Z08yMjLo168fffr0ISwsjJMnT/Lxxx8zadIkPv/8c2P+mzZtom/fvmRkZNClSxeeeOIJAAoKCujc
uTMdOnQgLS2NN998k/79+3P48GFj2rVr19K2TRtcTSZOJyRw7MABFhYXUwhMEKFFYSFj4+I4vmED
6z/5hMUffghYjiRXr15daVtERkYGPyckUAN4GMj7HdtxKdANS3tQUVERq8q0/ZZv13nyyScB2L17
NwA//PADWVlZ9OzZE4BTp05x7tw5kpOTef/995k1axaxsbHExcURFxdHbGysVQ/UU6dOcebMGVJT
U1m6dCnDhg0ztlXpUcj06dM5d+4ckZGRPP/884BlJyYmJsb4QqWnp7Nz50769evHoUOHePvtt9m3
bx+ZmZns2LGDiIgIwPrLn5SURMeOHRkzZgzp6ens37/faCMs//lp377979ii6np0qR/fli1bYjKZ
eOaZZ6yOLvft28fXX39NQUEBrq6uODs7Y29vb8yvdJ5Dhw5l8eLF7Nq1i+LiYlJSUjh06BCnT59m
w4YNXLhwAUdHR9zc3IzpSzsRXSrgSr300kt8+eWXlR6JNmrUiK1bt1JcXEy9m2/mUnVXgUAiVVc9
3ww4ODmRnZ3NuXPn+Ne//lXlvNauXcuJE5ao9/LywmQyYW9vT6dOnTh58iSvv/46eXl5ZGVlERsb
C1T+HsyaNYvc3Fzi4+NZsmQJvXv3vsQa/Kaq9zM7O5tq1arh4+PDhQsXjKaHy003cOBA5syZw08/
/VThoOevdkOF7969e0lJSaFLly7cfPPN1K1b1+qoycnJifj4eDIzM/H09LTqeFGZVq1a0aVLFwDS
0tL4v//7P+bMmYOTkxMNGzbk0Ucftery36ZNGzp06IDJZGLAgAHExcUB8NVXX3HhwgWee+45HBwc
uOuuu+jUqZNVO8YtkZG8M3MmW7OyeKGoCH9gEJa90l7Afiy9kffk5NASePrxx3lj3jy2bduGv7+/
sS5lnTlzhmIRHgNuArryWwAPAN6qMIVFDvAx0BNLL2h3Bwerk+iratepip2dHTNmzMDR0RFnZ2dW
rlzJ1KlT8fPzw8/Pj2nTplU4SX/mzJk4OjrStm1bHnzwQdasWWMM6969O02aNMHe3p7+/fsb7TpN
mzbF09PT6JyxatUq7rrrLvz9/bG3tycvL4/4+HgKCgoICwszqsHKvv8rV67k3nvvpXfv3tjb2+Pj
40ODBg2M9a7s86NuXFV1HCo1cOBAfvzxRwYMGGC8lpmZybBhw/Dx8SEiIgI/Pz/Gjx9fYR5NmzZl
8eLFjB07Fi8vL6KiokhOTqa4uJj58+cTHByMr68ve/bs4d133wUs1bMRERFXdKRXo0aNKr970dHR
NGzYkIiICE5duABOTlUe4fYs+esLNKlkeIK7O1Ht29OwYUOaNGlCjx49qux3sW/fPlq0aIGHhwcP
PfQQb7zxBhEREbi7u/Of//yHTZs2UaNGDW655Ra++OKLCtusVLt27YiMjOSee+5h/Pjx3HPPPZWO
W366qt7PgQMHEh4eTnBwMPXr1zd2rCobt6zu3buTnJxMt27dcHZ2rnSd/zK2PKn4z3r00UelS5cu
xvNZs2ZJo0aNZMSIETJz5kz55ptv5KGHHhJvb29p166d/O9//xMRkc8//1xCQkKs5jVt2jTp37+/
8fyrr74Sf39/q3Heffdduffee43xy578XfZE9FWrVknTpk2tpn3uuedk2LBhImI5cd7s4CBJJSe2
fwASVeZE95tB7Ms8jwFpARLq6iotW7aUf/3rXyIiYjKZ5MiRI8Yy/vOf/4gJpBCkGKQPSAeQCyC1
QA5UcWL9ChDfkukEJMDZWZycnCQtLU1ERH799Vd57LHHJCgoSOrVqycffvihsczyZfj8888lODhY
RETq1asnX375pbi4uMiBAweMcX7++WdxcnIyxvfx8bE6iX/8+PEycuRIEREZPHiwtGnTxtjW5d+7
2bNny6BBg0REpHnz5rJq1Spj2MqVK6V169bi7e0tffr0kdTU1Arv3eOPPy7PPPOMVKaqz4/6+1q2
bJm0adPGZsubNWuWLFiw4KrOs7KLbFzpo7KLbPyVruUFPKoSGRkpO3futPlyb5jwzcnJEbPZLO7u
7hIYGCiBgYHi7e1d6dVgCgsLZf78+RIaGioiIl988UWF8C1/JZXk5GSxt7eXrKws47WJEyfKI488
Iu3atRMHBwdxcHAQPz8/6d69u8TGxhofot27d0tgYKAUFxcb0/bt21dmzJghFy9eFGdHRxla8mEf
BPJgufD9BcShzPMcEG+QVSAmMMKusuCjJGwFpACkI8gtIJ0v8YW7F8QJJLDkQcnDzc1NHn74Yavt
tHfvXnF2drYqQ/PmzcXZ2Vnc3d3FxcVFTCaTfPXVV8Y0tWrVkq1btxrPt2/fLhEREUaZ7e3trb6A
vXr1klmzZomIJXzbtm1bZfgeP35cvLy8ZP/+/eLp6SkXL16s8FnJzMyUvn37SnR0tIhYh+/s2bOl
W7duFaYpq/znR/09XbhwQZo3by7Lly+/1kX501bFxEioi4uxg38lj6SSHfxVMTE2K+f1Fr7//ve/
5eabb74my75hqp3Xr1+Pg4MDP//8s9GW+PPPP9OmTRuWLVtGQUEBH330ERkZGdjb2+Ph4WG0swQE
BHDmzBkyMzON+Um5qujQ0FBatWrFxIkTycvL44cffuDDDz9kwIABmEwmOnbsSJ8+fTh8+DDnz59n
5syZxrTNmzfH1dWVl19+mYKCAr744gs2b95Mnz59WLduHd4i1ACutD+1C9ADeBHwsrcnNjbWKO/6
9esZNWoUjRs3pmPHjjiYTDyEpfNUPnAv8AvgVsW8U4BdwBYgDugLODo4MGrUKG655RZGjBhRabuO
nZ2dsS0vXrzI22+/TVZWFlu3biU4ONiqs0rfvn2ZNWsW6enppKen88ILL1TozCAiFBQUsGfPHrZs
2WK0H5d/X8oLCQmhSZMmDBw4kIcfftjo2Xr48GF27dpFXl4e1apVs2qnK6tfv3589tlnrF27lsLC
QgKopFQAABWGSURBVM6cOUNcXNwlPz/q72f79u1Ur16dGjVq2PT0kr9K7z59eGbWLFq7uPDt5Ufn
W6B1yY0VbH1no6t9KuEfFRUVxciRI3n77bevTQGuSeRXoWPHjvLmm29avXbbbbfJ+vXrpUOHDtK4
cWOpXr26mM1mue222yQ+Pl7WrFkjLi4uMnHiROnQoYN4e3uLi4uLuLq6ipubm9SqVUu2bdsmQ4YM
ETc3N7GzsxN3d3fx8vKS1q1bWy3rxIkT0qlTJ/Hx8ZFatWrJ+++/LyKWa8R26dLFOJJ66623pHbt
2mJnZyc9evSQwMBA8fDwEE9PT3F3d5d69erJ+vXrZdCgQRLo6ys+II4gC0r+OpRUM3cp2QMNLlPt
XAjyYslrgPiDBLq7i5+fnwDywAMP/H979x4dZX3ncfw95EJuM8kkASRcEkuwArpGEIEqFvWArQgI
RQksWETlWjcURXddEBWxslUOKqUgxSoIAS9YESywcMgGtMoqrUA4yK0hQEgbYEiIIZmE+e4fE8ZE
QIKLDwE/r3NyzDyX3/yeJyEff5f5Pfbiiy/a+vXrLSsry7xerzUCiwJLALuH4JqusTXbEsG613RL
G9hvwG6o9X+/10dHW5MmTaygoMAiIyNt27Zt9thjj1mLFi0sLi7O2rRpY/PmzQvdozlz5lhkZKRF
R0fb22+/bTk5OaEWYmpqqq1du9YqKirs4YcfNrfbbWFhYRYVFWUDBw60o0eP2vr16+2KK64wl8tl
SUlJlpqaajNmzLBbbrnF3G63paSkWOfOnUMt1dWrV1tMTIwlJSVZQkKCde7c2WbNmmUul8tycnJC
9dqyZYvdeOON5na7LTEx0fr06WOHDh0ys2Avx6mfnZnZhg0brEuXLubxeKxVq1a2YMEC8/v9od8f
j8djN954o3300UcX6ldbxBFLsrOtmcdjt8fF2bs1vWGn/q37wd4Bu83ttmYej6MtXjldgwrft956
y7p06RJ6/be//c2SkpKsqqrKVq1aZZ06dbKSkhIzM9uxY0foj+vw4cNt8uTJZmb26aefWnx8vK1d
u9bMzA4ePGg7duywsrIy83g8tnPnTjMLjmvm5eXVq149evSwP/zhD2ZmVlxcbLfeeqvdd999Zmb2
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
AABJRU5ErkJggg==
"
>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="Making-a-two-mode-network">Making a two-mode network<a class="anchor-link" href="#Making-a-two-mode-network">&#182;</a></h1><p>If you wish to study the relationships between 2 tags you can use the <a href="{{ site.baseurl }}/docs/RecordCollection#twoModeNetwork"><code>twoModeNetwork()</code></a> function which creates a two mode network showing the connections between the tags. For example to look at the connections between titles(<code>'TI'</code>) and subjects (<code>'WC'</code>)</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[30]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span class="n">ti_wc</span> <span class="o">=</span> <span class="n">RC</span><span class="o">.</span><span class="n">twoModeNetwork</span><span class="p">(</span><span class="s">&#39;WC&#39;</span><span class="p">,</span> <span class="s">&#39;TI&#39;</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">mk</span><span class="o">.</span><span class="n">graphStats</span><span class="p">(</span><span class="n">ti_wc</span><span class="p">))</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt"></div>
<div class="output_subarea output_stream output_stdout output_text">
<pre>The graph has 40 nodes, 35 edges, 0 isolates, 0 self loops, a density of 0.0448718 and a transitivity of 0
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>The network is directed by default with the first tag going to the second.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[31]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span class="n">mkv</span><span class="o">.</span><span class="n">quickVisual</span><span class="p">(</span><span class="n">ti_wc</span><span class="p">,</span> <span class="n">showLabel</span> <span class="o">=</span> <span class="k">False</span><span class="p">)</span> <span class="c">#default is False as there are usually lots of labels</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt"></div>
<div class="output_subarea output_stream output_stderr output_text">
<pre>/usr/local/lib/python3.4/site-packages/matplotlib/axes/_axes.py:475: UserWarning: No labelled objects found. Use label=&apos;...&apos; kwarg on individual plots.
  warnings.warn(&quot;No labelled objects found. &quot;
</pre>
</div>
</div>

<div class="output_area"><div class="prompt"></div>


<div class="output_png output_subarea ">
<img src="data:image/png;base64,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
"
>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p><a href="{{ site.baseurl }}/docs/visual#quickVisual"><code>quickVisual()</code></a> makes a graph with the different types of nodes coloured differently and a couple other small visual tweaks.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="Making-a-multi-mode-network">Making a multi-mode network<a class="anchor-link" href="#Making-a-multi-mode-network">&#182;</a></h1><p>For any number of tags the <a href="{{ site.baseurl }}/docs/RecordCollection#nModeNetwork"><code>nModeNetwork()</code></a> function will do the same thing as the <code>oneModeNetwork()</code> but with any number of tags and it will keep track of their types. So to look at the co-occurence of titles <code>'TI'</code>, WOS number <code>'UT'</code> and authors <code>'AU'</code>.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[32]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span class="n">tags</span> <span class="o">=</span> <span class="p">[</span><span class="s">&#39;TI&#39;</span><span class="p">,</span> <span class="s">&#39;UT&#39;</span><span class="p">,</span> <span class="s">&#39;AU&#39;</span><span class="p">]</span>
<span class="n">multiModeNet</span> <span class="o">=</span> <span class="n">RC</span><span class="o">.</span><span class="n">nModeNetwork</span><span class="p">(</span><span class="n">tags</span><span class="p">)</span>
<span class="n">mk</span><span class="o">.</span><span class="n">graphStats</span><span class="p">(</span><span class="n">multiModeNet</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt output_prompt">Out[32]:</div>


<div class="output_text output_subarea output_execute_result">
<pre>&apos;The graph has 108 nodes, 163 edges, 0 isolates, 0 self loops, a density of 0.0282105 and a transitivity of 0.443946&apos;</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[33]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span class="n">mkv</span><span class="o">.</span><span class="n">quickVisual</span><span class="p">(</span><span class="n">multiModeNet</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt"></div>
<div class="output_subarea output_stream output_stderr output_text">
<pre>/usr/local/lib/python3.4/site-packages/matplotlib/axes/_axes.py:475: UserWarning: No labelled objects found. Use label=&apos;...&apos; kwarg on individual plots.
  warnings.warn(&quot;No labelled objects found. &quot;
</pre>
</div>
</div>

<div class="output_area"><div class="prompt"></div>


<div class="output_png output_subarea ">
<img src="data:image/png;base64,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
"
>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="Post-processing-graphs">Post processing graphs<a class="anchor-link" href="#Post-processing-graphs">&#182;</a></h1><p>If you wish to apply a well known algorithm or process to a graph <a href="https://networkx.github.io/documentation/networkx-1.9.1/">networkx</a> is a good place to look.</p>
<p>One of the features it lacks is pruning of graphs, metaknowledge has these capabilities. To remove edges outside of some weight range, use <a href="{{ site.baseurl }}/docs/metaknowledge#drop_edges"><code>drop_edges()</code></a>. For example if you wish to remove the self loops, edges with weight less than 2 and weight higher than 10 from <code>coCiteJournals</code>.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[34]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span class="n">minWeight</span> <span class="o">=</span> <span class="mi">3</span>
<span class="n">maxWeight</span> <span class="o">=</span> <span class="mi">10</span>
<span class="n">proccessedCoCiteJournals</span> <span class="o">=</span> <span class="n">mk</span><span class="o">.</span><span class="n">drop_edges</span><span class="p">(</span><span class="n">coCiteJournals</span><span class="p">,</span> <span class="n">minWeight</span><span class="p">,</span> <span class="n">maxWeight</span><span class="p">,</span> <span class="n">dropSelfLoops</span> <span class="o">=</span> <span class="k">True</span><span class="p">)</span>
<span class="n">mk</span><span class="o">.</span><span class="n">graphStats</span><span class="p">(</span><span class="n">proccessedCoCiteJournals</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt output_prompt">Out[34]:</div>


<div class="output_text output_subarea output_execute_result">
<pre>&apos;The graph has 89 nodes, 466 edges, 1 isolates, 0 self loops, a density of 0.118999 and a transitivity of 0.213403&apos;</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>Then to remove all the isolates, i.e. nodes with degree less than 1, use <a href="{{ site.baseurl }}/docs/metaknowledge#drop_nodesByDegree"><code>drop_nodesByDegree()</code></a> .</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[35]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span class="n">proccessedCoCiteJournals</span> <span class="o">=</span> <span class="n">mk</span><span class="o">.</span><span class="n">drop_nodesByDegree</span><span class="p">(</span><span class="n">proccessedCoCiteJournals</span><span class="p">,</span> <span class="mi">1</span><span class="p">)</span>
<span class="n">mk</span><span class="o">.</span><span class="n">graphStats</span><span class="p">(</span><span class="n">proccessedCoCiteJournals</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt output_prompt">Out[35]:</div>


<div class="output_text output_subarea output_execute_result">
<pre>&apos;The graph has 88 nodes, 466 edges, 0 isolates, 0 self loops, a density of 0.121735 and a transitivity of 0.213403&apos;</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>Now before the processing the graph can be seen <a href="#Making-a-co-citation-network">here</a> now it looks like</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[36]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span class="n">nx</span><span class="o">.</span><span class="n">draw_spring</span><span class="p">(</span><span class="n">proccessedCoCiteJournals</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt"></div>


<div class="output_png output_subarea ">
<img src="data:image/png;base64,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
"
>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>It looks a bit thinner, using a visualizer will make the difference even more noticeable.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="Exporting-graphs">Exporting graphs<a class="anchor-link" href="#Exporting-graphs">&#182;</a></h1>
</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>Now you have a graph the last step is to write it to disk. networkx has a few ways of doing this, but they tend to be slow. metaknowledge can write an edge list and node attribute file that contain all the information of the graph. The function to do this is called <a href="{{ site.baseurl }}/docs/metaknowledge#write_graph"><code>write_graph()</code></a>. You give it the start of the file name and it makes two labeled files containing the graph.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[37]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span class="n">mk</span><span class="o">.</span><span class="n">write_graph</span><span class="p">(</span><span class="n">proccessedCoCiteJournals</span><span class="p">,</span> <span class="s">&quot;FinalJournalCoCites&quot;</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>These files are simple CSVs an can be read easily by most systems. If you want to read them back into Python the <a href="{{ site.baseurl }}/docs/metaknowledge#read_graph"><code>read_graph()</code></a> function will do that.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[38]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre> <span class="n">FinalJournalCoCites</span> <span class="o">=</span> <span class="n">mk</span><span class="o">.</span><span class="n">read_graph</span><span class="p">(</span><span class="s">&quot;FinalJournalCoCites_edgeList.csv&quot;</span><span class="p">,</span> <span class="s">&quot;FinalJournalCoCites_nodeAttributes.csv&quot;</span><span class="p">)</span>
<span class="n">mk</span><span class="o">.</span><span class="n">graphStats</span><span class="p">(</span><span class="n">FinalJournalCoCites</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt output_prompt">Out[38]:</div>


<div class="output_text output_subarea output_execute_result">
<pre>&apos;The graph has 88 nodes, 466 edges, 0 isolates, 0 self loops, a density of 0.121735 and a transitivity of 0.213403&apos;</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>This is full example workflow for metaknowledge, the package is flexible and you hopefully will be able to customize it to do what you want (I assume you do not want the Records staring with 'A').</p>

</div>
</div>
</div>
{% include docsFooter.md %}
