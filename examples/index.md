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
<pre>[&apos;Nasalski, W&apos;]
[&apos;Nasalski, W&apos;]
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
<pre>Longitudinal and transverse effects of nonspecular reflection
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
<pre>[&apos;PT&apos;, &apos;AU&apos;, &apos;AF&apos;, &apos;TI&apos;, &apos;SO&apos;, &apos;LA&apos;, &apos;DT&apos;, &apos;ID&apos;, &apos;AB&apos;, &apos;RP&apos;, &apos;CR&apos;, &apos;NR&apos;, &apos;TC&apos;, &apos;Z9&apos;, &apos;PU&apos;, &apos;PI&apos;, &apos;PA&apos;, &apos;SN&apos;, &apos;J9&apos;, &apos;JI&apos;, &apos;PD&apos;, &apos;PY&apos;, &apos;VL&apos;, &apos;IS&apos;, &apos;BP&apos;, &apos;EP&apos;, &apos;DI&apos;, &apos;PG&apos;, &apos;WC&apos;, &apos;SC&apos;, &apos;GA&apos;, &apos;UT&apos;]
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
<pre>Longitudinal and transverse effects of nonspecular reflection
ASYMMETRICAL MOMENTUM-ENERGY TENSORS AND 6-COMPONENT ANGULAR-MOMENTUM IN PROBLEM CONCERNING 2 PHOTON MOMENTA AND MAGNETODYNAMIC EFFECT PROBLEM
WHY ENERGY FLUX AND ABRAHAMS PHOTON MOMENTUM ARE MACROSCOPICALLY SUBSTITUTED FOR MOMENTUM DENSITY AND MINKOWSKIS PHOTON MOMENTUM
CONSERVATION OF ANGULAR MOMENT WITH SIX COMPONENTS AND ASYMMETRICAL IMPULSE ENERGY TENSORS
LONGITUDINAL AND TRANSVERSE DISPLACEMENTS OF A BOUNDED MICROWAVE BEAM AT TOTAL INTERNAL-REFLECTION
CALCULATION AND MEASUREMENT OF FORCES AND TORQUES APPLIED TO UNIAXIAL CRYSTAL BY EXTRAORDINARY WAVE
GENERAL STUDY OF DISPLACEMENTS AT TOTAL REFLECTION
Simple technique for measuring the Goos-Hanchen effect with polarization modulation and a position-sensitive detector
MECHANICAL INTERPRETATION OF SHIFTS IN TOTAL REFLECTION OF SPINNING PARTICLES
PREDICTION OF A RESONANCE-ENHANCED LASER-BEAM DISPLACEMENT AT TOTAL INTERNAL-REFLECTION IN SEMICONDUCTORS
SPIN ANGULAR-MOMENTUM OF A FIELD INTERACTING WITH A PLANE INTERFACE
TRANSVERSE DISPLACEMENT OF A TOTALLY REFLECTED LIGHT-BEAM AND PHASE-SHIFT METHOD
A Novel Method for Enhancing Goos-Hanchen Shift in Total Internal Reflection
EXCHANGED MOMENTUM BETWEEN MOVING ATOMS AND A SURFACE-WAVE - THEORY AND EXPERIMENT
Goos-Hanchen and Imbert-Fedorov shifts for leaky guided modes
Goos-Hanchen shift as a probe in evanescent slab waveguide sensors
RESONANCE EFFECTS ON TOTAL INTERNAL-REFLECTION AND LATERAL (GOOS-HANCHEN) BEAM DISPLACEMENT AT THE INTERFACE BETWEEN NONLOCAL AND LOCAL DIELECTRIC
Experimental observation of the Imbert-Fedorov transverse displacement after a single total reflection
NONLINEAR TOTALLY REFLECTING PRISM COUPLER - THERMOMECHANIC EFFECTS AND INTENSITY-DEPENDENT REFRACTIVE-INDEX OF THIN-FILMS
Numerical study of the displacement of a three-dimensional Gaussian beam transmitted at total internal reflection. Near-field applications
OBSERVATION OF SHIFTS IN TOTAL REFLECTION OF A LIGHT-BEAM BY A MULTILAYERED STRUCTURE
EXPERIMENTS IN PHENOMENOLOGICAL ELECTRODYNAMICS AND THE ELECTROMAGNETIC ENERGY-MOMENTUM TENSOR
SPIN ANGULAR-MOMENTUM OF A FIELD INTERACTING WITH A PLANE INTERFACE
Transverse displacement at total reflection near the grazing angle: a way to discriminate between theories
INTERNAL PHOTON IMPULSE OF DIELECTRIC AND ON COUPLE APPLIED TO ANISOTROPIC CRYSTAL
DISPLACEMENT OF A TOTALLY REFLECTED LIGHT-BEAM - FILTERING OF POLARIZATION STATES AND AMPLIFICATION
Optical properties of nanostructured thin films
THEORETICAL NOTES ON AMPLIFICATION OF TRANSVERSE SHIFT BY TOTAL REFLECTION ON MULTILAYERED SYSTEM
INTERFERENCE THEORY OF REFLECTION FROM MULTILAYERED MEDIA
DISCUSSIONS OF PROBLEM OF PONDEROMOTIVE FORCES
ANGULAR SPECTRUM AS AN ELECTRICAL NETWORK
SHIFTS OF COHERENT-LIGHT BEAMS ON REFLECTION AT PLANE INTERFACES BETWEEN ISOTROPIC MEDIA
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
<pre>&lt;metaknowledge.record.Record at 0x107ebf550&gt;</pre>
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
<pre>TURNER RG, 1980, AUST J PHYS, V33, P319
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
<pre>(-2934461741943450621,
 {&apos;count&apos;: 6, &apos;info&apos;: &apos;LEVY Y, 1972, CR ACAD SCI B PHYS, V275, P723&apos;})</pre>
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
<pre>(-2934461741943450621, 5771341660216694527, {&apos;weight&apos;: 1})</pre>
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
RU5ErkJggg==
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
UxQL9j9sm2JAdoN43ifL8/f3T5vbe+rUKWnRokWW+xkMBhkyZIjExsYWSN/yKnXeahtX13uy/iTM
1ayeKVZMSrm4SNjq1WnH3b59Wz7++GNxc3NL66uNjY107tw5x3Wni7LUzDc1+ArIZ5YgWwZkCogH
yB7Ld+UPEpzuu7thyXbjLO/LODpKvXr1pGTJktKjRw954YUX5OOPPy7sbj7SNPgqlUlRXKouN22a
M2OGrF27Vry9vbMNwl26dJHo6GgxGo2ybNkyKVGiRJb7VahQQcLDwwu0j7mVmJgoYWFh0jwgQFzs
7KSyi4tUdnERFzs7aVK3rgQFBUnNmjWlbt26smTJkgxlNK9duybDhw8Xe3t7mT9/vkyZMkU8PT2l
f//+cuXKlULsVd7kdNBe6mDCXvcJvqkFWVJvO+dlMKH6iwZfpbKQk4yqtZubVSsBpbaphaNjtm1q
7uh4T5vu3r0rH330kTg7O2cZWB0cHGTcuHFy69YtuXr1qvTs2TPbYN25c2e5ePGiVfqbGzExMRId
HS3R0dEZnlGaTCbZtm2bBAYGiqenp4waNUqio6PTtp8/f16Sk5NFROT69esyevRoKVmypIwbN+6R
qnmckpIi8fHx8t5770mvXr0kISFBmtarJ2tAjmMeK3AB80jn8en+/fyIuXb4Ecu/peGYa4iL5d9V
/Zo1JSkpSWJjY2XYsGHSrFmzwu7qI0+Dr1LZuF9G1TwgQMLCwvL9Ge/9rAkLk9JublLH0TFtAFZl
y8sF82IKfg4OUtrNLctfCH799df7BtZy5crJypUrxWg0ytatW6VatWpZ7ufq6ipz586VlJQUq/U9
P0VFRcmoUaPE09NTAgMDZdu2bVlOsbpw4YIEBQWJl5eXzJw5U+Lj4wuhtQ8nt4P2BGQhSAVLEO6E
eVCWWH7JbNKkiXh4eOR6MKG6lwZfpXIgu4zKWrK67RyDue50NBnnIj/oVvjevXvlySefzDYIP/XU
U7Jv3z65c+eOvPfee2mrK2V+NWrUSA4dOmTlbyL/3LlzR5YsWSJ169YVHx8f+fTTTyUuLu6e/Y4f
Py6BgYHi7e0tK1eufOR+6SiKAwmVBl+liryCGARmNBolNDRUypYtm20Qfv311+XSpUty7Ngxefrp
p7Pcx9bWVkaNGiW3b9+28reSf0wmk+zcuVO6dOkiJUqUkKFDh8rp06fv2W/37t3SpEkTqVOnjnz9
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
QmCC
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
AAALEgAACxIB0t1+/AAAIABJREFUeJzs3XlcVNX/x/HXsK+D7LIIiJSlpFRo7pLlkpoZmeJualnq
V9MWy8Qty6+lllqWlrkLZtEXd/1+NdNKf2YqplaGCii4sMkiCOic3x8jN0YW0XTcPs/Hg4fM3HvP
PXNn5D333HPP0SmlFEIIIYQwG4tbXQEhhBDiXiPhK4QQQpiZhK8QQghhZhK+QgghhJlJ+AohhBBm
JuErhBBCmJmErxBCCGFmEr5CCCGEmUn4CiGEEGYm4SuEEEKYmYSvEEIIYWYSvkIIIYSZSfgKIYQQ
ZibhK4QQQpiZhK8QQghhZhK+QgghhJlJ+AohhBBmJuErhBBCmJmErxBCCGFmEr5CCCGEmUn4CiGE
EGYm4SuEEEKYmYSvEEIIYWYSvkIIIYSZSfgKIYQQZibhK4QQQpiZhK8QQghhZhK+QgghhJlJ+Aoh
hBBmJuErhBBCmJmErxBCCGFmEr5CCCGEmUn4CiGEEGYm4SuEEEKYmYSvEEIIYWYSvkIIIYSZSfgK
IYQQZibhK4QQQpiZhK8QQghhZhK+QgghhJlJ+AohhBBmJuErhBBCmJmErxBCCGFmEr5CCCGEmUn4
CiGEEGYm4SuEEEKYmYSvEEIIYWYSvkIIIYSZSfgKIYQQZmZ1qysghBDmlJOTQ2ZmJgDu7u64uLjc
4hqJe5Gc+Qoh7npFRUXExMTQMiwMP09PnmjYkCcaNsTP05OWYWHExMRQXFx8q6sp7iE6pZS61ZUQ
QoibZWVsLCOHDOEhpRial8fT/N3kVwKsAeY6OXHQwoJZ8+bRIyrq1lVW3DMkfIUQd63ZM2cyfdw4
viss5NGrrPsr8KyDA6+/+y4jRo82R/XEPUyanYUQd6WVsbFMHzeOH6sRvACPAj8WFDA9OpqVsbE3
u3rXZMCAAURHR9/QMqdOncqLL754Q8sU1SfhK8RdIiIiAjc3t2pfu9y2bRu1atW6ybW6NYqKihg8
YACFhYU0BNoAF6qxXQDQoaCAqJ49+emnn6q9PwsLC44dO3adtb06nU6HTqe7oWW+/fbbfPHFFze0
TFF9Er5C3AWSkpLYvXs3Xl5erF69+oaVe+nSpRtWljnNmTOHgqIitgEZwESq98dOAf8DnCwsmDx5
8jXts6oreBcvXrymssTdT8JXiLvAkiVLePLJJ+nbty+LFy82WbZ+/Xrq16+PXq/H39+fmTNnUlBQ
wFNPPUVaWhrOzs7o9XpOnTrFxIkT6datG3379sXFxYXFixeTlpZGly5dcHd357777uPLL7/Uyp44
cSLdu3enf//+6PV6QkND+fXXX7Xlv//+OxEREbi6uhIaGsqaNWu0ZQMGDGDo0KF07NgRZ2dnWrZs
yenTpxk5ciSurq48+OCD7N+/H4APP/yQbt26mbyuESNG8Oqrr1Z4PGIXLMAG45msJdAKsKnGcdwB
5AKvGwxs3bKFkpISbVliYiKtW7emRo0aeHp60rNnTwBatWoFQMOGDXF2dmbVqlVs27YNf39/Pvjg
A3x8fBg0aBDFxcW8+uqr+Pn54efnx6hRo7RWitL1p06diqenJ7Vr12bFihUmdcvKyqJz587o9Xqa
NGminWkPGzaM119/3WTdLl26MGvWLACmTZuGv78/er2eBx54gK1btwLG965v377aNj/++CPNmjXD
1dWVgIAA7XN05ednxowZ1TiS4qqUEOKOV6dOHbVs2TJ15MgRZW1trc6cOaMtq1mzpvrxxx+VUkqd
O3dO7d27Vyml1LZt25S/v79JORMmTFDW1tYqPj5eKaVUYWGhatmypRo2bJgqKipS+/fvV56enmrr
1q3a+nZ2dmrDhg3KYDCot99+WzVp0kQppVRxcbGqU6eOmjp1qiopKVFbt25Vzs7O6s8//1RKKdW/
f3/l4eGh9u7dqy5cuKDatGmjAgMD1dKlS5XBYFDjxo1Tjz/+uFJKqbS0NOXo6KjOnTunlFKqpKRE
eXl5aa+lrHPnzikHKytVG1Q7UBdAqWr+DAQ1GFQxKB2oJUuWaOVGRUWp999/XymlVFFRkfrpp5+0
ZTqdTh09elR7/P333ysrKyv11ltvqeLiYlVYWKiio6NV06ZNVXp6ukpPT1fNmjVT0dHRJuu/9tpr
qri4WP3www/K0dHR5Fi5u7urX375RV28eFH17t1bRUVFKaWU2r17t/L19VUGg0EppVR6erpycHBQ
Z8+eVX/88YeqVauWOnXqlFJKqeTkZK2eEydOVH369FFKKZWUlKScnZ1VbGysunjxosrMzFQJCQlV
fn7EPyNnvkLc4X788UdSU1Pp0qUL9913H/Xq1TM5a7KxseHQoUPk5ubi4uLCww8/DFTeTNqsWTO6
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
uf4Pb731FomJiSQkJJCYmEhqaqo2K9KMGTOoVasWGRkZnD17lqlTp1Z6fbdu3bpkZWUxePDga7oP
uqJ1y74Ps2fPZvXq1Wzfvp1Tp07h6urKsGHDKiyrV69eNGrUiMzMTKKjo1m8eLFWzuLFi8nNzeXk
yZNkZWUxb948k1G5xDW4hU3et1RgYKCysbFRGRkZJs+HhYUpnU6nkpOTq1VO2es+/fv3V+PGjat2
Hb7//vtyA9uby4ABA7RB3S9cuKC89XrtOti1/Fx5HeyfOnjwoGrbtq1yc3NTNWrUUI8++qhav379
DSn7XhUYGKicnJxUjRo1VGBgoBo2bJi6cOGCUsp4zfe9997T1p07d67q0KGDUso4qYKrq6tKTExU
Sin12muvqWHDhimllNqyZYu6//771a5du8pdKyz72XrppZfU6NGjy9UpPz9f1ahRQ3377beqoKDg
ml5P69atlYODg6pRo4by8/NTffr0Kff/WCmlsrOzlU6nU7m5uUoppSIjI5WjlZXJ53dABdd8g0Bt
ufz7/aBWX7E80NFRHTt2TPu/bzAYlKOjo8n1359//lnVrl1bKaXU+PHj1TPPPKMdx8oUFxer0NBQ
tWTJEtW5c2c1cOBAbbKE5s2bq7Vr1171eJT+n1FKqaCgILVlyxallFIPPvig9rtSxokqrK2t1aVL
l0yu+SYnJysrKyuT96RXr16qb9++SimlvvrqK9WsWTN14MCBqt8kcVX37JmvTqcjODjYZJD33377
jcLCwhs+afXtSl3+thwXF0eowVDp/ZBVqeo6mFLqmkcxevrpp2nfvj1nzpzh7NmzzJ49G71efx01
E6V0Oh3x8fFkZ2eTlJTEJ598oo2ABMbBHUqVHTPYzs6O7t27s3TpUpRSxMbGar1e27Rpw/Dhwxk2
bBje3t4MGTKEvLy8cvs+efIkderUKfe8o6MjK1eu5PPPP8fX15fOnTvz559/Vvv1zJkzh+zsbE6e
PMnSpUtxd3fHYDDw1ltvERISgouLC7Vr1wbQmk11Oh1W1/h/+yRQvvam0tPTKSgo4NFHH8XV1RVX
V1eeeuopbb9vvPEGISEhtGvXjjp16jBt2rQKy9m6dSslJSX07duXVatWcfToUQYPHkxubi5//vkn
LVq0uOrxyM7OZs+ePeXWSUpK4tlnn9XqV69ePaysrDhz5ozJemlpaRWOMV36/7hv3760b9+eqKgo
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
CwoKUu+//74KDAxUdevWVT///LMKCwtTWVlZJuuVDq5x6dIllZaWpuzt7dWlS5cqLLN9+/Zq1qxZ
5Z7fvn27qlGjhmrj6KgNfNET1KTLvw8ANa7MoBhfgIoo8/gvUDpQMZcH2ggKClLx8fHK0dpaFYPq
A2riFds/efn33aDcyiy7CMoR1JbLg29YW1io7t27V/h6S/e1ZcsWpZRSdevWVfHx8RW+Pi8vL3Xw
4EHtOVdXV227iRMnqj59+phsExERoRYsWKCUUuqJJ55Qc+fO1Zb9+eefytraWl26dKlcfa7ctqxv
vvlG2dnZqYKCggrfH3OSM18hxA2xZ88ejh49isFgYMOGDaxevZquXbve6mpdkwsXLrB+/XouXrzI
xYsXWbp0KZGRkbz88suMHTuW+Ph4XF1dSU9PZ/Xq1eW2v1qz+ODBg5k+fTp79+5FKUViYiIpKSk0
adIEV1dXdl+8yP8B2zB2oiodsflqFwIOXl4nMjJSe87JyYmH69VjzVW2vR9j0/Z6jONGT8F4VgzG
2dp8PD2rPXnD4MGDiY6OJjExEaUUBw4cICsri/z8fKysrPDw8KC4uJjJkydrZ7Fg7ACXlJRU6aWI
nj178tFHH5GUlER+fj5jx44lKiqq0sFMylq2bJnWIc/FxQWdTlet7W62W18DIcRd4fTp0zz++OM4
OzszatQoPv/8cxo2bHirq3VNlFJMnDgRNzc3rUfs5MmTGTlyJF26dKFdu3bo9XqaNm3K7t27te3K
NlNW1SzerVs33nnnHXr16oVerycyMpLs7Gysra1Zu3YttYKDaQoMAZZiDEYwNv+WbQgt+zgFeMXO
DktLy3IhOXTMGOY6OWnbVLS9CzAXGIzxOrMTxqZuME6T2ujyfcNlVdYsO3r0aLp37067du1wcXHh
xRdf5MKFC7Rv354OHTpw//33ExQUhL29vdbDG9Dux3V3dyc8PLxcuQMHDqRv3760atWK4OBgHBwc
TAbdqKqZeNOmTYSGhmqfy9jYWGwvzxB1K8msRkIIcRspHQryu0qGgizrV+BZBwdef/ddRoweXW55
UVERgV5erM/N5ZFrrMevQCe9npT0dJm28CaQM18hhLiNjBg9mg+/+opOej1POjkRh7G3cqkS4Fvg
CWdnOun1fLhgQYXBC2Bra8usefPoam/Ptdz4lYIx1GfNmyfBe5PIma8QQtyGiouLiYuLY+60aew9
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
RETEw/4fB8E6/pI51qAAAAAASUVORK5CYII=
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
