---
layout: page
title: Examples
excerpt: "Examples showing how to use metaknowledge to analyze data."
search_omit: true
---

<ul class="post-list">

  <li><article>
  <a href="{{ site.baseurl }}/examples/#Context">Context</a>
  </article></li>
  <li><article>
  <a href="{{ site.baseurl }}/examples/#Importing">Importing</a>
  </article></li>
  <li><article>
  <a href="{{ site.baseurl }}/examples/#Reading-Files">Reading Files</a>
  </article></li>
  <li><article>
  <a href="{{ site.baseurl }}/examples/#Record-object">Record object</a>
  </article></li>
  <li><article>
  <a href="{{ site.baseurl }}/examples/#RecordCollection-object">RecordCollection object</a>
  </article></li>
  <li><article>
  <a href="{{ site.baseurl }}/examples/#Citation-object">Citation object</a>
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
<h1 id="Context">Context<a class="anchor-link" href="#Context">&#182;</a></h1>
</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>{% comment %}</p>
<h1 id="Notes-for-those-who-downloaded-the-notebook">Notes for those who downloaded the notebook<a class="anchor-link" href="#Notes-for-those-who-downloaded-the-notebook">&#182;</a></h1><p>The notebook should just work as long as you put the sample file (<code>savedrecs.txt</code>) in the same directory as this file.</p>
<p>The one issue you will have is that the urls will not work. To make them work you will need to replace <code>{{ site.baseurl }}</code> with <code>http://networkslab.org/metaknowledge</code>, sorry about that.</p>
<p>{% endcomment %}</p>
<p><em>metaknowledge</em> is a python library for creating and analyzing scientific metadata. It uses records obtained from Web of Science (WOS) and mostly produces graphs. As it is intended to be usable by those who do not know much python. This page will be a short overview of its capabilities, to allow you to use it for your own work. For complete coverage of the package as well as install instructions read the full the documentation <a href="{{ site.baseurl }}/documentation">here</a>.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>This document was made from a <a href="https://jupyter.org">jupyter</a> notebook, if you know how to use them, you can download the notebook <a href="{{ site.baseurl }}/examples/metaknowledgeExamples.ipynb">here</a> and the sample file is <a href="{{ site.baseurl }}/examples/savedrecs.txt">here</a> if you wish to have an interactive version of this page. Now lets begin.</p>
<h1 id="Importing">Importing<a class="anchor-link" href="#Importing">&#182;</a></h1>
</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>First you need to import the <em>metaknowledge</em> package</p>

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
<p>And you will often need the <a href="https://networkx.github.io/documentation/networkx-1.9.1/"><em>networkx</em></a> package</p>

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
<p>I am using <a href="http://matplotlib.org/"><em>matplotlib</em></a> to display the graphs and to make them look nice when displayed</p>

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
<p><em>metaknowledge</em> also has a <em>matplotlib</em> based graph <a href="{{ site.baseurl }}/docs/visual#visual">visualizer</a></p>

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
<p><a href="http://pandas.pydata.org/"><em>pandas</em></a> is also used in one example</p>

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
<h1 id="Reading-Files">Reading Files<a class="anchor-link" href="#Reading-Files">&#182;</a></h1><p>The files from the Web of Science (WOS) can be loaded into a <a href="{{ site.baseurl }}/docs/RecordCollection#RecordCollection"><code>RecordCollections</code></a> by creating a <code>RecordCollection</code> with the path to the files given to it as a string.</p>

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
<p>You can also read a whole directory, in this case it is reading the current working directory</p>

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
<p><em>metaknowledge</em> can detect if a file is a valid WOS file or not and will read the entire directory and load only those that have the right header. You can also tell it to only read a certain type of file, by using the extension argument.</p>

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
<p>Now you have a <code>RecordCollection</code> composed of all the WOS records in the selected file(s).</p>

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
<p>You might have noticed I used two different ways to display the <code>RecordCollection</code>. <code>repr(RC)</code> will give you where <em>metaknowledge</em> thinks the collection came from. While <code>str(RC)</code> will give you a nice string containing the number of <code>Records</code>.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="Record-object"><code>Record</code> object<a class="anchor-link" href="#Record-object">&#182;</a></h1>
</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p><a href="{{ site.baseurl }}/docs/Record#Record"><code>Record</code></a> is an object that contains a simple WOS record, for example a journal article, book, or conference proceedings. They are what <a href="{{ site.baseurl }}/docs/RecordCollection#RecordCollection"><code>RecordCollections</code></a> contain. To see an individual <a href="{{ site.baseurl }}/docs/Record#Record"><code>Record</code></a> at random from a <code>RecordCollection</code> you can use <code>peak()</code></p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[10]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span class="n">R</span> <span class="o">=</span> <span class="n">RC</span><span class="o">.</span><span class="n">peak</span><span class="p">()</span>
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
<p>A single <code>Record</code> can give you all the information it contains about its record. If for example you want its authors.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[11]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span class="nb">print</span><span class="p">(</span><span class="n">R</span><span class="o">.</span><span class="n">authorsFull</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">R</span><span class="o">.</span><span class="n">AF</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt"></div>
<div class="output_subarea output_stream output_stdout output_text">
<pre>[&apos;ROOSEN, G&apos;, &apos;IMBERT, C&apos;]
[&apos;ROOSEN, G&apos;, &apos;IMBERT, C&apos;]
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
<p>Converting a <code>Record</code> to a string will give its title</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[12]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span class="nb">print</span><span class="p">(</span><span class="n">R</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt"></div>
<div class="output_subarea output_stream output_stdout output_text">
<pre>CALCULATION AND MEASUREMENT OF FORCES AND TORQUES APPLIED TO UNIAXIAL CRYSTAL BY EXTRAORDINARY WAVE
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
<p>If you try to access a tag the <code>Record</code> does not have it will return <code>None</code></p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[13]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span class="nb">print</span><span class="p">(</span><span class="n">R</span><span class="o">.</span><span class="n">GP</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt"></div>
<div class="output_subarea output_stream output_stdout output_text">
<pre>None
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
<p>There are two ways of getting each tag, one is using the WOS 2 letter abbreviation and the second is to use the human readable name. There is no standard for the human readable names, so they are specific to <em>metaknowledge</em>. To see how the WOS names map to the long names look at <a href="{{ site.baseurl }}/docs/tagFuncs#tagFuncs">tagFuncs</a>. If you want all the tags a <code>Record</code> has use <a href="({{ site.baseurl }}/docs/Record#activeTags"><code>activeTags()</code></a>.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[14]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span class="nb">print</span><span class="p">(</span><span class="n">R</span><span class="o">.</span><span class="n">activeTags</span><span class="p">())</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt"></div>
<div class="output_subarea output_stream output_stdout output_text">
<pre>[&apos;PT&apos;, &apos;AU&apos;, &apos;AF&apos;, &apos;TI&apos;, &apos;SO&apos;, &apos;LA&apos;, &apos;DT&apos;, &apos;C1&apos;, &apos;CR&apos;, &apos;NR&apos;, &apos;TC&apos;, &apos;Z9&apos;, &apos;PU&apos;, &apos;PI&apos;, &apos;PA&apos;, &apos;SN&apos;, &apos;J9&apos;, &apos;JI&apos;, &apos;PY&apos;, &apos;VL&apos;, &apos;IS&apos;, &apos;BP&apos;, &apos;EP&apos;, &apos;PG&apos;, &apos;WC&apos;, &apos;SC&apos;, &apos;GA&apos;, &apos;UT&apos;]
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
<h1 id="RecordCollection-object"><code>RecordCollection</code> object<a class="anchor-link" href="#RecordCollection-object">&#182;</a></h1>
</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p><a href="{{ site.baseurl }}/docs/RecordCollection#RecordCollection"><code>RecordCollection</code></a> is the object that <em>metaknowledge</em> uses the most. It is your interface with the data you want.</p>
<p>To iterate over all of the <code>Records</code> you can use a for loop</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[15]:</div>
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
<pre>CALCULATION AND MEASUREMENT OF FORCES AND TORQUES APPLIED TO UNIAXIAL CRYSTAL BY EXTRAORDINARY WAVE
WHY ENERGY FLUX AND ABRAHAMS PHOTON MOMENTUM ARE MACROSCOPICALLY SUBSTITUTED FOR MOMENTUM DENSITY AND MINKOWSKIS PHOTON MOMENTUM
INTERNAL PHOTON IMPULSE OF DIELECTRIC AND ON COUPLE APPLIED TO ANISOTROPIC CRYSTAL
Longitudinal and transverse effects of nonspecular reflection
SPIN ANGULAR-MOMENTUM OF A FIELD INTERACTING WITH A PLANE INTERFACE
Goos-Hanchen shift as a probe in evanescent slab waveguide sensors
Numerical study of the displacement of a three-dimensional Gaussian beam transmitted at total internal reflection. Near-field applications
EXPERIMENTS IN PHENOMENOLOGICAL ELECTRODYNAMICS AND THE ELECTROMAGNETIC ENERGY-MOMENTUM TENSOR
SHIFTS OF COHERENT-LIGHT BEAMS ON REFLECTION AT PLANE INTERFACES BETWEEN ISOTROPIC MEDIA
INTERFERENCE THEORY OF REFLECTION FROM MULTILAYERED MEDIA
Experimental observation of the Imbert-Fedorov transverse displacement after a single total reflection
DISCUSSIONS OF PROBLEM OF PONDEROMOTIVE FORCES
LONGITUDINAL AND TRANSVERSE DISPLACEMENTS OF A BOUNDED MICROWAVE BEAM AT TOTAL INTERNAL-REFLECTION
THEORETICAL NOTES ON AMPLIFICATION OF TRANSVERSE SHIFT BY TOTAL REFLECTION ON MULTILAYERED SYSTEM
Simple technique for measuring the Goos-Hanchen effect with polarization modulation and a position-sensitive detector
ASYMMETRICAL MOMENTUM-ENERGY TENSORS AND 6-COMPONENT ANGULAR-MOMENTUM IN PROBLEM CONCERNING 2 PHOTON MOMENTA AND MAGNETODYNAMIC EFFECT PROBLEM
RESONANCE EFFECTS ON TOTAL INTERNAL-REFLECTION AND LATERAL (GOOS-HANCHEN) BEAM DISPLACEMENT AT THE INTERFACE BETWEEN NONLOCAL AND LOCAL DIELECTRIC
A Novel Method for Enhancing Goos-Hanchen Shift in Total Internal Reflection
ANGULAR SPECTRUM AS AN ELECTRICAL NETWORK
OBSERVATION OF SHIFTS IN TOTAL REFLECTION OF A LIGHT-BEAM BY A MULTILAYERED STRUCTURE
EXCHANGED MOMENTUM BETWEEN MOVING ATOMS AND A SURFACE-WAVE - THEORY AND EXPERIMENT
NONLINEAR TOTALLY REFLECTING PRISM COUPLER - THERMOMECHANIC EFFECTS AND INTENSITY-DEPENDENT REFRACTIVE-INDEX OF THIN-FILMS
GENERAL STUDY OF DISPLACEMENTS AT TOTAL REFLECTION
TRANSVERSE DISPLACEMENT OF A TOTALLY REFLECTED LIGHT-BEAM AND PHASE-SHIFT METHOD
CONSERVATION OF ANGULAR MOMENT WITH SIX COMPONENTS AND ASYMMETRICAL IMPULSE ENERGY TENSORS
Goos-Hanchen and Imbert-Fedorov shifts for leaky guided modes
PREDICTION OF A RESONANCE-ENHANCED LASER-BEAM DISPLACEMENT AT TOTAL INTERNAL-REFLECTION IN SEMICONDUCTORS
Optical properties of nanostructured thin films
SPIN ANGULAR-MOMENTUM OF A FIELD INTERACTING WITH A PLANE INTERFACE
DISPLACEMENT OF A TOTALLY REFLECTED LIGHT-BEAM - FILTERING OF POLARIZATION STATES AND AMPLIFICATION
MECHANICAL INTERPRETATION OF SHIFTS IN TOTAL REFLECTION OF SPINNING PARTICLES
Transverse displacement at total reflection near the grazing angle: a way to discriminate between theories
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
<p>The individual <code>Records</code> are index by their WOS numbers so you can access a specific one in the collection if you know its number.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[16]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span class="n">RC</span><span class="o">.</span><span class="n">getWOS</span><span class="p">(</span><span class="s">&quot;WOS:A1979GV55600001&quot;</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt output_prompt">Out[16]:</div>


<div class="output_text output_subarea output_execute_result">
<pre>&lt;metaknowledge.record.Record at 0x10baccc50&gt;</pre>
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
<h1 id="Citation-object"><code>Citation</code> object<a class="anchor-link" href="#Citation-object">&#182;</a></h1>
</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p><a href="{{ site.baseurl }}/docs/Citation#Citation"><code>Citation</code></a> is an object to contain the results of parsing a citation. They can be created from a <code>Record</code></p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[17]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span class="n">Cite</span> <span class="o">=</span> <span class="n">R</span><span class="o">.</span><span class="n">createCitation</span><span class="p">()</span>
<span class="nb">print</span><span class="p">(</span><span class="n">Cite</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt"></div>
<div class="output_subarea output_stream output_stdout output_text">
<pre>Pillon F, 2005, APPL PHYS B-LASERS O, V80, P355, DOI 10.1007/s00340-005-1728-2
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
<p><code>Citations</code> allow for the raw strings of citations to be manipulated easily by <em>metaknowledge</em>.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="Filtering">Filtering<a class="anchor-link" href="#Filtering">&#182;</a></h1>
</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>The for loop shown above is the main way to filter a RecordCollection, that said there are a few builtin filters, e.g. <a href="{{ site.baseurl }}/docs/RecordCollection#yearSplit"><code>yearSplit()</code></a>, but the for loop is an easily generalized way of filtering that is relatively simple to read so it the main way you should filter. An example of the workflow is as follows:</p>

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
<div class="prompt input_prompt">In&nbsp;[18]:</div>
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
<div class="prompt input_prompt">In&nbsp;[19]:</div>
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
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[20]:</div>
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
<p>One note about implementing this, the above code does not handle the case in which the title is missing i.e. <code>R.title</code> is <code>None</code>. You will have to deal with this on your own.</p>

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
<div class="prompt input_prompt">In&nbsp;[21]:</div>
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
<div class="prompt input_prompt">In&nbsp;[22]:</div>
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
<div class="prompt input_prompt">In&nbsp;[23]:</div>
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
<div class="prompt input_prompt">In&nbsp;[24]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span class="n">selectedTags</span> <span class="o">=</span> <span class="p">[</span><span class="s">&#39;TI&#39;</span><span class="p">,</span> <span class="s">&#39;UT&#39;</span><span class="p">,</span> <span class="s">&#39;CR&#39;</span><span class="p">,</span> <span class="s">&#39;AF&#39;</span><span class="p">]</span>
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
<p>This will give only the title, WOS number, citations, and authors.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[25]:</div>
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
<p>The last export feature is for using <em>metaknowledge</em> with other packages, in particular <a href="http://pandas.pydata.org/"><em>pandas</em></a> but others should also work. <a href="{{ site.baseurl }}/docs/RecordCollection#makeDict"><code>makeDict()</code></a> creates a dictionary with tags as keys and lists as values with each index of the lists corresponding to a Record. <em>pandas</em> can accept these directly to make DataFrames.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[26]:</div>
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
<p>To make a basic co-citation network of Records use <a href="{{ site.baseurl }}/docs/RecordCollection#coCiteNetwork"><code>coCiteNetwork()</code></a>.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[27]:</div>
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
<p><a href="{{ site.baseurl }}/docs/metaknowledge#graphStats"><code>graphStats()</code></a> is a function to extract some of the statists of a graph and make them into a nice string.</p>
<p><code>coCites</code> is now a <a href="https://networkx.github.io/documentation/networkx-1.9.1/"><em>networkx</em></a> graph of the co-citation network, with the hashes of the <code>Citations</code> as nodes and the full citations stored  as an attributes. Lets look at one node</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[28]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span class="n">coCites</span><span class="o">.</span><span class="n">nodes</span><span class="p">(</span><span class="n">data</span> <span class="o">=</span> <span class="k">True</span><span class="p">)[</span><span class="mi">0</span><span class="p">]</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt output_prompt">Out[28]:</div>


<div class="output_text output_subarea output_execute_result">
<pre>(-7195789643546077181,
 {&apos;count&apos;: 1, &apos;info&apos;: &apos;Saleh B. E. A., 1991, FUNDAMENTALS PHOTONI&apos;})</pre>
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
<p>and an edge</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[29]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span class="n">coCites</span><span class="o">.</span><span class="n">edges</span><span class="p">(</span><span class="n">data</span> <span class="o">=</span> <span class="k">True</span><span class="p">)[</span><span class="mi">0</span><span class="p">]</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt output_prompt">Out[29]:</div>


<div class="output_text output_subarea output_execute_result">
<pre>(-7195789643546077181, 188038831039612651, {&apos;weight&apos;: 1})</pre>
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
<p>All the graphs <em>metaknowledge</em> use are <em>networkx</em> graphs, a few functions to trim them are implemented in <em>metaknowledge</em>, <a href="#filtering-graphs">here</a> is the example section, but many useful functions are implemented by it. Read the documentation <a href="https://networkx.github.io/documentation/networkx-1.9.1/">here</a> for more information.</p>
<p>The <code>coCiteNetwork()</code> function has many options for filtering and determining the nodes. The default is to use the <code>Citations</code> themselves. If you wanted to make a network of co-citations of journals you would have to make the node type <code>'journal'</code> and remove the non-journals.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[30]:</div>
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
<div class="prompt input_prompt">In&nbsp;[31]:</div>
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
AABjxBcwsnr1ak0mEkq9w3ekJD1KJlVUVLRcwwLgAuILGCkoKNCnFRW6+A7fcUFSdWUl//cCHzji
CxhqCYd1PDd3yc8fz8tTSzi8jCMC4AZWOwOGOGQDgMSbL2DK6/Wqt69P32Rna2IRz01I2ubzqbev
j/ACGYD4AsZ2hELaf+iQPs/O1shbfH5E8+c67z94kHOdgQzBtDPgkhdXCgbn5tTy+LG+1utXCl7Q
/H+8oytWqLevj/ACGYT4Ai5KJpOKRqM6fuSI/hwdVfHzKeVHyaSqKyvVEg6rsbGRqWYgwxBfIE3E
YrGFk6uKiorYTgRkMOILAIAxFlwBAGCM+AIAYIz4AgBgjPgCAGCM+AIAYIz4AgBgjPgCAGCM+AIA
YIz4AgBgjPgCAGCM+AIAYIz4AgBgjPgCAGCM+AIAYIz4AgBgjPgCAGCM+AIAYIz4AgBgjPgCAGCM
+AIAYIz4AgBgjPgCAGCM+AIAYIz4AgBgjPgCAGCM+AIAYIz4AgBgjPgCAGCM+AIAYIz4AgBgjPgC
AGCM+AIAYIz4AgBgjPgCAGCM+AIAYIz4AgBgjPgCAGCM+AIAYIz4AgBgjPgCAGCM+AIAYIz4AgBg
jPgCAGCM+AIAYIz4AgBgjPgCAGCM+AIAYIz4AgBgjPgCAGCM+AIAYIz4AgBgjPgCAGCM+AIAYIz4
AgBgjPgCAGCM+AIAYIz4AgBgjPgCAGCM+AIAYIz4AgBgjPgCAGCM+AIAYIz4AgBg7G93SKtLf8Q0
PAAAAABJRU5ErkJggg==
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
<p>A bit basic but gives a general idea. If you want to make a much better looking and more informative visualization you could try <a href="https://gephi.github.io/">gephi</a> or <a href="http://visone.info/">visone</a>. Exporting to them is covered below in <a href="#exporting-graphs"><strong>Exporting graphs</strong></a>.</p>
<h1 id="Making-a-citation-network">Making a citation network<a class="anchor-link" href="#Making-a-citation-network">&#182;</a></h1>
</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>The <a href="{{ site.baseurl }}/docs/RecordCollection#citationNetwork"><code>citationNetwork()</code></a> method is nearly identical to <code>coCiteNetwork()</code> in its parameters. It has one additional keyword argument <code>directed</code> that controls if it produces a directed network. Read <a href="{{ site.baseurl }}/examples/#Making-a-co-citation-network"><strong>Making a co-citation network</strong></a> to learn more about <code>citationNetwork()</code>.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>One small example is still worth providing. If you want to make a network of the citations of years by other years and have the letter <code>'A'</code> in them then you would write:</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[32]:</div>
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
<div class="prompt input_prompt">In&nbsp;[33]:</div>
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
XTs78TaZMtR/y5YtUrNmzQyB08vLK0NKxMy++eYb8fLykvnz50tERIS0adNGFi1aJMWKFcs2mLdp
00YuXLhwP34GpdR9pAH4EZRXGYwSEhIkJCREGgUGisloFF+TSXxNJjEZjdIoMFBCQkLy9Z3v7dyu
/n379hUvLy8ZMWJEhoxHycnJMnv2bPHy8hInJycZO3asFCtWTPr37y9///13ts/av3+/VKpUKS1X
ccmSJeW7776Tdu3aZRuEvb295bvvvrtfP4VS6j7QAPyIyuscvjExMRIVFSVRUVESExOThy3JGzer
/9mzZ6V9+/ZStWpV+e233zLcc/XqVVmzZo2IiFy5ckXefPNN8fb2lq+//jptlnMqi8Uibdq0yRBk
7e3t5X//+5/MmjVLTCZTtoH4tddek7i4uLz/AZRSeU4D8CPsYR82zi8Wi0VCQ0PFx8dHBg0aJNev
X7/ptZGRkdK0aVPx9/eXX3/9Ne14bGysNGrU6KZDzrt27ZJ69eple75ChQqybdu2+9FUpVQe0gD8
iHvYh43z0+XLl+Wll16S8uXLy4YNG256ncVikWXLlknZsmWla9eucurUKRERSUpKkvfeey/bIOvr
6ytbt26VMWPGiIODQ5bzdnZ2MmLECElMTLxfzVVK5TKDSB7mglMPldjYWKKjowEoWrQoHh4et7lD
AXz//fe88cYbtG7dms8+++ymv9uNGzf47LPP+PLLL3nnnXcYMmQIzs7OfP/997zyyitZEjUYjUYm
TpzIU089Rc+ePTly5EiWMp988kkWLVrE44/fyUIwpdSDQNcBqzQeHh74+fnh5+enwfcOtGnThgMH
DiAiVKtWjR9++CHb61xcXBg5ciQRERFERkZStWpVwsPDef7559mzZw916tTJcH1SUhIDBgzg888/
59dff+XNN9/MUubvv/9OjRo1mD59ep7mVVZK5T7tASuVizZs2MDrr79OvXr1mDx5Ml5eXre8dsCA
ARQvXpwpU6ZQqVIlhg4dytSpU7NcW7FiRcLCwjh//jyvvvoqFy5cyHJNq1atmDdvHsWLF8/VNiml
8ob2gJXKRU8//TT79u3D29ub6tWrs2zZspv2TJ9++mn27t1L+/btadq0Kf/9738ZNWoU3377LW5u
bhmuPXbsGE899RRnzpxh3759dOzYMUt5a9asoVq1aqxYsSJP2qaUyl0agJXKZSaTiUmTJrFixQpG
jhxJx44dOX/+fLbXOjg48Pbbb3Po0CHMZjOVK1fm6tWr/P777wQEBGS41mw28/rrrzN48GAWLFjA
/PnzswTqK1eu0LFjR3r37p1hy0ul1INHh6CVykMJCQmMHTuWmTNnMn78eIKCgm6Z83jPnj0MGDCA
69evM2HCBEJDQ5k9e3aW66pWrUpYWBhOTk707NmTrVu3ZrnGz8+PRYsW3Ta9Y2xsLFeuXAHA09NT
3/8rdb/k2/xrpR4he/bskZo1a8ozzzwjf/311y2vtVgsEhwcLKVLl5YePXrI5MmTxcXFJctSJJPJ
JIsXL5bk5GT59NNPxWg0ZrtcadiwYVmWkpnNZgkODpaGAQFiMhqlnKurlHN1FZPRKA0DAiQ4OFiX
nymVxzQAK3WfJCUlyaeffiqenp4ydepUSUlJueX1cXFx8uGHH4qnp6cMHDhQKleunO2a4b59+0p8
fLzs3r1bqlSpku01NWvWlEOHDonIvxuwtHBzk/BsNmBZDtLc1VU3YFEqj+kQtFL32eHDh3nttdcA
mDt37m3X8B4/fpzBgwezb98+fH19+fXXX7NcExgYSFhYGCVLluT999/Pdia1k5MTbVq2ZMePP7Ii
Pp5at6lnBNa0kUPGjGHAu+/msHVKqZzSAKxUPrBYLHz11VeMGjWKIUOGMGTIEBwcHG55z08//cSA
AQOwt7fn2LFjJCYmZjjv7u7O/Pnz6dixIz///DNBQUGcO3cuwzWewG6gbA7reQpo6OLC53Pn0rVb
txy3Tyl1exqAlcpHJ06c4PXXXyc6Opp58+ZlmfmcWVJSEtOmTWP06NEAxMTEZLmmadOm/PPPPxw8
eJASJUpw4sQJAJyBwUAocAFoCMwDStjuawVsSVdOIvA4MB9o6eqKOdNzrl+/zsSJExk0aNCdNFkp
ZaPLkJTKR+XKleOnn37izTff5JlnnmHEiBEkJCTc9Hqj0cigQYM4fPgwbdq0wdHRMcs1v/76K3Fx
cbz44os0bdqUhQsX4uTkhC8wC1gFRAN+QPd0960B4tJ96gNdgFqAPzB79mzi4uKIi4tj//792NnZ
0alTp9z5IZR6BGkAViqfGQwGevfuzd69e9m/fz81atTgt99+SzufXS/Xx8eHRYsWsWnTJnx9fbMs
bfrzzz8JCwvjzJkzFDIacU5M5DHgRaAKYARGAJuAv7Kp0wlgM/CK7Xv/a9f4evz4tPMLFiygSZMm
lC2b08FspVRmGoCVekCULFmSFStW8PHHH/PCCy8waNAgwsPDKVeuHLNnz852R606deoQFRXFiBEj
sLe3z3DObDazft06Brz8MgkWCxWxTolOZbH990A2dVkINObfd8XtgN0HDxIbG4uIsHDhQnr16nWv
TVbqkaYBWKkHiMFgoGvXrhw4cIBz587RpUsXYmNj6du3Ly1atCAqKirLPXZ2dowaNYpjx45Rvnz5
DOcKActTUigGtAa+BfYD8cBowADcyKYeC4GgdN+NgFehQkRHR7NlyxYuXbpE586dc6HFSj26NAAr
9QDy8vKiaNGipKSkpB3bsGED1atXZ/LkyRmOT5s2jdq1a1O5cmUaNWrE4MGDAXDAOonqZeAkMAEY
BHTC+v73V6y94FcBN8AR67veLcBFYDjgYjvnBlw0W6dhLViwgM6dO+Pi4pJn7VfqUaABWKkHVNWq
VbMEuRs3bjBo0CAaNWrEH3/8AUCpUqUYMWIEvXv3xmAwMGHCBEaMGIEHcBRYhnUGtC/wo+3YBeD/
ABNwnoyTrhZgDdL2wPe2c9GAvZ0dzs7OhIWF6fCzUrlAA7BSD6i3336bAwcO0Lx58yzntm/fTmBg
IOPGjaNNmza0b98eT09PAFJSUli/ciVFsAbdAKAGEAhsBKKwru/tC7wDePDvpKsuWIepg2zPSX1n
vAqo+cQTbNiwgaJFi9K0adM8aLFSjxYNwEo9wPz8/Pj555+ZM2dOliQJiYmJDB8+nDp16rBnz560
SVoffvgh2/bv5xhwBGvvtwTwje2+J4C6QANgjO1Y6qSrCKAI0NR2vAdQDHjd3p7nu3Vj4cKF9OzZ
M28aq9QjRjfiUOohce7cOd544w1WrVqV5Zy9vT1169alQoUKjBw5kuYBAcy5do3uwHqgDFASSACC
ga6Z7q8IfMS/y44AtgM1gV1AM8C1SBH++usvzZakVC7RHrBSD4mSJUuycuVKQkJC8PLyynAuJSWF
bdu2sWrVKiIiIgBoDozE+j63MvAC1iHlzBtepk66yjynuZ7teHsgCbh69SoDBgzIdjmUUurOaQ9Y
qYfQ5cuXeeeddwgODs72vJOdHf9YLBjTHTsKVAe8ge8gLRnD61gD7DeZyogAngNigJR0xzt16sT8
+fNxc3O753Yo9SjTHrBSDyFvb2+WLFnCqlWrKFGiRJbzDhYL4Vg32RD+nXQ1FJgIPA+0AELIOOkq
CViO9R1xI4OB5i++mCH4Aixfvpy6dety5MiR3G+YUo8Q7QEr9ZB7//33GZ9um8hUNYFk4DjWdby9
gbFYN99IBMKxDlEf5d8dr/623XcSSCxenLi4OOzt7blx4wbJyckZyndzc2PRokW0b98+L5qlVIGn
PWClHnL/+9//EBHWr1+Pn59f2vE/sGYyuoZ1re84rMEXrDtkdQMOA1eBX2yfQ1gzJl0EoqOjmThx
IjExMRw9epTAwMAMz42Li+OFF15gxIgRGTYGUUrljPaAlSpArl+/zvDhw5kyZQoikqP8vwlYe8Nf
A3uw7n4lwD9Yd8eqUqcOq1atws3NjX79+rF48eIsZbRs2ZLg4GCKFCmS201SqsDSHrBSBYjJZGLS
pEls3bqVypUrE4N1SDniJtcvxbpZxzzgXawTri4Bl7H2nL8B2LmT8iVKMOHzz1m4cCFTp07FwSHj
XOq1a9dSu3Zt9u3blyftUqog0h6wUgWQiBAUFMT27ds5duwYTiJUB97DmtnIAZiKdX/oFfw7I/pm
UmdE12vZkpXff8/WrVvp0qULFy9ezHCds7Mzc+bM4aWXXsr1NilV0GgPWKkC6JNPPuHAgQPs3r2b
3bt381hAADuxznY2YZ2UNQbrGuDbBV9s1+wGtq9di3/16lSoUIGIiAieeuqpDNfFx8fTo0cPBg0a
RFJSUq62SamCRnvAShUwwcHBfPDBB/z2228sX76cb775hgMHDuDn58eRI0cQEZyxTrYKxZqYoSHW
YejUBU2tsAbnVIlYMyvNt12bYjTi5uZGSkoKzs7OXLhwIUs9mjRpwtKlS/Hx8cm7xir1ENMArFQB
snnzZjp16sT69eupXr06K1aswM7Ojh9//JGIiAjKlSvHnj17sP/zT6KxpiSsCAzEOgP615uU2wzr
zlrDsSZ3SH3T+9Zbb1GlShXee+89EhMTSUxMzHBfqVKl0tYNK6Uy0iFopQqIo0eP8uKLL7JkyRKq
V68OQIcOHdIyJV24cIH27dtTzNmZx4AXgSqAERgBbAL+yqbcE1gzJaXuE/0R1iFssOYinjVrFgBz
586lTJkyGe49e/YsjRs3Zvbs2bnZVKUKBA3AShUAly9fpnXr1owbN45nnnkmy3mLxcLFixcJCAhg
7x9/UJF/Uw0CWGz/PZBN2amZklKXMrXDunQpVWRkJNeuXSM2Npbff/+dZs2aZbg/MTGRvn370rdv
XxISElBKWWkAVuohFx8fT/v27enSpQt9+vTJ9pro6GiMRiPOzs54OzrSGusWlPuBeGA01k06bmRz
70L+3aoSrD1mD4Mhy3VvvfUWAwcO5Ntvv2Xw4MFZzs+ePZvGjRtz5syZO2ugUgWUBmClHmIWi4Ve
vXpRtmxZxo4de9PrTp48mWEyVPpMSX62jxtQOtN9N8uU5OLiQsuWLbM8Z+nSpTz55JO8+OKLhISE
4OLikuH8zp07qVWrFhs3bsxhC5UquDQAK/UQGzZsGOfOneObb77Bzu7m/+98+vRpfHx88PT05HJC
AklAf6z7QF8AOmLdN7papvsWYA3S6cNoEnA5IYHExESeeuqpLEH2r7/+omHDhpw4cYJt27ZRoUKF
DOcvXbpE8+bNmTx5sqY2VI80DcBKPaRmzZpFeHg4K1euxMnJKdtrUlJSMJvNnDp1Cm9vb5ycnAis
UiXbTEnvAB7p7o0nY6akVOGAo7Mz7u7ubNmyhYiICAICAjJck5yczAcffMDgwYP5/vvvad26dZZ6
DRo0iJdffpkbN7Ib+Faq4NNlSEo9hNauXUtQUBCbN2+mUqVKN71u5MiRjB49GhHBYHtv26lTJy6v
WcPV69ezzZSUKgQYRtaZ0ZWBI4CTk1OGLSmfe+45li9fnqUO3t7ezJ8/n99//51Ro0ZlOe/v78+G
DRvw9PTMUduVKii0B6zUQ2bfvn307NmTsLCwWwZfsAbghQsX0rlzZywWCxaLhcWLF3PY3v6mmZJS
dSdr8I3A2mMGMJvNvPzyy5w9e5a4uDjCwsJYtWpVlkB6+fJl2rRpwz///MPy5ctxd3fPcL506dKa
xEE9kjQAK/UAiY2NJSoqiqioKGJjY7OcP3fuHG3atOHLL7+kYcOGOSpz06ZNNGrUKO27o6MjU2bO
5AVn57RgmhOnsO4HHZ/u2IwZM6hWrRpr164FoG3btkRGRtKkSZMs90+aNIlx48axbNkyqlatCkDR
okU5ePAgkZGRd1ATpQoIUUrlK7PZLMHBwdIwIEBMRqOUc3WVcq6uYjIapWFAgMybN086deokERER
EhgYKJ988skdlV+5cmXZs2dPluNTJk6UMs7OsgtEbvPZBVLG2VmaNGggWF8dZ/kEBQVJdHS0iIgk
JyfLmDFjxN7ePst1JpNJZs6cKb169ZJDhw5JaGioeHl5yaJFi3Ll91TqYaEBWKl8FBoSIj7u7tLC
zU3CQZLSBb1EkOUg9e3txRnE3s5OWrduLRaLJcflX7x4UTw8PCQ5OfmWz2/u6irLs3l+GMjTbm7i
4+4uoSEhIiKyceNGqVixYrZBuHjx4rJixYq08rds2SJly5bNcl3Xrl0ztGP//v1SsWJFefvttyUx
MfEuf02lHi4agJXKJ3faA/UEKWRnJz///HOOnxEWFiatW7e+5TUJCQkSEhIijQIDxWQ0iq/JJL4m
k5iMRmkUGCghISGSkJCQ4Z4bN27I0KFDxc7OLttA3LVrV7l06ZKIiERHR0unTp3Sztnb28uQIUMk
KSkpQ5lXr16V559/Xho1aiTnz5/PcRuVelhpAFYqD3355ZdSq1YtcXR0lKCgoLTjoSEhUsRolHIg
riAtQc6lC7ifgVQDcQPxA/kc5CSIt8Eg8+bNk61bt8qTTz4pbm5u4u/vL1u2bMn2+QMHDpRPP/00
x/WNiYmRqKgoiYqKkpiYmNtev2PHDnniiSeyDcKenp4SHBwsFotFLBaLzJgxQ9zc3OSHH36QZ555
RurXry8nTpzIUF5KSop8/PHHUrp0adm2bVuO663Uw0gDsFJ5KDw8XFauXClvvPFGWgA2m81SxMVF
ioIcsg31vgHSJFMA3gOSAnIExBck1NYT9nZzk6JFi0pYWJhYLBZZvHixFClSRK5evZrl+TVq1JCt
W7fmaRvNZrN89NFH4uDgkG0gbteunZw9e1ZEJK2OKSkp8tlnn4m3t7eEhYVlKXPVqlXi7e0tM2bM
uKMhd6UeJhqAlboPhg8fnhaAg4ODpazRKG+mC7jnQAwgUTcZgh4A8rbt3/5OTlKqVKkM5T/22GMy
d+7cDMdiYmLEZDJlGT7OK3v37pUaNWpkG4Q9PDxk7ty5WYLpjh07pHz58tK3b1+5fv16hnNHjx6V
J554Qnr37i3x8fH3pQ1K3U+6DEmp+0DS7Xfz9fjxBCYl5TgbkWBNFZi6TWRrs5mrV65kuMZisXDw
4MEMx7Zt28aTTz5JoUKF7rH2ORMQEMCOHTv45JNPsjwzNjaWPn368Nxzz3HixIm043Xq1GHPnj3E
xcVRp04dDhz49xeoVKkSv/32G3FxcTRq1IhTp+5k0ZRSDz4NwErdB6m7UMXGxrLn0CHeJOfZiEba
/vuq7b8DgRtmM/PnzycpKYkFCxYQFRXFjRs3iI2NZffu3bz//vssXLiQ+vXr52WzsjAajXzwwQfs
3buXevXqZTn/888/U61aNb766issFuufHe7u7ixZsoShQ4fSrFkzpk+fnvYHi6urK0uXLqVLly7U
rVuXX3755b62R6k8ld9dcKUeBR9++KEEBQXJ8ePHpZyrqwjIVyCVQHxAPgXxANmSaej5S5DyIGcz
HfdxchJ/f38pWrSodOnSRapXry6+xYuLyWiU0k5O4gVSCMTdYJDmzZvft2Ho9JKTk2XSpEni7Oyc
7bB0o0aN5OjRoxnuOXz4sNSoUUM6dOggV65cyXBu3bp14uPjIxMmTND3wqpA0B6wUveBIZv8ubfL
RjQP+AxYD5TMdK+TvT0rV67k66++4tc1a/jzwAF6XbhATFISp81mLmPdZnK+COZNmyjr7c3S0NA8
aNnN2dvb884777B//36aNWuW5fzmzZvx9/dnwoQJpKSkAPD444+zfft2ypYtS40aNdi8eXPa9c2b
N2fHjh0EBwfTvXt3rl+/ft/aolRe0ACsVB5KzUaUnJxMSkoKrq6uXDKbucatsxEtAT4EfgLKZSoz
CbiYkEDIokUMfvVVmsfFUVuEUYBDuuuMWAP7lqQkfvjnH4b26cPUL77Is7beTIUKFVi3bh0zZ87E
zc0twzmz2czQoUOpX79+2jtsR0dHJk+ezFdffcWLL77I6NGj0wK0r68vW7ZswdnZmaeeeopjx47d
9/YolWvyuwuuVEH28ccfi8FgyPAp6+MjC0H8QUwgxUGGgVjSDTH72YaQXdN93rCdCwPxcHERA4g7
SDeQyznYzOMkSBkXl7QdrfLDqVOnpFWrVtkOSRuNxixLps6ePSvNmjWTxo0by+nTp9OOWywW+eqr
r8Tb21u+//77+90MpXKFBmCl7rPg4GBpbnsPfLvPlyC1QBxBgmzHnnZ1FQ9nZxkOUpHsN/JomSl4
FwKpbltH7OPuLkeOHJGmTZuKi4uLVK5cWdatW3ff2m+xWGThwoVSpEiRDAHYz88v220ok5OTZdy4
cVKsWDFZuXJlhnNbt26VUqVKyahRoyQlJeV+NUGpXKFD0ErdZx07duSAnR27c3BtKWAE1ny9YE0H
uDclBT8RZgGrgGjAD2v6wFRrgLh0n/pAF6AW8ITFQps2bahVqxbR0dGMGzeOzp078/fff+dK+27H
YDDQs2dPDh06RIcOHQBwcHDAzs6OTp06cfbs2QzX29vbM2zYMFauXMk777zDW2+9hdlsBqB+/fr8
/vvv/PTTT7zwwgvZZpBS6kGlAVip++xO0gF2ANoDnsB1oIOLC97e3pQ1m3kRqIL1Xe8IrGuFM+fv
BaA18T0AABlPSURBVDgBbAZesX1/4do1jh07xqhRo3B0dKRjx474+/uzfPnyXGhdzhUvXpzly5ez
bNkyPv/8cw4ePEiNGjUIDAxk3rx5GdZOA9SrV489e/Zw6dIl6tSpwx9//AFAiRIl2LBhA76+vjz5
5JNZ1kMr9cDK7y64Uo+qO0nG0BvExd5e/jd27P+3d+dxVZb5/8dfhMgmi4LaVw2l3HJBQJRR4We5
pZmOuR7N1MDdzBaVpnTS0XFkNHP76YCGu2khzmiWftPJ0HJFMcAxZ4bCTH+FkgcVZD2/Pw4QmE3q
CDcH3s/Hg4eHc58bPhf/vL2u+7o/t8XVwcHyKlgmlzp+saiT1q47nDsXLE+W+v79os+W7vU8depU
y9SpUw38a/wkMTHREhgYaOnZs6fl66+//tnxwsJCy5o1ayze3t6WNWvWlLklaf369RZvb2/L+++/
X4EVi9wfzYBFDPLSq6+yKCaGvu7u9KhVizistyIVywN2AN3d3NhesyYdQkIYMnw4dR0deZq7b+Sx
ERhT6vtbgMNDD5GRkVHynru7O9evX3+Qw7tvxR21unXrRlBQUJmmHWBdwh47dizx8fGsWLGCYcOG
ce3aNQBGjx7Nvn37mDFjBjNnziQ/P/+Xfo2I4RTAIgYaZjJxIT2dsWvWsNTfH08HB5q4utLE1ZXa
Dg4s8/dnXHQ0U199FV9f35LzumPtkDUI6/VfX8ANaHTbzz8MfA8MLvVeLfjZ8u61a9dwd3d/0MO7
bzVq1OD111/n8OHDbNmyhSeeeILz58+X+czjjz/OsWPHqFevHgEBARw5cgSAwMBATp48yenTp+nd
u3eFXdsWuVcKYBGD1axZE5PJRPzp03yXns6nSUl8mpTEd+npxJ8+jclkokYN6x2+Xl5epOfkkMev
N/IA2IA1pF1KvdccyLNYyvRrPnPmDK1bty63Md6vli1bcujQIQYNGkTnzp1ZtGhRmVmtk5MTK1eu
5J133mHAgAEsWLCAgoICvL292bt3L0FBQQQFBZGQkGDgKETuTAEsUol4eHjg6+uLr68vHh4eP2vk
4eTkhP/jjxPHf27kAdal6Q8ou/wMcA5wc3Fh6dKl3Lp1i7i4OJKTkxk0aFD5D/A+2NvbM23aNI4f
P87HH39M586dyzy0AWDAgAGcPHmSffv20atXLy5duoS9vT0LFy5k8eLF9O7dmw0bNhg0ApFfYPRF
aBH5ZXdq5DF48GBLV1fX/9jIwwKWrWBpcodNWd3c3CzLly+3PPHEExZnZ2dLy5YtLQcOHDB6qHel
oKDAEhUVZfH29rb84Q9/+Nl9w/n5+Za5c+da6tevb9m9e3fJ+ykpKZZmzZpZJk+ebEhfbJE7sbNY
brsYJCKVWk5ODo3r1eOjzEwC7/HcBKCvuzsX0tMr7DGF5eHbb79lwoQJXLp0iZiYGAIDy/4lDh06
xMiRI3n22WeJjIzE0dERs9nMqFGjuHLlCh988AENGtzeYVukYmkJWsTG3Mt9xKVdwHof8bKoKJsO
X4BHHnmEPXv28Nprr9G7d2/eeOONkuYcAKGhoZw+fZoLFy7QqVMnzp8/j4eHBzt37qRPnz506NCB
w4cPGzgCEbQELWKr7uU+4pNFfaCXvf220WU/cJcvX7YMHDjQ0rJly5/1ki4sLLSsWrXK4u3tbVm3
bl3JPcN79uyx1K1b17Jy5Uo92lAMoyVoERu2fds2pk2YQJvCQibfuEF/fnoiUh7WVpWr3NxIsbNj
WVQUw0wm44otZ7GxsUydOhWTycT8+fNxdXUtOZaUlITJZMLf35/Vq1fj7u7Ov/71LwYOHEhgYCCr
V6/G2dnZwOqlOtIStIgNu9v7iC+kp1fp8AUYPHgwycnJXLlyBT8/P/7+97+XHGvbti0nTpzAzc2N
gIAAjh8/TtOmTTly5Ag5OTmEhISQlpZmYPVSHWkGLFKFmM3mkg5XderUwcPD41fOqJo+/PBDJk2a
xNNPP82f//znMn+H2NhYJk+ezPTp05k+fTp2dnYsXbqUyMhINm/eTI8ePQysXKoTBbCIVEnXrl1j
xowZ7Nu3j6ioKPr06VNyLC0tjREjRlCrVi02bNjAww8/zKeffsqIESN45ZVXmDFjBnZ2dgZWL9WB
lqBFpEry9PRkzZo1xMTEMHnyZEaPHl2yOtC4cWM+++wzOnbsSGBgIPv27ePJJ5/k+PHjxMbGMnTo
0ErTG1uqLgWwiFRpPXr0ICkpCQ8PD9q0aUNcXBxg7Tc9b948tm7dytixY5kxYwb169cnPj4eDw8P
fvOb3/ys/7TIg6QlaBGpNg4fPkx4eDjt2rVjxYoV1K9fH4ArV64QFhbG5cuXee+992jatCnR0dHM
mjWLtWvX0r9/f4Mrl6pIM2ARqTZCQkJITEzE19cXPz8/tmzZgsViwdvbm7/97W+MGjWKTp06sWXL
FsaPH8+uXbuYMmUKb731VplHIoo8CJoBi0i1dOLECcLCwmjSpAl/+ctfaNiwIQCJiYmYTCaCg4NZ
uXIlWVlZDB06lFq1arF582Zq165tcOVSVWgGLCLVUocOHUhISKB9+/b4+/uzdu1aLBYL/v7+JCQk
UKNGDdq3b8/FixfZv38/zZo1o0OHDiQlJRldulQR9nPmzJljdBEiIkawt7fniSeeoHfv3syePZsP
PviA0NBQ6tWrx29/+1vq1q3LyJEjcXR0ZM6cOXh5eTFixAh8fHxo0+b2py+L3BvNgEWk2vPz8+Po
0aP07NmTDh06sGLFCgoLCzGZTBw9epTt27fzzDPP0KtXLz755BPeeOMNXnvtNfLz840uXWyYAlhE
BOttSREREXz++eds27aNrl27cv78eR599FEOHTpE27ZtCQgI4OrVq5w8eZKUlBR69uzJDz/8YHTp
YqO0BC0iUoq3tzdjxozh5s2bjBo1CoDOnTvTq1cv/Pz8GD16NFlZWaxevZpvvvmGKVOm0KVLl5JN
XCJ3S7ugRUR+QWpqKuPGjSMzM5OYmBjatm3LDz/8wJgxY8jIyOC9994jMTGR8ePHs3DhQsLDw40u
WWyIlqBFRH7Bo48+yv79+xk/fjzdunVj7ty5eHp68uGHHzJ06FA6duxIbm4uhw4dYvHixUycOJGc
nByjyxYboRmwiMhduHjxIhMmTODbb78lJiaGoKAgEhISMJlMdO3alXnz5jFlyhQuX75MbGyslqTl
V2kGLCJyFxo1asSHH37IzJkz6du3L6+//jqtWrXi1KlT5OXl0a1bN2bPnk3//v3p0KED8fHxRpcs
lZwCWETkLtnZ2TFy5Ei+/PJL/v3vfxMQEMCXX37Jhg0bePPNN+nVqxe1atUiJiaGIUOGsHz5crTI
KL9ES9AiIvdpx44dTJ06lSFDhrBgwQIuX76MyWSiYcOG/P73vyc8PJw2bdoQHR2Ni4uL0eVKJaMZ
sIjIfRo0aBBJSUn8+OOPtG3blrS0NL744guaNWvGgAEDWLhwIWC9jSk1NdXgaqWy0QxYROQB+Oij
j5g4cSK9e/dm0aJFHDlyhLCwMMLDw6lTpw4LFy5k48aNPPXUU0aXKpWEZsAiIg/A008/TVJSEnZ2
drRp04aCggJOnTrFsWPH2LFjBytWrOCFF15gwYIFui4sgGbAIiIP3IEDBxg3bhxdunRhyZIlrFu3
jsWLFzN//nxiYmJo0KAB69evx93d3ehSxUCaAYuIPGDdu3cnKSkJLy8v/Pz8ePTRR9m9ezeRkZG0
bduWOnXqEBwczLlz54wuVQykABYRKQeurq4sXbqU2NhYZs2axaJFi9i7dy83b97k6NGjDB8+nNDQ
UHbu3Gl0qWIQBbCISDnq0qULiYmJNGvWjJCQEPr06cNrr73GihUrCA8PZ9q0abz55psUFBQYXapU
MF0DFhGpIAkJCYSFhdGoUSNmzpzJyy+/TIMGDcjMzMTV1ZWtW7dSp04do8uUCqIZsIhIBWnfvj0n
TpwgODiYwYMHM3bsWJo2bUpaWhqenp4EBQWRmJhodJlSQTQDFhExQHJyMmFhYbi5uTF8+HBmzZpF
aGgoBw8eZOnSpTz33HNGlyjlTAEsImKQ/Px83nnnHSIjI5k6dSoHDx7k+vXrXLlyhQEDBrBo0SIc
HByMLlPKiQJYRMRgX331FeHh4RQWFhIcHMzmzZtp3Lgxrq6uvP/++9SvX9/oEqUc6BqwiIjBWrRo
QXx8PCNGjGDTpk0MGTKE9PR0srOzad++PUePHjW6RCkHCmARkUrgoYce4sUXX+TEiROcP3+e2rVr
4+npSY0aNejbty/R0dFGlygPmJagRUQqGYvFQkxMDBEREXTq1InDhw/j4uJCnz59WLlyJU5OTkaX
KA+AAlhEpJL67rvvmDhxIufOnaOwsJDc3Fzq1avHX//6Vx555BGjy5P/kpagRUQqqYYNG7Jr1y7m
zp3L9evX8fLyIjU1lYCAAA4ePGh0efJfUgCLiFRidnZ2jBgxguTkZJo3b46zszM5OTn069ePt99+
+1cfbWg2m0lNTSU1NRWz2VxBVcvd0BK0iIgNiYuLY9KkSQBkZWXRvXt3tmzZgqura8lncnJyiIuL
Y1VkJKfPnqWuoyMA6Tk5BLRqxeSICAYNGkTNmjUNGYNYKYBFRGxMRkYG06ZNY/fu3WRnZ9OgQQP2
79/PY489xvZt25g2YQJtLRYmX79OP6BG0Xl5wG5gVa1aJD/0EMuiohhmMhk3kGpOASwiYqM+/vhj
Ro8ejdlsxt7enpEmE3u3bWNndjbtf+XcBOBZFxemz5vHS6++WhHlym0UwCIiNiwzM5OXXnqJzZs3
41lQwCnA5y7PvQCEuLiw6N13NRM2gDZhiYjYkNzcXMLDw2nSpAnu7u507dqVQYMG4enoyP8C/wRa
Aq5AN6whW1oE4F30tQrYmZXFtAkT+O677xg+fDgNGzbE09OTkJAQjh8/XpFDq3YUwCIiNiQ/Px8f
Hx/i4+PJzMxk/vz5DBs2jJZYZ74DgT8CPwJBwLBS50YBfwO+LPraDZwEWhcWsmPHDoKDgzl16hQ/
/vgjo0ePpm/fvty8ebNCx1edaAlaRMTGuTo7M+XWLZoCG4HDRe9nYZ3pJgLNgc5AGDC26Pg6IBqY
Dizz9yf+9OkyP9fDw4ODBw8SEBBQ/oOohjQDFhGxYf/85z/JunWLMUAK0K7UMRegadH7AGdvO+5X
dKw/cColpcx9womJieTm5tK0adNyrL56UwCLiNiovLw8xowZg1uNGrQCbgLut33GHbhe9PoG4HHb
sRuAA+BdsyYZGRmAdWPX888/z5w5c3BzcyvXMVRnNX79IyIiVYvZbObq1asAeHl54eHh8StnVD6F
hYU8//zzODg44OngAPn51AIyb/ucGSiO0NuPm4veKy07O5t+/frRuXNnIiIiyqd4ARTAIlJN2Hp3
qJycHM6fP8/Zs2dJTk5m06ZNpKenk5eXx0N5eeQBrYENpc65Cfy76H2K/k3EujkL4AzQBmuDjiu5
ubi6ujJgwAB8fHyIioqqmIFVY9qEJSJVni11hyodtCkpKaSkpHD27Fm+/vprmjRpQuvWrfnmm2+4
fv06mzZtwt/fnx7Bwbxy5gz/B+s13xjgaeD3WDdkfVH0s6OAZcB+wAL0AqYBXsA77dpR+5FHqFGj
BrGxsdjb21f00KsdBbCIVGnLlyxh8axZla47VHHQFgdscdh+8803+Pr60qpVK1q3bl3yb/PmzXF0
dCQtLQ1fX1+cnJxKQjI/P5/HLBaSc3I4ALwIpAG/AdZTtjFHBLC26PU4YCHQ3c2NLi+/zPz583Fx
ccHOzq7k83v37qVLly7l+reorhTAIlJlbd+2jRlhYRzOzjasO1TpoC0dtsVBWzpkW7VqVRK09/o7
Gterx0eZmQTeY30JQF93dy6kp1fa5feqSgEsIjYtNzeXSZMmceDAATIyMnjsscf405/+xJNPPknj
evWYk5nJUuBbIJg7zwjfLXo9FuuMsDiUwqZMYffu3Zw7d46wsDC6dOnC2bNn6du3L6GhoWXqyMnJ
4auvvvrZ0nHpoC0dts2aNbvnoP1PKsN/NuTeaBOWiNi00p2hfHx82LNnD0OHDuWPf/wjzQsKiMB6
TbQfMAtrZ6gjReeW7gwF0BPwBSYATbOz2bJlCzk5OeTn5xMdHU10dDQA165d4+LFiyVhe/bs2ZKl
4eKAHTZsWMnScUXMLIeZTHx/6RIh97HcrvA1hmbAIlLltGvXjlyzma5paSRz752hjgA7gBf46R7a
0tzc3Hjqqad+tnRcGZZwizectSksZPKNG/Sn7IazXcAqNzdS7OwM33BW3SmARaRK+f7772nSpAl2
+fmE5+dTCPzfUsf9gLnAs4An8AnQoehYAvAk1ntl87DeI5t7h9/RsmVL/vGPf5TXEP5rubm51luu
Fi7k2JkzPFy0sepKbi6BrVszOSKCgQMHVor/MFRnWoIWkSojLy+P5557joEDB/LFrl1k37hB3ds+
czedocDaHcoNuFr0fZ06dQgJCaF169b4+fmV1xAeiJo1a2IymQgMDKRHjx4c/OwzwDoGW2w6UlUp
gEWkSijuDOXk5MScOXPotWvXf90ZysnRkd2xsWzdupUWLVrw1ltvld8AysGxY8fo1KkTvr6+Rpci
d6Be0CJi8ywWC+Hh4aSnp7Njxw7q1atHek4OLbF2eyr2S52hihV3hgLrEvS1wkJCQ0Oxt7cvc2+s
rTh27BjBwcFGlyG/QAEsIjZv0qRJnDt3jl27duHo6IiHhwcBrVrhBCQDccAtrNd+/bFuwAIYBSwB
LgHfFb0eU3RsFxDQqhWOjo4UFBSQl5fHrVu3KCwsrMCR3Tuz2Uxqaiqpqal8/vnnCuBKTJuwRMSm
3akzFMCYMWP4x/r1/O7GjXvuDAXW7lD5AQEcOnSozO9bv349o0aNKp/B3Kc79rm2WLh08yZBbdvy
4u9+V6n7XFdXCmARqZKqS3coW+pzLWVpCVpEqiRHR0eWRUUxwNmZC/dw3gWsDSqWRUVV+vBdvmQJ
M8LC2JOZySfXr/MsZXfWOgADgf03brAnM5MZ4eEsX7LEmGLlZxTAIlJlDTOZmD5/PiHOziTcxecT
sLZmtIXuUNu3bWPxrFkcvouuVwDtgcNZWSyePZvt27aVd3lyFxTAIlKlvfTqqyyKiaGvuzs9atUi
DsgvdTwPa9er7m5u9HV3Z9G775b7k5DuxcqVKwkKCsLJyYkXXngBsC6vT5swgdHZ2XTHeltVH+By
qfOuAaOB+kVfc7Fe+96ZlcW0CRP47LPP6NixI+7u7rRr147PP/+8QsclCmARqQaGmUxcSE9n7Jo1
LPX3x9PBgSaurjRxdaW2gwPL/P0ZFx3NhfT0SjfzbdiwIbNnzyYsLKzkvbi4OBrm5hKNdbd2BtYe
1sNLnfcK1p3facBxYBPWDWjtgeYFBTzzzDNERERgNpuZOXMm/fr149q1axUzKAG0CUtEqiGz2UxG
RgZgO92hZs+ezcWLF1m3bh2h/v7UOXOGR4CVRccvAw2x3ufsC9QFPgaCio7/qej7eOB3wHInJ25m
Z5f8/BYtWhAREVEm6KV8qROWiFQ7Hh4eNhG6pRXPlcxmM6fPnmUC1hluseK7k5OxBjCA5bbjyUWv
g4HsW7cwm80lf4fCwkJSUlLKqXq5Ey1Bi4jYgOJOXFevXqWuoyNPAx8ASUA28AfADusTnwB6A5FY
e1v/C+sjGYvnu6FFn924cSN5eXls2LCB1NRUsrKKz5aKoAAWEbEBt18t7A7MAQZhnfH6Yt2M1ajo
+HLACWiG9clPI7AuUQN4AXWdnFi7di0PP/ww+/bto0ePHjRq1AipOApgEREbUDwD9vLyIj0nhzxg
MnAe+H9Y7/fN56de1rWBzVivDScBBViXnsG68/tGQQHx8fFcvXqVjRs3cu7cOTp27Fhh4xEFsIhI
pVZQUMCtW7fIz8+noKAAJycn/B9/nDis13QtWJuHjAde5qfHK6ZifZRiAdbNV2uAWUXHdgHNfX1x
cXEhMzOT6dOn4+PjQ8+ePStyaNWeAlhEpBKbN28eLi4uREZGsnnzZpydnfmf5s1Z7erKc1iXnYOB
LsC8UuclAH5Yn3H8JrAVeLzo2Co3N5y9valbty4+Pj58//337Ny5swJHJaDbkEREbE516XNd1WkG
LCJiY6pDn+vqQAEsImKDqnKf6+pCS9AiIjas+HGEbQoLmXzjBv0p+zjCXViv+abY2elxhJWMAlhE
xMbl5uYSFxfHqshITqWk4F20vHwlN5fA1q2ZHBHBwIEDtexcySiARUSqEFvsc11dKYBFREQMoE1Y
IiIiBlAAi4iIGEABLCIiYgAFsIiIiAEUwCIiIgZQAIuIiBhAASwiImIABbCIiIgBFMAiIiIGUACL
iIgYQAEsIiJiAAWwiIiIARTAIiIiBlAAi4iIGEABLCIiYgAFsIiIiAEUwCIiIgZQAIuIiBhAASwi
ImIABbCIiIgBFMAiIiIGUACLiIgYQAEsIiJiAAWwiIiIARTAIiIiBlAAi4iIGEABLCIiYgAFsIiI
iAEUwCIiIgZQAIuIiBhAASwiImIABbCIiIgBFMAiIiIGUACLiIgYQAEsIiJiAAWwiIiIARTAIiIi
BlAAi4iIGEABLCIiYgAFsIiIiAEUwCIiIgZQAIuIiBhAASwiImIABbCIiIgB/j/fLGSFBndLDQAA
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
<h1 id="Making-a-co-author-network">Making a co-author network<a class="anchor-link" href="#Making-a-co-author-network">&#182;</a></h1>
</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>The <a href="{{ site.baseurl }}/docs/RecordCollection#coAuthNetwork"><code>coAuthNetwork()</code></a> function produces the co-authorship network of the RecordCollection as is used as shown</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[34]:</div>
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
<h1 id="Making-a-one-mode-network">Making a one-mode network<a class="anchor-link" href="#Making-a-one-mode-network">&#182;</a></h1>
</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>In addition to the specialized network generators <em>metaknowledge</em> lets you make a one-mode co-occurence network of any of the WOS tags, with the <a href="{{ site.baseurl }}/docs/RecordCollection#oneModeNetwork">oneModeNetwork()</a> function. For examples the WOS subject tag <code>'WC'</code> can be examined.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[35]:</div>
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
<div class="prompt input_prompt">In&nbsp;[36]:</div>
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
AAALEgAACxIB0t1+/AAAIABJREFUeJzs3X98zfX///HbOfZ7ds7Oftvsh9mbjPwmCg3v5E0K1YwM
URRqb6qvkpkiIqQSyXvIZKT0nt/zRt7oU3kjKQqbtrH5sTGz2U87z+8fZzt27IeRjh89rpfLLu28
fjxfz9fraPfzep7n8/nSKKUUQgghhLAa7e2ugBBCCPFXI+ErhBBCWJmErxBCCGFlEr5CCCGElUn4
CiGEEFYm4SuEEEJYmYSvEEIIYWUSvkIIIYSVSfgKIYQQVibhK4QQQliZhK8QQghhZRK+QgghhJVJ
+AohhBBWJuErhBBCWJmErxBCCGFlEr5CCCGElUn4CiGEEFYm4SuEEEJYmYSvEEIIYWUSvkIIIYSV
SfgKIYQQVibhK4QQQliZhK8QQghhZRK+QgghhJVJ+AohhBBWJuErhBBCWJmErxBCCGFlEr5CCCGE
lUn4CiGEEFYm4SuEEEJYmYSvEEIIYWUSvkIIIYSVSfgKIYQQVibhK4QQQliZhK8QQghhZRK+Qggh
hJVJ+AohhBBWJuErhBBCWJmErxBCCGFlEr5CCCGElUn4CiGEEFYm4SuEEEJYmYSvEEIIYWUSvkII
IYSVSfgKIYQQVibhK4QQQliZhK8QQghhZRK+QgghhJVJ+AohhBBWJuErhBBCWJmErxBCCGFlNre7
AkIIUS4nJ4fz588D4O7ujl6vv801EuLPIXe+QojbqqioiPj4eDq3bImfpyfdW7Sge4sW+Hl60rll
S+Lj4ykuLr7d1RTiltIopdTtroQQ4q9p9apVRI0axf1KMTo3lz5cbY4rAdYDC+rW5Retlg8WLWJA
RMTtq6wQt5CErxDitvhw7lxmT5rE1wUFtLnOtvuBfk5OvDp1Ki+PH2+N6gnxp5JmZyHuIlqtlhMn
TlS7vlmzZuzatavKdTt37sTf379W29bGiy++yLRp02q17bBhw4iOjgZg9+7d+Pn5MXvSJPbUIngB
2gB78vOZHR3N6lWrbrrOt0qvXr2Ii4u73dUQdzEJXyGsICgoCHt7e3NnonKtWrVCq9WSlpZ2w2VW
DLRyv/zyC126dKnV/jeybVUWLlzIpEmTarWtRqNBo9EA0L59e0rz8vh3QQEBN3C8AODr/HyiRo26
Zd8BHz58mB49euDu7o7BYKBt27Zs3rz5uvtt2rSJyMjIW1IH8dck4SuEFWg0GoKDg4mPjzcv+/nn
nykoKDCH0r2u/BuutWvX0sxopPVNlNEGaGo0snbt2irLv9Fv0fr06cOjjz7K2bNnOXfuHB9++CE6
ne4maibEjZHwFcJKBg8ezPLly82vP/vsM4YMGWIRGGFhYcTGxppfL1u2jM6dO1cq69NPP2XlypXM
mjULFxcXnnjiCcB0h719+3YACgoKGDZsGG5ubjRt2pT//e9/FmUEBQWxY8cOAPbu3Uvbtm3R6/X4
+PjwyiuvmLfbs2cPDz74IAaDgYCAAPM5VLzz3rlzJ/Xr12fGjBl4enrSoEEDVq5cWeV1mB4dzcG8
vKv1AOYALQBXIAIoKlt3EXgM8ALcgD7AgLw8Fsycab5ekyZN4qGHHsLZ2Zk5c+bQtm1bi+PNnTuX
vn37VqpHVlYWKSkpPP/889jY2GBra8uDDz7IQw89ZN4mISGBli1botfrCQkJYevWrebjVnyflixZ
QmhoKG5ubvTs2dOiJUOr1bJo0SIaNWqEwWBg7NixFvVYvHgxoaGh6HQ6mjZtyo8//ghARkYGTz75
JF5eXgQHB/PRRx+Z96np/RJ3BwlfIaykQ4cOXLp0id9++43S0lJWr17N4MGDLbap2Dxbk5EjR/LM
M88wYcIEcnNzSUhIqLT/W2+9xe+//86JEydITEzks88+syi74u9RUVGMGzeOnJwcTpw4QXh4OACp
qan06tWLqKgosrKyOHjwIC1atKiyrmfPnuX8+fNkZGTw2WefMXLkSI4fP25R75ycHJJSUnCseM7A
GiAR+B04BCwrW2cERgBpZT+OwEbgwOHD5OTkALBixQr+9a9/kZeXx8svv8zvv//Ob7/9Zi4/Li6O
oUOHVrqG7u7uhISE8Mwzz5CQkMDZs2ct1u/du5ehQ4cyZ84ccnJy2LVrF4GBgZXOPSEhgRkzZvD1
11+TlZVF586dGThwoEVZGzduZN++fRw6dIgvvviCxMREANasWcNbb71FXFwcly5dYt26dbi7u2M0
GunTpw+tWrUiIyOD7du3M2/ePHP4V/d+ibuHhK8QVhQZGcny5cv5z3/+Q2hoKH5+fn+ovJqaWdes
WcObb76Jq6sr9evXJyoqqtrt7ezsOH78OFlZWTg5OfHAAw8AsHLlSh555BEGDBhAnTp1cHNzM4dv
VcefOnUqtra2dOnShd69e7N69WqL9efPn0dva1vp+C8DPoAB093twbLlbkA/wAGoC0wEdgMednZc
uHABjUbDsGHDaNKkCVqtFjs7O8LDw1mxYgVg+k43NTWVxx57rNIxNRoN33zzDUFBQbzyyiv4+vry
8MMPk5SUBEBsbCwjRoyge/fuAPj6+tK4ceNK5XzyySe88cYbNG7cGK1WyxtvvMHBgwc5efKkeZvX
X38dnU6Hv78/Xbt25aeffgLgX//6FxMmTKBNG1O3s4YNGxIQEMD//vc/srKymDRpEjY2NjRo0IDn
nnuOVWWdzap7v8TdQ8JXCCvRaDRERkby+eefV9nkfKtlZGRY9G4OCKi+e1NsbCzHjh2jSZMmtG/f
no0bNwJw6tQpgoODa3U8g8GAo+PVe9rAwEBOnz5dq319KvzuCJQ3SucDozA1TeuBh4EcLEO/4jkC
DB061NzkHRcXx4ABA7CtIvAB/Pz8+Oijj0hKSiI1NRVnZ2eGDBkCmM69YcOG1617amoqUVFRGAwG
DAYD7u7uAKSnp189P5+rZ+jk5EReWbN7dcdITU0lIyPDXKbBYGDGjBmcO3cOqP79EncPmV5SCCsK
CAggODiYzZs3s2TJkkrrnZ2duXz5svn1mTNnqi3res3T9erVIy0tjSZNmgDU2KM6JCTEHFhfffUV
Tz31FOfPn8ff35+9e/fWqg7Z2dnk5+fj5OQEmAKkefPmFtu6u7uTU1KCR401v2oOcAzYi+l734NA
ayCruBg3N7dKdQBT876dnR27du0iPj7eopNbTerXr8/o0aMZNGgQYAr18rvgmgQEBBAdHV2pqbk2
qjtGQEAADRo04NixY1XuV9X7deHCBYsPP+LOJne+QlhZbGwsO3bsqPIPZcuWLVm7di0FBQUkJSVZ
dOq5lre3d41jfsPDw5kxYwYXL17k1KlTFh12rrVixQoyMzMB0Ov1aDQa6tSpw6BBg9i2bRtr1qzh
ypUrnD9/3txkWlXv4piYGEpKSti9ezcbN27k6aeftthWr9cTEhREQfWXx0IepjthPXABeKtseeum
Tc3zPlfVehAZGcnYsWOxs7PjwQcfrLLsixcvEhMTQ3JyMkajkaysLJYsWULHjh0BGDFiBEuXLmXH
jh0YjUbS09M5evRopXJeeOEFpk+fzpEjRwDT99pr1qyp9pwqXrfnnnuO2bNnc+DAAZRSJCUlkZaW
Rvv27XFxcWHWrFkUFBRQWlrKL7/8wr59+4Cq3y+tVv6c303k3RLCyoKDg2nd+upAm4p3buPGjcPO
zg5vb2+effZZBg8eXG0nqREjRnDkyBEMBgP9+/evdJyYmBgCAwNp0KABPXv2ZMiQIdXeLScmJtKs
WTNcXFwYN24cq1atwt7enoCAADZt2sScOXNwd3enVatWHDp0yFyXiuX5+PhgMBjw9fUlMjLS3MP3
2m37DhxIXg137ZqyH4B/AgWAB/Ag8A9AAS/+v/9X5TUpFxkZyeHDhyt1aKvIzs6O1NRU/v73v6PX
67n//vtxdHRk2bJlALRr146lS5cybtw4XF1dCQsLq7L1oG/fvkyYMIGIiAhzOeUdqqqqX8Vr8dRT
T/Hmm28yaNAgdDod/fv3Jzs7G61Wy4YNGzh48CDBwcF4enoycuRILl26BFT/fom7h0wvKYT4w3bu
3ElkZKRFJ6PqFBUVEejlxaZLl254rO9+oLdOR1pmJnZ2dtVuV1BQgLe3Nz/++GOtvrcVwtrkzlcI
YVX29vZ8sGgRfR0duZF5vdIwze/8waJFNQYvmGbfat++vQSvuGNJhyshxC1xIzN1DYiI4GxGBp1u
4sEK13uyUVBQEBqNhn//+9+1ro8Q1ibNzuKuIg9bv7eUP1KwmdHI6Lw8HsfykYLrgAUuLhzWaOSR
guKeIuEr7nhFRUWsXbuWBTNn8uORI3iWdSzJLCqiVWgooydM4Mknn7xuU6S4MxUXF5vf3wOHD+NR
9j5mFRfTumlTRk+YQP/+/eX9FfcUCV9xR5OHrf+15OTkcOHCBQDc3NykZUPcsyR8xR2rtg9bTwOa
AG6Ojrw2bZo8bF0IcceT3s7itli2bBn3338/zs7O1KtXj9GjR5snygfTHW91D1sPAnZUeB0AXAa+
LSi4Yx62LoQQNZE7X2F1c+bM4b333mP58uV0796dU6dOMXr0aDIzM/n2228xGo01jgNtAPwL6F7F
utqOAxVCiNtJ7nyFVV26dIkpU6Ywf/58evToQZ06dQgMDOSLL74gJSWFFStWMGjQIIyXLzML0GF6
gPqhsv0jMTUz9wFcgNlACqZ/yMaybRuVltKjRw/8/Pxwc3OjX79+gOn5rY899ph58vsuXbr8qQ82
EEKI6sg4X2FV//d//0dhYWGl6RCdnZ3p1asX//nPf9j37bdkl5YSDnwOzAP6AseBOGAPEAt0K9s3
5ZpjXL58mZM//cTxlBScnZ357rvvANMdt7+/P1lZWQB8//33NzQ2VQghbhW58xVWlZWVhYeHR5WT
wNerV48zZ85wOjOTtkB/oA4wHigEvq9F+acxPfnmctkj22xsbOjcuTNgmsv39OnTpKSkUKdOHR56
6KFbck5CCHGjJHyFVXl4eJCVlYXRaKy0LiMjg7p16+JsY0PFJ7RqgPpARi3KP4npAeye9vbmISvl
XnvtNUJCQujRowcNGzZk5syZN38iQgjxB0j4Cqvq2LEj9vb2fPXVVxbL8/Ly2LJli/lutOL0/Ebg
FOBb9rqmhmJ/TI+eM1bxXW7dunWZPXs2ycnJrFu3jrlz57Jjx45K2wkhxJ9NwldYlV6vJyYmhpde
eonExERKSkpISUkhPDwcf39/hg8fzuUrV9gPfA1cwfSdrwPQoawMbyC5mvLrAT2BjIICtFotJSUl
bN68mRMnThAbG8uPP/6IUgqdTkedOnWoU6fOn33KQghRiQw1ErfFkiVLeP/990lOTkan09GvXz/e
ffdd9Ho9gT4++J09SwCwCfgbpg5WLcv2XQe8BFwCojF9N9wQ04xXWuAz4P8ZDBQZjVzOy0MZjfg7
O5NTXMzF4mI0Wi2urq5ERUUxefJka5+6EEJI+Io7z1NPPcW3CQmcvnLlpvbv4uDAIY2GdjY2MiWl
EOKOJM3O4o5z3333cVGj4cBN7Lsf2F9YyJaCAv6Tm0s/LMfT2WK6U96Wl8fGS5d4bcQIPpw791ZU
Wwghak3CV9wyYWFhxMbG/uFybG1tadehA30dHYkEptVyvzRM3/fO4ur3wzVpA+zJz//TpqTcuXMn
/v5X+203a9aMXbt23VRZQUFBbN++/VZVTQhxm0n4ihsSFBSEk5MTLi4u+Pj48Oyzz3L58mXA9DD1
WzFpRUxMDLt27eLVadP4r6Mj/6jFPvsxhemzwJgbOFYA8HV+PsOGDMHW1pYzZ87cTJVr5ZdffqFL
ly43te+turZCiDuDhK+4IRqNhg0bNpCbm8uBAwfYt28f06bV9t70xrw8fjzvLVlCb52Ov9ety1pM
vZ/LlQBfAd1dXOjh6IiPvT2zbuI49wElJSX4+vqyYsWKW1F1IYSokYSvuGm+vr707NmTw4cPm5el
pKTQqVMndDodjz76KOfPnwegd+/ezJ8/32L/5s2bk5CQAMC4cePw9vZGr9fTvHlzjhw5AsDmLVsY
PmYMzy1ezLyWLalbpw52Wi1awB6YEhzM859+ipu7O5lFReiAYGDlDZzHV4Af4Ah89tlnFuumTJnC
U089RUREBDqdjjZt2nDo0CHz+qCgIN59912aNm2Km5sbw4cPp6ioqMrjVGw6Vkrx7rvvEhISgoeH
BwMGDCA7O9u8bVxcHIGBgXh4eDB9+vQbOBshxN1AwlfcsPIO8idPnmTz5s20atXKvHzlypUsW7aM
c+fOUVxczOzZswEYNmyYxV3lTz/9REZGBr179yYxMZHdu3dz/PhxcnJyWLNmDW5uboDpTtvGxoaI
iAhmL1qEvbMzSz77jOQTJzjy6698uWkTXbp0IenUKb7BNPzoO64OS6qNz4ARwMmMDJKSkjhwwLKr
17p16wgPDyc7O5tBgwbRt29fSktLzetXrlzJ1q1bSU5O5tixY9W2BFRsOv7www9Zt24du3bt4vTp
0xgMBsaMMTWYHzlyhNGjR/P555+TkZHB+fPnOXXq1A2ckRDiTifhK26IUoq+fftiMBjo3LkzYWFh
TJw4ETCFy/DhwwkJCcHBwYHw8HAOHjwIQJ8+fTh27BjJyabpMeLi4oiIiMDGxgZbW1tyc3P59ddf
MRqNNG7cGB8fn0rHjo2N5bnnnmPw4ME0aNCA++67j8aNG3PhwgW0wK9AAaZJOEJreT5pwE4gAtOU
lJ07d2b58uUW27Rt25b+/ftTp04dxo8fT2FhId9//735nMeOHYufnx8Gg4E333yT+Pj46x530aJF
TJs2DV9fX2xtbYmJieHLL7+ktLSUL7/8kj59+tCpUyfs7OyYOnVqlXNhCyHuXvJ/tLghGo2GhIQE
srOzSUlJYf78+djb25vXVwxNR0dH8soecFAexnFxcSilWLVqFZGRkQB069aNsWPHMmbMGLy9vRk1
ahS5ubmVjn3q1CkaNmxYabmTkxOeDg58gmkKyseAo7U8nzigGdCo7PU//vEPVq5caXFnW79+fYvz
r1+/PhkZV2eartijOSAgwGJddVJSUujXrx8GgwGDwUBoaCg2NjacPXuW06dPWxzTyckJd3f3Wp6R
EOJuIOErrGbo0KF8/vnnbNu2DScnJx544AHzupdeeol9+/Zx5MgRjh07xnvvvVdpf39/f5KSkiot
d3d3J6+0lI3AGUwdqJ6vZZ2WY3pUYT0g7fJl3nnnHbKysti4caN5m5Mnr840bTQaOXXqFL6+vuZl
aWlpFr9XXFedgIAAtmzZQnZ2tvknPz8fX19f6tWrZ3HM/Px883fnQoh7g4SvuKVqmjCtY8eOaDQa
Xn31VYYMGWJevm/fPn744QdKSkpwcnLCwcHBPOeyUspc5ogRI1i6dCk7duzAaDSSnp7O0aNHKSoq
IsDPjzWYJtFwxvQoQjA961eLqXn5Wt8BJ4D/Ae8A7Zs25fDhwwwaNMii6Xn//v18/fXXXLlyhXnz
5uHg4ECHDh3M9VuwYAHp6elcuHCBd955h4hazJj1wgsvMHHiRHNwZ2Zmsm7dOsA0w9eGDRv49ttv
KS4uZvLkyVU+BUoIcfeS8BW3VMWxqFWNTR0yZAg///wzgwcPNi+7dOkSI0eOxM3NjaCgIDw8PHjt
tdcqldGuXTuWLl3KuHHjcHV1JSwsjLS0NFMwOToyFHAHdgMLy8o+CQRh6s18reVAX6Ap8LmLC/+c
NAlvb2+ioqLYuHEj2dnZaDQannjiCVavXo2bmxuff/45a9euNX840Gg0DBo0yPyYwr/97W9MmjSp
yutRUVRUFI8//jg9evRAp9PRsWNH9u7dC0BoaCgff/wxgwYNwtfXFzc3N4umbSHE3U/mdhZWFRcX
x+LFi296pqfqFBUVEejlxaZLl2hdYfk7gBc1N0PvB3rrdKRlZmJnZ2ex7q233iIpKYm4uLgq923Q
oAGxsbF069btD56BEOKvRO58hdXk5+fz8ccfM3LkyFtetr29PR8sWkRfR0eLJuY3qTl404B+Tk58
sGhRpeCFmpvRhRDiZkn4CqtITEzEy8uLevXqMWjQoD/lGAMiInh12jQ6OTqyvxbb7wc6OTnx6tSp
1T7ZSKZ1FEL8GaTZWdxzVq9aRdSoUTQzGhmdl8fjWD5ScB2wwMWFwxqNPFJQiBrk5OSYe9q7u7uj
1+tvc43uHRK+4p5UXFzM2rVrWTBzJgcOH8ajrEk5q7iY1k2bMnrCBPr3719lU7MQf2VFRUXm/3d+
PHIEz7Jx/JlFRbQKDWX0hAk8+eST8v/OHyThK+55OTk5XLhwAQA3Nzf59C5ENcpbje5XitG5ufTB
stVoPbCgbl1+0Wql1egPkvAVQgjBh3PnMnvSJL4uKKDNdbbdj6mj4qtTp/Ly+PHWqN49RzpcCSH+
ssLCwoiNjb2lZb744ot/2mM2/yyrV61i9qRJ7LkmeHcCVY0wbwPsyc9ndnQ0q1etskody1V8Otjd
TMJXCHFPCwoKwsnJCRcXF3x8fHj22We5fPky8Of0Zl+4cKHFRCt/hsTERLp06YJOp8PLy4uwsDDW
r19/U2UVFRURNWoU/y4oIOAG9gsAvs7PJ2rUKIqLi2/q2Dejpvds2LBhaLVa82xx5caNG4dWq630
yNDqBAUFsWPHDvPrlJQUtFrtLZ1pTsJXCHFP02g0bNiwgdzcXA4cOMC+ffvuujvTir788kvCw8MZ
NmwY6enpnDt3jrfffvumw3ft2rU0MxotJqeprTZAU6ORtWvX3tSxbzWNRkOjRo0spoe9cuUKX3zx
BSEhIbX+oKXRaKoc438rv6WV8BVC/GX4+vrSs2dPDh8+bF6WkpJCp06d0Ol0PProo+ahNb1792b+
/PkW+zdv3pyEhATAdDfl7e2NXq+nefPmHDlyBDDdfUVHR5v3SUhIoGXLluj1ekJCQkhMTARg2bJl
NGzYEJ1OR3BwMCtXrrxu/ZVSjB8/nsmTJzN8+HBcXFwA6NKlC59++ql5m2nTphEUFIS3tzdDhw7l
0qVL5nPVarUsX76cwMBAPD09eWP8eEaXPX2sABgGuGGadvV/1xw/A3gS06xxwcBHwOi8PBbMnMmU
KVMIDw9n6NCh6HQ6mjVrxv79V0fcz5w5k/r166PT6bjvvvvMd5ZKKd59911CQkLw8PBgwIABZGdn
m/eLi4sjMDAQDw8Ppk+fft1r1KdPH/bs2cPFixcB2LJlCy1atMDb29scnsnJyXTr1g0PDw88PT0Z
PHgwOTk5AERGRpKWlkafPn1wcXHhvffe4+GHHwbA1dUVFxcXfvjhBwCWLFlCaGhtH2B6DSWEEPew
oKAgtW3bNqWUUmlpaapp06Zq8uTJSimlHn74YdWwYUN1/PhxVVBQoMLCwtTrr7+ulFLqiy++UA88
8IC5nIMHDyp3d3dVUlKitmzZotq0aaNycnKUUkr99ttv6vTp00oppYYNG6aio6OVUkr98MMPSq/X
m4+fnp6ufvvtN5WXl6d0Op06duyYUkqpM2fOqMOHD1/3XH799Vel0WhUSkpKtdvExsaqkJAQ9fvv
v6u8vDzVv39/FRkZqZRS6vfff1cajUaNHDlSFRYWqj179ihA/QJKgZoAqguobFAnQTUF5V+2rhRU
a1BTQZWAOgEqGNRGUM62tmrChAnKwcFBbd68WRmNRvXGG2+oDh06mK+Pv7+/+Rqlpqaq5ORkpZRS
8+bNUx07dlTp6emquLhYjRo1Sg0cOFAppdThw4dV3bp11e7du1VRUZEaP368srGxUdu3b6/y3IcN
G6YmTZqkRo4cqRYuXKiUUurpp59W8fHxqlOnTuqzzz5TSimVlJSktm3bpoqLi1VmZqbq0qWL+uc/
/2kuJygoyOIYKSkpSqPRqNLSUvOyf//73yokJET99ttv133fqiLhK4S4pwUGBqq6desqV1dXFRgY
qMaMGaMKCwuVUkqFhYWpd955x7ztggULVM+ePZVSShUUFCiDwaCSkpKUUkq98sorasyYMUoppbZv
364aNWqkvv/+e4s/yEpZhu/IkSPV+PHjK9UpLy9Pubq6qq+++krl5+fX+lz27NmjNBqNKioqqnab
bt26mYNHKaWOHj2qbG1tVWlpqTl809PTlVJKJScnKzutVq0uC9hgUIllvytQn4KqX/b796ACKqxT
oKaDehZUoLOzevnll9UjjzxiPu7hw4eVo6OjUkqp48ePKy8vL3PgVdSkSROLoMvIyFC2trbqypUr
6q233jIHsVJKXb58WdnZ2V03fPfs2aM6duyoLl68qLy9vVVBQYFF+F7r66+/Vq1atTK/vjZ8y69b
xfe6Z8+eKjY2ttr34Xqk2VkIcU/TaDQkJCSQnZ1NSkoK8+fPx75s4ggAHx8f8++Ojo7klTXBOjg4
EB4eTlxcHEopVq1aRWRkJADdunVj7NixjBkzBm9vb0aNGkVubm6lY586dYqGDRtWWu7s7Mzq1av5
5JNP8PX15bHHHuPo0aPXPRd3d3cATp8+Xe02p0+fJjAw0Pw6ICCAK1eucPbs2SrPWavRkFf2ewaW
vZsrdsBKLVtvqPAzAzhXYRtvb2/z705OThQWFmI0GgkJCWHevHlMmTIFb29vBg4caD6HlJQU+vXr
h8FgwGAwEBoaio2NDWfPnuX06dPUr1/foszya1AdjUbDQw89RGZmJtOmTaNPnz44ODhYbHP27Fki
IiKoX78+er2eyMjIG35mdmpqKlFRURgMhhvar5yErxBCVGPo0KF8/vnnbNu2DScnJx544AHzupde
eol9+/Zx5MgRjh07xnvvvVdpf39/f5KSkqosu0ePHmzdupUzZ85w33338fzzNT0CxKRx48b4+/vz
5ZdfVruNr68vKSkp5tdpaWnY2NhYBGM5d3d3io1GSste18Py2dcVf/cHGgDZFX4uAV9jmjnOycmp
xroPHDiQ3bt3k5qaikajYcKECYDpw8GWLVvIzs42/+Tn5+Pr60u9evU4efKkuYz8/Pxah+TgwYOZ
O3euxbM8LC3vAAAgAElEQVTDy02cOJE6derwyy+/kJOTQ1xcnEVP5ms7ZlXVUSsgIIBPP/3U4vvp
GyHhK4T4S1M19GDt2LEjGo2GV1991eKP+L59+/jhhx8oKSnByckJBwcH8zOelenrPABGjBjB0qVL
2bFjB0ajkfT0dI4ePcq5c+dISEjg8uXL2Nra4uzsbN6/vFNUWlpapfpoNBrmzp3L1KlTWbZsGZcu
XcJoNLJnzx5GjRoFmELu/fffJyUlhby8PCZOnEhERARabeU/93q9HhcnJw6WvQ7HdDd7ETiFqUNV
ufaACzALU8esUuAXYC7QumlTi9aEax07dowdO3ZQVFSEvb29xfV64YUXmDhxovl8MzMzzUOFnnrq
KTZs2MC3335LcXExkydPrnG4T8Vr//LLL7Nt2zY6d+5cabu8vDycnZ3R6XSkp6dX+uDk7e1NcnKy
+bWnpydardZi2QsvvMD06dPNHe1ulISvEOIvreJdTVVjSIcMGcLPP//M4MGDzcsuXbrEyJEjcXNz
IygoCA8PD1577bVKZbRr146lS5cybtw4XF1dCQsLIy0tDaPRyPvvv4+fnx/u7u7s3r2bhQsXAnDy
5EmCgoLw8/Orsr5PPvkkq1evZsmSJfj5+eHj48PkyZPp27cvAMOHDycyMpIuXboQHByMk5MTH310
NUavPT+/wEC+KQvOGCAQ0x1uT2AIUL51HWADcBBTT2dPYCSwytGR0RMmVHntyl8XFRXxxhtv4Onp
Sb169cjKymLGjBkAREVF8fjjj9OjRw90Oh0dO3Zk7969AISGhvLxxx8zaNAgfH19cXNzw9+/qmk/
rh6v/JgGg4GuXbtWuV1MTAwHDhxAr9fTp08fnnzySYu6v/HGG0ybNg2DwcDcuXNxcnLizTff5KGH
HsJgMLB371769u3LhAkTiLjJKTZlekkhhKhBXFwcixcvZteuXVY53jvvvIOXl1etmqFvhaKiIgK9
vNh06dINj/XdD/TW6UjLzJQHLdwgCV8hhKhGfn6+uXNVxTvfe83qVat4bfhw9tzALFdpmJ6H/V5s
rDxg4SZIs7MQQlQhMTERLy8v6tWrx6BBg253df5UAyIieHXaNDo5OrL/+puzH1Pwvjp1qgTvTZI7
XyGEEMDVRwo2MxoZnZfH41g+UnAdsMDFhcMajTxS8A+S8BVCCGFWXFzM2rVrWTBzJgcOH8aj7Lvc
rOJiWjdtyugJE+jfv798x/sHSfgKIYSoUk5ODhcuXADAzc0NvV5/m2t075DwFUIIIaxMOlwJIYQQ
VibhK4QQQliZhK8QQghhZRK+QgghhJVJ+AohhBBWJuErhBBCWJmErxBCCGFlEr5CCCGElUn4CiGE
EFYm4SuEEEJYmYSvEEIIYWUSvkIIIYSVSfgKIYQQVibhK4QQQliZhK8QQghhZRK+QgghhJVJ+Aoh
hBBWJuErhBBCWJmErxBCCGFlEr5CCCGElUn4CiGEEFYm4SuEEEJYmYSvEEIIYWUSvkIIIYSVSfgK
IYQQVibhK4QQQliZhK8QQghhZRK+QgghhJVJ+AohhBBWJuErhBBCWJmErxBCCGFlEr5CCCGElUn4
CiGEEFYm4SuEEEJYmYSvEEIIYWUSvkIIIYSVSfgKIYQQVibhK4QQQliZhK8QQghhZRK+QgghhJVJ
+AohhBBWJuErhBBCWJmErxBCCGFlEr5CCCGElUn4CiGEEFYm4SuEEEJYmYSvEEIIYWUSvkIIIYSV
SfgKIYQQVibhK4QQQliZhK8QQghhZRK+QgghhJVJ+AohhBBWJuErhBBCWJmErxBCCGFlNre7AuLm
5OTkcP78eQDc3d3R6/W3uUZCCCFqS+587yJFRUXEx8fTuWVL/Dw96d6iBd1btMDP05POLVsSHx9P
cXHx7a6mEEKI69AopdTtroS4vtWrVhE1ahT3K8Xo3Fz6cLXZogRYDyyoW5dftFo+WLSIARERt6+y
QgghaiThexf4cO5cZk+axNcFBbS5zrb7gX5OTrw6dSovjx9vjeoJIYS4QX/5ZueUlBS0Wi1Go/F2
V6VKq1etYvakSeypRfACtAH25OczOzqa1atWXXf7Zs2asWvXrj9cz2v16tWLuLi4W16uEELcC+6p
O9+6deui0WgAuHz5Mg4ODtSpUweATz/9lIEDB1baJyUlheDgYK5cuYJWe2d9FikqKiLQy4tNly7R
+gb33Q/01ulIy8zEzs7uz6ie2ZQpU0hOTpawFUKIWrqz0uYPysvLIzc3l9zcXAIDA9mwYYP5dVXB
e6dbu3YtzYzGGw5eMN0BNzUaWbt27a2ulhBCiD/ongrf6hiNRt59911CQkLw8PBgwIABZGdnV7lt
Tk4OI0aMwNfXl/r16xMdHW3RJL148WJCQ0PR6XQ0bdqUH3/8EYBff/2VsLAwDAYDzZo1Y/369eZ9
hg0bxujRo+nVqxcuLi507tyZM2fOEBUVhcFgoEmTJhw8eNC8fVBQELNnz+a54cP5Ni+PEcBZ4B+A
HngEuFi27U7A/5pzCAJ2AKPz8pjwz38SHh7O0KFD0el0NGvWjP3791sca/v27QCUlpYyffp0QkJC
0Ol0tG3blvT0dACioqIICAhAr9fTtm1b9uzZA8CWLVuYMWMGq1evxsXFhVatWgEQFhZGbGwsAEop
pk2bRlBQEN7e3gwdOpRLly4BV5v9ly9fTmBgIJ6enkyfPt1cv71799K2bVv0ej0+Pj688sorNbzT
Qghxl1D3qKCgILV9+3allFLz5s1THTt2VOnp6aq4uFiNGjVKDRw4UCml1O+//640Go0qLS1VSinV
t29f9cILL6j8/Hx17tw51b59e7Vo0SKllFJffPGF8vPzU/v27VNKKZWUlKRSU1NVcXGxatiwoZox
Y4YqKSlRO3bsUC4uLuro0aNKKaWGDh2qPDw81IEDB1RhYaHq1q2bCgwMVHFxccpoNKpJkyaprl27
WtS9ffv2ysnGRqWC8gLVCtRBUIWguoF6C5QC9Q2o+mW/l/8EgdoOqhiUrVarHBwc1ObNm5XRaFRv
vPGGateunUpOTlbJyckqICDAfJ1mzZql7r//fnXs2DGllFKHDh1S58+fV0optWLFCnXhwgVVWlqq
5syZo3x8fFRRUZFSSqkpU6aoyMhIi+sfFhamYmNjlVJKxcbGqpCQEPX777+rvLw81b9/f/P25dd/
5MiRqrCwUP3000/K3t5e/fbbb0oppTp06KBWrFihlFLq8uXL6vvvv781/0CEEOI2+kuEb5MmTcy/
K6VURkaGsrW1VaWlpRbhe+bMGWVvb68KCgrM265cudIcjD169FAffvhhpWPt2rVL+fj4WCwbOHCg
mjJlilLKFL4jR440r/voo49UaGio+fWhQ4eUq6urRd3ff/99FVS3rlKgngQ1ukK4fgSqby3CV4HS
29qqTp06qcLCQrVy5UrVunFjBaigunVVUN26SgOqWXCwWrlypfrb3/6m1q1bV6vrazAY1KFDh5RS
SsXExKjBgwdbrK8Yvt26dVMLFy40rzt69Gil65+enm5e3759e7V69WqllFJdunRRMTExKjMzs1b1
EkKIu8FfYoarlJQU+vXrZ9GhysbGhrNnz1psl5qaSklJCfXq1TMvMxqNBAQEAHDq1CkaNmxYqfyM
jAz8/S0bfwMDA8nIyABAo9Hg5eVlXufg4GDx2tHRkby8PIv9PTw8rq4HvCuscwAst65ZYWEhgV5e
3K8UI3NzeRFIzstDCzQAnjpxgtiRIzmel8exo0ehT59KZcyePZslS5aQkZGBRqPh0qVLZGVl1er4
p0+fJjAw0Pw6ICCAK1euWFx/Hx8f8+9OTk7m6xEbG8vkyZNp0qQJDRo0ICYmht69e9/A2QshxJ3n
LxG+AQEBLF26lI4dO1Zal5KSYv7d398fe3t7zp8/X2XPZ39/f5KSkiot9/X15eTJkyilzL2tU1NT
ue+++266zjqdjsyiIkrKXlfXJd0ZyK/wuhTILPu9BLhcUsKRH39kV2kpbYCUKsroDMTk5REEvPvm
m9hqtRZjhHfv3s17773Hjh07aNq0KQBubm6oso7y5edcHV9fX4vrnJaWho2NDd7e3qSlpdW4b0hI
CCtXrgTgq6++4qmnnuLChQs4OjrWuJ8QQtzJ7soOV2lpabi4uJj/+F/PCy+8wMSJE81/6DMzM1m3
bl2l7erVq0ePHj0YP348ubm5GI1GkpOTzeNgn3vuOd566y06duyIUoqkpCTS0tLo0KEDTk5OzJo1
i5KSEnbu3MmGDRuIKJtlqrb1rKhu3bq0Cg1lfTXrDwPRQCOgENiEKWynAUVl20wA7IBHy4L3esYC
nsXFzHjzTVbFx3Po0CEuXLjAu+++S0FBAR4eHhQXF/P222+bO0yB6a41JSWl2vMcOHAg77zzDr6+
vuTl5TFx4kQiIiJqNbRrxYoVZGaaPk7o9Xo0Gk2t9tu5c2el1og70Ysvvsi0adNudzWEEFZ2V4Zv
QEAAubm5173jKhcVFcXjjz9Ojx490Ol0dOzYkb1795rXVyxn+fLlFBcXExoaipubG08//TRnzpwB
4KmnnmL69OlkZ2ej0+no378/2dnZ2Nrasn79ejZv3oynpydjx44lLi6ORo0amcuveIxrX19bB4Az
Z87w7aFDhAOrgOmAC7AG0FT40QMLgOeA+kBdTL2fi4HFQGTZMotjlf13GXC6wvLxwDNAncJCBg0a
xHPPPUdhYSHr16/n6aefplGjRgQFBeHo6Ghuigd4+umnAdMDHtq2bVvp+g8fPpwePXpw7tw5goOD
cXJy4qOPPqp07q+88goeHh7s2bOHBQsWAJCYmEizZs1wcXFh3LhxrFq1Cnt7e8DUo9rR0REXFxfz
zxNPPFHp+H+EVqvlxIkTt7TMihYuXMikSZP+tPKFEHeo2/mF893mypUrVjtWeUckLxcXtf+aDlUK
1DBQk6pYXv4zDdQDNaxXoJaC6lTNum5166r4+HhzL/A/6ptvvlH169evdv2WLVuUt7e3Sk9PV0VF
RWrbtm3XLbNip64bPV5taTQalZSUVO36kpKSP3wMIcRfzx1z5xscHMyWLVvMr3///Xe6dOmCTqfj
kUceYcyYMURGRgKVp4QMCwtj8uTJdOrUCZ1Ox6OPPmp+3B7A999/z4MPPojBYKBly5b897//Na+r
aVzvsmXLeOihhxg/fjweHh5MmTKFZcuW0blzZ/P+Wq2WRYsW0ahRIwwGA2PHjjWvMxqNvPLKK3h6
ehIcHMz8+fNveCrLeZ98Ql9HR2r+ZhQ2AC0BA9AWmAX8v7J1J4H+gBfgAbwE/Aa8AHyH6Y7arWzb
YcCLQHZeHs888wzffPMNw4YNIzo62nyshIQEWrZsiV6vJyQkhMTERACWLl1qHgPdsGFDPv3001qf
p52dHY6Ojnh7e2NnZ0f37t1rvW9tZGRk8OSTT+Ll5UVwcLDFnbfRaLQY39yuXTtOnTpFly5dAGjR
ogUuLi6sWbOGnTt3Ur9+fWbNmkW9evUYMWIExcXF/POf/8TPzw8/Pz/GjRtnfrpU+fZz587F29sb
X19fli1bZj52ba+tEOIec7vTv9zChQuVr6+v+XWHDh3Ua6+9pkpKStSePXuUTqerNDa0/K7s4Ycf
ViEhIer48eOqoKBAhYWFqddff10ppdSpU6eUu7u72rx5s1JKqf/85z/K3d1dZWVlKaVqHte7dOlS
ZWNjo+bPn69KS0tVQUGBWrp0qerUqZO5nhqNRvXp00fl5OSotLQ05enpqbZs2WI+p9DQUJWenq6y
s7NV9+7dlVarrdXdZPk5XrlyRX0wZ47yd3RU+6q58z1QNhZ4L6j/gTLY2ioNqHxQV0A1BzW+7HUh
qG/L9ltWxZ3vUFB6ULtAOdvaqrNnz6phw4ap6OhopZRSP/zwg9Lr9eY70/T0dPOY3I0bN6oTJ04o
pZT673//q5ycnNSBAweUUte/E01PT1c6nU4NGzZMGY3G614fpUx3vv/617+qXFfxeKWlpap169Zq
6tSpqqSkRJ04cUIFBwerxMREpVTl8c0//fSTeXyzRqNRycnJFuXa2Nio119/XRUXF6uCggIVHR2t
OnbsqDIzM1VmZqZ68MEHzderfPuYmBh15coVtWnTJuXk5KQuXryolFK1vrZCiHvLHRO+ly9fVhqN
Rp09e1alpqYqGxsbi/G2gwcPNo8lvTZ8w8LC1DvvvGPedsGCBapnz55KKaXefffdShNAPProo+qz
zz677rjepUuXqoCAAIt9qwrfb7/91vw6PDxczZw5UymlVNeuXdWnn35qXrdt2zaLetek/BxdXV2V
q6urcnZ2VhpQHZyc1FeghoCKLgvMkaCeAtXNxUV563Tqg3nzlI1Go/4L6v9AeYIqrWWz87CyAFag
Ap2d1YkTJywCYuTIkWr8+PHXrb9Spg82H3zwgVKq5vAtLi5WzZo1U8uXL1ePPfaYGj58uDmAH3ro
IbVhw4Yq93v44YeVk5OT+Rq5urqqyZMnVzre999/X+l9nD59unr22WeVUko1atSo2vHNVYWvnZ2d
eYIRpZRq2LCh+cOdUkolJiaqoKAg8/aOjo4W77mXl5f64YcflFLqpq+tEOLudscMNXJycgJM8zOf
O3cONzc3HBwczOv9/f05efJktftXHCdacdxsamoqa9assZju8cqVK3Tr1o20tLQax/WWH/d6qhuj
evr0aYv969evf92yrlVx2FNxcTFr165l3syZfPfTTzjb2LDczo5T+fkojQZHoxFbW1uiJ0+mVClO
Y+pcFciN9ayr6YxPnTpV7TjbzZs389Zbb3H8+HGMRiP5+fk0b978usfbsWMHJSUlREZG8vTTT9Oz
Z0+ee+453n//fY4ePUqnTp2q3E+j0fDRRx8xfPjwGstPTU0lIyMDg8FgXlZaWmpuVq5u/HZ1PD09
LR5WkZGRUWkcc/kYbzB1RKvYQ7viv5GKarq2Qoh7yx0TvhXVq1ePCxcuUFBQYB7PmZaWVuvezRUF
BAQQGRlZ5fePp0+frnFcL1x/DGtN6tWrZ/GBoaYPD7VhZ2dHREQEERERPPPMM7i7uzNu3DimTp1K
SEgIEydOBEzfY/t5etK/pIR9QBqm8b91rimvpjMrAbKKi3Fzc7NYXt1Y56KiIp588klWrFjBE088
QZ06dejXr1+thllduXKFkhLTiGYHBwfWr19P165dadeuHQMHDkSv11+3jJr4+/vToEEDjh07Vu36
pKQkQkNDa1Xetf8myscxN2nSBDD9W/X19b2pelZ1bYUQ9547psNVRYGBgbRt25YpU6ZQUlLCd999
x4YNG2oMwur+yA8ePJj169ezdetWSktLKSwsZOfOnaSnp193XO/NUKamfADCw8P54IMPyMjI4OLF
i8ycOdPiHKZMmULXrl2vW15VbG1t0ev1NGjQgDFjxvDJJ5+wd+9elFLY2NgQWL8+XwAPAPWA1zFN
xlEI/F9ZGd7AKTBP5AFXJ/NYB7Ru2hS9Xm9xTiNGjGDp0qXs2LEDo9FIeno6R48epbi4mOLiYjw8
PNBqtWzevJmtW7fW6pp17tyZwsJCYmJiKCwsxGg0EhYWxvHjx687mUZtwr19+/a4uLgwa9YsCgoK
KC0t5ZdffmHfvn2Aafx2dHQ0SUlJKKXM45sBvL29SU5OrrH8gQMHMm3aNLKyssjKyuLtt982dw68
ntpcWyHEveeOCt+KwfT555/z3Xff4e7uTnR0NAMGDLBo6qtpnGzFcbT169cnISGB6dOn4+XlRUBA
AHPmzDH3OK5pXG9143GvPVZ1659//nl69OhB8+bNadOmDb1796ZOnTrmu+yTJ09W26RaztXV1WIc
67x58yodp02bNixevJixY8fi5ubG3/72N3Te3ix2dkYLrAeSgABMTcpflJXdHWgK+GDqCQ1Xxw8v
cHFh9IQJlY7Vrl07li5dyrhx43B1dSUsLMw86cmHH35IeHg4bm5uxMfHVxpzW92HJ51Ox9atW/n+
++/x9fUlJCSEixcvsnfvXpYuXWp+OlJVxo4da3F92rVrV+l4derUYcOGDRw8eJDg4GA8PT0ZOXKk
eaKQ8ePHEx4eTo8ePdDr9Tz//PMUFhYCpg9IQ4cOxWAw8OWXX1b5b2LSpEm0bduW5s2b07x5c9q2
bWsxdremD401XduuXbtedwYwIcTdSaNqc+twBxgwYAChoaHExMTc7qrctM2bN/Piiy+ap1ps1aoV
O3bssPgu8lYpKioi0MuLTZcu3fDzgPcDvXU60jIzLT7wCCGEuDXuqDvfivbt20dycjJGo5HNmzez
bt06+vbte7urdUMKCwvZtGkTV65cIT09nbfeeov+/fub1//4449/SvAC2Nvb88GiRbUaI1xRGtDP
yYkPFi2S4BVCiD/JHRu+Z86coWvXruZpBT/55BNatGhxu6t1Q5RSTJkyBTc3N1q3bk3Tpk15++23
rXb8ARERvDptGp0cHdlfi+33A52cnHh16lQGlM1LLYQQ4ta7a5qdxc1bvWoVUaNG0cxoZHReHo9z
tZt7CabOVQtcXDis0fDBokUSvEII8SeT8P2LKB8jvGDmTA4cPoxHWZNyVnExrZs2ZfSECfTv31+a
moUQwgokfP+CcnJyzENp3Nzc/vA4WiGEEDdGwlcIIYSwsju2w5UQQghxr5LwFUIIIaxMwlcIIYSw
MglfIYQQwsruyKcaCSHEzcjJyeH8+fOA6VGO0pNf3KnkzlcIcVcrKioiPj6ezi1b4ufpSfcWLeje
ogV+np50btmS+Ph4iouLb3c1hbAgQ42EEHet8tnb7leK0bm59MFy9rb1wIK6dflFq5XZ28QdRcJX
CHFX+nDuXGZPmsTXBQW0uc62+zE9MOTVqVN5efx4a1RPiBpJs7MQ94iwsLAan318M1588UWmTZt2
S8u8FVavWsXsSZPYUxa8QcD2GraPBsbn5zM7OprVq1ZZrEtJSUGr1Zqf8d2rVy/i4uJuum4zZszg
+eefr9W2U6ZMITIyEsD8XGy5H/prkPAV4i4SFBSEk5MTLi4u+Pj48Oyzz3L58mUANBoNGo3mlh5v
4cKFTJo06ZaWWVFYWBharZZDhw5ZLO/Xrx9arZZdu3ZV2qeoqIioUaP4d0EBAWXLNGU/AFOAyGv2
2QT8E/g6P5+oUaNq/A5406ZN5kC8GW+88QaLFy+u1bYV36+AgAByc3Nv+Xso7kwSvkLcRTQaDRs2
bCA3N5cDBw6wb9++O/LOtLY0Gg2NGzdm+fLl5mXnz5/nu+++w8vLq8p91q5dSzOjkdY3cbw2QFOj
kbVr195chW8xa93llt/VizuHhK8QdylfX1969uzJ4cOHzctSUlLo1KkTOp2ORx991Dzspnfv3syf
P99i/+bNm5OQkADAuHHj8Pb2Rq/X07x5c44cOQLAsGHDiI6ONu+TkJBAy5Yt0ev1hISEkJiYCMCy
Zcto2LAhOp2O4OBgVq5cWevzGDRoEKtXrzYHUXx8PP3798fW1ta8TcV6LJg5ky55efhXUdYWYAaw
GnABWpUtDwPKG+RH5eXx6ssv4+npScOGDdm4caNFGRWb75OSknj44YdxdXXF09OTiAodtg4fPswj
jzyCu7s7Pj4+zJgxA7BsSi5v0l68eDF+fn74+voyZ86cKq/Dtc3fYWFhTJ48ucr3E+Dpp5+mXr16
uLq68vDDD5vfs/Lr9eKLL9KrVy/q1q3L3Llz8fHxsQjhtWvX0rJlyyrrIv58Er5C3GXKQ+rkyZNs
3ryZVq1amZevXLmSZcuWce7cOYqLi5k9ezZg+mO8YsUKcxk//fQTGRkZ9O7dm8TERHbv3s3x48fJ
yclhzZo1uLm5AZZN2Xv37mXo0KHMmTOHnJwcdu3aRVBQEJcvXyYqKootW7Zw6dIlvvvuuxv6o+7r
60toaKg5yOPi4hgyZIjFNuX1yMnJ4ccjR3iomrJ6AhOBCCAX+LF8f642S2cCGZmZ7Nq1i3379vHl
l19aNPVWPOfo6Gh69uzJxYsXSU9P5+WXXwYgNzeXv//97/Tq1YvTp0+TlJRE9+7dzftfa+fOnSQl
JbF161ZmzpzJ9u01fUN9VXx8fJXvJ5g+UCUlJZGZmUnr1q155plnKu0bHR1NXl4eL730Eu7u7mzd
utW8Pi4ujqFDh9aqHuLWk/AV4i6ilKJv374YDAY6d+5MWFgYEydOBEx/9IcPH05ISAgODg6Eh4dz
8OBBAPr06cOxY8dITk4GTH94IyIisLGxwdbWltzcXH799VeMRiONGzfGx8en0rFjY2MZMWKEOWR8
fX1p3LgxAFqtlp9//pmCggK8vb0JDQ29ofMaMmQIy5cv57fffuPixYt06NChynM/f/48nvb21Knp
GpX9VOcrwGBnh4ODAwaDgYkTJ1bb/GtnZ0dKSgrp6enY2dnx4IMPArBhwwZ8fX0ZN24cdnZ21K1b
l/bt25vrea2YmBgcHR1p1qwZzz77LPHx8TXU0ESj0fDss89W+X6C6QOVs7Mztra2xMTE8NNPP5Gb
m2te37dvXzp27AiAvb09Q4YMMX8Au3DhAlu3bmXQoEHXrYf4c0j4CnEX0Wg0JCQkkJ2dTUpKCvPn
z8fe3t68vmJoOjo6kpeXB2D+4x0XF4dSilWrVpmbRrt168bYsWMZM2YM3t7ejBo1yuKPeLlTp07R
sGHDSsudnZ1ZvXo1n3zyCb6+vjz22GMcPXr0hs6pf//+7Nixg48//rjSXe+tdhqwuaajU3VmzZqF
Uor27dvTrFkzli5dCphaHYKDg2t9TH//q43kAQEBZGRk1Gq/6t7P0tJSXn/9dUJCQtDr9TRo0ACA
rKwswHRNKx4T+P/t3Xl4VNXh//H3kH0byEI2skGiIPBjUUSoRPKgoBREwI0IAYtWK0KtLfwoFb5S
iCJlERfUyM/KDkpJDSCIAo1Aa9XI1wCBGrYQIBEChOxMEnJ+f0wyJiQBtHQK+nk9T55k5t575tw7
eVkEMqwAABnoSURBVPLJPXMWRo4cyfr16ykvL+f999/njjvuICQk5IrPQa4uha/IT8SYMWNYsWIF
W7Zswdvbm9tuu82xbcKECWRkZLBv3z6ys7OZM2dOo+MjIyM5ePBgk2UPGDCAjz/+mG+//ZYOHTpc
8VCbOl5eXgwcOJC33nqryZ7GPj4+lJeXExgYSIHNxvFLlHW5vsKhwLmqKkfTem5ubrP7hoSE8Pbb
b3PixAlSUlIYN24chw4dIioqisOHDzf9+k00O9d/jdzcXNq0aXOZWl7aypUrWbduHVu3bqWoqIgj
R44Al+7AFRERQa9evUhNTWX58uX/Vo9u+fcpfEV+RC71x7d3795YLBYmTpzY4O4yIyODzz//nKqq
Kry9vfH09MTFxcVRXl2Zjz32GO+++y7btm2jpqaGEydO8M0333Dq1CnS0tIoKyvDzc0NHx8fx/F1
nYguFXB1XnzxRT799NMm70S7devGxo0bqampodMNNzDjEuWEAjk03/R8A+Dq7k5paSmFhYW89NJL
zZa1Zs0ajh+3R32rVq2wWCy4uLgwePBg8vPzeeWVV7DZbJSUlPDFF18ATb8HycnJVFRUkJWVxeLF
i3n44YcvcQbfae79LC0txcPDg4CAAMrKyhwfPVzuuNGjRzN79mz27t3L8OHDr6gO8p+h8BX5EWmu
41Cd0aNHs2fPHkaNGuV4rri4mCeeeIKAgABiYmIICgpi0qRJjcq49dZbeffdd3n22Wdp1aoVCQkJ
5ObmUlNTw8svv0ybNm0IDAxkx44dvPnmm4C9eTYmJuaK7vTCwsIcn6leLCkpia5duxITE8PJsjJw
d2/2DvfB2u+BQI8mth/09SWhXz+6du1Kjx49uP/++5sdW5uRkUGvXr3w8/Pjvvvu49VXXyUmJgZf
X18++eQT1q9fT1hYGDfeeCPp6emNrlmdvn37EhcXx1133cWkSZO46667mtz34uOaez9Hjx5NdHQ0
bdq0oXPnzo5/rJrat77hw4eTm5vLsGHD8PT0bPKcxTk0vaTIT8iyZctYtGhRk5NX/Ce88MILBAcH
f+9m6Eux2WxEBwezsbj4e4/1/QoYZLWSW1CAu7v7VatTc3JycmjXrh3V1dW0aHFt3OvccMMNpKSk
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
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
<h1 id="Making-a-two-mode-network">Making a two-mode network<a class="anchor-link" href="#Making-a-two-mode-network">&#182;</a></h1>
</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>If you wish to study the relationships between 2 tags you can use the <a href="{{ site.baseurl }}/docs/RecordCollection#twoModeNetwork"><code>twoModeNetwork()</code></a> function which creates a two mode network showing the connections between the tags. For example to look at the connections between titles(<code>'TI'</code>) and subjects (<code>'WC'</code>)</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[37]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span class="n">ti_wc</span> <span class="o">=</span> <span class="n">RC</span><span class="o">.</span><span class="n">twoModeNetwork</span><span class="p">(</span><span class="s">&#39;WC&#39;</span><span class="p">,</span> <span class="s">&#39;title&#39;</span><span class="p">)</span>
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
<div class="prompt input_prompt">In&nbsp;[38]:</div>
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


<div class="output_png output_subarea ">
<img src="data:image/png;base64,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
AAAAAElFTkSuQmCC
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
<p><a href="{{ site.baseurl }}/docs/visual#quickVisual"><code>quickVisual()</code></a> makes a graph with the different types of nodes coloured differently and a couple other small visual tweaks from <em>networkx</em>'s <code>draw_spring</code>.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="Making-a-multi-mode-network">Making a multi-mode network<a class="anchor-link" href="#Making-a-multi-mode-network">&#182;</a></h1>
</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>For any number of tags the <a href="{{ site.baseurl }}/docs/RecordCollection#nModeNetwork"><code>nModeNetwork()</code></a> function will do the same thing as the <code>oneModeNetwork()</code> but with any number of tags and it will keep track of their types. So to look at the co-occurence of titles <code>'TI'</code>, WOS number <code>'UT'</code> and authors <code>'AU'</code>.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[39]:</div>
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


<div class="output_area"><div class="prompt output_prompt">Out[39]:</div>


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
<div class="prompt input_prompt">In&nbsp;[40]:</div>
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


<div class="output_png output_subarea ">
<img src="data:image/png;base64,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
1mVNZUJgExGBKvMzJemdIINfei/t37+d3LkHAauSPaqByBug16f/xCtXIPlaPEKgDgig1PnzpJ63
ex44Eh/PBx98kHUNl6Q3QI7qkd5b58+fp149D5488SVhHL8J7JaB2yOYPg00mpRPOHkSxoyBQYMg
adXR5ctxCg7mSkwMuZLXDXhoNExfsADv//u/N/OCJCmLyOCX3msXLlxg8uSfzTN3TSYTN+9e5+yz
p+h8fF7skXv7NvYzZ5JDqyX5AsglS5Ui6p9/aHjnDsUSF0szAXNk6EvvMBn8ktUxGo30GziQfYcO
mR+zU6mYNWWKxQXpbt++zby5c4k3GMyP1WvQQO6IJb2zZPBLkiRZGXlzV5IkycrI4JckSbIyMvgl
SZKsjAx+SZIkKyODX5IkycrI4JckSbIyMvglSZKsjAx+SZIkKyODX5IkycrI4JckSbIyMvglSZKs
jAx+SZIkKyODX5IkycrI4JckSbIyMvglSZKsjAx+SZIkKyODX5IkycrI4JckSbIyMvglSZKsjAx+
SZIkKyODX5IkycrI4JckSbIyMvglSZKsjAx+SZIkKyODX5IkycrI4JckSbIyMvglSZKsjAx+SZIk
KyODX5IkycrI4JckSbIyMvglSZKsjAx+SZIkKyODX5IkycrI4JckSbIyMvglSZKsjAx+SZIkKyOD
X5IkycrI4JckSbIyMvglSZKsjAx+SZIkKyODX5IkycrI4JckSbIyMvglSZKsjAx+SZIkKyODX5Ik
ycrI4JckSbIyMvglSZKsjAx+SZIkKyODX5IkycrI4JckSbIyMvglSZKsjAx+SZIkKyODX5IkycrI
4JckSbIyMvglSZKsjAx+SZIkK/P/t/3GxD1otsYAAAAASUVORK5CYII=
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
<p>Beware this can very easily produce hairballs</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[41]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span class="n">tags</span> <span class="o">=</span> <span class="n">mk</span><span class="o">.</span><span class="n">tagsAndNames</span> <span class="c">#All the tags, twice</span>
<span class="n">sillyMultiModeNet</span> <span class="o">=</span> <span class="n">RC</span><span class="o">.</span><span class="n">nModeNetwork</span><span class="p">(</span><span class="n">tags</span><span class="p">)</span>
<span class="n">mk</span><span class="o">.</span><span class="n">graphStats</span><span class="p">(</span><span class="n">sillyMultiModeNet</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt output_prompt">Out[41]:</div>


<div class="output_text output_subarea output_execute_result">
<pre>&apos;The graph has 1184 nodes, 59573 edges, 0 isolates, 1184 self loops, a density of 0.0850635 and a transitivity of 0.492152&apos;</pre>
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
<div class="prompt input_prompt">In&nbsp;[42]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span class="n">mkv</span><span class="o">.</span><span class="n">quickVisual</span><span class="p">(</span><span class="n">sillyMultiModeNet</span><span class="p">)</span>
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
<h1 id="Post-processing-graphs">Post processing graphs<a class="anchor-link" href="#Post-processing-graphs">&#182;</a></h1>
</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>If you wish to apply a well known algorithm or process to a graph <a href="https://networkx.github.io/documentation/networkx-1.9.1/"><em>networkx</em></a> is a good place to look as they do a good job at implementing  them.</p>
<p>One of the features it lacks though is pruning of graphs, <em>metaknowledge</em> has these capabilities. To remove edges outside of some weight range, use <a href="{{ site.baseurl }}/docs/metaknowledge#drop_edges"><code>drop_edges()</code></a>. For example if you wish to remove the self loops, edges with weight less than 2 and weight higher than 10 from <code>coCiteJournals</code>.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[43]:</div>
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


<div class="output_area"><div class="prompt output_prompt">Out[43]:</div>


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
<p>Then to remove all the isolates, i.e. nodes with degree less than 1, use <a href="{{ site.baseurl }}/docs/metaknowledge#drop_nodesByDegree"><code>drop_nodesByDegree()</code></a></p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[44]:</div>
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


<div class="output_area"><div class="prompt output_prompt">Out[44]:</div>


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
<p>Now before the processing the graph can be seen <a href="#Making-a-co-citation-network">here</a>. After the processing it looks like</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[45]:</div>
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
<img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAeAAAAFBCAYAAACvlHzeAAAABHNCSVQICAgIfAhkiAAAAAlwSFlz
AAALEgAACxIB0t1+/AAAIABJREFUeJzsnXlYlOX3xs/MMBszwwCzsO+IC6CICIrihrupuaOZlhaa
e6alZqWVlrkUuZtaagGaa/60MuvbZpZrbpUZlpSmogiurHP//hiYREBmg0E5n+t6L2XmXZ53eJn7
ec5znvsIAIAYhmEYhqlRhI5uAMMwDMPURViAGYZhGMYBsAAzDMMwjANgAWYYhmEYB8ACzDAMwzAO
gAWYYRiGYRwACzDDMAzDOAAWYIZhGIZxACzADMMwDOMAWIAZhmEYxgGwADMMwzCMA2ABZhiGYRgH
wALMMAzDMA6ABZhhGIZhHAALMMMwDMM4ABZghmEYhnEALMAMwzAM4wBYgBmGYRjGAbAAMwzDMIwD
YAFmGIZhGAfAAswwDMMwDoAFmGEYhmEcAAswwzAMwzgAFmCGYRiGcQAswAzDMAzjAFiAGYZhGMYB
sAAzDMMwjANgAWYYhmEYB8ACzDAMwzAOgAWYYRiGYRwACzDDMAzDOAAWYIZhGIZxACzADMMwDOMA
WIAZhmEYxgGwADMMwzCMA2ABZhiGYRgHwALMMAzDMA6ABZhhGIZhHAALMMMwDMM4ABZghmEYhnEA
LMAMwzAM4wBYgBmGYRjGAbAAMwzDMIwDYAFmGIZhGAfAAswwDMMwDoAFmGEYhmEcAAswwzAMwzgA
FmCGYRiGcQAswAzDMAzjAFiAGYZhGMYBsAAzDMMwjANgAWYYhmEYB8ACzDAMwzAOwMnRDWDqBrm5
uXT16lUiItJoNKRWqx3cIoZhGMfCI2Cm2sjPz6e0tDRKiIoiH52OEps0ocQmTchHp6OEqChKS0uj
goICRzeTYRjGIQgAwNGNYB4+Nqan08RRoygSoDE3blBP+i/cUkhEO4lomVJJJ4VCSlm5kgYlJTmu
sQzDMA6ABZixO+8uWkQLZs6kbXfuULMq9j1MRH2cnWnKa6/RhMmTa6J5DMMwtQIWYMaubExPp6kj
RtD3d+6Qv5nHZBJRa2dnmr9mDY+EGYapM7AAM3YjPz+fAvR62n39OkVbeOxhIurh4kKZWVkkkUiq
o3kMwzC1Ck7CYuzG1q1bKcJgsFh8iYiaEVG4wUBbt261d7MYhmFqJTwCZuxGQlQUPXvsGPW18vgt
RJQSFUXfHj1qz2YxDMPUSliAGbuQm5tLPjod5RQWWr24vJCI3MRiOp+VxeuEawG8dpthqhcOQTN2
4erVq6STSm1ydhETkVYioezsbHs1i7EQXrvNMDUHCzDDMERkzGAP0Otp7ahRNPnYMcopLKQ/b96k
P2/epGuFhfTssWO0JjmZ/HU62pie7ujmMswDD1tRMnZBo9FQVn4+FZJxJGsNhUR0paCA3N3d7dgy
xhxK127vqmTttpiI+hJR35s3jWu3R46kSxcu8NpthrEBHgEzdkGtVlPTRo1opw3n+ISIosPDea6x
htmYnk4LZs6k780wTiEyZqx/f/s2LXjpJR4JM4wNcBIWYzfS0tJoTXIy7b1506rjE1UqenrVKkpi
M44ag9duM4zj4BEwYzf69u1LJ4VCOmLFsYeJ6JRAQH37WruIibEGXrvNMI6DBZixG1KplFJWrqRH
5XLKtOC4TDL6QaesXMkjqRpm2bx5NMbKiAUR0ZibN2nZvHl2bBHD1B04BM3YHS7G8GDAa7cZxrHw
CJixOxMmT6b5a9dSDxcX6qhU0lYiKrrr/UIyul7FkXEOcf6aNSy+DoDXbjOMY2EBZqqFQUlJlJmV
RU+99x69ExVFrmIxBSoU5CeTkUogoJSoKMpv0oTeTEnhCkgMw9RJOATN1Ai5ubmUnZ1Nv/76K02Z
MoV++eUX2rJlCy1evJi+/vprRzevTlIagr5WWGjT2m0OQTOMdfAImKkR1Go1BQUFUbNmzejKlStE
RNSzZ0/69ddf6ffff3dw6+omvHabYRwLCzBTo2i1Wrp27RoVFRWRRCKhYcOG0dq1ax3drDrLmBde
oGVKpdXHL1OpaMwLL9ixRQxTd+AQNFPjeHh40M8//0xeXl7022+/Ufv27SkzM5PEYmsDoYy1sBEH
wzgOHgEzNY6npyddunSJiIgaNGhAoaGhtHv3bge3qm5SW9Zu5+bm0tmzZ+ns2bOUm5tr8/kY5kGA
BZipcTw8POjixYumn5966ilavXq1A1tUtxmUlERTXn+dWsvldNiM/Q8TUeuStdu2ZLBz6UOmrsMC
zNQ4Hh4ephEwEVH//v1p3759dP78eQe2qm5z99rtBLG40rXbiSqVXdZuc+lDhmEBZhzA3SFoIiKF
QkGDBg2iDz74wHGNYmhQUhL98uefdFQiobcaNTKt3Q5UKMhNLKaUqCh6etUqyszKsmnk++6iRTR1
xAjadf06fXHjBvWhsnVRS0sf7r15k3Zdv05TR46kdxctsvHuGKb2wfWAmRrHw8ODLly4UOa1p556
igYMGEDTp08noZD7hY7i448/po4dO9L27dtNa7eJiNzd3e2y1Oju0of+ZuxfWvqw9UsvkYe3N5u2
MA8V/E3H1Dj3hqCJiKKjo0mtVtP//vc/B7WKAUCLFy+m8ePHE9F/a7eDgoLsIr75+fk0cdQo2m6m
+JbiT0Tbbt+miaNG8Zww81DBAszUOPeGoImIBAIBJ2M5mK+//poMBgN16NChWs7PpQ8ZpiwswEyN
c28WdClDhgyhTz/9lK5eveqAVjFLliyhcePGkUAgqJbzc+lDhikLG3EwNc6lS5coIiKCsrKyyr03
dOhQat68OU2cONEBLau7ZGZmUlRUFGVmZpLSBmesyuDShwxTHh4BMzWOVqulnJwcKiwsLPdeaRia
+4U1y4oVK+jxxx+vFvEl4tKHDFMRLMBMjSMSiUij0VQ4Am7bti3l5eXRgQMHHNCyukleXh6tXr2a
xo4d6+imMEydggWYcQgVZUITGZOxRo4cSWvWrHFAq+om6enp1KxZMwoLC6u2a2g0GsrKz6fyMQ/z
KSSiKwUF5O7ubq9mMYxDYQFmHEJFmdClDB8+nDZv3kw3bUjYYcyjdOnRuHHjqvU6XPqQYcrDAszU
CPea7VeWCU1E5OXlRW3atKFNmzbVcCvrHj/++CPl5ORQt27dqv1aXPqQYcrCAsxUG/cz29/32Wf0
+eefV2qswGuCa4YlS5bQ2LFja8R9rG/fvnRSKKQjVhx7mIhOCQTUt29fezeLYRwGCzBTLVRltj8/
K4v+2bKlUrP9rl270rlz5+jUqVMOaH3d4OLFi7R7924aMWJEjVyvtpQ+ZJjagmjWrFmzHN0I5sEh
NzeXLly4QNeuXSOhUEgymazcPu8uWkSzJ06kT27dohcKCqghle3piYioIRGNMBiofX4+jfz0UxLJ
5RTXsqVpH6FQSNeuXaMDBw5Qly5dqvu26iQLFy6kgIAA6t+/f41dMyIigkRyOY345htqW1xM3lXs
f5iIupSUPhz59NM10USGqTnA1EpycnKQkZGBjIwM5OTkOLQteXl5SE1NResmTaAQixGoVCJQqYRC
LEbrJk2QmpqK/Px8AEB6Whr85HKcIwLM3M4Rwc/ZGelpaWWum5GRAZ1Oh7y8PEfc9kNNfn4+vLy8
cPz48Rq/9oULF+Dm6gqNszMSlUpsIULhXc9DARE2E6GDSgUPF5dyzwXDPCywANciLBG6miI9LQ0e
Li7oqFJhawVflFuIkKhUwsPFBRvWr4eHiwsOWyC+pdshIni4uJS7v8TERGzcuLHCttWmTsqDRlpa
Gtq1a1fj1y0oKEBCQgJmz56N/Px8pKWlISEqCgqxGAEKBQIUCijEYiRERSEtLa3Gn3eGqUlYgGsJ
lghdTY0IUhYuhJ9cjkNmCqi3RIIGEonF4lu6dVAqkXbPvaWmpqJTp06mn2tjJ+VBpFWrVti8eXON
X3fKlCno1q0biouLy7yek5ODs2fP4uzZs9yZYuoMLMC1AEuFzs/ZGSkLF1Zrm6wNJXsTId1KAd5M
hISoqDLtuHPnDjQaDc6ePVsrOykPIkeOHIGvry8KCwtr9LpbtmxBYGAgrly5Uu3X4ugI8yDAAuxg
7Dlnai/y8vJsCyUTId+KYwuIoBCLy31hTpgwAV07dqx1nZQHlREjRmDOnDk1es3Tp09Dp9Ph4MGD
1XYNjo4wDxoswA7EZqGrYM7UHqSmpiJRqbQ+lEyENCuPDVAocPbs2TLtmTdvHrQCQa3qpDyoXLly
Ba6urrh8+XKNXfPmzZuIiIjAypUrq+0aHB1hHkRYgB2IzUJXwZypreTk5KB5gwbYYmWbTKFkOwlw
be2kPKi8+eabGD58eI1dz2AwYOjQoRg+fDgMBkO1XKM2TuEwjDlwPWAHkhAVRc8eO0bWevtsIaKU
qCj69ujRCt8vKCiga9euUXZ2Nl27dq3S/2dlZVFGRgZdy8yk6/n5RER0i8i2uq1EdJ6ILHHtraje
a1paGq1JTqa9VvpCJyqV9PR771FSUpJVxz9MFBcXU3BwMG3ZsoViYmJq5JrLly+nFStW0P79+8nZ
2dnu59+Ynk5TR4yg7+/cIX8zj8kkotbOzjR/zRoaxM8F40BYgB2EvQqUuwiF1KFrV7p9+zbl5OTQ
9evX6fr163Tjxg0qLCwkpVJJzs7OpFAoSC6Xk1wuJ5lMRlKplCQSCV2+fJl+//lniiSi54qKKJyI
uhDRnzbeXyAR/Y+Igiw4pqIORXV3UuoS27dvp3nz5tH+/ftr5HoHDhygRx55hH744QcKDQ21+/nz
8/MpQK+n3devU7SFxx4moh4uLpSZlcXuWozDsKU+NmMDpgLlFRSlNxcxESkNBvruu+9MwiqXy8nf
35+USiWpVCqSSCQkkUhILBaX+/fkzz/TPz//TF8VFVGzknOetcvdWce9Zvu5ubl09JdfqJcN5+xF
RMNPnaLc3Nw6X0VnyZIl1V71qJQrV67QgAEDaNWqVdUivkREW7dupQiDwWLxJSJqRkThBgNt3bqV
oyOMw2ABfsBxcnKiNp06UXFxMeXk5FBOTg5dvXqVMjIy6MaNG6RUKsnV1bXcdvnSJTr+7bf0U1FR
mdCdhoiyyDi6FlvZpkIiukJEllRtrchs316dFK1EQtnZ2XVagH/55Rc6deoUDRgwoNqvVVxcTI89
9hglJSXRo48+Wm3XWTZvHj1rQ8nKMTdvUsq8eSzAjMNgAXYQdxcot0XosouK6NixY9S6dWvq3r07
xcfHU6NGjUgoFFJxcTHduHHDJMylW1ZWFr0wYQLtvUd8iYxztk2JaCeR1WHfT4gogsyf/80koh4i
ESm0Wrpy5Qp5e1flEMxYypIlSyg5OblGwq2vvvoq5efn05w5c6rtGhwdYR4GWIAdgMFgoMOHD5O7
QkE7c3JsErrYJk1o6fr1tH//ftq3bx/Nnz+fsrKyKC4ujlq2bEnx8fEUFxdHgYGBpuPS0tIo2smp
0tDdGCJaRtYL8DtE9AcZR7XNqtj3MBnnnIePHUvuej3FxcXR9u3bqVmzZnbrpFwpKCB3d0vG4w8X
ubm5lJaWVmVlqdzcXLp69SoRGTuI1ojS7t27ac2aNXTo0CFycqq+rxeOjjAPBY5Nwq5b/Pvvv5g7
dy5CQkLQuHFjDB8+HB1sWYakUlW4DOnSpUvYsWMHXnjhBbRp0wYKhQIRERFITk7GBx98gOb16993
mVEeGc00bDHi+LDk38SSNZgVme03J4KcCEqFAq6urrh69Sq2bNkCrVaLTZs2AQBaN2li+5Koe9y1
6hrvvPMOBg0aVOF79jSv+PPPP6HX6/Hdd9/Zs/kVkpGRgUAb/nYqW/bGMDUJCzCq17auqKgIu3bt
wqOPPgpXV1c89dRT+Omnn2AwGGpsjWtBQQEOHjyIlJQU9OnTB9J7BLGiLZ0IfkSWm1/Qf1aU+WQ0
5EgggoIIASWbMxE8pFIIBAIIBAKo1WrIZDLEx8ejuLgYR44cgZ+fH2bPno2PPvrItrXSlXRS6grF
xcWoV69ehaJoT/OKO3fuoFmzZli0aFF13UoZcnJyoBCLUWCD+FbmvMYwNUWdFeDqtq07d+4cXnnl
Ffj5+aF58+ZYtWoVrl+/Xm6/mraitGTkkFIiqGYbHJQcU9H7OUQ4W7I1I8KCBQvQsmVLiEQivPzy
y4iMjIRMJsPMmTMBGEvWxcXFYcCAAWzEYQOffvopoqKiyplg2Nu8Ijk5Gf379682s42K4OgI86BT
JwW4umzrCgoKsHXrVnTr1g3u7u4YO3Ysfv755yqPq0knH0tDd+lUdSi5Q8k+5hRhOEQEhVCIHTt2
ID09HQKBAB988AHCw8ORkJAAuVyOzz//HABw+/ZtDB48GMHBwfCVydiK0gq6d++ONWvWlHnN3p2+
Dz74APXr10dubm5N3RYAOzjJ1fHoCON46pwAV4fYnTlzBtOmTYOnpycSEhKwbt063Lp1y6J2paam
QiEUoq1MVqnQxQmF0NgoKtaE7ioKJWuJICVCXMl75hRfOEcEDREERPDw8MC+ffsgFArRoUMHfPXV
V/Dz84OPjw/UajXOnTsHwGhl+Prrr0OjVsNHKmW7QQs4c+YMtFotbt++bXrN3tMeP//8M7RaLU6e
PFnj98c2pcyDTp0SYHv2/O/cuYPU1FS0b98eOp0Ozz33HH799Ver27Zx40ZER0cjNTW1TIFyL7EY
cqEQCVFRGDduHFq3bm3rx2BT6C6HCEuJEBEUhFkzZ0IrEmF7yetVfeFpiCAigkgkgkwmg0QigbOz
M8RiMW7cuIFBgwZh5MiRUCgUaNKkCfLy8kxt3rJlC1RKJdzlciQqlZWPxlUqNtwv4dlnn8Xzzz9f
5jV7+o9fu3YNoaGh+OijjxxxezAYDHhi+HBoyYpcBY6OMLWAOiPA9uotnzp1CpMmTYJWq0XHjh2x
cePGMkJhDQUFBQgNDcXevXtNr5UWKJ85cyaSk5MBAIWFhQgKCsK+fftsup4tX8J5RAgmgooIMoEA
XmIxdGQcDUcSYQP9Nxq+O9tZ5eQEgUAAoVBoSr7q2LEjhEIhiAiPP/44MjMzodFoMHXqVLi7u2P0
6NFl2l1ax7Z///6ICQuDhAieJR0VhViMhKgopKWl8agGxgpE7u7u+PPPP8u8bq95U4PBgN69e2Pc
uHEOub+8vDw8+eSTiIyMxEvTp3MxBuaBpM4IsK09/wSpFGFhYfDy8sKMGTOQkZFht7atWLECnTp1
qvC9TZs2oU+fPqafly1bhl69etl0PWs7I+lkDD3HEVU6dx5LxixnZYkoezg7Qy6XQyAQ4K233gIR
wd3dHUQEiUSCsLAwkyA3aNAAEydORI8ePdC2bVu4u7tjw4YNZdpempzVvHlzEBEaNmyIs2fPcibr
PaxYsQK9e/cu81rp9ENVGfD320ozh2fNmoW4uDiHdHbOnz+PuLg49OvXDzdu3ADwX14HR0eYB4k6
I8D26Pk3DgpCYWGhXdt169YteHt749ChQxW+v2/fPsTGxpp+vn37Njw8PHDq1CmbrmtpOD6FCL5k
fkZ0abhZLpdj1apVcHJyQkhICNzd3aHRaCAQCODu7g6BQAAnJyfI5XLodDqIxWK4uLhg+fLlcHd3
h6urK44fP16m7bdv30a9evVMYn769GmbPouHDYPBgIiICHzxxRdlXrfX2llfmQxarRaZmZk1fm8/
/vgjfHx88Nprr5XLuM7Pz0daWlqZKRyOjjC1mTohwPbs+dt7pDV37lwMHDiw0vf/+usv+Pj4lHlt
zpw5dqnpam5CWjoRfMjyeTYtkSnLefr06SAiaLVaTJgwAUQET09P+Pr6gohAROjcuTPmzJkDsVgM
gUCA0aNHQ6fTISQkpNzn3rFjRwgEAigUihqtb/sg8L///Q8NGzYsJ1D2EmCtQID169fX+H2tXbsW
Wq0WO3bsqHLf0ikcjo4wtZk6IcC11TXn6tWr0Gq19x3B5efnQywWo6ioyPTatWvX4O7ubsoUtoWq
QndpZAwnWzt3LidjqPns2bOmUeulS5cgl8vRo0cPREREQCqVmkR44sSJuHDhAjw8PCAUCuHm5gZ/
f3/06dOnjKAEBweDiDBz5kwQEVJTU23+LOxBdZq6mEvfvn2xdOnScq/by7xCLhTW6L0VFBRgwoQJ
qFevHn755Zcauy7DVDcswA4U4KlTp2LUqFFV7ufh4YHz58+XeW3KlCmYNGmSXdpRWehOQoQwPz8k
SKVWf2YtRSKTuAYGBoLIuAQpPj4eQUFBmDlzJqRSKVxdXUFkzJBu0aIFDh8+DBcXF3h6eoKIoFQq
MXv2bJN5ioQIOiIEKpWQCgRwFYnQv39/mxPirKG6TV0s4dy5c3Bzc6vQ9AUAWjVubHsSVpMmNXIv
AJCVlYX27duja9euuHbtWo1dl2FqgjohwLXRtu7vv/+Gu7t7OWGtiOjoaBw4cKDMa+fPn4ebmxuu
XLlil/aUcnforkGDBogJC7P5C1stFMLJyQkNGjQwibFMJsPUqVPh5eUFoVCIl156yTQfLBKJ4O7u
juTkZPTp0wcTJ04ElYymEySSShPAWgqFcBGLsX7dOrt+JvejukxdrGX69OmYMGFCudd/+eUXTJky
BS4uLmgpFFr9+2x/1zKk6ubYsWMICgrC888/XyYCxDAPC3VCgAH7JGE19PW1m+A99dRTmDZtmln7
9uzZE9u2bavwHLNmzbJLe+4lJycH7dq1g1wksnnuXFIiuh4eHggJCYFarTYJcWhoKAQCAXbt2mXK
iPb29oZUKoVYLIa7uzueefppeIrFZieA6QQCvPryy9XyudxNTTqYmcOdO3eg0+lMUxq5ubl47733
0LJlS3h5eWHatGk4ceLEA2FesWnTJmi12loztcAw1UGdEWBblyG1dHJCixYt4OLigt69e2Pz5s1W
hzt//fVXaLVaZGdnm7X/6NGjsWTJknKvnz59GjqdDjdv3rSqHfdybyhV7+QEnQ3iW7r5OztDIpGA
iODk5ISPP/4YRARnZ2fTkiQiQmxsLEJDQ+Hp6Yng4GCoVCoIiKwyWtAKBHhj7ly7fC4VUdMe3ubw
wQcfoHPnzvj2228xfPhwqNVq9OnTBzt37iyTvV8b215KcXExXnzxRQQEBODw4cPVei2GcTR1RoBt
NeKQE8HFxQUrV67EmjVr0K5dO1OY9Ntvv7XIhL5fv36YN2+e2fu/9tprmD59eqXnSklJMftclVFR
KDWDCIF2EOAAhQKRkZFo1aoViAiurq7QarUQiURo3rw5fH19ERISYhJioVCIxMREeHh4QE7WJ4A5
CwTVMoKqjRaI//zzD7y9veHl5YWGDRtiwYIFuHjxYqX717bRO2CMujzyyCNo06YNLl26VK3XYpja
QJ0RYMC2nv/69evx2GOPQSgUIiQkBAcPHsS5c+cwd+5cNGzYEIGBgZg5c2aVa1IPHDgAHx8fi7yi
lyxZgj59+lSYWXvgwAH4+/ujoKDAqs8EqPzLOIeM3s+2zp1LiKBSqaDT6SAUCiGXy9G9e3cQEerV
qweVSoW+fftiyJAhUKlUkEgkEIlEEIvFiLXh2m2dnaHRaDB79my7Vumxp52jLeTn52PLli3o0aMH
VCoVVCoV9u3bZ/a9jh41Ckqh8L7mFXFCYY3MX58+fRoNGjTAmDFjbHqWGeZBok4JMGB7z//cuXOI
i4uDQCBA+/btcenSJRgMBhw+fBiTJk2Ch4cHYmNjsXjxYmRlZZW5tsFgQIcOHbBq1aoq23l3ONhZ
JIKHSFRpZm2HDh2wzsrEo6o6Ja2JbJ47VxGhQYMGkEqlcHNzg5OTU5l54NJRb8eOHeHp6QmdToem
TZvCV622+dotwsMRFxeHpKSkMkUJbMHRZfBOnjyJyZMnQ6/Xo02bNli3bh0GDhyIhRaMUP/991/o
dDocOHCgwgx4ZycnuDk54Z133qn2Od/du3dDp9OZ9XfBMA8TdU6AAfvY1n399dfw8fGBSCTCqFGj
TF9ShYWF2L17NwYPHgwXFxf07NkTmzZtwp07d7Bnzx6EhYVV6aZlaWbtnj17EB4ejuLiYos+B3NC
qalkLEVordjEkjF0X7rESCQSwcXFBWKxGDKZDBqNBhqNBl5eXrjbppLIaGVpD/OUf//9F0OGDEHz
5s3Nyjq/H44ydcnJycHKlSsRGxsLb29vzJgxA7///jsAo5i6urqanVMAAAMHDiyXBFiaAX/w4EH4
+Pjgk08+Mft81mAwGPDGG2/A29sb33//fbVei2FqI3VSgAH72dYtXboUzs7OcHZ2xpIlS8qE/65f
v44PPvgAiYmJcHNzg0ajwaxZs+4rlNaM0N9ZsADR0dFmf2EWFhZi//796N+/f5VLUvLIWOvXlrlz
lUqFHTt2QCwWg4jgKhJBQsbkKi0ZQ9QaiQTJycmm8LNAIICHSGS1yJVu/s7OOHv2LAwGA+bMmQM/
Pz+bkntqck25wWDA119/jWHDhkGtVqNfv37YtWtXuQ7c7NmzTQU7zOGTTz5BaGhohRGBoqIiJCYm
YsaMGWafzxpu3bqFQYMGISYmBn///Xe1Xothait1VoDvxlbbuvz8fIwaNQoikQg+Pj748ssvy+2z
bNky+Pj4ICIiAgEBAZgxY0a58oW2zFFPnDAB8fHxlbYxIyMDK1asQN++feHq6orGjRsjWKczK5Sa
TgQ/sjwTWUP/hZhDgoPhKpVWWchBftcxWhtFLocIrkR45JFHTNMBW7ZsgVarxccff2zx77n0c6xu
Af7777/x+uuvIyQkBOHh4Vi0aBEuX75c4b75+fnw8vIq55ddGbm5ufDz88NXX31V4fsvvvgiEhMT
q3Xd7V9//YWoqCg8/vjjdpsWYJgHERZgO3Lp0iW0a9cOAoEAsbGxplJwd5cbNBgMOHr0KCZPngxP
T0/ExMQgJSUFmZmZNmfWBgcH47vvvgNg7FRs3boVzzzzDEJCQuDh4YHHH38c69evx4ULFywOpaaU
iLC5I3MtGYsxUMm/GguO1QuFEJFxZGxpAlgeGcPmrcmYQHb3KDsiIACpqan46aef4OfnZ1VyVnWZ
uuTl5eEM2kkuAAAgAElEQVTjjz9Gt27d4ObmhlGjRuHAgQNVti89PR1t27Y1u/1jx47FyJEjK3xv
586d8PPzq9YM5K+//hqenp5YtGiRXRPjGOZBhAXYjpT6AG/duhWBgYEQCoUYPHgw3n77bXTs2LHc
/kVFRfj8888xdOhQyOVyxNsQcu2gVKJnz56oV68e4uPjoVQq0blzZyxYsADHjh2zizF/OhnD0YlE
lc6dl45i5XI5pk2bBioRX2sKOcjJsgSw0vZ1pMpH2S2EQuiUSixftszs5Kx7/Z3tmYR1/PhxTJo0
CTqdDu3atcOGDRssypBv1aoVNm/ebNa++/btg5eXV4VzxRkZGdDr9fjhhx/MvrYlGAwGLFmyBHq9
Hnv27KmWazyo1Ab/cMYxsADbyP18gBv5+UEmk4GIMHr06PvO/cZHRNj8pa6TyaBQKLBq1SpkZWXh
9OnT+Prrr5GWloZFixZhypQpeOyxx9ChQweEhIRYZbKRT8YCDQlUdoQpFQjgIhBAp9NBLpdDoVBA
q9VC5eRk0/xxjJn7WzpC1wkEeOqJJzBo0KAKk7Pu93ut7++PNjKZ1b+r9kolRowYgZiYGPj6+mLm
zJn4448/LH72jhw5Al9fX7NKZObl5aFhw4YVht5v376Npk2b4t1337W4DeaQl5eHkSNHIjw83Kr7
fBipTf7hjONgAbYBc7KVW0skUAiFEAoE0Gq12Lp1a7nz2CuzVioQmJb5yOVyBAcHo3Xr1hgwYAAm
TJiAN954A+vWrcOePXvwww8/QOHkZFMoNYsIYjKGmeVyOYRCIe5eWiQQCGxax9u85PxVCbgtc9RO
IpHJHjM1NRXFxcVV/l7TyfYKUf369cOnn35qmmu1ZhQ0YsQIzJkzx6x9Z82ahV69elUY9h05ciSS
kpKqJSR84cIFtGzZEn369Km0QERdo7b5hzOOgwXYSizNVvaVyxFevz6EQiHCw8Nx4sQJ07nsldjj
IRJhwIABkMvlmDVrFt5//31s2rQJu3btwtdff41Dhw7h119/RWZmJq5evYpWkZE2j7pdhUIIhUJT
aUGBQGAa9auEQqy38fxeSuV9Q9j2yNIODAxE27ZtIRKJoJBK4SESVVuNZE8nJ9N6V1tGQVeuXIGr
q6tZ87WnTp2CVqutMNt49erVaNiwIW7cuGHlX0Ll/PTTT/D19cXs2bMtXiL3sFIbHcgYx8ECbAW2
ZCvPmzcPDRo0MInWlStX7CbAXmIxxo8fj9jYWERGRmL48OHo378/unXrhoSEBERHR6N+/frw9fWF
m5sbRCKRzSNUjUaD0tFuVFQUXAQCSOm/0LSCjAlRqWQMX1ty/lIXLYlQCC1VHF62dZ1yvFgMT09P
CIVCxMbGWuQ7nUIE30raVdGXqbdEAjeVCidOnLB5FDRv3jwMGzasyme1uLgY8fHxWLZsWbn3jhw5
Aq1WWy01dtetWwetVlthEZG6Sm324GYcAwuwhdjLB3jjxo1wc3ODWCxGUlIS5EKhzZm1UjKGgps2
bQqpVIrFixfj1KlTlS4psYc/NhFBLBZDTnTfJUaJZBypplt4nbuXMkmJ0JgI6++6hj2culyI0Lhx
Y6t8p9PJ2NGIo8oT0+42dUlLS4ObSgVfmczqUVBRURECAgJw8ODBKp/XpUuXolWrVuVGoNnZ2QgO
DkZ6erptfxD3UFhYiEmTJiE0NBQnT56067kfZGqjfzjjeFiALcQePsBr167F1q1bMWLECKhUKlCJ
CNgjHDx8+HBs27YNLVq0QKNGjUxVhdq2bYspU6Zg48aNJmMKwLxeeQ4ZCzNklPzflKUsl0OjVlu0
xMiPjCNHSwRYQcaRsI7+W1Lkctfr9iiXKJFIrI4G5BMhVCCAq0gEuVAIP7nc2O4KTF3S09LgLZHY
NAravn074uLiqnxWMzMzKxzhFhcXo2fPnpg4caJd/zauXLmCxMREdO7c2SJXrrpAbfEPZ2oXLMAW
Yo8lKGqhEJ06dcLbb7+N3377DdnZ2YiNjbUpHBxLhPDwcOh0OggEAgQGBkKpVCI7OxtXrlzBZ599
htdffx29e/eGt7c3NBoNunTpgpkzZ+LpJ58sNyK7dz1tYMnmTEZzCyeBAI8PHWpVqUA/Mm8kXDqq
30AVj6obk+1mHSDj3LlKILD596qVSPD0009j0aJFICLs2bOn3Fpfe4yCEhMT8eGHH973OTUYDHjk
kUcwe/bscu/NnTsX8fHxdh1RHT9+HMHBwZg6dWq1mng8qDjaP5ypnbAAW0B1+gDn5eVBp1TaVHov
KioK9erVw5tvvokuXbpAIBBAKBSiS5cuOHDgQJnrnT9/Htu3b8eLL76ILl26wEkkMoWRJ1PV62lj
ySjGb1grJlT1nPBmMi53quz9DCL42/C7KN00ZMy2tvX3KhcKEeLhAalAAC0ZDUXkQiGiQ0OxYcMG
rF+/3uZR0IIFC+Dh4VFlLeqNGzciPDy8nMju3bsXXl5e+Oeff+zzR4H/3MWq6hTUVRzlH87UfliA
LcBeyVK+Mhk2b96Mn3/+GWfOnMH58+eRk5ODDz/80OokjenTpsHX1xe9e/dG48aNERcXh+XLl8PN
zQ316tWDoGQZ1HPPPVcuPPjNN9/A29sbAwcOhNbVFTqqvpCySUzIuJ74fvvEEmH4fd63V7lEKRF0
VXhim7PpibCcKu6wxBFBTbZPMwRpNHjppZfu+5xevXoVXl5e5Uw1/v77b3h6elZolWoNxcXFeOml
l+Dv749Dhw7Z5ZwPI9VtX8pGHg8uLMAWYK8/JC0RtFotvLy84OHhAXd3dyiVSgiFQohLRk/mCqCn
WIw+PXti+fLlWLZsGVq3bg0fHx888cQT8PLygpubG5577jkcO3YMw4cPh4uLC4RCIRo3boyPPvoI
169fR2hoKMaPHw8vT0/rOgBkeXJVVaPbQyWC5lvFue1VLtEeoewAIpyt5L0cMkYM7DFffa+H+L2M
GDEC48aNK/Nafn4+WrZsiTfeeMMufwu5ubno1asXWrdujYsXL9rlnA8r1SHAbOTxcCAAAGLMIjc3
l3x0OrpWWEhiK89RSERqoZCmvfIKXb16lf7++2/Tlp2dTV5eXiQRi+nSuXPUWCCgyYWF1IuInO46
/hMiekcqpZNE1L5bNwoMCqLbt2/TrVu36Pbt25SRkUG//PILubu7U15eHuXm5pJYLCaBQEAFBQUk
kUjIYDBQUVERERGJRCIiIpIT0TfFxRRt4T0dJqIeRJRJRBILPgc3IjpPROp73sskotZENJ+IQqs4
dxoRrSGivRa2uZSWIhGdkMmo8NYtuklk0++1svshIjpLRIlE9KeV5y/FUySi/WfOUFBQUIXvf/nl
l/Tkk0/SqVOnSKVSmV6fOHEi/fXXX7Rt2zYSCoU2teHMmTPUu3dvatu2LaWkpJBEYu5vvW5ir+8N
N7GYzmdl0WeffkoTR42iSIDG3LhBPans98NOIlqmVNJJoZBSVq6kQUlJ9rgNpjpwdA/gQcMeyRRa
iQSenp548skn8fHHH5vCRnl5ecjIyMA333yDDz74AElJSQjSaCATCKArGRmXZgAHBQVh8ODBmD59
OpYtW4adO3fi6NGjuHLlCgwGA/766y80bdoUepkMUiJ4ikTQkXGeMq5RIyxfvhzvv/8+ZDKZycEq
zob7MiekbM6IsaKw9v3ObQ8jDrFYbJcs9KrmqwNtHAGBjNMXlVVRun37NkJCQrBz584yr6elpSEk
JATXrl2z+fn/9NNPodfrsWLFCpvPVZewVxIWG3k8XLAAW4itywlaOjlBoVBg2LBhmDlzJrp27Qql
Uol27drhrbfewqlTp8pZAt5dLjEtLQ16vR4ikQgxMTGYNm0akpOT0a1bN0RERMDV1RUSsRgKoRDx
IlGlSVQJEgkUAgE8PDwwd+5cxNSvX60CdD8BNq2XpYrXCld1bmutKLVEkInFcHZ2Nhpx2HD/VXVA
7DVffb9EnBdeeAGDBg0q81qpC9bRo0dteu4NBgPeeusteHl5mSpuMeaTmpqKtnK59c+XSoUJ48ez
kcdDBguwhdhjKcnZs2cxY8YM6HQ69OzZEzt37sQnn3yC0aNHw9/fH4GBgRgzZgz+7//+r8LKOEVF
RXjnnXfg7OwMqVSKF198EXfu3AFgudWdlgix0dGQC4W2Z2mWCI25+0vJKJwKMgpsGlWcGW3OuS0t
xuBHhFlkzIDu3KkTXnjhBauMOEy/10rafvdmj/nqFo0aVfhcHjlyBDqdrsx87PXr19GgQQO8//77
Nj3zt27dwuDBgxEdHY3MzEybzlUXOXPmDLp37w6FUGj186UvMXNhI4+HCxZgK7CXpdzt27fx3nvv
ITw8HBEREVi9ejVu3bqFkydPYt68eWjbti1UKhW6deuGxYsXlws95ubmIjk5GWKxGK6urhgzZoxV
7XIjgocdsoAD6P5JSHebeWwmY8j7LJkn2vc7d+mWTsZEp/Z0H1cqKjvKvtvRq3HjxvCWSqstCc1W
28xYIkglEnTv3h1btmwxfaEWFhYiOjq6jNAaDAYMHDgQTz/9tE3P+rlz59C0aVM89thjVZZtZMpy
48YNTJs2DRqNBvPmzcOECROsWzfv7Izx48axkcdDCAuwldhzLsZgMOCLL75Ajx49oNPp8OKLL5rK
4127dg2bNm3CE088AQ8PDzRo0ADPPfccvvzyS9MXcEZGBlq3bm31CG47kVWlCasSycrMPBRE8CLC
ODLfH7oyAb5b2LPIKMBr6L9yiQEl2/1G2c3JKMAqlQpysbjanL1sna/WknEOeGhSEhISEqDX6/Hc
c89hypQpSExMLDN18c477yA6OtoUGbGGb7/9Fp6enpg/f361VEp6WDEYDNiwYQN8fHzw+OOP459/
/sG8efPg6+uLqc8+a9X3Bht5PJywANtAqaF+olJplg+wOZw+fRrjxo2Dm5sbhgwZUsZAo7i4GAcP
HsTs2bMRGxsLtVqNvn37YvXq1Vi6dCnaWTnHlEPGcLDN85P032g2nao28zDXH/rec9/PpcuT/iv8
kENG0a5qlL2ZCO5iMYRCodG8RCCAnIwjzsp+r7Fmtv3ezdr56tJR9t2RlNOnT2PUqFEQCARo2rQp
Vq9ejevXr+P777+HXq+vNFnLHJYvXw69Xo/PPvvM6nPURQ4ePIiWLVsiJiYGP/zwA/Lz8zFixAhE
RUWZqlFZ+r3BRh4PLyzANpKfn4+0tDQkREVBIRYjQKFAgEJRoQ+wJVy7dg0LFy5EQEAA4uPjsXHj
xnKF1y9duoT169dj0KBBcBWJbOohR5L9soCtmY+93yjy7nPbU9jvPk5C/xV9IDJmRisUCrgKhZCQ
cfSpKdlPRQQREW5a+VnZ+vmUzunl5eWhY8eOePPNN7Fjxw707t0barUazs7OVo9a8/PzkZycjEaN
GuHMmTMWH19XuXTpEkaOHAlPT0+sWbMGxcXFyM7ORvv27dGrV69y5R4t+d6obiMPxnGwANuRu7OV
7dXTLCwsxJYtW9CmTRv4+flh3rx5uHr1arnr2tpDXk9kUxZwWzKGd20d4VX0fmmGsb2F/e5NQwQn
JyeTAAuFQri7u0Oj0UAul0Or1ZrqHBMZRdiWDks3IijJ2Fkwd766zGeiVGL06NFo2rSpqWNWWFiI
+Ph4JCYmIiwsDA0aNMD8+fPNqhkMABcvXkSrVq3Qu3dvXL9+3S7P78NOQUEB3n77bWi1WkyePNn0
d3/mzBmEhYVh8uTJVXpjV/W9wQL88MIC/ABx+PBhDBs2DK6urhg9erSpyo09/kDzyBjCtdqLmowi
rLHhHBVlEpe+/iHZX9jv3nQCAQQCAXr06IH169dDq9UiMjISKpUKEokEvr6+kEgkZX6OFYnKJJZZ
cr+lwppGls1Xl26bieAmEuHw4cOm52PatGno1KkTioqKYDAY8N133+GJJ56AWq1Gnz598H//93/l
oiilHDx4EH5+fnjllVfKlS5kKubzzz9Hw4YN0blz5zIVp7755ht4eHhg5cqVdrlOaQe7OpewMY6B
BfgB5N9//8Urr7wCDw8PdO3aFWvXrkWgQmFzD9lNJIJeKLRK5D4kY1JVSxuuf+9a2tJzbyDbkpeq
WiJ0d0lCuVyOhg0bokuXLlAoFBAIBJDL5ZBKpWjbti2WL1+OlStXolVkJKRkLAZRmljWmv6bf75f
m76m8mUUzZ2vvrfNMTExeOutt7B8+XL4+/sjKyur3POSm5uLVatWIS4uDt7e3pgxYwb++OMP0/sb
NmyAVqvF1q1ba/IxfmDJyMhA7969ERISgh07dpQJ9a9btw46nQ579uyx6tz3+jqfOnUKU6dOhZuN
U0ychFU7YQF+gLlz5w7ef/99RJaIga09ZAkRnIgs8qK+O8xrj3WuCXedW0OEICJMItuW71RlkrGZ
jO5izZs3h0ajQWkIWiAQgIgQFhaGs2fPmpJnOqpUVs8/nyOCO9kn69zf2Rnr1q1DUlISBAIB6tWr
h9mzZ+PEiROVzv+eOHECzz77LHQ6Hdq0aYNu3bohODgYJ06cqOGn98Hjxo0bmDFjBjQaDebOnVsm
w7y4uBgvvvgigoODy9Vfrop7fZ0DFAr4SKWQltSY1ul0UCqVSJBIrP8bUKl4GVIthAX4IcBgMCAq
JMRm8fNWqeDj4wNRSWnC+2UB3zs/Wer0ZGumpjMRmtJ/a3OlUilUZJyjtuXe4qjykWVzIigUCshk
MojFYiQkJGDWrFl44403IBQK4eLiAicyhqltmX8+RAQviQSBvr7Q22HdtZYI3bt3h5+fH9588018
9913mDRpEvz9/REWFoZp06bhwIEDFYrxv//+i8aNG0Oj0cDV1RXPPPMMDh48yMuNKsBgMOCjjz6C
r68vHnvssXKlHG/fvo0BAwYgPj4ely9ftujcpk6dUllpp66NVAq9SgW1TMZGHA8ZLMAPCbZaZJaK
kK+vL6ZOnYq3334b7du3h5tIZMoCDqDK5yft5XWsof+SnCRkrKmrJctCvBUJu5SM4n7vOUqNOGQy
GTZs2IDc3FzTZ/rjjz+iadOm+HDDBniIRFaH5jeXfL5uMhlCQ0IQGBgICdkesXAWiRAZGQlPT0+o
VCrEx8djzpw5OHr0KA4ePIjp06cjLCwMfn5+mDhxIr755hsUFRXhxIkTCAkJweTJk1FYWIjMzEy8
+uqrCAwMROPGjZGSklIu0a+ucuTIEbRq1QrR0dH4/vvvy73/77//IjY2FkOGDLF4zXXKwoXwlcnM
7tR5SyTQODmxFeVDBAvwQ4KtFpluUilcXV0hEonQqFEjqNVqPPLII9ixYwfef/99aOj+85P2EOBS
J6s4st8So9ItgAin7znHEjIK/rDHH4dUKi03B/ree+/hscces+lzlRMhzMsLUqkUISEhqF+/vjGZ
i6wL15eugY4kY6dCLxAgsGT5SpPgYHTp0gXBwcHw8fHB008/jW3btuHAgQN49dVXERUVBbVaDZlM
hilTppQbERUXF2Pv3r0YPHgw1Go1Bg0ahD179tTJpKzLly8jOTkZHh4eWLVqVYWZzMePH0dAQABm
z55tUeTg6tWrGPHkk9AJBBaLqZdYDI1YbJFoL5w3z54fDWNHWIAfIqy1yNQJBBAJhUhNTcWbb74J
Z2dnSCQSdOnSBc2bN4enpyfkQuF9R2y2FhuoziVGpQJ89p5zaInQNDwcHTp0QHh4ODw9PVFQUGD6
PCdMmIAhQ4bYHFkQlGRYCwQCJCUloVGjRtDr9RYv+zJrDbRSCQ8XFyxauBALFy5EYmIiVCoVOnXq
hK5du0Kv12PChAlo2bIl3NzcMHToUGzbtq2c5/jVq1exePFiREVFISAgALNmzcK5c+dq+pGucQoK
CpCSkgKtVotJkyZVWkFq9+7d0Ol0SE1NNeu8hYWF2LVrFwYMGACVSgUXJyerO3Xucjn0KhXaymT3
nSLSECFCKrXICIipWViAHzIstcjUCYV48vHHMXLkSAiFQjz55JO4ceMGJk6caMoKTk5ORqC7e5Uj
NmuTsKpj7fDdW2XFHM6RMcStUirRvXt3iMXiMqOZ9u3bo0lQkO2JZU2aYOzYsVCpVGXWGltiHWpx
B+Uu69N//vkHsbGx0Ov10Ol0CAsLw7PPPov09HSkpKSgQ4cOcHFxQb9+/ZCamlomDA8Yl7+NGTMG
7u7u6Ny5MzZu3Ii8vLwaf7army+++AKNGjVCx44dcerUqUr3W7x4MTw9PbFv374qz1maxezl5YW4
uDgsX74cc+fORSux2OpnqoNSiaGDB0MjFqMZVb2EjcsS1l5YgB9CzLG6ay2RwFkggJ+fH0JDQ1FU
VIT09HSIxWLUq1cPFy9exMWLFzFo0CA4iUQQU9VLjKwpNmCrP7I5VYjuV87wEBHUJR0NlUoFgUAA
pVKJ6OhoiMViyOxQJUoqEJjC+0QEX19fHDx4ECnvvAMNVd3xsLqD4uyMd95+G+Hh4Xj66aeRl5eH
4uJiHDp0CLNnz0ZcXJzJzvTtt9/GokWL8Mgjj0ClUqF79+5Ys2ZNmWVNt2/fxocffoj27dtDq9Vi
4sSJOH78uAOfdPtw9uxZ9OnTB0FBQdi2bVul4eTCwkKMGzcOjRo1uq+hxdWrV7F06VI0b94c3t7e
eOGFF/DLL7/g6NGjSEpKstm1bjMR3O8KX5uzhI3ngmsnLMAPKeZY3d24cQPr16+HTCaDt7c3UlJS
cPz4cXh5eUEmk2H37t2mRJEfzBBKa8TU1gpBVS0xMmefDiX1mIcMGQKZTIZnnnkGy5Ytg1gstku2
sodIBDc3N/j5+cHJyQlDhw4FAHz//fcI9PW9b8TC1g6Ks0CAd999t1JRuXTpEtatW4eBAwfC1dUV
0dHReP755/Haa6+hf//+cHFxQfv27bFkyZIy2b9//PEHXnzxRfj4+KB58+ZYsWLFA2fycPPmTbz0
0ktwd3fH66+/ft8kqtzcXHTr1g2dOnWq8D7vDjG7uLhg0KBB+PTTT1FQUICvvvoKnTt3ho+PD159
9VW7+Do730ds7/c8cDZ07YIFuA5QldXd2rVrERMTgwEDBsDd3R3jx49H27ZtIRAI4HlX1qU5IzFL
R2v2XDtc6ZcO3X+UvJkIQRoNJBKJyW6ydB5cLxDYLMCeTk7Yu3cvZs+eDZlMBldXV1y+fBmLFi3C
mDFjTBGLFkJhuYjFejI6jFl77bZyudnrPwsKCvDNN9/g+eefR3h4OHQ6HYYMGYIpU6YgKSkJ7u7u
aNGiBd566y2TkUdRURF27dqFvn37Qq1WY9iwYfjmm29q9XImg8GA9PR0+Pn5YfDgwaYiCZXx119/
ISIiAqNHjy6TIwBUHGLOzs5GUVERtmzZgubNm6N+/fpYs2YN8vLy7GcrSVWX56xo47KEtQsWYAb5
+fnw9fXFoUOHcO7cOTz//PNwd3evsIC4OXOR5s5X5pCxJ29zlReqeDRg7jxxqQmJQqEwzdGWmnDY
Y7lQqQVgYmIi9Ho9Hn30UUyfPh2DBw821fC9efOmMVNar4fCyQl6oRCeTk5wIds7KHENG1r1XPz5
559YunQpunfvDpVKhYSEBIwcORIDBgyAXq9HkyZNMHv2bJw8eRIGgwGXL1/GwoUL0ahRI9SrVw9v
vPEGLly4YMcn1XaOHj2KNm3aoEmTJvj222+r3P/HH3+El5cX3n77bVOnorIQM2BcjfDee+8hLCwM
sbGx2Lp1a5ksckcLMDti1S5YgBkAwKJFizBgwADTz2vXrkWCVFrhH3FpNu79CgmEElVp5tGSbHOE
Kq0F7E2En+95z5piDEFBQRCLxSbx9ff3R6BGYxcLwN9++w0eHh547bXXMHDgQLi7uyMwMNCU7JOe
ng5vb2+8++67yMnJwbFjx+Dq6gop2d5BkRBBq9Vi5syZ+Pbbb60qtHD79m3s2rULY8aMQUBAAAIC
AvDoo4+id+/e8PX1NRl/HDx4EMXFxdi/fz+eeuopuLq6omfPnti+fXu50WNNkpWVhdGjR0Ov12PF
ihVVFkgAgE2bNkGn0+GTTz6pNMRc6q2dm5uLt956C97e3ujatSv+97//VRgFyM7OhrOTk11Lf1p8
LHtC1xpYgBkARps9rVaL33//HQCqLACeT/cvJDCJjNV+XFQquFWyzztk+drhimoB60v+36rkuu3I
8rXCGjJ6QQcGBkIoFIKIIJfL4e/vjxY2zAM3J2M4WyaTQaFQwNvbGwKBAAqFAkSE8PBwNGnSBEql
Emq1GkFBQWjTpg0iIiIgk8mgs0MIXFtyb0QElUoFqVSKsLAwJCUlYf78+fjyyy+RnZ1t9rNiMBhw
8uRJzJs3D23btoVKpUKrVq3QuXNnBAUFlTH+yMnJwdq1a9GqVSt4enri+eefx2+//VZdj3E5CgsL
sXjxYuh0OowfP94sgxGDwYA5c+bAz88PmzdvrjDEXMq///6LadOmQaPRYPDgwTh69Gi58/35559Y
tWoVunbtCmdnZ7gIBNU67VLVxlWRag8swIyJl19+GcnJyRaXN6woC7OACGL6b6lNRftYunbYnHWw
LcnotfyhBV9IpU5ZYiL4SCTwEoshIYJaKMSYMWPgZoMFoF6pxB9//AFXV1ccOHAAmZmZ6NKlC3r3
7g0nJyfs378f6enp0Ov16Nu3LyZNmoSdO3dCo9FgxowZ8LJhuUrp5iOVYsCAAXB2djZlejdt2hRv
vvkmJk6ciISEBKhUKgQFBaFfv36YM2cOPv30U7PLGF67dg0bN27EsGHDoNPpEBISglatWiE0NBQ6
nQ7Jycn47LPPcOzYMUydOhUeHh5o3bo13n//fdy8ebPanuevvvoKERER6NChg9le13l5eUhKSoKf
nx+ioqLKhZhLOXPmDEaNGgU3NzeMHTu2jKBlZ2djy5YtGDVqFHx9faFQKODi4gJXV1cMGzYMM2bM
sGltuTmJhyzADwYCACCGIaIrV65QWFgY7d69mwZ36kR/3rxp0/lURNSIiH66zz4JRPQsEfWt4lzv
Eu8N+YAAACAASURBVNECItpGRM2q2PcwEfUhoilENMGMdm4holdLjnMqea2QiHYS0TwiOkZESiI6
QkT+ZpyPiCizpJ2vLltGQqGQPvvsM9q2bRsREX322Wc0cuRIUqvVNGzYMPrjjz8oKCiILl68SGFh
YXT8+HGSSCQ0dOhQahcfTzeJSGzmde+lsKTt7p6elJOTQy4uLnTt2jXje4WF1LhxY1q7di01bdqU
zpw5Q0eOHCmzKRQKatasGUVHR5s2b29vEggEFV7PYDDQwYMHaffu3bRr1y76448/KDAwkG7dukVZ
WVnUq1cv6tWrFxUXF9OHH35I+/bto/79+9PIkSMpNja20vNawrlz52jKlCl08OBBevXVV6lVq1Yk
EAhIo9GQWq2u8JiioiLavHkzjR8/nnJycqh379701FNPUceOHcnJycm035EjR2jevHn01Vdf0ejR
o2n8+PGkVqtp//79tHfvXtqzZw+dPHmS9Ho9Xb9+nZRKJSUlJVG/fv2oefPmJBQKKT8/nwL0etp9
/TpFW3hvh4moBxmfL4kVn00hEbmJxXQ+K6vSz4KpQRzdA2BqF+PHjzcab9ghUcSNqk4gMmcZUnUb
dVQ1ojhEBDVZWIzB2RkeGg1+//13REZG4osvvjB9xkVFRZDL5aaqRGq1GpcuXcK4ceMwfvx4+Pr6
4u+//0ZYWBjC/fxsL7KhVEKr1eKll17CoUOHsG7dOnTr1g1SqdQ03y0Wi9GiRQuMHTsWixcvxhdf
fIHMzExkZGTg448/xvTp09GlSxdotVro9Xp07doVM2bMwObNm/Hnn39WmvV84cIFrFmzBn379oWL
iwsCAgIQFBQEhUKBfv36YenSpXj55ZcRGhqK8PBwLFy40OKCBqXcunULr7zyCtzc3NC/f3/ER0ZC
IRYjUKlEoFIJhViM1k2aIDU11bQUpzSLWafTQSqVonPnzrhy5UqZ8xoMBuzduxcdO3aEr68vFixY
gP3792PhwoXo1q0bVCoVwsLCEBUVBVdXV0RGRlZZlcoW17rJNj4PnIRVe2ABZsrw119/wdXV1eYC
4FlUvuZtRVtV61yr26jDXDOPc2Sc03YWCNBKLK7c4OQu67/IyEi8//77qF+/fpkvYoPBAIVCgaFD
hyIiIgIxMTEAgNGjR0On02H79u3o168fRo8ebXORjdZSKcRiMZRKJSIjIxETE2NK/CooKMD69esR
EBBgmiP29/fHwIED0a5dO+j1ejg7OyMiIgIDBgzAa6+9hk2bNuGLL77A5s2b8corr6Bnz57w9vaG
m5sbEhMTMXXqVKSlpeH06dPlPKTz8/Px5ZdfYvLkyQgNDYVarYavry9kMhk6deqE559/HgMHDoRa
rUa/fv2we/dus5KlDAYDNm3aZJyvb9ECeqXyviUjOyiVcJPJEBwcDG9vb9MSqzVr1pQ5b1FRETZt
2oRmzZohJCQEI0eOxODBg+Hh4YGgoCB06tQJrVu3hlqtRnx8PBYsWICMjIwq23v58mWsXr0azZs2
tbhTN/yxx2wLX3NZwloFCzBTjqFDhyLM09OmkddSMj/D+X4j3Oo06rBklFz6JahxdsaQIUPg6+Ji
qhKlFwohEwjgpVTC19fXNLqKi4tDYmIiUlJSyny+mZmZ0Gg0cHNzM9lD3rlzB82aNUNUVBQWLlyI
mJgY5OXl4c6dOzbNQXu4uCAnJweDBw+GUCiEp6cnXF1dMX/+fJO4FRcX45NPPkF4eLhpGZZeLoez
kxMCFAr4y+WQi0QI0esRExOD+vXrm4pL9OjRA8899xwWLFiA+fPnY/r06ejbty8CAwNNS5cmTZqE
9evX4+TJk6asYcBo5vHuu+8iMTERcrkcer0eMpkMMTExGDhwIJo0aQJfX1/MnDmz0jnL48ePo127
dmjcuDHGP/OMRTas3lIpkvr3h16vx1dffWU65507d5CSkgIvLy94enrC19cX7u7u6NWrF5544gl0
7NjR5K+9fPny+y61OnHiBF5//XV07doV/v7+po6OXC5HvXr1EBsbCzeZDO0Visp9nVUqU6fO1qIr
bMRRu2ABZspx/PhxqNVqm3rajS0QYFDla4ery6jDmoIOoLJGBtnZ2UhMTMSjjz6K9u3bQyQSQSQS
oVu3blixYgWaNm0KZ2fncks+tmzZgh49eiAmJgbBwcHo0aMHpk+fDrlcjpEjR8LDwwN//fUXMjMz
0alTJ2N1I6nUKivKtWvWICMjAxkZGThy5AgiIyMhEAig1WrRsmVLnDlzxtSutNRUaBUKxAuFVRZ7
+PDDD/Hrr79i27ZteOONNzB8+HCTtaVGo0GrVq0wdOhQJCcn44knnkD37t0RGhoKhUKBFi1aYMyY
MVi9ejWOHDmC/Px83Lx5Ezt27MCIESOg0WhM2dpBQUGIj4+Hm5sbOnTogI8++gh37tzB1atXMXbs
WOh0Oixbtgwfffih1SHdRQsXorCwEHv27EHHjh0hFoshEonQtOn/s3fd4VFV23fNTKZnUqak9x5a
QkuAFJqU0CWE8OjgQxABKSJIV1BEUYrSi0gNXYQHqCAEAoKCtEAARbqhE0gjZWb9/kgyj5DCZBKB
n2/W990Pcu+5dc69+5y91167NseOHcsxY8awefPmtLGx4euvv86VK1eWYI3n5uZy586dHDZsGBs0
aECtVkuhUEiBQEB7e3vWrVuXAwcO5KZNm0oQz0xRrXvaaJrrvnaTybj8mVm+BS8XFgNsQamIiYmp
1MxLa21NhUhUITd2AgrixuGFH/t7KGBJV5VQR9GMIhrmlTQsMug+Oh1TUlJIkp06deLmzZuZk5ND
uVzO/v37s3Xr1uzbty/FYjElEgk7d+7M2bNn87fffmN+fj7HjBnDDz74gCEhIfTz82NSUhLFYjHr
1KlDa2trbty4kV9//TW1Wi2nTZvGmzdv0lappBamFWM4DFAtkTDI2bnUGOg777xDW1tbWllZUaFQ
8Msvv+TsmTMrNHssS9zfYDAwNTWV+/bt44IFC/jOO++wVatW9PT0pEwmY2BgIMPCwhgREcHw8HD6
+PhQJpOxbt26HDBgABcsWMAjR47wyJEjnDp1KqtXr06JREKJREK1Wk0PDw/K5XLKZDLGxcXx3r17
lZ4VqqysKJFIKBKJGBwczA8//JAfffRRsYpRmzdvNhrO27dvc+nSpezevTurVatGa2trAqCVlRVd
XFzYrFkzTpgwgUeOHKlwKcfnqdYVoaJFV7QAdRJJqXFwC14eLAbYglJx8OBBOuh0Zo20HUUiOjs5
sa6/f4VmrwkA3QB+iYJZqxwFOb7mGt+iRQtQKxJRJhTSBgUpSs+L+ZZn0OVCIR0cHBgZGcng4GDu
2LGDJNmgQQOuWLGCrq6uzM7Oplwu57hx47hmzRoOHDiQwcHBtLOzo0aj4euvv047Ozva2dnRV6ej
BAUeA0eRiDKBgDqZjNOnT+fx48dpbW1NLy8vTps6lQqBoFx3ZXWplAqAjWWy585i27ZpY5y1m1Ob
1lRx/ydPnnDt2rVsVLMmFVZWdJNK6SKRGO9TLBZTp9MxMDCQwcHBdHV1pUQiYVBQEHv37s3p06dz
woQJrF27trGso1QqpUKhYEBAAPv06cNmSqXZ/SMMYL169fjOO++wVq1adHR05MCBA7l7924eO3as
VBdy0bm7dOnCr776iteuXfu7X8kSMKXoyrODzWf7gKU4w8uFxQBbUCYiIiLYt2dPukqlFZ4ZjRs3
jgKBgA1MFJIojWx1EgXCHVVhgNetW8eTJ0/SqxIf6qLFXS7nhQsXuGXLFtrY2NDGxoZDhgxh9+7d
+emnnzI0NJSTJ0+mo6Mjly9fXuyZpqamUi6X09XVlQqBgOEoO6e5sUxGOUBXFxemp6czPDyc8+fP
L9VdKRMKaWtlRecKFGt3Vyj4wcSJtBaJ/raYYpGRKI8U1dzamjpra44dM4azZs3iwIEDGRUVRY1G
Q6lUSrVabTR8dnZ2bNCgAevWrUs7OzsKBAKqUPkwhUYs5uuvv87Y2FiGhYVRo9GU6kLevHlzidrJ
LxPPuq9dJBLqUCDx+mxZwvLeVwteDiwG2IISMBgMPHnyJOPi4iiRSOjk6Eg7qZRNFYqyZSWtrGgn
lfKrr74yChnMmDGjVD3p0pbSyFYVFeoobSkS2XjjjTeYkpJC1zLkNStq0Bs3bsxjx44xICCAe/bs
4aRJk2hvb0+1Ws24uDg6OjqyZcuW/Oqrr4o923PnzlFnb2+yO/kYCgx+bMeObNy4cTGX5tPuymVL
lxYrnGHKchUFrurGMpnZzyJcIODUqVNL7UcVdZM+awyysrI4duxY2tjYsGPHjhw+fDibNm1KBwcH
40wYMI1t/7w+IgEoEono6urK5s2bc+LEifzll18q7EJ+mVi+bBmdpVIehOkylZYyhS8XFgNsgREp
KSmcMmUKg4KC6OnpydGjR9PHx4e7d+8uNtKWCQR0lUqLEUVmz55NmUxGW1tbTpw40RgvW7FiBR1F
oucahrLIVlVBwrIBCBQUWKiK4gpSwKj7K5VKuXfvXpKFxlWnY6NGjQgUyEwOHDjQSIJKS0vj4Lfe
MsvdqwHYv1+/EjmqJCsVA61bBc9XBdDd3Z1JSUnGazKXKOSuUHDd2rXctGkTvby8GBsby8uXL5fQ
Yu7SpQsXL17MKVOm0FEkMvv6ixYPheL/tTqUhR39/xMWJaz/cVy+fBnr169HQkIC7ty5g65du6Jb
t24IDw+HQCDAqlWr8PXXX+Onn34y7hMVFYWBAwciIiIC9vb2SExMxMiRI6FUKmFjY4ODBw8WUzSa
+P77WPjJJ9iN0lWsHgFwBZCG/ypRFWEdgGUA9ph5f2EAfn3qbxsAX+P5yltlYTOAfgBqNmqE//zn
P9DpdLC1tUWDBg0wadIktG7dGu3atcN//vMfiDIz8SgnB3ZCIcRiMdL0eljl5+M9FKh0VUTJ6DiA
plZWgFwOT09PREdHG5f9+/dj2ZtvYk8FlcvKe+6mIg+ArVAISKXIzs6Gs7MzVqxYgd5xcWYrPTUR
ieARGIgvv/wSTk5OWLFiBVavXg0PDw/ExcVBq9XiyJEj+PHHH5GWlgbxo0dIzc838w4K4CAQwLlm
TWi1WqhUKqhUKlhbWxv/b8rfcrm8SpS8TMGjR49w//59AIBGo8HOnTvN6gNFaG5tjQFLlqBbt25V
eZkWPAcWA/w/iBs3bmDDhg1Yv349Ll++jNjYWHTr1g2RkZEQiUTF2ubl5cHPzw8bN25EWFgYAKB6
9epYv349RCIRhg8fjuvXr2POnDlo0qQJ6tSpg0mTJiEuLg4AcOLECbRr1w5t2rTBtnXr4JuVhdEk
OuC/H/0LAF4DcL2Ua80B4AlgJ2DWx7yxUIjA0FCcOnUKer0eQIFRLk8eszyECwT4pfCVsbeyQmZ+
PlyUSuTm5eFebi7EAgEMJOpLJBiem4v2KClvOR9AMoA5AOIrcO7m1tbov3AhAgMDceDAARw4cAAH
Dx6EMCMDi3JzKzyo+BNAcwCXK7jfs/BSKvHT6dPYt28fRo4cicePHyNcIMARMz8tURIJfP/1L5w7
dw43btxAkyZNoFKpcPLkSZw7dw5BQUFQKpVIT0/H9evX8eju3UrLdaoEArTu0AHe3t5wcHCAWq2G
Xq9HRkYG0tPTjcuzfz+9Licnp5hRrqgBf/ZvhUJRzKDn5ORgy5YtmD9jBk6cOwedVAoAuJuTA5VI
hG5PnmAGzJOo3AxgTmgoDpw4YeZTtMAcWAzw/whu376NTZs2ISEhAWfPnsXrr7+O+Ph4NGvWrJjW
bWmYO3cuEhMTsXnzZgCAWq1GfHw8Nm3ahPHjx+Ptt9+GWFzw+Tt48CC6d++Oc+fO4fjx4+jatSsW
LFiA2NhY5ObmYs2aNZg8ciRup6VBIxYjLy8PjwHYAbhdxvnXAxgNIAkV02KuA+B+Kdvkhccyx6BH
ocCfHQJgDFDMwM5CgV71d6h6vWqg4CM5OyQEB06cMH6YHz58CDcHBzzKz6/wLLaqDLCrRIJ569ej
devWkMlkqOnlhQ+uXq2Ul+EtmQxqT09cuXIFcrkcAJCZmYn8/HwIBAKo1Wr4+fnB19cXB3bswOxH
jyp1vmk+Puj19ttITk5GcnIyzp07B7VajRo1ahRbgoODjdfzLPLz85GRkfFco23q30+ePIFSqYRK
pQJJpN++jVoCAd7V66t0YFd0DItG9IuHxQD/g/HgwQNs2bIFCQkJOHbsGNq1a4f4+Hi0bNkS0sLR
synIzMyEt7c39u/fj8OHD2PAgAHo378/pk+fDgcHhxLte/fujfT0dBw6dAjr169H06ZNAQC5ubm4
dOkSvvzyS6xbtw7pjx9DZTBgJ4AWAB6i7FlMRYsxtBOLcS8vD207dsS2bdtgb28Pd3d3JCcnw9bW
FlZpaThGVtig5wDYX8o1mDtIiATwGUz7YBYVVsgFIBKJIBKJIBQKoXryBHdMPOfTKHJBl/fcTbkm
G6EQ/tWr448//oCPjw8upaQg3WColFvbGkC+UAiRSARPT0/UqlUL0dHRaNq0KVQqFbZs2YK1a9ci
NTUVoaGhyE5MxL6sLLPOFwYgIzgYK1euRL169QAUFJW4cuWK0SAXLb///jvc3NwQFBSEgIAA+Pv7
w9fXF66uriCJvLw85ObmIi8vr8L/f3Zdbm4usrKykHzyJG4kJ2OnwfC3DOyK4KVUYt+ZM/D29q7w
M7TAPFgM8AvCszGbv2uU+fjxY2zbtg0JCQlISkpCy5YtER8fjzZt2kChUJh93DfffBNbt26Fh4cH
Ll++jAcPHpTazmAwYMqUKZg2bRr69+8Pa2trXLx4ERcvXsSNGzfg4uKCmzdvIi4uDv/ZtAl7c3JQ
B6ZVRVoP4B0ANQAMBoq5sfNQMPOcgYJZgMTWFo8ePYKVlRUaNWoEkjh16hQAIDQ0FDevXkXO7dv4
9skTkz5qrQrPcQYlDWxl3eTPq27zCP+dyYcLBFD7+0MkEhldpHmpqbhjrrsXplWjKgubAQyWy+Ff
pw6kUikyMzNx5ddfcctgMPOIBXCVSDDuiy8QEBCAvLw8PHjwAElJSThw4ACuXbuG2rVro06dOvDy
8sKTJ08wY8oU/JSba16YQiBArpUV8vLyYGVlBRsbG0ilUqMxLDKI+fn5EIlEsLKyglAoBFDQ3/V6
PfR6PSQSCeRyOZRKJaytrWFrawuVSgWJRAKJRAKxWAyxWPzc/z+97tTJk9ixciWO5Ob+bQO7IlgM
8IuHxQD/jSgvZlO7WjUMHjMGsbGxkEjMidr8F5mZmdixYwfWr1+PPXv2oEmTJujWrRvat28PlUpV
qWPfunUL77//Pnbt2oWMjAxs3rwZ7777LhITE42G9eLFi7hw4QIuXryIlJQUGAwGuLm5ITc3FyNH
jkRgYCACAgLg7e1tLMvm4+ODpW++if3Z2QBMJ1vlAtiCAnfbbwC0RdcJQC4SoW6TJkhLS8Px48ch
l8uxa9cu3Lp1C2fOnMGBAwdw6NAhkISjoyPu378POYCgvDyMQfkGPR/AEZRuYCtLFGsOYACAp+kv
OU/d5wkAusL1qQBsZTIYrK2RkZEBgUAAQ3Y20mHeLLYqSG4nxWIIBAKQhMFggL1ej7tmHq8IOgBC
BweQRFZWFrKzs2FrawtnZ2c4OzvD2toacrkccrkcf/31F/bu2QM7vR7HUfGSkdGvv44JEyfi8uXL
+OKLL3DkyBGIxWLExsZizJgx8Pb2hkQiKWZ4n0VWVhZSUlJKzJjT0tJQrVq1Eq5sJyen5xK2XmTZ
QosL+iXhRdOu/1dgqgCBuWo02dnZ3Lp1K7t160ZbW1u2bNmSy5cvL6FRay5ycnI4ffp02traskOH
Dpw0aRKrVatGtVpNsVhMGxsb1qtXjz169OAHH3zANWvWsHv37gwODubNmzeZl5fH0NBQrlmzxnjM
1atX08/Pj0OHDqW9lVWx9Bdzqh6lAfwT4DaASqGQcrmcdnZ2dHR0pLu7O2UyGT08PLhkyRLm5uaS
LCiEIJFIqNFo2LFjR4pEIqOYg6Qw3UdXmK6kfapcX3g511HVetUJhc/iNZQj0iGXU6tUMj4+njqZ
zOzzPwGoruBzfzp9RVOo9tWiRQu6ublRJBJVWaqXlZUVPT092apVK/bu3Zvx8fFs27Yto6OjWbt2
bfr5+VGhUBh/I6lIVKH8amexmF06daK7uzvbtWvH48eP8/r167x8+TLfeecdKpVKWllZMTw8nLt3
7y6ztGB5ePjwIZOSkrhw4UIOGTKETZo0oUajoUajYePGjfn2229zwYIFPHjwYIl3t7KVsJ5XZrNE
H7SUKXzhsMyA/wbM/eILzJwwAVuzs02L2SgUeHfqVAwbObLctnl5edizZw8SEhLw3XffISQkxFjs
W6fTlbtvWdDr9bh69Wqx2ezPP/+M06dPw2AwwNvbGzVq1EBAQAB0Oh0mTZqE5s2bY/v27cYRfF5e
Ht544w38+eef2L59O+zt7QEAP//8M2JjY7Fr1y6sW7cOM2fOhKOjI3r27Il5X3yBtGeIQ5UhWzVq
3x579uzBkydP8O677+LatWvYu3cvwsPD8fvvv+POnTuoW7cutFotkpKSkJWVhcePHxuZ0QBgb29f
kNYiFkOv10MkEoEkZHl5WIHS3bRVlcpjD+AmgG9QsVh3W5EICldX6K5dM5vZXUMqxUMSP1fQzVkH
wGOxGCRhZ2cHhUKB9PR06B8+rHSqV38AInt75OTkQCKRoHbt2ggNDUXNmjVRq1YtyOVy9O7dG1Kp
FBcuXMCqVasQGRmJ1atXY/J776G6wYChWVmlejVmicU4ZTBALxajSdOmyMjIwNmzZ5GRkQE7Ozs8
efIEGRkZkEqlEIvFyMrKQn5+PqysrODj44Nq1apBrVaXyXgu6/9FREWSuHPnjnGWfObMGSQnJ+Ps
2bOwtbU1zpJ3bdiAqdevV+o5zgFwwIS2zVUqDFi82JKG9IJhMcBVjPUJCRjdvz+SsrMrFrNRKPDZ
smWIf+YF0Ov1SExMREJCArZs2QJ/f39069YNcXFxcHFxMen4JHH37t1iruKi5c8//4SDgwMCAgLg
5OSEkydP4t69e5g6dSr69Olj/GgUoX79+pBIJDh06BCAAtdb165dAQAbNmwwxpnv37+PjRs3YvLk
yUhPT4erqyvCw8OxatUqXL58Gc1DQnC5lJzFipKtWgHIlkiQlZtrXC+TySCVSuHo6IirV6+iS5cu
sLKyQlJSEjIzM9G2bVts3boVnTt3xp49Bc7XK1euwM7ODn369MHt27cRFBSEadOmoXXr1ti7axce
6/XFDGxRXPYagL4ArpjyQ5QDLwCjUBC3q+gApDaAHKEQBwwG81yVNjZ4b/x4zJo82eSYeFuRCDp/
fzzJz8f169dhZ2eHR48ewd/fH8HBwbi7Ywd+MpMUFS4QwKFtW7Rr1w7JycnYt28f/vjjD7i4uECp
VOLu3bu4ffs2bGxskJOTg759+6JNmzaoVasWPD09kZeXZwz9/Hb2LLSFIZ57ubmoU706Bo8Zg86d
O2PIkCF48OABNm7cCABYunQpxo0bh9mzZ6N79+7IysoyMpKTkpIwd+5cnD59GgKBALVr10bjxo1h
Y2NTgslc1v9FIlG5RlosFiM7OxuZmZkF5/zpJ2SQVTKwK8+pXNQHrt29W+lwmAUVxMubfP/zUFVq
NHq9ngcPHuSQIUPo6OjIOnXqcMaMGbx8+XK5509PT+dvv/3GhIQEfvjhh+zRowfr169PW1tbqtVq
NmzYkH369OFHH33EjRs38tSpU8zMzGRGRgbHjx9PtVrNjz/+mE+ePCnzHG+88QaVSiUzMzP54MED
NmrUiL1792Zubi6zs7O5ceNGdujQgSqVih06dOCnn35KhUJBBwcHrlq1iosXL+bo0aPLVS8qcsE2
L3S3llojFQV6t0CBwpW/vz8FAgGFQiFlMhm9vLyYmJjIWbNmMTw8nHl5eTQYDNyzZw8bNmxIpVJJ
mUzGlJQUfvzxxwQKpAi1Wi21Wi2PHDnC77//niKRiI5CodFduxYFLmclQC+ArqhY2cWyFo/C45jb
d+QCAbUovaZyWctVFNQydnJ0pEwmo0gopBwFxQnKeu7hhW1cnJ3p7e1NhULB9u3bc9myZbx9+3aV
vAcauZwDBgygvb09O3XqxF27dvH+/fvcvn07w8LCKJVKKRQKaWVlxYiICHbs2JHNmjWjq6srbWxs
GBERwUGDBnH+/PncvXs3T506VWp1oSdPnjAsLIwzZswwrjtx4gT9/Pz45ptvMisrq0T/v3r1KgcP
Hky5XE65XM7q1atz1apV5b4zZIG8a3Z2Nu/cucNLly7x1KlTTEpK4rZt2/jOO++wmpsb5SIRXSQS
uojFlAgEVdKvPFEQpimvD1ikKF8eLDPgKsS6desqpUbTRKGAddOmOHXqFGxsbNCtWzfEx8cjICDA
2CYvLw+XL18ulQD18OFD+Pn5GUlPTy8ajabE+Uhi/fr1GD16NKKjozFjxgy4ublBr9fj8ePHePTo
EdLS0or9O2/ePFy7dg0+Pj5ISUkxKgddu3YNDx48MLptRSIR7OzsYG1tbczljImJQV5eHpKSkpB+
7165xKGyyFb3UOD6fBMFbsq8wvUBAQHQarU4fPiw8Rh2dnZ4/PgxBAIBFAoFPDw8YGtrCzs7O/z2
22+4ffs2NBoNPDw8kJqaisePH8NgMIAk1Go1jh49ip07d2LCwIH4EgUM7JooYGAX5WFWVSqPCkAE
gL1mHiNaKoVbhw5I2rHD5NBHKxRcf/2GDdG0aVOEh4fD398fP/30ExZ+9hn+uH4dKhIkkS4QQK1U
Ir9Q7alDhw7o0KEDXnvttVLzYs31BDUQi5EukWDkqFEYOnQotm7dikWLFuHWrVsQCoXG/pyYmIiP
PvoI58+fR1JSEg4dOgSdTof69evD3d0dYrEYqampOHPmDM6ePQudTmd0Xxctfn5+SE1NRVhYIYCy
3wAAIABJREFUGFatWoXXXnsNQEEmwYABA3DhwgVs3LgR/v7+Ja41IyMDX3/9NaZPn24kww0cOBBv
v/02PD09Tbrf9QkJeGfgQNQkMTg9vVhub3niNBWBF4B9AErjNVck/GXB3wOLAa5CRIWGYsSpU5WK
2Yx1dMSWH3+EWq0uZmSLDO21a9fg6upq/BA9bWzd3NwgEAiQnZ1dqvF8+t9Lly5h3759BUxLT0+Q
NG7PzMyEjY2N0Vg9/e+BAwfg4uKCI0eOwM/PD/fu3YOtrS2io6PRpk0b1KlTB+7u7pDJZACAf//7
3xCLxfjll1/g5OSEI0eOICoqConbt2OZwWDSs3oEoCjpSY0Cd1pRnDBDKIShMOUlJiYGcrkcW7Zs
AQCsXbsW3bp1w4ULFxAZGYl58+bB1dUVd+7cQd++fY2xxQMHDhjTSzIzMwEUpJcIhUKQhJiEI8p2
i1dFKs8QAPMqeYyJrq6w9/TEqSNHUN1gKJPZPVcuR4pIhDmLF+PJkyeYOHEiRo8ejeTkZCQmJuLe
vXtGmdFbt27hxIkT0Gg06Ny5Mzp06ICwsLAy2cBFePz4Md4eOBA/bNhgev5qoTHo3LUrhg4dipSU
FCxatAjZ2dno2bMnfHx8cOLECdja2mLRokV4/fXXi6UDJScn4+DBg0hKSsLBgweh1+sRFRWFRo0a
wdvbG7m5uTh79ixOnz6N06dPIzU1FUFBQdDpdDh06BAWLVqEFi1aQKfTgSQWLFiAyZMnY968ecYw
y7MwGAzYtWsXPvroI5w6dQokER0djREjRqBFixZlPqfn8USqamBnh4KBjeapdd8BmK9S4axAgDmL
FpUIe1nw4mAxwFWER48ewVWnQ1peXqViNioAIoUCCoUC7u7ucHZ2hlarha2tLZRKpdFIlGVci3Jf
bW1tSzWgUqkUv/zyC86dO4e4uDh07NgRarW6WDtra+tSPxw3btxAnTp1jDnAISEhEGZkIOXy5VJT
rOzs7DBgwAD861//woIFC5CZmQmtVovMzEzUqVMHohMn8HVhnFCD8uNUz6JI41kgEKB///5Yu3Yt
8vLy0KpVK+zcuRMkIRAIEBISguHDh+PevXtYunQpjh8/jqVLl2LPnj2oWbMmdu/ejeTkZAQEBCA5
ORkAYGNjAwBIT0+HytoakvT0ctNbKpvKE4GCVKPHqByRyxqAxtkZgYGBsLGxwZUzZ3Dp+nVoC3+b
ohhoXP/+UCgUOHToEBITE3H79m0IBAIMHToUUqkUv/32G/bt24e6deuiQ4cOaN++Pfz8/J57DU+e
PMGuXbuwdu1a/PDDD2jSpAm8vLywdtky+GZl4T2y1AFBWcZg06ZN6N+/P/R6Pb755hssW7YMAoEA
rVu3xtdff22cqfbr1w+Ojo7FroUkrly5Uswgp6amomHDhoiMjERUVBSqVauGP/74A2fOnME333yD
U6dOwcrKClKp1DhLVqlUWLJkCdq3b4/Zs2eXK2Bz5swZzJw5Exs3bjTmA7/zzjvo168f1Gq1sZ2p
3oEqGdjJZEjX68uMg1tivi8XFgNcRfjzzz/LJBZVBFoAuSoVNBpNCeNp6r+lvVT5+flYvHgxpkyZ
gvj4eHzwwQfFPgpl4dGjR9iyZQtWr16NX375BRkZGWjXti1+3rcPAU+eYLTBUKos3hdiMX7Ly0Ou
UAixRILevXvj6NGjuHjxIkaOHIltq1bh4rVrcAIgBHAXBWSiwQBiUX7uYpEkZG6hGIVIJIKrqytS
U1Ph4OCA+vXr49tvv4WtrS0yMzNhbW0NsViM+/fvQyKRICcnByKRCB4eHrh+/TqUSiWWL1+OSZMm
QavVIjExETKZDNnZ2SbJVlZWiCMCBQOvyubOliakkJaWhlOnTuHo0aM4ceIEfv75Z2RnZ6Nx48aI
jo6Gh4cHzp07h3nz5uGvv/5C+/bt0aVLF8TExJQatngWer0e+/fvx9q1a7F161aEhoaie/fu6Ny5
s7F/devWDUKhEDdSUsolRT3db1NTU9G9e3cAgIuLCzZu3IhGjRrhxx9/hLiQeX3s2DEsWrQImzdv
RosWLTBw4EA0bdq0zFnn3bt3kZSUZDTI586dQ2hoKCIjIxEZGYnly5fDxsYGH374IZKTk40z5RMn
TuDixYuQSCR47bXX0KhRI9SqVQs1a9aEu7t7iXzeu3fvYuHChZgzZw7EYjHS09MRFxeHIUOGoEaN
Gibn9lY6v7yQ2RwTE2McNKvVakue76uEFxxz/sfi0qVL9KpEzp6RNKFUVnlZtP3797NWrVps0qQJ
T58+/dz2OTk5/O6779i1a1fa2NiwU6dOHDVqFHU6HSVCYYVqvDqKRJwyYQJjY2Pp5eVFOcAGAkHZ
udEoIGAllEMa0QKUy2Rs3LgxgQIiVq9evYw1YmUymZGcZWVlRYFAQKlUyri4OMpkMjo4OLB9+/Z0
cHCgUCikSCQykmp8fHxYu3ZttmjRghqNhmEm/m4JAN3NIEHpBAIGBgRUDeFGqeSlS5d48eJFLlmy
hD169KCbmxudnJzYrVs3LliwgKdPn2ZiYiJHjRpFf39/urq68q233uKuXbs4cOBARkdHl0o+ehoG
g4FHjx7l8OHD6ezszLp16/Lzzz/njRs3SrS9cuUK1Wq1kQD1dA3jZ0lRRfjpp5/o4uLCKVOm8M8/
/2RQUBB79erFGjVqsFWrViXej7S0NM6bN4+1atWin58fP/30U965c+e5/Tw9PZ179uzh5MmT2axZ
MyqVSkqlUkZHR3PdunXF7ic7O5ujR4+mSqVix44d2bJlSzo5OdHW1pZRUVF8++23uWjRIh4+fJiP
Hz8mWUDyWrlyJWvUqEGtVkt7e3t6e3sz2sT6y+bkxhd79ywlBl95WAxwFSEtLY1KsbjSAgRKsbjM
D1NFce3aNcbHx9PDw4MbNmwoV0jAYDDw0KFDfOutt6jVahkZGcmFCxfy/v37XLhwIV1cXDh58mSz
mLY6gYD+3t50EApNL84OcE5p6xUKKiQSarVaxsTE0NfX12iElUql0QgXiTN06NCBiYmJtLGxoUQi
oVgsppWVFeVyOcPDw+nu7k6xWMwhQ4YwIiKCVlZWtLe3p1Qqpa9OVyGBizmF123qPboClBVee1WI
V8gEAup0Orq6urJHjx5cvHgxL1y4wMePH3Pz5s3s3bs3NRoNQ0NDOWnSJB4/frxYn9Dr9ezevTvb
tWtnFC55GikpKZw4cSJ9fX3p7+/PyZMn8/z58+X2weHDh/Pdd981qb/q9XpOmzaNTk5O/OGHH5ic
nEx3d3fOmjWLJJmbm8vp06dTo9Hws88+Y15eXok+/PPPP7Nv3760s7Njt27duG/fPpMFNHJzc7lx
40YqlUpGRUVRo9HQ29ubvXr14uLFi5mSksIjR47Q09OTw4cPZ05ODu/cucO9e/dy1qxZ7NevH+vW
rUuFQkEfHx926tSJkyZN4oYNG7h69Wp27NiRtkJhhfqUuQM7C7P5/wcsBrgKERkSUnlFpCpQo8nO
zubUqVOpVqs5adIkZmZmltn2/PnznDhxIn18fBgUFMRp06YZZxgGg4FTp06lp6cnZ86cSZWVlVmj
8Y8Bswy3O8DVhc+lkVhMa5GIKpXKOKvVaDQcOHAgfXx8CBQoJ7m5uREA1Wq10TCLxWIqlUpKJBIK
BAL6+voyNjaWBoOBzs7ObNeuHWfNmsWcnBxaW1vzzJkzDA0NpUwgKDZLN/WDaUoKVdEsvz5Aa2tr
VnNzq3TfUQsEVFpZMTIkhPPmzeNXX33FmJgYqlQqtmjRgl9++SWvXr1abt/Jzc1l27Zt2b17d+r1
el6/fp2fffYZa9euTWdnZ44YMYK//vqrSUbtwYMHtLe35/Xr15/b9u7du2zdujUjIyN548YNJiUl
0cHBoZiSWhH++OMPvvbaawwNDeUvv/xS6vEePnzIuXPnsnr16gwMDOTnn3/Oe/fuPfc6SPK7776j
m5sb//rrL547d46LFi1iz5496enpSa1WyzZt2rBatWqsXr06f//99xL75+fn8/z589ywYQMnTJjA
Dh060Nvbm3K5nNJn+sTfMbBzl8s55/PPTbpXC14uLAa4ClFZ6bhoa2vOnj2bly5dMmsWbDAYuHXr
Vnp7e7Nz585lurJv3brFOXPmsH79+nRycuKIESN47Ngx40c1KyuLu3btYp06dSiTyahSqVinTh1G
isUVvqfKutHkAD3s7dmzZ0/u2LGDN2/e5JQpU6jT6Whvb8/vvvuOwcHBbNSoEQFQLpcTgDFPFAD7
9evHjh07UlA4Q7SxsaFMJuOUKVPo5ubGw4cP09vbm/n5+WzdujU3btzISZMmUWvm75iDAgnAKBRI
KnqgIB9TWbhuXWGbIsPppVZToVAwwoznW7QUyQ4WufLDAdqIxRw2bFiF+9L169fp7+9PFxcX2tnZ
8Y033uDevXuZn59foeN8/PHH7N2793PbHTp0iO7u7hwzZgzz8vK4fft2arVa7t69u8x9DAYDV65c
SUdHR77zzjtGt29p7ZKSktirVy/a2dmxR48ePHDgwHMHEJMmTWJ0dHQJT8C1a9e4du1aDho0iE5O
ThQIBAwJCeGUKVO4d+9eZmRklHnMkydP0l0uN+v3NWVgF4aC3HipUMjIkBCuXbvW4oJ+xWExwFUI
cwQIisQd6hZ+rL2USnpZW1MpFlfoJTp37hxbtGjBatWq8ccffyyxPSMjg2vWrGFMTAxtbW3Zq1cv
fv/998zLy2N+fj6PHTvG6dOnG2NhOp2Onp6e3L17N3Nzc82e3a8t/GiYa1iaWltz3VOutLy8PH71
1Ve0s7Ojvb097ezsKBAIGBMTQ4VCwaLY79PGWKfTccaMGQwICGCPHj0ol8uNbby8vPjBBx/QycmJ
0dHRdHV1NbqpzTXATy/uABNRIIaQVsr2orDD2bNnaSeVmh/vw3+N+tPr3RUKk2ZDGRkZXLduHdu3
b2+M+/v4+PD999+v2EtQiOzsbDo5OZXLOTAYDPz888/p4ODA7du3kyS//vprOjk58ejRoyad5+7d
u+zTpw89PDz43Xffldv2/v37nDVrFoOCghgcHMzZs2eXqZ2u1+sZExPD4cOHl3vMnTt3UqvVMiws
jA0aNKBCoWBYWBhHjRrFb7/9lnfv3jW2rSxPpGhgpxEIKC/UvXYsNLqR+O/Ariq05i14MbAY4CpG
wrp1dJfLTXK3Fo1qm6Fs0f3nvURpaWkcMWIEtVotZ8+eXWzEnpeXx927d7NXr160tbVlTEwM16xZ
w4yMDP75559ctGgR4+LiqNFoGBwczGHDhnHDhg1s3rw5O3ToYCTjFMW3K+o6I6qmUIGnWs3IyEi6
u7vTysqKNjY2FAgElEgkxrivv78/HRwcWOR2fnYRCoXUarV0cXGhTqejVCottr3IIIvFYuPsWYrK
x2WVZRjeYkZaLuf777/POnXqmO2qL4+0VlY8MDc3lzt27GD37t1pa2vL1q1bc+XKlXz06BFJ8s6d
OwwMDOQXX3xR4fdgyZIljImJKXP7w4cP2bFjR9avX5+XL1+mwWDgJ598Qk9Pz+fGlUvDnj176Ofn
xy5duvCvv/4qt63BYGBiYiK7d+9OOzs79u7dm4cOHSoxK75//z59fHxKdYM/jSL3eUREBC9evMj9
+/dz6tSpbNWqFW1sbBgcHMw333yTixYtotLKqtJ9Si4U0lkq5TaUPbAzZxBmwYuHxQD/DZjz+efP
ZQpXOK7zzEuk1+u5bNkyOjk58d///rdRBtBgMPDYsWMcPnw4nZycWL9+fc6ZM4cpKSncuHGjMWbq
5OTEnj17csWKFUa257179xgeHs5+/foVI7iYO3JPKzRA5hjupz84UoChoaFs27Yte/fuzb59+1Kl
UrEo7iuRSOjv7093d3cKhcJiRreoHVBQ3UguFNJNKqW7TEYJQBX+a4RFIhGrVatGoVDIo0ePMiwo
qEqrHJW1aAHGx8czISGBUydPrhDLvDSyWmnt1HI579+/T71ezwMHDnDQoEHUarVs1KgRv/rqK2P/
eRZXr16lh4cHly9fXur2tLQ0Xrp0qVjYRK/XMzAwkD/99FOp+xw7doze3t4cNmyYUXp1xIgRrFGj
RqlMalORlZXFcePGUavVcsGCBdTr9c/d5+7du5w5cyYDAgJYo0YNzp07lw8fPjRuP3nyJLVaLU+d
OlXucfR6PT/++GM6Ojpy165dxvV5eXk8fvw4Z8+ezS5dupSoAmZOn1ILBBZS1j8EFgP8N6GoHGFz
a+sSMZvVAF1gPrPxyJEjrF+/Phs0aMBff/2VJPnnn39y2rRpDAoKMroOV6xYwffff5/169enSqVi
TEwMv/jiC54+fbrEaP/atWsMDg7mmDFjSmwz1wBfQoFesrkfm6cNlLe3Nxs1asQOHTqwf//+rFGj
BjUaDYOCguji4sK5c+fyjz/+4JgxYyiVSikWiymTyShAQRw5HGV7GcIAKgQCCgDKZDKKxWIGBgZS
oVCwQaEOtDmLKeXgclHAgAZAW1tbNmzYkHFdulAtlzNSIjGJyGXKtTQQiWhlZUWFQkFPT89iZLvn
4fz583R2duaWLVtIFoRa1q5dy8iQECrFYnpZWxcLm4waNYq1a9cu0Y8MBgPnzZtHnU7HjRs3kixI
eevRowcjIiKqrJTmmTNn2LBhQzZq1IjJyckm7WMwGPjTTz8xPj6ednZ27Nu3L3/++WcaDAauXr2a
Pj4+Jl3f/v376erqyvHjx5dgaZPkmjVr2FSpNLtPhaGA1FjR/SxpSa8mLAb4b0ROTg7XrVvHqNBQ
KsVieiqV9FAoKIf5pCQbsZjOzs5cuXIl7969y4ULFzIyMpJarZZdu3blkCFD2LJlS6pUKoaHh3P8
+PHcv39/uS9eSkoKPTw8OHPmzFK3p6amUi4UVth1VlUGuLTc6Pnz5zM0NJQdOnSgs7OzcYY2dOhQ
tmzZku3ataMIBfV9TZ1NagGKAKOLWiAQUApwv7kfPJSMyz67bAIY4OREJycnikSiYjN4ALQpvAYd
CtKWSiNymbJsAuij1XLs2LGsX78+nZ2dOWrUKJ48edKkvnz8+HHqdDqOHzfuuXWuGwqFVMvlxWZc
jx8/Zrdu3RgSEsKLFy+SLMjDbdWqFdu3b//c3OOKQq/Xc/78+dRqtZwwYQKzs7NN3vf27ducMWMG
fX19WatWLc6bN4+DBg1imzZtTJpV37p1i6+99hobN25cwh1e2UIV1hX83Z9emj3Dp7Dg5cNigF8Q
igQIZs+ezWaVIGJEiMUcPHgwO3XqRJVKxfr16zM6Opo6nY7+/v586623uGXLFpNnE0ePHqWjoyNX
rFhR6vbExET6+/vTzda2wq6zIhd0ZWNeCpGIFy5cKHZdv/32G728vBgSEkKJRMIxY8aQJNu0acOE
hATa29nRWSyukJfhYuEHToWCWamDQEBnKytKUDDzWGvix+95cdmnlyiZjGFhYbSxsaGvry8VCgUn
T57MQ4cO8f3332d4eDhtbW0pLry+58WTy3uOT+eYp6SkcNy4cfTw8GDNmjX56aef8ubNm+X2lWGD
B1eo4H1R2OT06dMMDAzkgAEDjIb27t27DAsLY//+/UudKVYVbty4wc6dO9Pf379Ml3hZ0Ov13LNn
D+Pi4mhra0tHR0f++9//NikFKz8/n1OmTKGzszP37NlTbFtFeCJP9yktwJGVeJeqKs3RgqqDxQC/
YFRFrrBaLKaTkxPVajXj4+O5ZMkSXrlypcLX8sMPP1Cn0xkZqE/j0aNHHDRoEF1dXbl161YuXryY
4WZcb1WQsJyVStrb2zMoKIiDBg1iQkICr1+/TqVSSWtra9aoUYONGzcmSQYFBfH48eO0l8kqNMso
IsQ1Rdmu6iZ4vtvX1LhsUVuVlRUXL15sjMGeO3eOoaGhfP311415q3+nypper+f+/fv5xhtv0N7e
ni1atODKlSuZnp5erJ25RsNZIqHK2porV640HuvKlSsMDAzk2LFjTRbJqCy2bdtGd3d39u3b1+R8
4Kdx69Ytjhs3jiKRiD4+Ply4cGGZqU9PY8+ePXR2duaUKVOKpXGZwhN5up+4SKWUofJ8iqoU+rGg
8rAY4BeIyrCJn36J5EIhExMTTXKHlYWEhAQ6ODjw4MGDJbZt376d7u7uHDBgAG/fvs1Zs2ZRq9Wa
5TpfW2i4zL3fMPyXpWxnZ0cvLy/6+vrS2tqacrmcOp2OISEhtLe35++//06JRMK+ffuygUBg8jkq
SohzAfjFM7/JJphmoJ82To4iERfMn89Tp05x7969TEhI4FdffcXx48czJCSEcrmctWvXZmBgIHUV
uJ+yFheJhGvXri2TcJWVlcWEhAS2bduWtra27NmzJ7///ntmZmZWym2qs7Y2hkDOnDlDNzc3o7rV
i8Tjx485bNgwOjo6ctWqVWYZ/6SkJNra2rJly5a0t7fnm2++yePHj5e7z19//cXGjRvztdde461b
t4zry+OJGPuUUkkHlYpz5sx5ZaVuLTAfFgP8AvGq6EXPmzePrq6uJZidd+7c4b/+9S/6+vpy7969
3Lx5M/38/BgTE8MTJ05QVKgDXVG3rgKV07PNzMzkoUOHOHbsWEZFRdHBwcGYNlTkLtaiIE4qAWgv
EHA4THMXmyv1p0GBu1onEFAC0KbwWn428b40KIg3azQa1qhRg02aNGFcXBzfeustTpw4kXPnzuWY
MWOoVqvZs2fPKklfkQmFbNCgAe3t7anVahkdHc1BgwZx7ty53LNnD1NTU41G6fbt25wzZw7r1atH
Ozs7s0RYipai2GN56lYvEkePHmVISAhbtGjBP/74o8L7z58/nzVq1ODvv//OadOm0dPTk/Xq1eOS
JUtKeA6KkJeXx/Hjx9PV1ZX79+83rn+WJ+IqldJBKKQEoEYopFYqpcLKivWCgugmlb70b4cFVQuL
AX6BeNkG2GAwcPLkyfTz8yu2fxHT08HBge+++y4PHDjAqKgo1qxZkz/88APJAnUkFxeXCrvO3BUK
9unZ0yz3ZVmpE0Uzh2ip1OyiDkTVqHTVBLiq8BpMUSuKlEqps7ZmwwYNqFQqaWNjw2HDhpU5K719
+zbbtGlDR7m8ymRODQYDU1NTuXfvXn755Zd86623GB0dTY1GQ3t7e0ZERHDAgAGcNWsWf/jhB4b6
+lb63LW8vZ+rbvUikZubyxkzZlCj0fCTTz4pVfu6LBgMBvbt25fx8fE0GAzMz8/nzp072bFjR9rb
2/Ott94qk9y2a9cuOjo68qOPPirmwUpYt446lYoRSiUXALz3TN9ZCVRNXrrFBf1KwWKAXyBeZsGG
/Px8Dh48mLVr1y7mBrt69SpjYmJYs2ZNfvfdd+zevTudnZ25dOnSYjGr48ePM7TwA26K66yZSlVM
QCQ+Npa6ihRjKEM8oMIDAJQdj62sSldjlEwzelqGUll4fm3hx1MFsEePHrx37x6/+eYb+vj4cPDg
wXz77beNut2lxRUNBgP79OljVgy+aGmmUpnEgL1z5w7379/P+fPn8+2332ZUVJRZ+sXP9lkJwL17
91aoz74IXLp0iS1btmStWrVMVt8iC9z1derU4efP9NEbN27wgw8+oLu7O8PDw7l8+fIS8pTXr19n
REQEW7duzbt375rcp6uCT2EhYb1asBjgF4yXUbDhyZMn7Nq1K5s2bWpUOdLr9Zw3b54xTeO9996j
Wq3mxIkTS3Wj7dy5ky1btjT+XVqKladSSaVYzKjQUK5bt84Y97t58ya1Wi0/+/RT6qytGS4QmGy4
n8a6tWvpKpVWmVJUlXzQytmehgKlooMA7fFfcZCi+HVRqlFRcYmnVblEIhElEgnlcrmRbFaZ9DWl
UMiaNWuydu3arFu3LuvXr8/w8HA2bNiQERERjIqKYuPGjdm0aVM2b96cLVq0YKtWrdi4cWM6iURm
P6OixV0uf2VdnwaDgWvWrKGjoyOHDh1qErmKLCCTOTo6ct++fSW25efnc/v27WzXrh3VajWHDBnC
M2fOGLfn5ubyvffeo0atNrlPV3bAaOogzIIXB4sBfsGobMGGir5Ejx8/5muvvcbOnTsbcyHPnz/P
yMhINmzYkJMmTaKTkxP79OlTbtWaFStWsFevXqVue16N186dO3PChAkkydjYWPbo0aOE4ZYKBKzt
51fMcBdBr9dz/fr1tBaJqkwruapUukyRmiy6BnmhgS3S965Xrx61Wi3PnTtnvNcTJ06wdevW9PT0
5PLly5mens709HQ+evSIy5YupZtMVuEBiKtUyhkzZvDEiRM8fvw4f/31Vx49epQ///wzDx06xIMH
DzIxMZH79u3j3r17+eOPP/L777/nrl27uHTpUrqbWL+2vOX/Q+zx3r177N+/P93d3fntt9+atM8P
P/xAJyenct+da9eucdKkSXR1dWWjRo24YsUKZmVl8cmTJ9QoFCb3aUt94H8eLAb4BaOyifgVeYnu
3LnD+vXrc8CAAczPz2dubi4/+ugjajQaDho0iMHBwWzSpMlzWZwkOWPGDI4aNarC97tlyxYGBgYy
OzubycnJdHR0NLrkigx3SkoK5XJ5ibKJ2dnZXLJkCQMCAujr68vGlTAEz6pSVZlICApmuaa0jSrU
nw4KCqKDgwMbNGjAGjVq8KOPPirx3Pbv388GDRqwVq1a3LFjh5EcVVEXvJOVFasFBFS4klERXsU6
13839u3bx4CAAL7++usmSWN+8sknDAsL45MnT8ptl5eXx23btjEmJoYajYatWrViU4WiQs/SUh/4
nwWLAX4JMDen0l2h4PJly0po75aGq1evMjAwkOPHjzfqQ4eEhLBRo0aMiIhgQEAAt23bZnIqxqhR
o/jpp59W6D7T0tLo6urKxMREkmR8fDxnzJhRot3hw4dZp04d498PHz7k9OnT6ezszDZt2nD//v2M
rFWrSt3FL8MAbwJoKxTS2dmZ586dY3x8PIVCIW1sbLhhw4YSA6ui8pLBwcGMiori4cOnqha9AAAg
AElEQVSHSf43Bt9UqXyuK3/N6tVs2rSp2VWNyFenzvWLRHZ2NidOnEitVst58+aVm/JnMBgYGxvL
N9980+TjX7lyhX4ODmY918rqyFvw6sBigF8SKjKTOQxQLZEwyNm5VO3dZ0sWnj17lu7u7pw9ezaz
srL43nvvGdNOdDodv/zyywqxPkmyV69eZapllYVBgwZxwIABxmtycHAoNb78+eefc/Dgwbx+/TpH
jRpFtVrNXr16GUvZVVX+9NPu4qpS6TLVBV3UXoICzec1a9YwJyeH1tbWVCqVbNCgAR0dHTl27Fhe
unSp2PPJy8vjsmXL6O7uzo4dO/Ls2bP/jcGHhFAuFFKLAldzaTH4O3fu0MPDg5s2barQ71eEFx02
eZVw9uxZRkREsEGDBuWWVnz8+DGDgoK4ZMkSk45b2T5dxLgPQ9mM+/L4FBa8GrAY4JcIU9jE1aVS
KgA2lslMKll4+PBhOjo6cvXq1dy/fz99fX1Zo0YN2tnZcfTo0cUqvVQELVu25M6dO01uf/DgQbq4
uBjP969//YvTp08vtW2rVq0YFRVFe3t7jhgxglevXi22vcrSt1B8tvp3k7BKW7QoKPjg6+vLvLw8
tmvXjtHR0fzyyy95/vx5jhw5klqtli1atOCmTZuKDZSysrI4c+ZM6nQ69u3b1/ic0tLS+O2339LL
y4vdu3cvlUT066+/UqvV8uzZsyb/hkV4kWGTVxF6vZ4LFy6kVqvl+++/X6ZudUpKCrVarUls6qro
0zkoqPAVHhz8XCKkBa8mLAb4JaM8NrG/iwtdJJIKydXZKpXcuHEj33zzTdrb21OtVrNr166VJsCE
hoaaFCsmCz7YQUFBxhnXuXPnqNPpihkGg8HAgwcPsl27dhQKhRwxYkSZ+tV/lwGuNKsUz692VJoB
btasGQMCAvjNN99w7ty5bN68OZs1a2a83+zsbK5evZpRUVF0cnLiuHHjiv1+Dx8+5Lhx46hWqzly
5EijtGJ6ejr79+9PPz8//vLLLyWe49dff01/f3+zYrGVCZv8U2Zgf/31F+Pi4ujr61tC37kIW7Zs
obu7e5l53UWoak2A5xEhLXg1YTHArxCefomWL1tmnvauWEyVSkWNRsN69eoZ44aVhbOzc7lMz6cx
efJkduzY0Rhf7t69u5FopNfruXXrVjZs2JB+fn785JNPqFary41FVxURSIHiAgfpANWoBKsUFatM
U+SCnjJlCsPCwujr68szZ87Q1dWVKpWK9+/fL3HvZ8+e5fDhw42knS1bthhnxX/99RcHDRpEjUbD
adOmGcltGzZsoE6n4yeffFIidjl48GC2a9fOLBlTc0RY/omxx+3bt9PDw4O9e/fm3bt3S2x///33
2bRp0xJFJp6unXz16tX/OXKbBSVhMcCvICrr8lMIBFyzZk2VCd3r9XpaWVmZ5M5KTk6mVqs1skfP
nz9PrVbLO3fucMmSJQwMDGT9+vW5adMm5ufnc/PmzWzbtu1zj1sVRCB7gYBKsZgOQiE1AJVWVrSX
SqmBGaxSmF6L9+lrsBMK2atXL9rY2DAqKqogzcfdnc2bN+c333xT5v1nZWVx5cqVjIiIoIuLCydM
mGAswHHx4kXGx8fT2dmZ8+bNY25uLq9evcqoqCg2a9asGJM3JyeHERERnDJlSqnnedpIlPZhN0eE
5Z+I9PR0jhgxgg4ODvzmm2+KvWv5+fls0aIFR48eXW7tZCeZzGTJ1LL60/83cpsFxWExwK8gKk16
qeK6n/fv36ednd1z2+n1ejZq1Ijz5s0zruvatStbtGhBZ2dnxsTEcN++fcU+VqNHj+bUqVOfe+xp
06axYSUEISIkErZv355paWls2bIl5XI5e/XqxWrVqhXUABYIqkRdq7wlDGC9evWoUqnYvHlzjhkz
hl5eXuzXrx979OjBTp06mfR7JCcnc9iwYVSr1YyJieG3337LvLw8Hjt2jC1atKCvry/XrVvH3Nxc
fvjhh3RwcODWrVuN+6emptLV1dVYBas8I1EayS8nJ4cDBw6kvZUVFVZW/9Oxx2PHjrF27dps3rw5
f//9d+P6e/fuUafVUi2Xl187GaYX8Cjxnv8/JrdZUACLAX4F8aqlfZw7d44BAQHPbTdv3jw2atSI
er2eN27c4BtvvEGBQMCuXbuWKPxQhKioKP74449lHvPChQuMi4ujk5NThUsMPm00rUUiow5xv379
aG1tTWtra/r7+1MsFhMA7aTScmd2YQIB5QCnm3kNcoCDBw9mt27d6OrqyubNm7Nly5YcMGAAW7Ro
QZVKVSIXujxkZmZyxYoVbNiwIV1dXTlp0iRevXqVe/bsYb169Vi7dm1+//33PHToEL29vTlo0CDj
8Q8fPkydTsdZX3xBRxubco3E0yQ/g8HA6dOn09PTk+fPn7fEHlnAUp85cyY1Gg0//vhj5ubmcs7n
n9NVKv3bBnX/BHKbBRYD/MqhylJuqjA2tH//fkZFRZXb5vr169Rqtdy2bRv79etHe3t7BgcHc8SI
EWXuk5ubS6VSWep13rx5kwMHDqRWq+XHH3/MjIwM84lAcjllUqlRKOHdd9+lQCCgXC6nlZUVZTIZ
AfDChQtct24dPdVqSlFQsahIx1krkdDBwYGRERFmuazd5HJ6eXlx+PDhHDp0KGNjYymRSLhr1y66
uLhQpVKxSZMmxWaqFcHp06c5ZMgQqtVqtm3bltu2bWNCQgIDAgLYtGlT7t27l927d2dwcLCxUEB8
bGzFZv5yOZtGRbFGjRomCVT8r+Hy5cuMiYmhu5tblUqmltr2H0Ru+1+GxQC/YnjZFZNKw/r16xkb
G1vmdoPBYBT3cHR05LRp0/jrr79So9GUm/Z0/PhxVq9evdi6hw8fcuzYsVSr1Xz33XdLFE83hwj0
Rp8+jImJMR5jypQpFAgE9PX1pUgkolKppLu7Ozt06ECDwUBXV1fGx8cTANVqNcViMW1sbNipUyfq
dDo6qNV0FIlMvgYNwIjwcMbFxXHIkCHs0qUL79+/T7lczhEjRrBNmzb09PTksGHD2Lt3bzN/pQJk
ZGRw+fLlDA8Pp5ubGydOnMhPPvmELi4ujI2N5aeffkqtVsvevXubNZjRCYVcunRppa7xn4zs7Gyq
5fK/jdj3Tya3/S9CCAsseA7u3LkDR0fHEusNBgO2bduG4OBg/PLLLxg6dCguX76M8ePHY968eRgy
ZAjs7OzKPO6RI0fQoEEDAEB2djY+++wz+Pv7486dOzh58iQ+++wzaDSaYvsMGzkSny1fjrY2NoiW
SrEFQP5T2/MAbAYQLZMhWiDA6OnTIZJK0bJlS2ObmzdvgiTu3bsHknBycsKECROwc+dOnDhxAlKp
FPv370enTp2QkZEBg8EAkUiEyMhIpKWlwUatxvTFixEFIBwo8xoaCoWIAnAfgMzaGsePH8f9+/eR
mpoKtVqNd999F/Pnz8eoUaPw4MED5ObmYseOHcjLy6vAr1McSqUS/fr1w5EjR7Bjxw7cu3cPM2bM
QGhoKKytrTFjxgw0adIEm1evxrfZ2fCowLE9AOwyGDB+5Ejk5uaafY3/ZGzduhW1RSLUMWPfugC8
AYxF6f2puUqFtjY2+GzZMgwbObIKrtaCl46XPQKwoDheRe3dCf/X3p0GRXWmbwO/e4VeoKGbZutm
aSMqEAU0bhGjCWY0GUcNRCVmmVIJbnFJyiUTtxiTVBytUQxRcZ1opNEYMprMIjr+HSumjBM1E4Vo
VNwy+maICuoAjdLX+wHpEWmg99Pi/aviA2d5+njK4upzzn3uZ968JlWztbW1WL9+PTp37oy0tDSE
hoY2mWT8zJkz0Ol0Lb7X2+jll1/GmjVrsG7dOhiNRjz33HNNJiZozYoVKxAWFobeSUm296f1IhEU
YjEilEps3boVY8eOxbJlyxAXF2drQGGxWKDT6UDUMOvQsmXLMGDAAKxevRpqtRoDBw7EmDFjIBaL
8f3332P16tUgIrz00kuIjY2FRCJBUFAQ/vjHP0Iul0MikSBUIoFSKkUYEWKVSgSIRNCIRNBqtejR
oweIGqYhHDhwIFQqFYxGI4CGZ7hyuRwjRozA448/jpiYGPTs2RN79+5tsxrZGbdu3cL69evRs2dP
GI1GdO7c2b2pDT1c5NeeeKJ+IzIwkBtrPCQ4gP2QvxVh5ebmYvXq1aisrMSSJUsQHR2NIUOGYN++
fcjJycGkSZOabD9u3DjMnz+/1TGtVisiIyNhMpkwcOBAHDp0yOHjyc/PR1xcnO0We2Mh0DPPPIPg
4GBbE4q//OUv6N69OwwGg63y+r333oNKpQIRISUlBUDDrfDIyEjk5uZCKpVi0KBB0Ov1AIAXX3wR
IpEIIpEICxYsABHhN7/5DYKDg2EwGGAymaDT6VBZWYnRo0dj+vTpWL58OYYMGYLw8HBIpVIQEcaN
G4eIiAjo9XoQ/W9u3KysLERFReGdd94BEWHo0KEw6XQOVSO74ujRo4jXav3q/1d74cn6jQsXLjz0
xW0PAw5gP+RvvXcHDx6M4cOHQ6vV4sUXX7QV8ezfvx9Go7HJH4jy8nJotVq7TSUa7du3D2lpaRCL
xU1m+nHERx991CR87/Xkk0+ic+fOtt9ra2uhUCgwatQoAA0N8JVKJaRSKcRicZPXpV555RVMmzYN
RASlUokpU6bg7Nmz0Ol0CA0NRW5uLsRiMWQyGcLDw9GpUyeIxWIMGTIEarUaX331FU6dOgW9Xo9j
x47BaDQiICAATz31FIgIUVFRyM3NhUgkglQqRVhYGNasWYMdO3agV69eCAoKglIkQj+JxKFqZFf5
Y5Ffe+GP9RvMv3EA+yF/6b1bVlaGcePGQSKRYOTIkbbGD0BDsUmnTp2aVe3m5OTY5v6939GjRzF4
8GB06NABs2bNQkZGhlPHs2rVKsTGxjabrABo6MOr0WiQmJjY5NatwWDAuHHjADT0s24M35iYGLz7
7ru2/S9dumR7NYmIcOnSJeTm5mLevHno1KkTysrK0K1bNxARPv/8c1uQymQyLFq0yDblYlZWFpYv
X46oqCgYDAYMGDAARIRvvvkG/fr1g1gshkKhQGxsLOLi4jBp0iSoAgIQKZX6pMMUh4T38LllzuIA
9lNC9t49ePAghg0bhrCwMMyYMQMGg6FZH+i5c+ciMzOzybJz587Zvfo9ffo0srOzERkZifz8fFgs
FsybN6/FoLantfCtqalBt27d0CkqCnIixKtUtlu3wSIREhMT8fnnn0Mul0MkEmHGjBlISEjA9OnT
m4zTvXt3BAUFofEWcWhoKCoqKtCvXz8cOHAAb7/9NogIISEhiI6Ohlwuh1wux7PPPousrCy8+eab
OHz4MGJiYjBq1CgkJiYiOTkZRITKykpYrVZ07NgRMpkMCQkJCA0NRUR4OMLId/O7ckh4jz/WbzD/
xgHsx3zZe7e+vh47d+5E3759ER4ejkSDwfYcUn/3j0Ljc8gjR44gLCwM//73v5uMkZubi7feesv2
+5UrVzB58mTodDosXry4yVSEgwYNwpdffunQsa1evbrF8C0ym6FTKtFHJGrx1m0vamiCQUQYMWIE
Dhw4gISEBIwZM8Y2TuPrR0SE4OBgGI1GzJw5EwAwfPhwFBcXIzs7G0ajEXK5HIGBgcjIyIBSqURy
cjJycnIQHh6OgwcPIjk5GXGhoQggQrhIhLB7zl+/fv3Qs2dPjBw5EhqNBkqRyKd3OjgkvMvf6jeY
f+MA9nPe7r1bW1uLjRs3IjExEab4+DZb52Wo1VBLJMjJyWkyzoULF6DVavHLL7+gsrISc+fOhVar
xeuvv96sYf2dO3cQHBxst5H9/dasWYPY2FicOXOm2Tpnv6CEEWH50qX45z//iY4dO+Lpp5+2jVVa
WoqIiAgQETp06AAisrUWfPnll/Hee++ha9eu6Nu3L2JiYkDUMK/v+vXrERkZiejoaDzRvz9UYjEG
KhQtnr90uRxqiQQvvPACVq1ahX4ymct/rF2tRuaQ8B5/q99g/o0D+AHQ2pSFrr6eUFlZid///veI
jo7G4MGD8drEic5dbSsUTa62J06ciJkzZ9qdr/Z+J06cQMeOHds8xjVr1iAmJsZu+Lpzi37Z0qWI
j49H6j0hsmzZMhgMBnTp0gV6vR4SiQRPP/000u9OeB8tl0MvEiFQJEKoVIqQkBAQEebOnYuysjJo
VCqE3T03jpy/SKkUXaKiBAlCDgnv8Zf6DfZg4AB+wLjbe/fy5cuYPXs2tFotxowZg++++87t583l
5eVQqVSIjo7G8OHDceLEiVaPYf369XjppZda3aagoAAxMTFNGtw3cvePnF6thsFggMFgsI2ZkZEB
qVSKDz74AAEBAVAQoTdRy030JRKoxGKIRCJMnzYNxsBAp87fcWpocSlENTKHhHfx3MnMURzAD4kf
fvgB48ePR2hoKKZNm4Zz584BcP+PsU6hQEhICIxGIw4ePOjQseTk5CA/P7/F9a2FL+D+FdyTKhWC
goIgl8thtVpx8+ZNBAYGQiwWY3BGhlNtJsMlEgSS83MKnyVCrBvh2/jjajEUh4R38dzJzBEcwO3c
119/jeHDhyM8PBzvvPNOs97K7oZZb5EIgYGB+Pnnnx0+pkcffRTffvut3XVr165tNXwBzzzD1IjF
UKlUqKqqwq5duxAcHIz4uDiXKpL15Px0cmeJEC9gAAMcEt7GcyeztnAAt0P19fXYtWsX0tPTYTKZ
8NFHH7U4zZ0nwuyRu12jHFFVVQWVSoW6urpm6xpbUv74448t7u+pRhJyIlvQT5gwAUSEYKnUa030
7/+pJILq7rG48+9wtxqZQ8K7vFG/wdoPDuB2xGKxYNOmTUhKSkL37t1RVFSE27dvt7i9x7oiSaUO
h8CePXuQnp7ebLkj4Qs0vMdqDAhw+8pRR4ROnTph9+7d0Ol0EIvF6C0SuTzeU0QwO7lPOpFfVCNz
SPgGz53M7if13bQP7F5VVVV09epVIiLS6XSk0WhcHuvGjRu0du1aWrFiBSUnJ9PKlSvpqaeeIpFI
1Op+V69eJX1AAEndmH1HRkRhAQF07do1h/4Nhw4dor59+zZZtmHDBlq0aBHt27ePEhISWt3/xo0b
ZPHATDwiIrp25gyNePZZktXXk0Yqpdl37rS5X0smE1EeEWU7uc8qIsp08TNXBQXR5DlzXNz7f+Ry
OWVnZ1N2djZVVVXRtWvXiIhIq9W69f+SNaXRaPh8siZ4OkIfslgsZDabqX9qKhn0espISaGMlBQy
6PXUPzWVzGazU9O8Xblyhd58803q0KEDHT16lL788kvavXs3ZWRktBm+Qrl3CkIioo0bN9LChQvp
73//e5vhS0S0bt06uikSketfGRqmd6shojNWK1XV11M+EVXfuUPD3BhzGBEdJaIqJ/bJJKITd/dz
1hEiKhWJKDPT1fi2T6PRkMlkIpPJxGHBmLcJfQn+sGh81tZWkwtHnrWdPHkSOTk5CA0NxdSpU10u
wvF1VySr1QqdTmfroLVhwwYYDAacOnXKoeMtKytDWFgY+iQluX/r9p7fPVYQRYRyJ/f5hMinrSgZ
Y/6DA9gHPFVt+vXXX2PEiBEIDw/HokWLHOok1RZfdkU6ffo0YmJiAAAbN250KnytVit+9atfYfny
5e43kqCmz2uFDOAdREiIjuZqZMYeQhzAXubu+5b19fX44osv0L9/f5hMJuTn57dY0ewKX3ZF2rJl
C0aOHIlNmzbBYDDg5MmTDh/nzp07kZiYiLq6OvcbSVDTimWPVSTfHcuZ/QaqVNiwYQNXIzP2EOIA
9iJ3g0KrUCAxMRFpaWltVjQLdYzOdEWaMmUKsrOznQ7fmpoadOjQASUlJbZlLn+xIfvv7HqkItmF
86ckglIqRXpKCjZv3owtW7YgvVs3yIkQLZcjQiLhamTG2ikOYC9y9+qyj0SCt956y6kJ613hq65I
8fHxCAsLcyp8AeD999/HiBEjmi13+tY+EfJaWF9IhAw3ArgXET508cuAvRqAF154ATNnzoRarcZ/
/vMfp84XY+zBwAHsRQ/SrDPe7opUUFAAkUiEY8eOOXVcly5dgk6nszsVIeBgIwlquO3cWreq2rvb
uHonIDQwEMbAQLe/DDSe24k5ObapC/fv3+/UOWOMPRg4gL3EY00ufDjvqiNh9rhM5vRzyI8//hg6
nQ5du3Z1+pjGjBmDuXPntrrN/Y0kYpXKhjmMqeG2sJkc61JVdDcYXb0T4KkvAxeoYbYplUqF1157
rckcy4yx9oMD2EvOnj2LeDduPzf+uNPr1xUtdkWSShEikSA/P9+p55CbN29GdHQ0Zs2ahalTpzp1
LF999RWMRiNu3brl8D6VlZXYv38/DEql0wVRuHtVGkOOTyt4/52A+89f2N3xnP0y8C0RgmUyTJw4
EY899phT540x9mDgAPaSBzWA73Vv67wZM2Zg0qRJTu3fGL5lZWXIzMzE1q1bHd73zp07SEtLQ2Fh
obOH7fb7zUV3r1J7EbV4JTtAoWjzTsD69euRJhKhnJyvjgYRnlAo0LFjRwQFBTWbRIMx9uDjAPYS
Xze58KaKigpotVpcuHDB4X22bNmCqKgolJaWwmq1IioqyqkvEmvXrkV6errLBWjuPn83E6FzXBz6
de0KOREiJBJbf+REoxE9evRo806AJ2oAQiQSZGRkYNu2bS6dB8aY/+JWlF6i0WgoLSmJvnBjjF1E
1D05WfCWgH/4wx9o5MiRFBsb69D2n3zyCc2ePZv27t1LSUlJ9NNPP1F9fT3Fx8c7tP/169dp/vz5
tHLlSpdbak6eM4dWqdUu7UtEtC4oiN7+4AOa8957FKTT0Rvvv0//d/w4/buigv558iSdP3+efvrp
pxb3r6qqomNlZW63t6wFSKFQUElJiRsjMcb8ktDfANozXza58JZffvkFWq0W58+fd2j7Tz75xHbl
22j79u0YNmyYw585ffp05ObmOn2s9/LU+80TJkxAQEBAs1eBZs2ahddff73Fz/fUIwhjYCC6dOmC
mJgYr7+OxhjzLb4C9qLMzEw6IRb7VbN9Zy1fvpyysrIoLi6uzW0LCwtp1qxZtGfPHkpKSrItv38C
htaUlpbS1q1b6d1333X5mImIAgICKK+ggEYoFHTRif0uEtFzSiXlFRSQTCajP/3pT5SUlER6vb7J
dlOmTKGPP/6Ybt686dZxtkUikdCVK1eovr6eTp065dXPYoz5mNDfANo7XzW58IarV69Cq9Xi3Llz
bW67detWREVF4cSJE83WPf7449i3b1+bY1itVmRkZCAvL8+Vw7XLnfebT506BZVKhaVLl9odOysr
Cx9++KHddZ6sAXjllVfQq1cvj54XxpjwOIB9wNtNLrxl/vz5GD9+fJvbFRYWthi+FosFSqUSN27c
aHOc4uJiJCcno66uzqXjbYmrfZZXrFiBwMBAnD592u64Bw4cQEJCAurr6+2u91QjlpKSEnTs2BFD
hw716HlhjAmLA9hHHrRm+9euXWu1A1WjwsJCREZG4vjx43bXHz58GN26dWvz86qrq2EymbB3716X
jrctLb3frJRIYAgOtttnuU+fPjAajS2OabVakZqaij//+c921xcWFqKvWOx2DcDt27eh1WoRFBTE
vaAZa0c4gH2oxSYXfthsf+HChRg7dmyr25jN5lbDFwBWrlzpUEHV4sWLkZmZ6fRxuuLe95tLSkrQ
q1evZttUV1dDLpfjjTfeaHWsTZs2YfDgwXbX1dbWQi2ReGSii1dffRUxMTHclpKxdoQDWCD3hoDQ
7/ne7/r169DpdDhz5kyL2xQVFSEyMhLff/99q2ONGTMGGzdubHWbixcvQqfTOfSs2dNOnz4Nk8nU
bPlf//pXKBQKfPPNN63uX1NTg4iICPzwww9213fo0AHhYrHzNQAKRZM7IXv27EFUVBS3pWSsHeEq
aIFoNBoymUxkMpkEf8/3fnl5eTR06FB65JFH7K7ftm0bzZgxg0pKSqhr166tjuVIBfTs2bNp8uTJ
Dr8n7El6vZ4qKiqaLTebzSSVSumxxx5rdf/AwEDKzc2llStX2l2v1WpJ+8gjlK5Q0BEHjucIEfWS
SCiic2caNXq0bfnAgQOpurqavvjCnTfLGWN+RehvAMy/VFZWQqfT4ccff7S7ftu2bYiMjMS//vWv
Nsf6+eefERIS0mKREtBQyBQTE4P//ve/Lh+zO6xWK+RyOWpqapos1+v1yMrKcmiMy5cvIyQkBNeu
XWu2rkePHhg0aJBTNQCbP/4Yffr0wYIFC5qMlZOTg8DAQJSXl+Ps2bM4e/as3909YYw5jq+AWRMr
V66kZ599lhISEpqt+/TTT2n69Om0e/du6tatW5tjHTp0iHr37k1isf3/ZvX19TR16lRaunQpKZVK
t4/dFSKRiMLCwppcBZ87d44qKytp/PjxDo0RFRVFv/71r2nDhg1210skEhqdnU0XKyooZ906WpGa
SiEyGcWrVBSvUlGoTEZ5qan06tq1dLGigl5+5RXauXMnbdmyhbZs2UJERBaLhSIiIiiwro4eTUig
jJQUykhJIYNeT/1TU8lsNlNdXZ37J4Qx5jtCfwNg/qOqqgphYWE4depUs3Xbt293+Mq30e9+9zss
XLiwxfVr1qzBE088IXiHp5SUFBw5csT2+wcffACZTIba2lqHxzh8+DDi4uJw+/btJsvT0tLwzDPP
NNvekRqA0tJShIeHY+GCBYgIDsYgtRrFdq6ePyNChlrtNxX0jDHHSIX+AsD8x4cffkiDBw+mTp06
NVn+6aef0tSpUx2+8m106NAhmj17tt11169fpwULFlBJSYnL/Z495f7nwGazmbp3704BAQEOj9Gz
Z0+Kjo6mXbt2NeleBsDuv0+j0bT57D8pKYlGPvccffTOO/Q3IuphZxsZEWUSUeatW3SEiJ4bP55+
vnyZpr3xhsPHzhgTBt+CZkREdPPmTcrLy6N58+Y1Wb5jxw5b+KakpDg8Xn19PawkuowAAAdzSURB
VH377bfUq1cvu+sXLlxIWVlZTo3pLfcGsMViodLSUho7dqzT40ybNs1uMVZLt+Dbsq2oiHZt3kxH
yH743q8HEX1VXU3L5s+nbUVFLn0mY8x3OIAZERHl5+fToEGDqEuXLrZln332Gb322mtOhy9RQ0/n
6Oho0mq1zdYdP36cioqKaPHixW4ftycEBwfTyZMnqby8nHbu3ElWq5VG31OB7KisrCw6c+YMfffd
d0TUMCNSTU0N1dbWUlVVlVNjWSwWmj5hAv2ppoYcm4OqQSwRfV5dTdMnTOBnwoz5O6HvgTPfqqys
bFZBe/PmTej1epSVldm227FjByIiInDs2DGXPqegoAC//e1vmy23Wq148sknkZ+f79K4nlJbW4vC
wkKkp6RAIRYjWiZDvFqNQJEIOrkchYWFLjVFWbRoEQYMGID0lBSoZDKEi8WIlEigksmQnpLi8Lhu
z6SlVgs+kxZjrHUcwA+Be8NGdTdo4tVqWyhkZ2fj+eeft23/2WefISIiAkePHnX5M8eOHYvVq1c3
W75jxw507dq1WbGSLzW+EjQoKMijRU1FZjPCg4LQm8jtcT3VR5ox5r84gNs5R8Kmt0gEvVqNIrMZ
xcXFbocvACQmJja7eq6urkZcXJxDMyN5i7cmxvDkuI0zKd12YKyWfhpnUuL3hBnzXxzA7ZizoRAt
lyNErXY7fK9fvw61Wt3sKnfRokVNrrR9zVtTQ3p63LNnzyLejdvPjT9xKhXKy8u9eUoZY27gAG6n
XA0FQ2Cg2++S/u1vf8OAAQOaLLtw4QK0Wi3Onz/v1tiuqq2tRURwsEcmRvD2uBzAjD0cuAq6HXKn
gnZnba3bFbT2+j/PmjWLpk6dSnFxcS6P647i4mJ61Gql7i7s24OIkq1WKi4u9sm4Op2OKiwWuu3C
mI1uE9EvdXV2q9AZY/6BA7gd8lbYOOrQoUPUt29f2+/79+9vtSmHL6xasoQm37rl8v6Tb92iVUuW
+GRcjUZDaUlJ5M60C7uIqHtyst9N9MEYu4fQl+DM84SsoK2vr0doaCiuXLkCALh9+za6deuG7du3
e/Kf6BRvFTV5s1jK7deQgoL4NSTG/BxfAbczVVVVdKysjIa5McYwIjpaWup08wgiotOnT5NGo6HI
yEgiIlq7di1ptVp6/vnn3Tgi91y9epX0AQHkTt9VGRGFyeV07do1r49LRJSZmUknxGI66sKYR4io
VCRq0hKTMeZ/OIDbGW+GQkuqqqqovLycysvLad++fbbnv1evXqW3336b8vLyBO/3/KAJCAigvIIC
GqFQ0EUn9rtIRM8plZRXUEByudxbh8cY8wCejIG5xGKxUHFxMa1asoSOlZWR/u7EBf+vupriIiPJ
bDbTP/7xDxo1apRTEzh4w71FTTIXx7BX1OStcRuNzs6mny9fpvR58+jzmpo2+0EfoYbwnbl4MY3O
znbxiBhjPiP0PXDmWY3PJeu88FyykSPNPZ5UKqEUibB+3TofnwH7vPVc3BfP2xvPd4Zajc/snO8d
d5/58nSEjD1YOIDbIW+Ggrc6SXmbt4qafFUsZbFYYDab0T81FSqZDHEqFeJUKqhkMvRPTYXZbHap
dzVjTDgiABD6Kpx5ltlspg25ubTXxddjMoKC6NW1ayn7vtuY24qKaNa4cfSVE+8XXySidKWSlm7Y
IOhtUYvFQnHh4fSXGzecfj3rCBH9OjiYLlZUNHuu6q1xW1NVVWV7Pq/VavlVI8YeVEJ/A2Ce543u
TN7qJOVLD0orSsbYw4GroNshb1TQCt3cwxNGZ2fTzHffpXSFgo44sP0Rarh6b6uoyVvjMsbaOaG/
ATDv8eTz2vY0PZ63ipq4WIox5gwO4HbOE6HQHqfH81ZRExdLMcYcxUVYD4G6ujrbO7tHS0sp7O7t
5V/q6qh7cjJNnjOHMjMzWywEKi8vp4yUFDrnRs9jIqJ4lYr+7/hxMplMbo3jad4qauJiKcZYaziA
HzKuhEJ7D2DGGBMCd8J6yGg0GqevxLzd8Ykxxh5GXAXN2sTT4zHGmOdxADOHTJ4zh1ap1S7vvyoo
iCbPmePBI2KMsQcbPwNmDhGi4xNjjLVnfAXMHMLT4zHGmGdxADOHcccnxhjzHL4FzZy2raiIpk+Y
QI9arTT51i0aRv8rp79NDQVXq4KCqFQkoryCAg5fxhizgwOYucTd5h6MMfaw4wBmbuOOT4wx5jwO
YMYYY0wAXITFGGOMCYADmDHGGBMABzBjjDEmAA5gxhhjTAAcwIwxxpgAOIAZY4wxAXAAM8YYYwLg
AGaMMcYEwAHMGGOMCYADmDHGGBMABzBjjDEmAA5gxhhjTAAcwIwxxpgAOIAZY4wxAXAAM8YYYwLg
AGaMMcYEwAHMGGOMCYADmDHGGBMABzBjjDEmAA5gxhhjTAAcwIwxxpgAOIAZY4wxAXAAM8YYYwLg
AGaMMcYEwAHMGGOMCYADmDHGGBMABzBjjDEmAA5gxhhjTAAcwIwxxpgAOIAZY4wxAXAAM8YYYwLg
AGaMMcYEwAHMGGOMCYADmDHGGBPA/wctG4Yq7dB05wAAAABJRU5ErkJggg==
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
<p>Hm, it looks a bit thinner. Using a visualizer will make the difference a bit more noticeable.</p>

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
<p>Now you have a graph the last step is to write it to disk. <em>networkx</em> has a few ways of doing this, but they tend to be slow. <em>metaknowledge</em> can write an edge list and node attribute file that contain all the information of the graph. The function to do this is called <a href="{{ site.baseurl }}/docs/metaknowledge#write_graph"><code>write_graph()</code></a>. You give it the start of the file name and it makes two labeled files containing the graph.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[46]:</div>
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
<div class="prompt input_prompt">In&nbsp;[47]:</div>
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


<div class="output_area"><div class="prompt output_prompt">Out[47]:</div>


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
<p>This is full example workflow for <em>metaknowledge</em>, the package is flexible and you hopefully will be able to customize it to do what you want (I assume you do not want the Records staring with 'A').</p>

</div>
</div>
</div>
{% include docsFooter.md %}
