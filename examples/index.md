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
  <a href="{{ site.baseurl }}/examples/#Importing">Importing</a>
  </article></li>
  <li><article>
  <a href="{{ site.baseurl }}/examples/#Reading-Files">Reading Files</a>
  </article></li>
  <li><article>
  <a href="{{ site.baseurl }}/examples/#The-Record-object">The Record object</a>
  </article></li>
  <li><article>
  <a href="{{ site.baseurl }}/examples/#The-RecordCollection-object">The RecordCollection oject</a>
  </article></li>
  <li><article>
  <a href="{{ site.baseurl }}/examples/#The-Citation-object">The Citation oject</a>
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
<h1 id="Getting-Started">Getting Started<a class="anchor-link" href="#Getting-Started">&#182;</a></h1>
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
<h1 id="The-Record-object">The <code>Record</code> object<a class="anchor-link" href="#The-Record-object">&#182;</a></h1>
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
<pre>[&apos;Flory, F&apos;, &apos;Escoubas, L&apos;]
[&apos;Flory, F&apos;, &apos;Escoubas, L&apos;]
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
<pre>Optical properties of nanostructured thin films
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
<pre>[&apos;PT&apos;, &apos;AU&apos;, &apos;AF&apos;, &apos;TI&apos;, &apos;SO&apos;, &apos;LA&apos;, &apos;DT&apos;, &apos;DE&apos;, &apos;ID&apos;, &apos;AB&apos;, &apos;C1&apos;, &apos;RP&apos;, &apos;EM&apos;, &apos;RI&apos;, &apos;CR&apos;, &apos;NR&apos;, &apos;TC&apos;, &apos;Z9&apos;, &apos;PU&apos;, &apos;PI&apos;, &apos;PA&apos;, &apos;SN&apos;, &apos;J9&apos;, &apos;JI&apos;, &apos;PY&apos;, &apos;VL&apos;, &apos;IS&apos;, &apos;BP&apos;, &apos;EP&apos;, &apos;DI&apos;, &apos;PG&apos;, &apos;WC&apos;, &apos;SC&apos;, &apos;GA&apos;, &apos;UT&apos;]
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
<h1 id="The-RecordCollection-object">The <code>RecordCollection</code> object<a class="anchor-link" href="#The-RecordCollection-object">&#182;</a></h1>
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
<pre>Optical properties of nanostructured thin films
Experimental observation of the Imbert-Fedorov transverse displacement after a single total reflection
ASYMMETRICAL MOMENTUM-ENERGY TENSORS AND 6-COMPONENT ANGULAR-MOMENTUM IN PROBLEM CONCERNING 2 PHOTON MOMENTA AND MAGNETODYNAMIC EFFECT PROBLEM
Longitudinal and transverse effects of nonspecular reflection
DISPLACEMENT OF A TOTALLY REFLECTED LIGHT-BEAM - FILTERING OF POLARIZATION STATES AND AMPLIFICATION
A Novel Method for Enhancing Goos-Hanchen Shift in Total Internal Reflection
NONLINEAR TOTALLY REFLECTING PRISM COUPLER - THERMOMECHANIC EFFECTS AND INTENSITY-DEPENDENT REFRACTIVE-INDEX OF THIN-FILMS
ANGULAR SPECTRUM AS AN ELECTRICAL NETWORK
RESONANCE EFFECTS ON TOTAL INTERNAL-REFLECTION AND LATERAL (GOOS-HANCHEN) BEAM DISPLACEMENT AT THE INTERFACE BETWEEN NONLOCAL AND LOCAL DIELECTRIC
SPIN ANGULAR-MOMENTUM OF A FIELD INTERACTING WITH A PLANE INTERFACE
GENERAL STUDY OF DISPLACEMENTS AT TOTAL REFLECTION
Numerical study of the displacement of a three-dimensional Gaussian beam transmitted at total internal reflection. Near-field applications
INTERFERENCE THEORY OF REFLECTION FROM MULTILAYERED MEDIA
Goos-Hanchen shift as a probe in evanescent slab waveguide sensors
SPIN ANGULAR-MOMENTUM OF A FIELD INTERACTING WITH A PLANE INTERFACE
SHIFTS OF COHERENT-LIGHT BEAMS ON REFLECTION AT PLANE INTERFACES BETWEEN ISOTROPIC MEDIA
EXCHANGED MOMENTUM BETWEEN MOVING ATOMS AND A SURFACE-WAVE - THEORY AND EXPERIMENT
CALCULATION AND MEASUREMENT OF FORCES AND TORQUES APPLIED TO UNIAXIAL CRYSTAL BY EXTRAORDINARY WAVE
EXPERIMENTS IN PHENOMENOLOGICAL ELECTRODYNAMICS AND THE ELECTROMAGNETIC ENERGY-MOMENTUM TENSOR
TRANSVERSE DISPLACEMENT OF A TOTALLY REFLECTED LIGHT-BEAM AND PHASE-SHIFT METHOD
CONSERVATION OF ANGULAR MOMENT WITH SIX COMPONENTS AND ASYMMETRICAL IMPULSE ENERGY TENSORS
PREDICTION OF A RESONANCE-ENHANCED LASER-BEAM DISPLACEMENT AT TOTAL INTERNAL-REFLECTION IN SEMICONDUCTORS
Transverse displacement at total reflection near the grazing angle: a way to discriminate between theories
THEORETICAL NOTES ON AMPLIFICATION OF TRANSVERSE SHIFT BY TOTAL REFLECTION ON MULTILAYERED SYSTEM
Goos-Hanchen and Imbert-Fedorov shifts for leaky guided modes
Simple technique for measuring the Goos-Hanchen effect with polarization modulation and a position-sensitive detector
LONGITUDINAL AND TRANSVERSE DISPLACEMENTS OF A BOUNDED MICROWAVE BEAM AT TOTAL INTERNAL-REFLECTION
DISCUSSIONS OF PROBLEM OF PONDEROMOTIVE FORCES
OBSERVATION OF SHIFTS IN TOTAL REFLECTION OF A LIGHT-BEAM BY A MULTILAYERED STRUCTURE
WHY ENERGY FLUX AND ABRAHAMS PHOTON MOMENTUM ARE MACROSCOPICALLY SUBSTITUTED FOR MOMENTUM DENSITY AND MINKOWSKIS PHOTON MOMENTUM
MECHANICAL INTERPRETATION OF SHIFTS IN TOTAL REFLECTION OF SPINNING PARTICLES
INTERNAL PHOTON IMPULSE OF DIELECTRIC AND ON COUPLE APPLIED TO ANISOTROPIC CRYSTAL
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
<pre>&lt;metaknowledge.record.Record at 0x10b67a828&gt;</pre>
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
<h1 id="The-Citation-object">The <code>Citation</code> object<a class="anchor-link" href="#The-Citation-object">&#182;</a></h1>
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
<pre>BEAUREGA.OC, 1974, CR ACAD SCI B PHYS, V278, P635
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
<pre>(19371682830160896,
 {&apos;count&apos;: 1,
  &apos;info&apos;: &apos;EMILE O, 1995, PHYS REV LETT, V75, P1511, DOI 10.1103/PhysRevLett.75.1511&apos;})</pre>
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
<pre>(19371682830160896, -4340207522918580061, {&apos;weight&apos;: 1})</pre>
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
dWRkRPc7jgZEtDUYVMfn0+B7763c49jYmB46dEgLhYK+evVKm5ub9fHjxybXNzU1pV1dXVpTVcUm
G7sY8cWOK4cFJlueFl/1JOLW/To+n4ZCIa2vr1dni99rvfGbn5/X6elpnZ6e9sz2kW67ePGitrS0
6PDwsEYiEb19+7aqLq1EPnXqlA4MDKiqak9Pj166dGlbr2V+fl7Pnz+vjuPo1atXdWR4uKQFiGwv
WR6IL3ZcOcTXzWPp3JrGXn7SL4fx87KhoSGNRCI6OjqqjuPo+Pi4qi7NUIRCIc1kMnr//n1tb2/f
lp+/uLiot27d0kgk8rdDNkp9Tw3vI77YcW7HaLuU+qtQ6z2JuDmNXS7j52VjY2PqOI5euXJFHcfR
VCqlqqq9vb167ty5lcM8pqamXP25qVRKOzs79fjx4/rgwYN1v2b5PfVufhdfiYgvPMHLC65Wc+tJ
xM1p7HIaPy+7e/euhkIhvXDhgra0tOiTJ090dnZWm5qaNJVKaV9f3zsdYvEu5ubmtKenR5uaml47
x3kj+Xx+17+LrzTEF57gdoy2kxtPIm5OY5fb+HnZw4cPNRwO65kzZ/TgwYOayWT0+vXreuLECZ2Y
mND9+/fr3Nzcawd9bEaxWNSbN29qc3OzxuNxffHixaavsRLexVcC4gtPcDtG282NJxE3p7HLbfy8
LJ1Oa2trq548eVJjsZjmcjk9cuSI9vb2auOePVr9/vsrp07V+P3aefSojoyMvHX8JicntaOjQ2Ox
mE5MTBjdDbyK+MIz3IyRpa08ibi5oKZcx8+Lnj59qgcOHNBoNKrRo0e1sbpaP/b59M46Mx0/iOi/
ams3nOnIZrOaSCQ0HA7rjRs3tFgs7sAdwWuILzylEld3urmgphLHb7s8f/5cWyMRDfl8JY1nsVjU
oaEhDYfDmkgkNJvN7vAdwUuILzynEld3urmgphLHbztsZSbh8uXLGovFtKOjQycnJ3f6VuBBnOcL
TyoUCnLnzh259u23MplOS+ivzftfFAry0eHDkujvl9OnT3t+U/9S5HI5mZ2dFRGRhoaGks5jreTx
c0M+n5d9TU3y8x9/bPrwi0ci8qnPJwPffSdnz56VqirOr8HfEV94nhsxqmSM3+Ylk0n5Ph6XX16+
LOnzn9XWSnxoSLq7u12+MuwWxBcA1uiKRuX8b7/J6RI//4OIDESj8v9ff3XzsrCLEF8AWCWXy0mL
48j8wkLJZzgviMg//H75fWaGmQasi5cRALBKNpsVJxAoObwiIn4RCe3ZszLdD6xFfAEAMEZ8AWCV
xsZGmcnnZWEL32NBllaWNzQ0uHVZ2GWILwCssnfvXjnW3i4/beF7/CgiHx0+zPtebIj4AsAaif5+
uVZbW/Lnr9XVSaK/38Urwm7DamcAWGOrm2z8u75ens3MsIkJNsSTLwCsEQgEZGBwUP4bDMqzTXzu
mYh8Xl0tA4ODhBdvRHwBYB1fdHdL3zffSGcwKI/e4esfiUhndbX0ff21fMHOVngLpp0B4A1uj47K
/778Uo4sLkri5Uv5j8jK7wAvyNLiqmt1dZL2+WRgcJDw4p0QXwB4Cw6qgNuILwBsAgdVwA3EFwAA
Yyy4AgDAGPEFAMAY8QUAwBjxBQDAGPEFAMAY8QUAwBjxBQDAGPEFAMAY8QUAwBjxBQDAGPEFAMAY
8QUAwBjxBQDAGPEFAMAY8QUAwBjxBQDAGPEFAMAY8QUAwBjxBQDAGPEFAMAY8QUAwBjxBQDAGPEF
AMAY8QUAwBjxBQDAGPEFAMAY8QUAwBjxBQDAGPEFAMAY8QUAwBjxBQDAGPEFAMAY8QUAwBjxBQDA
GPEFAMAY8QUAwBjxBQDAGPEFAMAY8QUAwBjxBQDAGPEFAMAY8QUAwBjxBQDAGPEFAMAY8QUAwBjx
BQDAGPEFAMAY8QUAwBjxBQDAGPEFAMAY8QUAwBjxBQDAGPEFAMAY8QUAwBjxBQDAGPEFAMAY8QUA
wBjxBQDAGPEFAMAY8QUAwBjxBQDAGPEFAMAY8QUAwBjxBQDAGPEFAMAY8QUAwBjxBQDAGPEFAMAY
8QUAwBjxBQDAGPEFAMDYn3QBkYOsP7jWAAAAAElFTkSuQmCC
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
/c8w6M6dO8fmzZt5Zdky/vvAAVKcSvvUuXMMu/FG5i1YwN133617vJdB4Ssi8jPwcw+6s2fPcvr0
aQCSkpL+IVuvujKFr4jIz4yC7pdP4SsiIuIyrXYWERFxmcJXRETEZQpfERERlyl8RUREXKbwFRER
cZnCV0RExGUKXxEREZcpfEVERFym8BUREXGZwldERMRlCl8RERGXKXxFRERcpvAVERFxmcJXRETE
ZQpfERERlyl8RUREXKbwFRERcZnCV0RExGUKXxEREZcpfEVERFym8BUREXGZwldERMRlCl8RERGX
KXxFRERcpvAVERFxmcJXRETEZQpfERERlyl8RUREXKbwFRERcZnCV0RExGUKXxEREZcpfEVERFym
8BUREXGZwldERMRlCl8RERGXKXxFRERcpvAVERFxmcJXRETEZQpfERERlyl8RUREXKbwFRERcZnC
V0RExGUKXxEREZcpfEVERFym8BUREXGZwldERMRlCl8RERGXKXxFRERcpvAVERFxmcJXRETEZQpf
ERERlyl8RUREXKbwFRERcZnCV0RExGUKXxEREZcpfEVERFym8BUREXGZwldERMRl/wtGiiXNJG+W
0wAAAABJRU5ErkJggg==
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
<img src="data:image/png;base64,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
6AYEAJHAW8Cw7GzenTqViRMn0rNnT/r374/ZbKZ+/fr8+OPFuelTp04lJCQEs9nMbbfdZvQsRYT/
/Oc/REVF4efnR69evTh16pSx3YIFCwgPD8fPz49XX331iueoS5cubN26lczMTADWrl1Lw4YNCQwM
NILnoUOHaN++PX5+fvj7+9O3b1+ysrKAogQvKSkpdOnSBQ8PD1577TXatm0LFGU98/Dw4Pvvvwfg
o48+om7duvj4+NCxY0erzG52dna8++673HLLLcYLSdR1EqXU30ZERIR89dVXIiKSkpIi9erVk/Hj
x4uISNu2baVWrVry22+/SU5OjkRHR8vzzz8vIiKffPKJ3HnnnUY9u3btEl9fX8nPz5e1a9dKkyZN
JCsrS0REfv31Vzl69KiIiAwYMEDGjRsnIiLff/+9eHp6GvtPTU2VX3/9VbKzs8VsNsuBAwdEROTY
sWOyb9++Kx7LL7/8IiaTSZKSksosEx8fL1FRUfL7779Ldna2xMTESFxcnIiI/P7772IymWTIkCFy
/vx52bp1qwCyF0RARoO0ATkFcgSkHkjohXWFILeDTALJBzkMEgmyCsTN0VFGjx4t1apVkzVr1ojF
YpExY8ZI8+bNjfMTGhpqnKPk5GQ5dOiQiIi88cYb0qJFC0lNTZW8vDwZOnSoxMbGiojIvn37xN3d
XbZs2SK5ubkyatQocXBwkA0bNpR67AMGDJCxY8fKkCFD5L333hMRkR49ekhCQoK0atVKPv74YxER
OXjwoHz11VeSl5cn6enp0qZNG3n66aeNeiIiIqz2kZSUJCaTSQoLC43PvvjiC4mKipJff/1VCgsL
ZfLkydKyZUtjvclkkg4dOsipU6fk/PnzV7y26so0+Cr1NxIeHi7u7u7i5eUl4eHh8uSTTxp/DKOj
o+WVV14xyr777rvSsWNHERHJyckRb29vOXjwoIiIPPPMM/Lkk0+KiMiGDRukdu3a8t1331n9QRax
Dr5DhgyRUaNGXdam7Oxs8fLyks8++0zOnTtX4WPZunWrmEwmyc3NLbNM+/btjcAjIrJ//35xdHSU
wsJCI/impqaKiMihQ4fEyc5OllwIsJEg6y78LiBzQEIu/P4dSFiJdQLyKsijIOFubjJ8+HC59957
jf3u27dPXFxcRETkt99+k4CAACPglVSnTh2rQJeWliaOjo5SUFAgL730khGIRUTOnj0rTk5OVwy+
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
RK5CYII=
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
Dqxa+wAAAABJRU5ErkJggg==
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
<img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAX4AAAEACAYAAAC08h1NAAAABHNCSVQICAgIfAhkiAAAAAlwSFlz
AAALEgAACxIB0t1+/AAAIABJREFUeJzsnXd4FFXbh+/Zkk2l916kvigovlJFEARBX0FUpAgiqHTp
AlJFiiAISBUp0hQRBVS6FKVJkyZVaugkBFK3z3x/PNlsNgUsqHzm3F65ZHfKzswmv3POUzXDMAwU
CoVCkWUw/dMXoFAoFIq/FyX8CoVCkcVQwq9QKBRZDCX8CoVCkcVQwq9QKBRZDCX8CoVCkcVQwq9Q
KBRZDCX8CoVCkcVQwq9QKBRZDCX8CoVCkcVQwq9QKBRZDCX8CoVCkcVQwq9QKBRZDCX8CoVCkcVQ
wq9QKBRZDCX8CoVCkcVQwq9QKBRZDCX8CoVCkcVQwq9QKBRZDCX8CoVCkcVQwq9QKBRZDCX8CoVC
kcVQwq9QKBRZDCX8CoVCkcVQwq9QKBRZDCX8CoVCkcVQwq9QKBRZDCX8CoVCkcVQwq9QKBRZDCX8
CoVCkcVQwq9QKBRZDCX8CoVCkcVQwq9QKBRZDCX8CoVCkcVQwq9QKBRZDCX8CoVCkcVQwq9QKBRZ
DCX8CoVCkcVQwq9QKBRZDCX8CoVCkcVQwq9QKBRZDCX8CoVCkcWw/NMXoFD8Ffzyyy+cOnUq5XVw
cDCNGjXCbDb/g1elUNwfKOFX/OtYv349zdu0wfLggwAYhoH7zBkeK1uWd95+G4fDwYKlS7G7XCnH
lCxalEnjxmGz2f6py1Yo/jY0wzCMf/oiFIo/y8SJE9m+fTsnTpzgxMmTULo0vPIKFCoE330H+/aB
2YzJ48FISMCoXh2qV0853rZlCw8Cc6dP58EHH0TTtH/uZhSKvxgl/Ir/d7w/bhzfb9mS8vrUyZNc
vHULKlWCw4ehWDHQdfB4IDISgoKgZEk4exZMJnjiCejdG1KLu8cDQ4bAoUNUqliRn3/6CavV+g/c
nULx16OEX3Hf4vV6WblyJYmJicxdsIA9+/fj9njw2mzw0ksi3Nu3w8WL8PLL8PXXMHGiCL/XC4MH
w5kzEB4uJ4yLg0cfhYEDA0Xfh8cDAwbAkSMEh4dTpUoVTJqG1Wxm9PDh1KpV6+99AArFX4Sy8Svu
S7xeL21ee43v9uzBWbAgHo8H8ueH6GiYMQMuXRJhdzrlgNmzIV8+sFj8ov/LL9CmDZQqJft89hnU
rJmx6IMcW6MGnD6No2NHfvLtd/EitRs0YP2qVTRs2PCvv3mF4i9GCb/ivsPr9dKkaVM2/PijzNYT
EsDthvh4v+iPGgXjxsFDD/kP/OYb6NMH/vMfOHIEunWDJk3821ev/m0X8Pjj8Mwzge/lyUOjpk2V
+Cv+FSjhV9w3xMbG8mLbtuz46SfsCQmQO3egAB8+LMKu6zByZKDoAzRtKv//5BN4/fVA0f89BAen
f++FF8Dj4enmzbl48iSFCxf+Y+dWKO4DVAKX4r7g3LlzPFK9Oltu3sResiTkzAmTJkGLFlC7NtSq
BZ06iaO2W7f0ou+jaVMR7ipV0m/Lkwe2bBFTUEY4HOIzyJ074+1PPIEBTJs27Q/do0Jxv6Bm/Ip/
nCNHjvBIzZp48ueHmBgx61gsMGEC2Gxiqw8NlZ2dTsiR484nNGUyn+nUSSJ3xoyBd96B1MlcDgf0
7w8FC8pgcwfGT55MtWrVaNas2e+4S4Xi/kEJv+If5cKFC9SoVw9Pu3YSqePD6YTXXhOH7eefy0wf
oF+/P/5hNpv4BoYMkZ/HHvNv27wZYmNh8mT/gBAfDydO+Pe5dQsAPSyMF1u35vrFi+TObHXwN3H5
8mWOHTuW8tpsNlO7dm2CfM9LocgAJfyKf4zo6Ggeq1OHxPLlRWTnzZMNefLAoUNQpIgIdWoR07TM
TTU+wsJg5Uro1St9BI/NBm+9BV26wIULsj0xER55BG7eFPHPlUtWHn36QESE3+YfGyv+hddfxztv
Hl988QVdu3a9dw/kDsz/9FMWLl8OgK7rJCQk0LBWLaZ98glGsWKYrVY0TcNz8yY1y5dn4pgxJCQk
pByfJ08eypQp87dcq+L+Rwm/4h/j4MGDRCcmQlJSoNllzRpJtvr220DRBwm3nDEDHnhABoi0HDsm
on3oEEyfLv6A1OJ//bokb7VuLTP4fPnA5YJNm+Dpp0Xshw0T53HdutC+vf9Yw4Bp0+Crr6BmTS5c
uHAvH0emzJg5k34jR2J/803wJZXFxvLz5Mnw/PPw5ptw5Yo8M6+XTbNnU7l6dSJKl07JQHZdvMjc
6dNp1arV33LNivsblcCl+Edwu93UrFePfUlJ8P77gQKfkCCz8sqV5f9pZ+1LlsD69fDhh4Hif+wY
DBok9vv//EfMQoULS9auj2++gRIlYPx4GRjy5YPmzaFhQxH/Tz6R1cILL0CHDukv3DBg1izYsoW+
7doxYcKEe/pcUuN0OqlZty4HTpzAmDZN7iU1hw7BiBHw7LOwfLn4Pux2WZVMmyaJbD7OnsXaty8v
NmnCw8mO7+eee45y5cr9ZdevuH9RM37FP0KPvn3Zn5gosfhpZ/Xh4fDRR+Js/eorePHFwO1t2sj/
O3SQpC6f4/fXX6FtW6hWTV5PmCDH2+3+Y8uWhfLl5d9JSYHnXb5cxNRmy1j0QQahzp1hzRr+yjmT
0+nkiaee4ucjR+Djj9OLPsjAOGKEDHCTJkly2/Tp/uzl1JQqhXviRD7v3ZsvLl7ElCsXoydMYPum
TVSqVOkvuw/F/YkK51T8I6zeuBGjadP0ou8jPBwaNBATRka0aiWC7/GISJcvjy0oCMv330tpBt85
Xn0V3nhDfkqVgv374fJlce5u3QpFi/rPee0aVKzoH0gyI3kF8lc5dp1OJ42bNeNgYqII/p1yBipX
luspUwZ27hSHeFrR91GqFLRvjx4VhScigtiyZXm0Rg327Nnzl9yH4v5FzfgV/wieuzlofWS0n66L
mScsDEJD0S5cIPfOnezat4+PZs5k7oABJI0bJzP9S5fkmP37Cfr6azp16kT2bNkASHjsMT6eMAH7
66/LLL97d6n788MPd70sk6bxyiuv/Nbb/V0sWLCAn6KicHboICufu5HaFGZJ/pM2DPj0U1i0SP7t
o2xZeX5BQVC2LE7DoEb9+lw6dYqCBQve0/tQ3L8o4Vfc3+zcKaaVkBB5retiyrh4EcaOhV69yD5r
FkXy56f1M8+AYZDv5k2uvPoqrjgPaBVE+HQDzVaYG9djmfThhykNWeo8/jht2ryC3WOCPXvgxx8l
ysdu939mWuLj0TweQjLb/iex2+14S5Twi/jvxTBg/nxJRvvqKwlJ/eILef/aNbm39evh9m0wDHSv
lyKlSzPtww/p0rnzPb0Xxf2JEn7FP0KQ2QwHDkiJ5IyKpum62Ntz5oRmzUSETSaJwNE0sWnnyYMt
PJzSUVFMO38+xW65BRhIKPAZ0DTllE5nIt9++yxt2nRkyZK5mM1mnn/+eZYsWUzr1q/gGDFCnMI1
akiVznHj0ot/fDx0747X7b7nz+TWrVv07t2bzz77DPfTT8ubkZHitK5YMeODNm0Sk5ZvkLh9W2b6
27fLAHn8uPg6evaE7NllH69XnNtBQRIlVLgw+uuv03XAAKbMmkXBIkUo/8ADfPTBB6o09b8UFdWj
+EcYPHQoYyZMEMdthw6B4u+b1V+6JLP6rl0luqdECdm+fTssXoytVCnK79vHNq+XiORDTwL/JYR4
Pie16PtJJDT0WVq0qMD8+TNS3s2bLz/RVR+RLOEJE2DhQllVvPeeP44/MVFCQa9cAY8Hk8nEhAkT
0HU95TyNGzemYmYinQHnzp2jT58+rF27Fqev0ihAw4aE/vorTapWZfXmzdjfey+9+H//vZiCpkyR
yKXjxyWqKS5OZvo+0R8zxu/Q9nHzpjzTMmXEKZyUJLWNPvsM6tYl5MYN6uTOzbfLlyvx/xeihF/x
j6DrOubgYOmQ9dhjgVm0mzaJuL7/vsy4O3YUQXvgAf8+06dT9KuvOGoYKaIPsADoRlMSWXmHT/+V
vHkbcePG2ZR38ubLT3TvXnD+vOQR9O4Nq1bBrl2+C5b/a5o4lMG/CvHlIHg8YBh88emnvPTSS5l2
8dq3bx8DBgxg69atAYNGakLDwnirRw/GjBnD2rVrebFtW+zNm/vj+G/fxrRypRz/7rv+SKZffoEe
PWRQePZZWRmlFX0fN2+KM7hgQbmX6Gjxm1y6BPPnEzJpEnXy5VPi/y9ERfUo/hE0TRPBbNNGomxG
jYKlS+XHMPyiDyL4Cxf6BRegcmVKhYYGiL6fuzVUz2C7YYi5pFUrKQo3YoSYmvLlE8ev1ys/qUX/
scdkcPD9rFwJFSvycvv2NGnaNEXUdV1n9erVlE5OqPrvf//L5s2bMxV9gGefeYYxY8agaRp58+bF
5IyFOXNg5kyYORPTF5/TrHFjdm3dSui4cbB7txzoWxVcuiRlL2w2OHfOH+mUmty5JarprbekVMX8
+WI2Mgx4803sBw/y/cGDTJky5S7PU/H/DWXjV/wjjB49WoTpww8lXv/YMTFLZETfvjB8uDRXGT36
jzs9M+HUqVPEJyaIWN64AevWSUJXRAQsXUowYAoNxe1243a7/aI/dGhgxrHVKqapESNYt307/3n4
Yc6eOIErVVP334aF0qUfQNM09u7dS716NXjxxcAk4tOnoVevFeTIkYNNa9ZQ/+mnSXI4ZHAym6Vc
Rd68koFsGJIU98EHgclsabFaZcAdMUJm/m+8gfett/hu7Vr6/ZkaSYr7DmXqUfztREZGUqpUKXRd
x9A0v/li2TJIDrVMR1yclFkoXlzi2mNieOLQIbamXgUAi4DO1CKJbUBmDdN3kD//q1y7dppTp05R
o0ZNbiXEY1gsYrpxu7GGhPBw5cq0ad6c4cPfx+l04HA4MAwPZAuRNo/mTFYWbreUUsibV1Yzv9sR
/BCDBv2Pl19+iVq1qiaLfvqwVhF/qFmzAR07vs7u3bv5aMECvMHBkrmbM6d/5++/l4zjtOLfrZv4
UMqVE1/ByZMyeERHy3Nu3RrrjBmM7N2bgf37/877UNyvKOFX/K0YhkHBggW5fv06mqZJ9qvJJA7U
3LlFsNKKv90Ob78tUSgnTkiUj9lM2Oef873HQ/VUu8YCNQnlNK/gYhbpxf8YNtuT9OnTkZo1a/Dq
q+25dSsGzWKBbNnQc+SAQoUIDQ3Fu3s32HWczi+BqsnHz4O8H8ggdSeef17s66+/fveicumoyoAB
DTl//ixXrnzJyJGZm4T27pVFxkMPZeNspItLzpwY06YHir4Pn/hPmSKifvCgzO6nT5dSFQ6H2PxT
tZxk2jTo3Jk8ixcTdfHi77wPxf2KMvUoMiUyMpLWrTsRExOb8t4DDxRnyZLZRERkbF2/G7169eL6
9esA/pIHui5RJS6XzEAnTRJTA4g56O23RYSyZxfTUHJ9mUSLhafmz2cjpIh/dmA7STzAYmIA+Ai/
+J8ErQ5aThczZs1g5syPyZMnJ3379km5vmWrVnEiWzaS+vSBo0fh7WEpZ7bRHhdLMcj1227WZvsj
jwgowIwZ86he/aEM9Ts1OXNKMdERI+J4qX0oxvARGYs+SCb0vn2SvRwVJaI/dKhf9EeODMykLltW
zF1jxuBSZZ7/VSjhV2RIZGQk1arVIyqqI15v3ZT3z5yZQ4UKj9KlSzuCk8McmzdvTsk72Y6TOXHi
BFOnTs18B49HEoxatpRZp6bJaqBaNSnGduGCzFZ9nD2LAwtN0GiLjgkNA4MzeLGHJkHQEoid49/f
ZIL/eXAUBMdsB9X/W5ctW1an3AfAW2+9xRONGnH0ww9x9ukD40dC/5YEOf9LWeKozZvMdH/ut6Vn
hNv9B8w7qYkgPn46W7a0+f3dI+8m0CaTJKmdPi3CHxMjFUunTMn42Mceg969SfgLi9Ep/n6U8Cv4
+eefOXXqVMrrq1evMmLEeBIS+qPrfQL2dbmqc/lyR4YMmYvF8gyaZmfs2Drs2rX5jvXedV3nscce
u3ths9Q2e5tNHLn794uD0uNJV7vHA8RjYT6hGBi4cBFMGHmSsmP2mHFancRki8HZ0QkhOlwH5lko
W7ocw4b144dU5RnKly9P8eLF+WH9euo0bMjhZcvwvvQSQWHhlHPGMIHRnOIUuNziBB04ML34u90y
c65c+e4inCmrgCfweB7B49l9xz1/txUJpJhdhQrw4IOwcaP4Te50rQ88gK4swv8qlPBncVatWkXr
jh0xP/wwIOaXhB0HwdEJ6JPBESZgLvAyHk8eYDgxMXOoUePJO4p/q1atiI+P/30X53TKz13w4CGe
eGzYaExjetITDQ1cYGAwKWYSG2ZuwFnXCetDCKIyOUMNerzUg7yWvHLfGJzRz7B+63oeeeQR3mjb
lr4bNmA/d46Q24lMYDRBBFGJSnRL6sD0nfMkwmjwYL/4+0Rf1yUSacAAEdTU1UF/E3bk2b/Gpk27
eOKJwDQHH/HxYvmqWTPVm6mar2SIwwHt2sGOHeLoLVcusJZPZhgG33//PQ0aNPgd96G4X1HCn4VZ
tWoVrTp2xD56dIrdHIBug+FYjTscaQIehWQrumG8TkwM1KxZn4sXTwWYTgD27t3Lsrs5Q/8kNmw8
zdN+0U9GQ6O33hviNDZ8uw2nMRWLeSj6sTzMcM0gCP9MdxvbaFS3Eeu3rvefWNcJ1cIC9nuR5pAE
03fPE0ezr/SByyUz6b59JeEsTx6J6smA1NdokJHw2oH5OJ02hg1zMnJkoPjHx0s15oceEn8sQNsX
7cwYNRTnh9MlMS4tX34pUTtdu8Izz4ip5+OP/clfd8Ji4VZy60nF/3+U8GdRJk6cSP/hwzEmTgwU
fQDz78/rM4zXSUgYRHx8fIDwe71eatWq9Wcv965YCUon+j40NHrTi83GTgy+oow3J6O8owLEHOBx
Hod4aFS3Ed37dvfdAOjphflFmpMtKRubLds45DqMwxQr9vNffpGeAI8/LqUlMpjthxDCy7yMOTmR
7CY3WctanKRd3djBDM4gaQpWpGjyvRkGMTHw5JOi4b4gnOeeNfB6Y/m4T7f04v/FF9KEJrnGESDm
qqNHpUT16dOBmdE+dB0WLsTsc7Yr/hUo4c+CrFu3jkHDhmE0bJhe9O8xderUkaSnP0iBAgWoXr06
mzZtSm8q8uUAGAYmtylD0U/ZFQ0TFmA7g5iaTvR9PM7jbDW2snrdOjwlSsDMWZlaQhrSgIaeBrhw
0dj0LPrCORKWeuWKdAFLTEx3TAghTGQiFagQ8H5xijOLWYHibwZyAR3AGQdnriZfiAese+BWnFhp
UleGeL6pwfXrsXzxajuswSGYzGapAWSxSAG6tD0EQkPF/NO7twwKqcVf16XOz9WrhKh+vf8qlPBn
MdatW8cLbdpI9cdMasmQPzscHwIeOxCE/Jo0AHzhiTeAhUBgNqfD4aBMmTIMHz6crl278v3337Nz
584/dJ3FihXj9ddf58033yR//vx88803PP/88/4yB5om5QU+/FAEqucwcNztrOIJNd2lUonL6eLQ
xYtgMpHt6jVuk8jnLKUVLdPtq6PzIR8SpNlw9Owp1xUXJ2afNNiwZSj6AM1oBsBMZuIi+VgL8AwQ
kvyT37+/+0HY8ZnE8KduKxwZCd9vCObzRfNo2LAhGzZsoH2HDjgLF5bVSL9+/gQuw5C6SBaLlKno
10/6DJvN8kzPnxcfS79+6O+8o+r1/4tQCVxZjFwFC3Lr7bfhzBkJnezePXCHkyex9R5IOWcpNF0D
QrlJFFGUxMkKJEWqHvASMCLVgaeASsAfn92bTCbKli1LyXLlKFqkCLquowHdOnWiTJkylCtXjkuX
LvlFf/p0qTVz/TrBbd/ka/dSQsi4Rr4dO8/THINgFjObvOTN9DoGMpA9toM82aAB82bM4LvvvuPd
d96lWWwzWuFvVq6jM57x/MAPOO4+6lCKUsxlbqbbDQye5En/GzagNVA8kwOcEDwb9HgIDrZhNlsI
CrLy8cef0rRpU1avXs1LrVtjL1QIunSR73vKFKhaVaKOQLpyHTwo1Tw1TQTfbBYTVYsWUL8+1gED
mDhiBD26dbvrPSr+f6Bm/FkMe1KS/LGfPw9XrwbaCk6exNZ7EEPsfalN7ZRjPHgYzAgO8SBONKAV
6UW/OhJc+fuxWq107tyZcuXK0X/ECE7UqyclA777DpxOPpk9O/AAi0WKivnaJubLh7d2DfrsfIcP
nWOwY/fPmoEgghjEYHTAhJ1oojMVfh2dW9zC5PGwY8cOyiULpGHoLAxexmbTbiyalJhITIoiyrj+
m0Q/LV68nOQkXvzxmIW5Q4vFjLCBoxywE8xmE507dyMiIoIjR46we/duJk+Zgr1WLSngputSfyhP
HolE8rV0vHxZ3ouIgPr1paJnVBT06QNhYWj9+jFmyBAl+v8y1Iw/C3H06FEqPfKIlBuwWKQ4Wtmy
0qTjyhVsb/RgiL1PgOj78OBhmGkYB42j2I1vIGVmvRKYjYi+kfzz28M2ixUrxnvvvYfZbKZDjx64
CheWLN7ISIKDsuOyx6aUNzYMHUxmdE2XSpipHY5eL9bRH5Bjx1FuGTFYQnyZxQYuRzwmtxeP5gFd
J5xwpjOdYgT2ptXRGc1otrNdBo7PP5cN+fKJ4zY2FlLlOzBxoiQ//UZ8M34vXkYEjWVf+HHMEclZ
toaB6foN4p3R/gNsiKnnoUxOaABfAsf8b/mfVfKfdUiIiL6miV2ocmUZNHfsgEce8cfvV6oETz8t
99O9O5qmkTs4mPEjR/Ja6upwin8FSvizED1692baxx+LoGXPLjHfb78t4l+6NA/P3M2H9lGZHh9D
DO2D2lOwhNR3j42N5saNOAxjOuCL5IkFugF3iSdPS1AQ1hAzBbLZqVIFdm0J5omkxnTTe6Q4ba9z
na7Wntz23ET/No3wgwxoXy6HaVMhfyqD+Jo1MHWqiDeArhPmMPMRH1EIiXwxMPiAD/iJnzBhSom4
8eDBmy83zkVzApOcYmMleieNw9lqtQZENXk8HuzJkT1hhDGHOUwPmsPeMrE4J44KLOvw3Wq59tS5
C1bE3JM2MdoANgG7+e3WNZvNb+LxJcKlLtOQkIA2eDC5goOpVr06X3z6KeHh4b/x5Ir/Tyjhz0J0
79WL6StWwKOPim1f00T8330XTp7kkfhyTOSDTI+/zW06hnfkZvxN5s9fQLdu72C3bwLSNvrYA9Tn
94i/1aZRpJDBmDEw7G0bD19tTGfPW+kida5zna505XbHF9Bfae3fsGIFLF8uzt7Uou9j7VqpZz9w
IGzZAlu2YHb4FdPAwIaNalp1hhiDU4TfjZt3tMEcyXMN5+Jk8Y+NlTjK69cDUmdttjAqVCjH22/3
wzAMtmzZzKFDBzh06DAejwcMsFgjoEwZXBPHZFzL57vvxHfhcvmbv1iBlyHAErSD3yf6GWGx+Cuj
IoPW+FGj6NWjx584qeL/A6oRS1ajQQOpfT9tmtj3w8Mlg7NvXwj+bUXFLl68SJcuvTIRfYDHkOlo
oKhYLJaUH7PZnNLVyWSC3DkN3n9fim+GR5XMUPQB8pOfCUzA+ulngfUK1qwRUc9I9AEaN5ZEpchI
MXE9+SRGsJVQvATjxaoFpRN9ACtWxhijeTC6ALaWr0pzllSiHxISQnBwCDZbOBUqPMSPP26lZcuW
HDiwlx9//JzKlX+mbVsPNWpAnrwaLpy4Rg7OvIDbs89KVlZ4eKqMYGApMCHVz58VfZASGHY72O2E
mUz8vGOHEv0sghL+rIbZLEJ/7Jhkl46fAOM+gpXfEuO4EuBsTMt1ruP1eJk4cSKGkYuMRd/HY/iE
32q1UrRoUc6fP09sbCznz5+nVKlKeDylgSroehWiosrTvXsoiYmQzRRxx5j8bGQDr0dWKqnFP03G
cDp82zUN+vVDe+QRngNaAjbDlk70ffjE37h1S57ZjRspol+uXDk8HgslS5bhxx/XEx4ezttv9+Hb
b2czfnwSrVtDVJSVfbvyEnVDExNNZsXdUj7QCp07S9nNlLaOSDSq7+ce93ovUKAAlSpVurcnVdy3
KOHPQrzQtCkhX30ls94PPoBixWDTMVhXHw624SoeRjAyQ/E/z3n60Y84RxwfffQRLtfda+gAWCwW
ihYtyk8//UThwoVxOp3Ur/8cv/5aC8M4BhwADuD1HiMqqguzZoXiNn6jqu3ZI/Xu+/SR/rG/B03D
+8ADJABLLBasWDMUfR+y3SSzZJMJzWqlXLlylC//CB5PferXr0tERATz589n1arZjBuXRLZsMHmy
lQ2rc5JXz8VKVhDMXQYnHxEREld/t8HsHmCxWBgzZsxf/jmK+wcl/FmIevXqsXzRIkKGDhXxr1kT
rPkQZ2xvnJxkL1aGM45YYolL/u8Up+hBDxJIwMC4e4XNVOi6zoQJE2jb9k2eeOJpChcux8mT1YBp
BDZJ0YAPSEjown77hYBwzLS4fdNdp1PCUg8cEJv43YqhZbB9ldmM45VXMm/WFYAmkTDVqmFUrcqR
GzfYe2gvqXv4njt3jlq1ksieXSokbPguJ3m8OZnOeLKRTaJuYmMz/whdl+2ads9bTGZGWFgYLVq0
+Fs+S3F/oOL4sxhNmjRh+aJFvPTKK5jz5iXBcRWDj4C3gBCcfMt+WvASrwKg4QJ03OmE+CawFaib
ySetALMXXdNp8XIHPO6hSGrtXmA6GSutiL+TT/mSZbThlXR72LEzjGHopOlKZbdLhMq0aVCgQPpT
r10rTUjatfO/ZxiSqVqhAm5jJV68mc763bjxWjSpuJnc6MSbkMDZnj3BegTDKJrumEuXTDj1KKbz
iZingPaetszrPQjnjAyc0LouCVaGIQPM8ePiAAkKEpNP2gHX4SAkJIQ8efKQI0cOuSavl3PnzqVE
Ev0WuqdN4lP861Ez/ixIkyZNOHbgAJuXLOHr5QvJkWMcmuZrkBKCg29xE40W1Aiv2YoLZ/oKkmYH
mJ9BxD8tKyCoDTzuBJMZj3stUma4PRKcfqfptYYJK0uDFrFG+y5gix07PenJec77Z/0+dF3CO3v0
kAzV1Ky4vDVaAAAgAElEQVRdC/PmSdy9r+zA5cvw7bci/JUq4bQZjDKNzdDM5cbNoKDhaA8/AskC
C0B4OMaUKVDYw+JlX3AzE3OTT/QBWugv0P52M2xd+wTmAPhE/8wZGDdO4u9v35awW5tNnO/z5/t/
GjdGCwmhRo0anDlzhsOHD3P48GGOHj3K2LFjCQkJRVYiFsgkmxnAbDYzfPjwTLcr/p2oGX8WJDo6
msOHD/P999+zdu1aEhOjMIwBSJ1936/EbbzeG3i9mSRjmYBHk2DfM+AeREAcf9BEaG+Xkj7UgoCu
uHdHQ+PRmi7m7JnGl66lJEdCkkACSSSlF30fui4O0XbtRKDdbpklW60i+sWSE7YuX5Zw1pAQqVED
OBfOZle7NxnlHssQfVBAOOcg8xB+eSgI5+ih6esbhYdDty7EvTuFGjUa0KZNM44fD8bjyTybt6X+
EtyG2a0kHDVlUK1USUQ/LEzq6kyaJDP+t99Ouc4UevQAs5mLJ08SHx9Prlz+dpA9e/YELAwaNB67
vRhwJHmLgQy6/tVAw4YNU6KrFFkHFcf/L0fXdY4fP87OnTvZvHkzBw8e5NKlSyQmJv4uW306rEAj
IB9w1ELKgkADHvZAAeAgsKYZuFYkb7yGRAJFAmkaqqeQiInCmK2xWK3iS01X78xq9cefm80S2eP1
+s0iSUnSVDw4GGbOlJl12bL+4/fulf0iImDGDP/7N24Q1PZ1cLmSC7kZeDUdLV8BXIvmBMS8B7B/
P7z7HlZHA4oV+5WwMAcREecoXdrNwoUaG9mAJYM5lm910Y7XuDKln3TE0jQR/aFDxWTVpAn8738Z
f65hoI0cSaELFyhYvDhVKlZkxuTJKUJeufIjHD5cHMmsBvmSDgNNgSQALl++TKGMavcr/tWoGf8/
yOrVq/n6O785w2I207NrVypWrPiHzxkfH8+ePXvYuXMnO3bs4OLFi0RFRRETE4P3D/XpC8SUnP2q
e3TYDrwBNM6gRk8S8KMGntTtofIjaaiNgPWkF/9EzDyJpnlxA24PEsZoNvtn2mazmGt83UcMQ0w2
x49DlSrw009SavjMGXjqKWk2smVLoGO3ShXJ5AVZFfgE3eHAFREElZJLGbjdctypU2J2yZt5YTeK
FsZ9bhPnLiRhtVgwaTp2O+QIDmGIYxijGJki/rvZzRGOAnCYQ1znqpTN8GG1ElquHI6oKPQiRTL/
TE3DKFaMy4mJXD53jv2HD7N42TLy58tH9f/+F02zAt2BvJgZj84gjFS+kQiTiYiIiExPr/j3omb8
/xDLli2jfbdu2Fu08EdvREcT9M03BFmtaFYrJsBkNtOmZUsaPPEECana6hUvXpxatWpx/vx5du7c
yc6dOzl+/DgJCQncuHGDa9euSR32e0ixYsWkNWNCgnRjMiHa/QaQunpCEjBPg1vh4I0l0KavI2J0
AFgDRKQcpNEAI/wIPOWQQ24Ce2zwcisxy4DUjv/6a3jvPTGNjBghYZ0+h25iohQdu35dEq3q1w+8
ievXpfZ8bKwMACaTdDm5elXs6B06SLJXahYtgg0bJCs4I/H/5hvYtk0am/gG12EfEHTAhdlsR7ef
oDKVGM1ItrCViXyCk674XGwm01ly595KRISJp556iqeffhrDMGjXrRsJ/ftDclvMDJk/X0pV9O/v
N2UBoQsWYD55hvio+Zg5SD5GspskfC5oHXgVjfMPV2HNDz+oASCLoYT/b+Ty5cssXLiQQ4cO8eXK
leiFComQhIeLPePYMQlR9HplZut0+mejyaWIbeXKgdmM58AByhQqRNEiRbh69SoXLlwgMTHRX6/+
HrN582beeustcubMSb58+fjqq69kg0WDUANKmfwDWKQGJSrBnl+QKJ4H05xNB3oCMwEDDU3s3BFB
0NMh69BI4EsbDBmZvuHs3r0wfLg8t/h4EX9f+8Aff4R16+CNNyQOvnlzKbIGKd2kaNhQSjx8+aV0
n3K7Jby1QwcxrWTE4sWwfr0Ibeowy+3bpfhZiRISUeRbmYycAFsrgzEaiMXGw1i4SRImDLYhJaxT
M4xs2T7h+PH9FCpUiHETJjBo3DiMQYMkwicz5s0TZ/Y77wS+73ZLJvPRoxRwOtkDpI070oFONhsn
KlZk3bZthKkuW1kGJfx/E1988QWvdeuGPXt2MVxHR0PTplIiGUTkZ8+WmZvPkXftmpgAmjSRyokr
VsDPP8OECTJj7d5dhC/5K9Q07c/Z7TOgbNmyrFmzhtdff525c+dSs2ZNzGYzOXLk4NipUyKCRYvK
NfqKoOXIIa0HJ02Gb38AtpFe/LcDjQnCg27y4CnhgTZIIIoDmGqFYaMy7jIOIv7Dhsksd+pUf6Gx
a9ekM0m3btJwZOlSf80bkHIIW7ZIkbK2beGzzyQTN2dOmTnfiSZNpI6Ob3Z85Ih89qhR4mxds8Zf
iuHqVejUG+IHIYPcT8BzwGbSi75gsbxL2bKrOXp0D29068acvXtlhfP++2K+SktkJPTqJc7f6hk4
0N1uePVVHrp1C5+HQwM6OxwpVf91oFZ4OEOWLuWZZ5658/0r/jUoG//fwKJFi2jXuTO8+qpfoBIT
RXQiIvyCabPB+PEy43/iCTFfTJkif9w5ckCnTtIcu18/Ef9p00T84+IA7rnot23blgULFqBpGpMm
TaJr16589dVX1K5dWxyImiaiP2NGxslGfXrLSmb948BkAiJ/LAMg3IJryAgYMlB8vr4QegfimM1M
9AH++1/Ilk0Ee9gwf5XJAgUkK7l/fxH/QYP8x7hcMsP3eKTJyNSpcg8PPCA2/LthGCLwmibfWbZs
Mtv3ta8cMkT+nfI9JIE2GAw3YgurSWaiD+DxdCUycpr/jWrV4Nw5mbmnFf/ISPnuW7fOWPRBEtvi
4jj85psc9mUAOxysnj2brx0OGiHGpjwm01+2UlTcnyjh/wuJjY2lRt26HD95UsToP//xb/zxRzHj
DBzoN0UYhgj9+PFQsaKYgQoUEGEbN05WCJ06yQzz22+hTRt48UX49NPAWe2fxGw2M3XqVLp06ZLy
XpUqVejZsydt2rThwQcf5Mjp0zLbLlXqzhmmr7SBH34ABojgyo1CvjAZvNxuSJsj8FvRNBHiSZNg
9Wp4/nl5v1Qpf+G5Zctkv5AQiIkRk8yYMTLwrlghg8szz8jAcTesVjH5ZMskIqls2cDiawMGyLUM
HAVXIsFT7fffX58+4lvo0UPO5XDIdRw+LM/98cczPnbPHhmU3n9ffCGpSCpThub9+6eIvyLroYT/
LyImJob/1q7N2fPnMxb9yZPl/bRNrEeNkqV7//4y6zeZpFOSD02T1z4R9c0+MxH+32v+CQ0NZf36
9dROGzcOVK1alevXr3MjLk5WKrGx0t2pbVuZoQ8YENis20dEOCz7IuMPHDcu896/d8Plknt/4AER
xNSUKiXPcPRoEc8cOcRvUqmSCObAgVKyonNnieuPjZWf7Nkz/qxr1+TzMiqw5ivB8NprGQ+CC6ZL
yejpJ37zreXMlo2gH37A9d13cn26LrN8TYMiRfyTgYyIixPn99ix6UQfgEqVSPrgA5r16cMVd6ZZ
EYp/MUr4/wKuX79O6UqVSKxYUWaWPtGPiZGyAdOmyUwsreiDmCvGj5fiY5cvy4x/2rTAJiBpsVhS
zaZF7DVNQ9f13yz6JpOJAgUKsHfv3kzjutu0aUPt2rX5fs8eqFMHXnjBv/HYMRmwxo+Hjetg0wZ5
X9eTzVqLoXWaEgwTJ0onqKefgV/WwcNOyQ8IApIc8OuvGT8jgNOnpZfAzJn+bFyvV5ytvsD/M2dE
qNNG9pw7JyGaH33kH0gbN5YVwsSJ6cXf15u4Vi0ZmH1omoSMzp0r/oS0ou9yScSPwwEnTwJngRgg
FxmzjbAw8R+80aEDk6dPh5dfDnzOR49KjP/ChVC6tEQc9e8fOCAlJUkS2J2qbVaqhDk4mI/dbg4h
g7oi66CE/x7jcDioXbcuiSVLygzQlw4fFSW2+pIlxbxRNH1tlxSCgkSM6tYVR2+1ajKbHjeO0EuX
sNjtaCYTxq+/Eh8bm07cDeP3FVKz2WxUrVqVzZs3Y8ukTvzJkyf5+eefCc6RQ0S/Z8/AmXrRojLr
79ULwt3QyuX/7XIAn82Hq9fgyWQRPnpMomTmzJGaNe22wRKnOHhDgf+5oX8v+GByevE/fVo+3+0W
J2++fCLAY8fKrLh4cRlwfBFSs2fDm2/KsceOSc9Z8F+/pkkUEIj4Dx4c0JWKYYPAkwAHfoaevfzb
4uNl1eZ0wpOpmqQDuFyEDB/Oo+Hh1Hj0UYzcudmU5OHnn2shXVTSiv93WCzt+frrdVy5coW6jRqh
t24NLVsG7la1qqxi3nkHihYDe5JMIgYODBT/32D6cyOdk51xccycOZN33303JU9D8e9GRfXcQ3Rd
p26jRmzbtUvErEABmXVOnSqC+NxzMoP73//8jt3MGDRI/sh9MdwXLmAaP56yhoGpYEGGjx+PxWKh
U+fOxNyMBow/ZOYPDQ2lXbt2zJgxI6Vfa0Y88sgjFC1alNUxMXhHjszcPLNqFXw7G9omBb4fC8wx
gasoWIqC2wkhp+Crr2QWHRcHIRa4+jNUSF69RAJnQkXkU8fxT54ss9rUVKggzs/RowPt7KdPi1g3
fU7i9keOlBn04sVSz79yZf/3YBjiL/n+e3kdHy91/7M7wREOU2cEmt1ABpK+feX6Fi5MCc0NGT6c
+kWKsOLzz7EkrwQMw6BDhy58+ukPwCT8pbLOExIyiMqVy5InTx7cbjcbTCaMt9/O9PtgwwaY8hkk
XYF8OaFQIRl8zWZZYe3ZI32J70TTpimBAQC1atXi66+/Jp/P56T416KE/x4SGRlJ8fLlxSnbqpUI
x7x5MhOuUcPviBs9WoQ/MychQK9e5Dl+nNBk0bjp8UB4OKtjYvjCZuNA2bKs376d6Oho6tSpRmzs
TZKS/pj4h4WFUaRIEerWrUuTJk2oWrUqhQoVShkItm3bRsuWLenatStDjh3zz46dzsCZZVCQlBv4
aDC0S0z/QbHAFAvoVyGoMoTZpQ3k7dtik547FzZthDzJDcg9Hjh7UQTdN9AYRnrRB1kVTJ2acWcr
3wrB44Hy5eV8iYlyrsREcZ6mLr4G8hkdOoiQ3roFn3ySXvR9HDsm5y9UCKZPJ2TWLOoHB7Ni6dIU
0fdhGAa9ew9kxsxPcefJA9kiMEde4OOPRtGmTRs++OADZsyYwbWGDf3ZyRnx888wbCUkDgOtGbR4
1l/t0+GQge3996UMREYcOULw4MGUKFyYEyf8voeSJUvy8ccf89RTT2X+2Yr/9yjhv0fouk7JChWI
dDhEgLJlk3T/Ll1EtHyZpV6v9Bd8/HGZKWa0tN63j+AhQzjkdKbEX0cC1QAnFrJjJQ4NPcjKhu0b
yZ07N1WrPgQkEhd3bwJ8zGYz2bNnp3z58hw/fpz+/fvjcDgY+euvYjZZuVLCOFObF/Lnh44d4dNx
GQs/wKggsOSHsjklizY+HpYskXh7X46Cb0CMjoZXXglsPp4Z774rJqjMmDxZfCYfpOopbBgyMO/Y
ESj+SUliWjOb5VouXpTErTvRsKGcr0gRsptMfLdgQYYOch/93+7P5JXL0Rs0JGLHT6ydNYsaNWoA
8Oijj7L/P//5jcL/IzAa8s6Cjql8KN9+K6vN8ePTi/+RIwQNGUL/Hj147733CAoKkp7AyZQoUYIX
XniBsWPHqgJu/1KUjf8esWTJEiLj4iTO3if6gwaJCaJ//0CBX7VKZpCQXvz37UMbOpQ1qUQfoBjS
ZvVxTDzJSzxJQ467jtP4ycas37qeokXz8+KLZxk9OoOiZn8Ar9dLTEwMO3fuBOCdd96RAezll0X0
ly6FBQv8jlUQU8eMGRB0p5HHAM9VeLmzZNyC2PrTin7K7nefl2iAcbfIILNZYv8DDtRkVm8YMmMf
Plze+/BDmd2fPi3f34ULd70GQFYUFy9iCg+/+74GVAg+z+3vF3LbmZd9+/enCH9QUNDdR++A7WEQ
fUuc1b77MgzxDw0eDO3b+zt52e0EL17M7GnT2Lp1K5qmcfLkSUqXLp1ytvPnz/Pll1+yf/9+5s6d
SylfkmEGuFwuxn3wAWvXrycmuSx1aHAwtWvVYuLEiWrguE9Rwn+PiI6OFhuyT7iGDhVRTCv6ILZV
EPG/elWck7747H37sAUHY0kbnoiI/2xcvMMO2vIahSlMcEIwT9d7mhz5bRkmd94zNE0iRVavFnv2
5MmBog9SDtnrhZXLIJHA+j0puAGLzLzHjBHxv3JFZsxpRT9HDlkpXbkSELWUGmvytbnTmmrSkpnT
UtNklbJqlSRgxcZKQ/r9+2WgyJHjd42kIV4vmbR7D8BsNnPqlIXi5TWu34yh1+DBfLJkCT3ffJPB
gwfz3Msvo9eu7U8OS01sLEyaDc72/vcMDZKSV1k+f8jOnfJ9zJlDsM1GWHg4uXPlYvCUKbRt25ZF
ixZhGAalSpViyJAhjBo1ClNyMldkZCRut5u2bdvSvXt3WrVqle4yXC4Xz730EhsPH0a/fVvMdgC6
zoFVq1i1fj3vjxgRkBxWqVIlKleu/NsepuIvQwn/PeLnn38OfOPAAZnJZiY4TZvCxo2SqJUrlwwC
7dtD69bYRo2SP6Q0eAEX4MFDHHGYMFGb2sTGxzLPPede31IgQUFi21+0SMwqaUXfx2uvwamjcGo/
pK0ttgmZnpvMMhP1CUVmwmqxSChrt27+WPZUWJH6M9bgYE5ev565PVvXZfDI7Jo1TXwDrVtLMtj+
/RJ6W6SI3K/HA4cOiSM4IzZtSjlPbqCo18ueXbsyNfV4PB7279+P12Tl1OMdUzp6HfF66TJgAN3b
tePdgQMZ1rcvxsSJgeIfGwtd+8P1F8Dry0pOCPyANN23GjVqxMaNG1nz9dcsXbqU+snhreXKlePV
jh3Rk1dLYblzk5jq9+7q1asYhsHy5cvZtGkTkydPJjx5NeMT/Q2//IKRkCCJh74icR4P3LpF5Btv
0Lp7d8zZsvkDB6Ki+G75cho1Uqlj/yRK+O8Bh5PL4VKvXuCGu5kfLBZxNs6fL5EmLVpkekw80Ihg
DqOjc51XeAU3bp7hGepQB4/LS1gYIqwafzgZ9o5omqxK7lbJMTS9qcPyo4Ucp3NwK8iOt317v+g/
/7zMtlOZGgLwNR3v3dtfntkwwDAwdJ1vgFi7nYYTJpCYLVv6Mg+6Liak27fhTmLjdMLsiZDDDK4o
8Lhg0ULo1l2OTw6nTSf+mzbJ6iW5vLNmNjM9IYF6w4ax66efqPTQQym7lilThhYtWvB8s2b8tGcP
nkGD/A7/ZAe322Jh0qxZUmsf4K23oPQDQDhghquREN8WvGOQL3oD8D4SMwuSBJH6y9do1aoVGzdu
pG7dusydO5fw8HDsdjubduzg17AwPL5n9uqrsHEj2q+/YiSvOK9du8b27dtp0KABzz33HBMnTuTh
hx9mwJAhbDx2DCMuLrDJzZ49sorzNcHRNLwej0x0cuWCTZt4unlzKlWsSN06dZg0blw6B7jir0c9
8XvA+fPnZdZ6+LA/+/O3+Mx1XUwmjz0m5oZk0TfSzGzjgYbYyEcdvmFAcpMQ6UjVn/7c5CY5c3qZ
NM2CYdbFxu7i3ou/3S7O2LvhBes3Vqyrk+27YZAnbx7ee/89Ovbo4TfpREXB5s1iTjlyRCpppl0h
nTkjK4z+/f2lLXz89BPPfPMNu51O1judNBo2jMTBgwPj/hcvgK0/SJhmZtUn4+JE6LsBEV65gShg
bhyMHwee5FLLAwZItJYvjj8uDlaswKrrBIWFkehygaZRFChoGCw/d47lqez9trlzGf3ee0RGRpLQ
pYsM+lFRcp5RoySTuFevlP2NffvEZ3T8GNI+cTxQBelq5hP95ojoe5P3+Rp4OtXNraFjx5Zomo2X
X+7Ijh17eO21buw5vJubpUri8TmxfTRqhDFgALazZ3HGxaFpGjdu3GDdunVUq1aNESNGUKdOHTZu
2YJeoICYw4oWlfyJnj3FZDlhQmCm+oYNsqKdOFEG30GD+OXYMX6124m8eJGvPvtMif/fjIrquQcM
HjyYMWPGiONz+3ap4OiLFc+o8TfIQNG2rZgTzp6V0Lty5eDzzwmeP59pbjdFkTSf7gSRn7r0TCX6
PhJIoC99ucwlXJWL4/aehatOWf3fS/G3WsWUcvq0DFYlS2a6a9Dgd2m/syx1qYuOzsSgiZRqVIo2
r7WhRfv2eLp1E5v+3Lkiem++KTWIHnpIZvc+8Y+JEfNS9+7pV1O+y5ozhyLLl3Pa6WQX0DI4GDvi
SYg3gVEEiPBAfFGY+JHE2acmLg56dYdCV+GpNH6EKKQbZWp3i8mENSiIF198kVw5c9K6ZUvKlStH
t27dWPXttwS5XFQwmThYoQLOrl3991K8OMTFYe7aFW90tAx+FosM/g6H5HZ06pR+xbd6tUSJOZ1I
v+LU15+YfKeZib6PNUBL4C2gFAR9Do86YOSIjEtQuFzQrx/FEhOJPHsWs9mM1+slNDSUMFsY0bei
8fdYMLDmyIfLGSf3M3ZsoOj7WL9e7qNGDfk+Bw6UDGqzmZy5cnHul1/Inlm5DMU9Rwn/n+TGjRsU
KVECt8Mhs8o335SwxmzZJNV/2jR/fLUPl0uWw1ar1Fz56SeZDT31FKHfrSZP7tyYTWYMDBzxcXiT
dJY4lmEl4wiJeOJ5jueg3uPg3AU1PPApslS4BxE+KZjNUojM45Hrzcjks34D4ZNm87HzIwohpR8c
OBgWOozgB4PZeewg3k6dpDDaJ59ITH2bNhJPP2CAFFHzxZBHRkrTlbuEUprr1ydB11Nqf0YDNYAL
T4C7HjL4rbPCrSIw5gN/rL/dDm/3hcJXoYEn4x7wh4HVGjj9DVisVjtz5sygXTt/+KTX66VZs2as
3rSJkNBQskdEEBQSApqGMymJuFy5SBo1SvIchg0T4XviCclcjomRFU1mpsElS2QSkYHDXwgB3gP6
IoPAT8iAoGOxzMdqjcIwLuL1XkfXi+M1JUGdwpIc2Lhxxn6oFSvk+0nlLzBjJhe5mMlMcpMbgAtc
4HVbdzzFC8lkp2HDTK4RifjavVsmQw89BLt2yd/BrFkUuXCBEwcPqp4AfxNK+P8kZ86coVKNGjii
o8XE07atbNi2TWaTdrvYhpMdeHi98tpqlcgf3xL35ZcJS0hk+NDh9B/YP+X8SUlJ1K9XnxyHc9DP
0S+lCXhqDAye5EkoGQwtHTIxjEeSQ/9oTL8FKIJfDBMRRW3yrIj1gQPpxT9Z9Kc6J1CCEgGnc+Dg
VV7lhhYlg+KkSZIh6xN+8CdTRUf7bl4GyQUL7nip5gYNSPB6CU6+xHrBwZz2OHH0NPwNvgxgoxUO
GP7XHqAE0CYT0Qc4BqyqDM6DAW9qpscpViYfufPn438NG1KsUEG69OiCxWShxQstmDt3rr9Npa7T
pkMHVu7Zg8PXY+GJJ+RUs2aJqSttaYbU7NghM+nETHIjCAOmAu0IDm5Prly7yZOnINeuHSdXrps0
a6azaZOVgweL4nY/J4doJgjaBrXywuAM8klWrJCw3evXwenMUPQBJpuns+olK5w7C82aZV4iGmQA
S0iQAf2XX2QV4/OZXL1Kbl1n8Zw5PP10RqsWxb1EGdbuAWabTcSsVSuxU4Ms7ceOlRlQx46BRdaq
V5cZn0/0Y2MJTbKnE32Qkgqbtmyicb3GTDk8hT6OPplfiE/0QQTvDxa9xIL0404dJKMjPbt1XSpa
zpolETy+AS0hkbAYJ1NdE9OJPkAwweQmNzdMN8Wn0auXxJn7Qg9BbPBDh/pfnzgh9uK74AUahoLb
Bee8QIiOyWOBeW7oiFhHNKChGxoiZrA5gMcGpZ2/4TnlTvO6Ioa+jQunanMhPp4jxyej229hy2Oj
xVMtmPvx3ICaNyaTiVFDh/Jj3bpceeopv+j/SSIiIjCZTCQmang8OsHB7alS5SobN/5M9+5vcvjw
PkaN0pk/38qRIyVwu3f578UAnImwozGMnpix+Cclye+o242ma0xhSoDoA+gmHaKjMZ08/dvmGCaT
lM0YOlQynu12KX6nadx0u2nasiWrli5V4v8Xo4T/HmB4PGL+8LX/c7vFRGGziWPLaoVUTdXTceIE
FcqXSyf6PkJDQ/l6zdcUK1iMPqQXfpfPnpNxfbXfR0aiD1JW5llgySYxxXTuLF3BkuPrTZ27Mk9f
Qj4yr/NiINE45Mwp/oJNm+TZ1Kzp70SWGrtdnJ/x8ZlHEl26JBE+D0KQBSqYIdHuIupwAaom1uKb
Od/gbuOWYBcQ09dnUCJ3CYKCgjjlOHXn5+EAjIxCciuC8TEk9MXtjoYXwbbelk70AY4dO0a9ejXw
6olyvatXywZf+OndFt2GQQmgDrAcaWkcGhrKxx9/TJkyZejRYyCHDi2mcmUzmzZ9w6JFi9i/fxXj
xyexdq2J774rgcORSvRTCAPnWvixIeRbCJ3ay9sej0TnNGkCzz4r2ec3Y8lOehv8r94ThG+9Qh5b
Ec5nkmuRgm+72Sxmpjx5pNpoXJxUo9U0XJUr80KbNny1ZIkS/78QVYrvT5I9e3Y88fF+J5nbLXZL
k0ls/s2bi7ni/PnMTxIbS9BdMhxtNpsIZxpcuOhPf2zF0qi+wR9z7OYlvej7KAI0d8pq5dAhcfCW
KQNlyqBpJrJxh9pDJAu/rkv4ptstIX4tW4pD9+zZwJ1v3xZzkNMp2c0ZRRNdugQ9e2IzmWi6G4ru
gJ9+NOHd+wgNnc+RQ8+BHq/DPDN8GgafhsNcE9Ur1eTMqTMs+3wZEYcjILMy+ReBtaHgyqxYmgmc
cVAOiAS308327dsD9vCJvsnlotSth6i3O4x6047y+NRD2Lr0EmfzihXiD8qIhARC582jldPJAqA3
EKZpzJ07l1atWnHu3DkuXz6GybSXzz+fQ2hoKNHR0VSpYickBM6cseJw9CC96PsIA08v2LFPXno8
MnihF+gAACAASURBVCM3mcQElzevlL7OgMUs5pIeyVTPJJonPY1t4vTM7+PIETEdpTYFeTzyu7Ru
nQw0IL0C3n2X5q1acfHixUyuWfFnUTP+P0mePHkYO3IkfX3lBz78UP5ohg2T2Wzr1pKd27OnJLmU
KBF4gqgozNNnYa34UNpTp8ODh1j8My8XLvrRj5M5TuJ6NZUX1wBWI60M73VHvZKAyymDW6qwSavJ
xlRjOv30PmgZ2E52sYtznJMXTqeUaChXTsSlYEER/9SJShcuSLijxSLJW337SgkMn3ksLk6ecXw8
hq4z1GwmNCiIGlWrs3/ffn5x/IIRFop35PiUZuWhXbrQ9fnnGT96NJqmUblyZbZs3MKjNR6FF5D2
jz4uAgut4F6GiOaeVBtLIw7VseCsBIfLgQYJXmjc+GWmTRtL3bpPcOvWLRo2rIvJ7aJ+UlM6ejvL
s0mODt3KD7y3YCy6pkPXruL8TB0FlpBA0Ftv0fLSJUYnz5ZHAWaTicmjRwPQo0cHGje2s3JlBBaL
haVLv2Dduo3cvGnC7TY4edKLOGjuwtVLMHoUJCU7c4cP95sn8+YFswWP1z+jP8Up5jOfucylBCUo
YZTAGetiTpfeOGdOCryPI0ckYW/YsMAku+3b5fdA1/1VU197DSpVwp0tG9HR0RS9U/lyxR9GOXfv
Adu2baNus2bojRtLpMKgQek7UW3cKDHZ/fv7zRYuF9qYMZSLzktExTB2H9mdaWnkixcvUrpsWbyY
yeUIxYQJBw4cmHE1jJF2ruAX/UPwh1orFQQ63WG7BxgNNG4SaKv2egmevZAnLzxAPyNQ/Hexi3d5
Fydpiq0FB4sfpEoVCRONivJvS0qSOvoFC4qt32QKrNKp67IKcLvJlpwX4PtVTkhIkH8/+6wMGMlo
9evjcjrTxYznyJGD2ITYwPWvF9BbICPnGkiJqDKS/10BWQIthgCH+2GgDnlsDkJNJux2O4mYeJWO
tKB1wOcuZjELWYgbt9xfRETKIAXAiROYo6P5yu2maarjrgKlg4Nx26wUK6bj9sCVSybavtCCZcu2
kJTUEZ/jQtMOYBj7gP1ATjLmSyjWEa7EwzP/x957xzlRru//70nZZAsLLL0qAgKKoiLlAAoiSFGa
KFVFLPReRVA60jsIHgQpKqAiIIggfZEiUhVYpC5IZ9menpnvH/dmk2yyy+LB8/n9OLl47WvZzGQy
mUmu53nucl0tZBDKYvxj6juUin/YmaxOJowwWvMKSVjYxna//b5VvuffpqUYC0glmwULWuId6cXw
NO1ZreKK9sIL0rQIssLr31862d98EwYM4Ns5c2jta0ITwn1DiPjvA44dO0bN+vWxRUbKbHb8+OAW
hNu3i/58QoIQW0QEj0RHk/jXbWKUGF564yXmLZgXQP63bt2iRt26XK5eHVdiGmxOA/tU5MvdHvL+
Dh6pGjuQwN8jfYC8QG+yXwveBuYDYWYpBaxVy7vthx8wxx6krPYIMRlGIyoqv/FbIOl74Ev+Hly9
Kh2r4eFS4eN0CtF7hMZA4uJZyxv1+JO33gCz5kkJKkL8TocDvV5PXFwcK1euBGDy5MlYs8gciKuZ
ipB81nOPBBoBqyFIlRUcJ4Ln2EwKdZDFQ11MNOYtP/LvQx9+5/fg18UH/ZACLZBhp7dez7zCheUa
efIJP26GXScRKb/SPs/WgL6I+ctWgpK/MhAqfgrxNvj8q+C9JwcPkmfUJzzqfIQJzgk0ohF6FLZm
IX6AS1zCilzPkYbx3BjZRRL5aWkyKTp9WgZwvV5WxYMHy/akJKnxT0qCyEiiVZXjv/3GQw89dNdr
FMK9IRTquQ+oUqUKoz/8kA8mTkTLSdCrfn35mTVL/t6+nSupqQwZNJA5U+fw3YrvcOs0FviYomSS
frVquDp1EuvGbZvA/jgwDLggOvfJ9+nNpCOT2DcI/HQkIA1NGkK6mzZJ8toDlwubZucEJ3L/ejab
1O/n9yGkpCTJi2Sdk2QlZ1+EAW8hk3APTrm8Ll6PerVOT5w4Qe0XXyT5ueekkqhNG3m9NWtk4DaZ
hPyuXZOwVgB0wIf4h1B8y6ieRKMZJ/mSOoie0C7s1GUZRoy04vW7XZWg0IAP9HoWFy4sYSGPMN2v
v8L+swSSPhnnNAsh/47I6sX3rYyBqAXQxAoLcihvSk8nVW/nesR1OtzukP1+QGmfczBpBgnnXLgg
n5dq1aRZ0TO5uXhRxPFAyP+TT0SbKTkZa7lybNmyhfc9/g8h3DeEiP8+YcjAgXz2xReci4+XOuVg
M36QOv7LlyVM8uef2F0upk6fzqDBA5k4YSIrfviBpcuXo2TM5FwOB7Rti+vtt7M0+AwBFhAg0HU3
6PX+3rBut7/ypQv4CyH/1nhn0KnAUjKqXDIey7ah6B7hcEi9+N9FMNIHicZgFfKfNht9WBhr167l
3Z49SXnvPVHh9MVTT0kc+vnnpQ8ju0FcbwWtBigZs31NBX1NcG5BYv+BKAWswE5nvvtbxK8BHfV6
VkZGojVq5D/gpqYCDQkkfQ8UoBvwIrDP5+EfIGoWvGeBaLIXFIyLgxmToYGVK9st6M16sEF5wljO
Yt7kHTQ0Ukjxe9pxjnNdd1P6D/bska7dfv38P8ePPea1jgTJ86gqPPwwzgsXOHv27D1cpRByixDx
30cM7duX7gMG4J46Vao1sgqGeZq3NE1KIn/6CSIisObJw5Q5c4iMyUdSgwbw2mve53hi2344DBzk
nknfZJIvmq/5+O7dUqHja3biAq4gE0W/8ydXlUIRSMqhts9jnwPXMw59X2ECmhBI+h5UAq5ZYcsm
XP3781rHjiiDBqFlJX2Q+zVmjMhFZxcB1QMFXdAZMGdkad3A6kNw/qUcyT9rT2p2ndi+0CHBpq5G
I9/lzYtmSYJjK7wv4dbgdx2ouSh9VKwYTS8R5tJlHlzNp2F1AEdAsbnR9uzx//zFxcHQAfCyVaqX
yoJ7nhuTHga47UxhNW7cnOEiRzmKIYNSHDhA0eHo0lkqfR56KJD0PXj0UfEQnjdPjGPMZhF9S0/n
8NGjgfuH8B8jRPz3Ee+/9x5pFgsfjB2Lw9OW71ufvmKFxPfHj5cPt6ZJSWKePNh69MB28qR0ab7+
enBBMVWVwcLlAHIIewSDySQVFRMmSFzVg8aNZZZ76JA/+f/NHEEEwsOr8I9+dwWq8w+Rv/ku203A
2XOQrwDo9cFJ34Pq1SWEcu1a4DY9UJAM0s/yeBurD/lvQuHkXU/rLd7iCEeClul6kA84aDCwt2hR
HGl3oI7Lm8j3oJwbVm9CpBpy6JzVNMo6StJJ7ZT50PlL51m2cBkm1c5qNzT+979h4QJv1EoBWruF
9EGa4cLArhroazQw1WZjBN9TgSqsY50f8Q/WBhO3aBmOCIMkdnNSqy1USD7fVqvsN3QoTJjAoRP3
EDYMIdcIEf99Rv8+fVBVlUEDB4qtny8eecRL+nfuCOmXLSuhoccekw7GuDjo3xdmzPInf1WVJfEv
v+TOitAXer04SWUlfc+2MWOk3O7wYUmk/k1EIBJhWUkfpFjoV6AaspjIFcxm//CDpuUc5w8GDRkj
jx+H30/I8axW/47h3EIlkPQ98JD/jCOYnC9RiziyijCkAS7cXOYyLlzMZgF6nsXFwWxf0gLszJ8f
0hKhWnog6QOUB9q4YFUDcJ0GgnkDb8eEkenqdMJ9ViQ1qUm0M5qlzOU2dvQOB+43kRVFIWTJESx/
rShYx49n0OCPeFqtzGjGZpI+QBhhTGEKQ+xDiLPHYc+tWu2oUVKNpdfD22+T3KMHmqZlW+0Wwt9D
iPj/AQzs1w+DojDo449xTZnil1gEhPR79oQCBYT0p06V/2saFIiBSyehfx9o8or3OYcPw8GD9076
IDH9F14IJH0P9HoJ/xw//h8RvxFpMArGEyDk3x64uwgDskKpX1/0Xzw5icOHRTgs4xpERUWhN+hh
N7AfnPmcWJpYvB3MGrDFAMcMEJ1BdpomXaIzZ8osMzs0by6+tb7XWyHn1YUeMNqpwmE2Yse3IDIe
SZkkk05XRgIKLpriYg/ZGiiEgy0vYAqHy7eCk74H5YG8Nkg4QyDxf46OYczBn/Q9eIVXsGOnC5+j
D7NRZHcx0tLSsDxpwVU3yPrMgAymkZHo9WZGq+P9SN+DMMKYzGQRELzb50pVRdK8ZUtxcvM8rGn0
HjiQudOn5/z8EO4JIeL/h9C3b18KFSrEG126oH3wgQi4gTfO73JJE9LUqdIBq2koM2Zh+uUIBR2F
SUtJJnnhwgyZg4znud3/p+/pvwIPybvd0vuwY4eULTZuLNfJZILZswk3GBg7dizPeYxMgKnTprJh
7gbcZdxYm1lhuwFuFoeVc/0lH77+WuLNwch/3z6ikpLQXb4s+v+pqVjS0vzMyHOGixdwBZB+DUXh
lq40qvtPJBttAf5FuO40LtV/qFQMGg6zW+JjuyHfb5dI9fZ9ZQ+dBnRHhtaMOn7+IIyJ1KY65Smf
7VOf5mmKFFboNlBj8uRkvvxiJb0G9OLKriv+5H8TKWbSAJcLoyEcgzN7GgkjDAMG7AcPSjixatXA
naxWie1rmmhb+c7uo6L44osvQsR/nxEi/n8QHTp0QFEUOvfujT0sTGbWycnyAa9cWapKkpJE6XLX
LrSd2ylasgiRJhNXTl5Bc/2PtViYTDLj27zZ2+Hscom09fnz0lhUpQrhkZHMmjw5oMzvyxVf8t57
77Hpp03Y/62i5ikCM+YG6vx4/GP79ZNje0pJ9+0jfPx4xowdm2kwrmkagwYNIj4+XjpX3WS/pNEA
vYGZZgOf+QzSFlXF+cwzqMdOgbsnUn2zErPuLI8qjzKacZkz5hRSGKD25Y79Do4ENxGHYKcGVXMT
6VA1alOMJCZ4LylGKtOMJAKtPIOhenUYMiSdt99ux/Ll39C9b3eu/HIFV22XkP4y5BrodN6y5Nyg
bl0RZhs71p/8rVap7S9aVEh/0CCRiMifX+55ePg9eR6HkDuEiP8fRvv27WnSpAkNmzfn1B9/oCoK
VodDkryrV2fup0tJoVH9+qz/9tvMztKdO3fSs2dPTp48+Z+dhMsl1TtNm/qXcnrgdsPOndkamucW
biAWCO40K/poe7N7sof0t20TjR5faYurVyU0ptMRdeYMH3/4YdDabp1Ox6JFi3j11VdZv3EjzJqU
vbhb+/bSE7FunSS94+MJX7yYLxYvpo2nmzQDderUoUbdulxIvIn29W2JV2Ulfw3YqoOoItg/m4Pd
N7RhNAqRLV0KyxaDqmLWhVFBeZTR7nEc5CBun/n8YPUDpjCRhBV3KKR385gKioZkxrPx9SENSNOo
zlMSWvHBGtZwi9vZPDEQ1atDmzbprFq1lK+++IomrZuQoqZIm4CdjMS/HS5exO2KREUNMAjywJ3x
z7R7N3arVYi/QgUJ/Vy5IqTudstk6OBBCXnGx8OZM7Ii++ADtIkTc33uIeQOIeL/LyBfvnwc3L07
8++zZ8/SpW9fUi2WzMeqNmrE3OnT/eQE6tWrx4kTJ3C73SxcuJDhw4eTFMSE/a5wu0X/fPhwSS57
XiMtTUrtFiz4j+P7INwzDmll6pVlmwNoDhwJ9kSTSXIQHv/arHpGxYtLqV/v3hhUjarBwgUZ0Ol0
VKlShR+3bMFpziYgb7MJ0bjdEvb57jsigIULFgSQPoge04Fdu3iyenWuaRGw8pIYWnnIXwM2K3Ax
P8ybLc5ip055D6DXy8AVFpYZxghXIxnNOMYyDDMXeCgjNKMBn6HRT/2QkepINIPkTpZr8M4SsHYm
kPzTgGVhYDIywz2X2XyKgkK4LpKBjl78zM/c4AY3uRlUPVVDY4Pxe4oW9wo7RUVBerqKyWQi2hCN
ZY9FVjy+cwOXE4fBzkTnRD7ggwDyd+NmvGE8OlXHxE8+oY9Hr+rYMZHjqFfP6zkMMvnYtUtE644f
l0EiJgY1JC5w3xEi/v8DlCtXju0ead5cQK/X06NHD3r06EFSUhKDBg1i2bJlOO+FqO12+cINGyaJ
3MRETMtXE+0wg1sF8mHBgh07LlxUrlyZF198ka1bt3Ly5Elyq+xhAYYijcT/8nl8ErIaCFqToyhw
86bMwrOSvgfFi0OXLugWLsrVeWQbGVnyOXz1Feh1QvyqBpoDVW+mocf5KwgKFizIE1WqcO3xx2HJ
ZzA7EcIUcLrAHQF2DQa8D7Nny8AybJg3Vv3XX1KtUquWzP41jQg1nLEMoxLn+AKH3wJiG9DWE67J
WAi0A7BnkP9r+NTxAxvDwGKA996HBg0y1w6pBw4watInmB0KUfoC9HD3ZD7z/MhfQ2OecQYni29l
6tjgDXkxMTEkJiXismdZEerA9pyV2GOxcAc+0Lzk78bNJPMklKoKK4eu5N1335XBVlUlQf/SS9C7
t388v1o1GSS3b5fPQokS0Ls3bUJ6PfcdIeL//xny5cvHokWLWLRoEXFxcbzxxhscOnQod0/2kP/x
45gcOnrQ3S8skEoqvejFVa5y4sQJTp06xYQJEzh16hTLly8nIiKC9PR0jEYj0dHRKIpCamoqdrsd
1ccg3gJMxD8akmPngadkM5j/qy/u3PF7nWD4/fffZZXkcgmBFC4sUsAGAyxeBFu+g34qRGUcRwN+
APtJB8nJyRTJapPpC02THE21WrJKadgQliyDvU+A+TSsXy+hpTFj/EXOypaVx4cPl8ak8HCsx+Ko
xO0A0gfpr12FjWbAdc1bnd8O0NvhrTUKtgIF4NZtiY1bU+H9LlKJ5Iv69UGnwzZxIkXdRl7gJXrQ
g1a0ytzlguEMfxU/wNS5Nj87YplTKNy5c4frN29iVTJE5JxOb8d2houZrYONPfP28IbpDcKNMiLZ
3DYqPl2RDT9vIDw8nBUrVtCseXMckyaJNENW0gf5HAwYIDpWP/wAO3YQpmm837lz9vckhL+FkEjb
AwBN01i7di1dunTh9u27x3JNmOhBj4BYMHjJ/xrXRDUSCZ+YzWbq1KnD7t27efbZZ0lISCA+Ph5n
hjqmzWYjMjKS8uXLc/XqVW7fvu1VyczxZExCzgUKyNK/RYvg+124AN0HEq6rQfXqOjZvXoPJ452b
gZ9//pkWbdtiK18eFEVeOzFRVgsPlYTN38GbNn+/csgk/wrOChz85SB5sskLNGrcmC0HD0oupHlz
cVb74gtYmgq44KHj8NnCAGXLTHgMx6tVI2LnLs6hZRuyBxFh2FoZIuNgq8vbmvV8eDixXbvK6qJl
S1lFdOuW/YFWr0b5dimmBA27akOHDoNBo359KFxE5bU2/h70Z8/CBx+YGTJkNOMnTCClQQOvReK5
c7BqVSb5G8INuOq6KHaqGFt/3Or3suXLl8foU0IcHR1NqqZJlVYOqyvWr5dQULNmmHftYve6dVSr
Vi2HKxXCvSJkxPIAQFEUWrVqxa1bt7BarQwcONDvC5cVT/BEUNIHyEMexjPez9tXNapY3Ba27N6C
HTsXLl4gOjqamjVr0qhRI6xWq8gPp6fjcrno0KEDtWvXpkCBAhQpUoQmTZpQuXLlAKLGZBLXsq5d
hW3u3Al+wpoGfYeCfTZW63p+/TWCRo1exe5TY+8hfevo0WiTJklCcNIkqdqxWuGbNdAmCOmDxIWa
wYWkC8TGxgY9hTNnzvDrsWMym3/zTXHR8piOxPwARTdDqRKBpH/yJKaWbTE2egXjxOkYbW5Mp+PR
uLvjowJQAdLbQgMDTEZUNKpbrYR5zFFUNed+BIDChdHCFPJq0XzLt2xlK8NcH3HgFyN1ng8k/X79
wG6Xclm704k5NVXuU61a8t67ds00rDdoBsx7zCiawmOPPeb3k/UzqGkautxWJIeHw6FD1KpSJcec
Tgh/D6FQzwMGs9nM1KlTmTp1KlevXqVt27YBrlA5acSkkMJVrqJ6HFyMiBVjRp5Uc2lcWXeFxKRE
wk3hpKSkoGka5cqVQ1EUTpw4wYEDBwBxDdPr9WzduhVVVXFn7UMwGKBVKxFH69RJkqIlSwafDabe
QiRDwWr9il9/7UDt2g2pXr0qt27dZO1PP+CaMN7f6AOEiMeOhSFDIDYOWmbTAKeAQ+dk5Tff0LRp
U79NZ86coWa9eiS/+SY8/rj8KIqEJWrVgiecEAMBFZMnT2LqP4yPHEOoQsaM2Q1rb/zAV/w7u1vg
c+7I1Kw8pHeEjw4BZ4zwUmPU5GTYu1fKgUtmJ1Tkc6gkI/O1+Zly2XWpB+kwsNcnROdXcSOG88nJ
OpYs+TozyW2xWHjxxRc52qIFNrtdwnH9+8M778DSpdgsFsLCwnKpw2HAgI5cFWfa7RhsNnq+/36A
lWUI/zlCxP8Ao3jx4pkz2G3bttGuXbscQ0GXuMRABhJFFDHEoKGR5k7DvsOJ6yHVG5Nt5MTysw1L
dGHpSr58mTPx8WhZuort99Jl/NprMrOfNk1++wrJ7c1aBGrEav2KQ4e+4NChNOAK1K8VSPoehIUJ
SQ/qnvM5mMNZtWEDx6pV44KP7V9aejpa7dpSDutB69ZSfvjjemgDWYQpYeZcTOs2MoqR1Myin/OG
2p7vWMqf2Mkuo+AALml4EyVlwGECrpigbVt5rGxZWLlSBqKcoKpU0Cpmkr4HdalHBXtFUq6nMEoZ
Q+EnC7Jnz5rMHgYQb99t27bx4ssvc9Rsxta+vdTav/KKXFeLBYfDwZ07dzh69ChP+foq+CA2NhaH
w41ZNeNYv17q+oOFxKxW+PFH0DTCH344RPr/EELE/z+CF198kVu3blGgQAEsdywB2z2k34lOHI44
TKzNG/LQ7miEGYvjaN1SEsRLl0IRO1z5C554Elq3RluyRGqv76XZxu2W2biv/o5OJ+Q/cRKZwRB9
viBPNgKeWv4oYF3uXzc7qOB45BGO37rlr2uUmiohnvXrAxOoTznFjvIKsO2wmIz8epiI9TvoRo8A
0vdgICNoxki2oZI1kOEAmurhUmnAo+59BnFaN6ZB/4z3neZGcevRli2T4vvSQWSZb92CTz+ltq1t
0PMomvEvhvyMGzfOj/Q9iIiIYNvGjeQvWFDKUqdNk4HUZwVnszmoW7cBu3ZtDSD/2NhYmjRpjcMx
mEfZzIWzp0kfNEi61n3J32qV1URSEhQvjnavukwh5Boh4v8fQ2pqKnHEsYhFvMd7AFzneibp/xr+
K/mfy0/ymuTMGO3NmzepU7sO13bGYp89Q2b5I0ZA1aelMWncOAmlfPnlvZG/J9Hnm7jbvBkWfgXa
fsTbFnBpSCxlM+J8FQy5MBe2KsKqwXKv+3VwzQ2uW9I4FJ3FOH7aNK+Noy/5F8/4XQJoaoU+/UAr
hqI9TpFs5/NQhzrsoj4v6LazVlUpk/G4BnQxGNirA2sZNxg0If3vER+V0pBZH3UFtGWQJy2a1F69
JJ/hS/63bkHfHihJSTRXX87x0oghVvZVVREREeg8A2GpUmKlOMTXhF5HSkoT6tZtzLRp4wjPEMFL
Tk5myJBRpKd/BVhQ2MKjVORI+lVJJvg6uO3eLaqob74Ja9dSUKfj+eefz/G8Q/h7CBH//whcLhc9
+/fHaTKBUeVb6xrQFN7jXY5znEpUEtJ/Pj/frP9G4rYZKFGiBPv276NmzZpc+fJLXB07Ctl/+CG8
+io8/bTUqb/1ljgq5Yb4TSYZPKKiRGraA4MB3mkHi+uBfRfwCDLz3wA0Bb4BXspysES4cVkSndmF
Bq5dA9UMS9OhE/7kvxfYFwYGc3DSl4sg5N+5MzRqJOefdUZaGnCqoO1BnGFyxkM8xFadgeYRYSg+
pKs++STWbt2gf2/4KwkuqPAqUAJMq01oZ30qpTRIU1Kliat7d1GA9Rzq0iWomoZ+hw4nzqACbR64
tHvs2vZoT3mPAPxMSsoE+vff5rclPX018DRmGpKXaA7qDsOoWXLfL1707pg/vwxW+fJhsNk4cPQo
MTH+4akQ7g9CxP8/AJfLxWsdOvDThQtC0IA9NZVvp8/nm9Rv0FCpRCUsMRa2rt/qR/oeFC1alP37
91O8RAlprqlaVUh7/XoJg4waJVosuakONpulFNLhkFDP88978weXMwi8aQ1YPxvcMzOeVBuoilSz
j4XMJiQnMBPOqTDhE/hwWCD5nzgBoyaDrS84x8A8HejdEBEuDVwOIxh0cl7BSN+DEiUkuamqsGwZ
/HkaKgN3kAWJCuhN4JJlgHqXVYiKilKjBunjxgTfYc6n8P77UDgKfkrAGK1S4WoFPnZ+nFl1dYc7
9Ff6kxJmk5JY3z6ExDuQZEX3qMKI0yOYqk4lLMhy5xu+JV6J5xlfo/cscDqdqFklPQLu9S3gQ9LS
DgC+PrnJmGlIJfT8SiyOeg1k1eAru7F9u3RnjxoF06fTtH59ChcO7DIO4f4gRPwPOBwOB02aN2fP
xYs4PLHqDJK154vG6HbyhOURXLiIyRsTlPQ9KFq0qP+XXVG8f1epAoUKYbh1C8VoxKnTSbOPh9A1
TUjT6RRivnFD5BImT5YkpQce9dLDv4FSMOsZIEI5u/GGdk4CiWDTiVfBhE+gW9csnq4TwDYAzNOh
WGkhx3PnoMbzMnsvVky6a6dNy91FXb5cGowKFIRDBrhyHZrbJeyTcVp2GjCHxVSiEnnJOjuG85xn
NavRGg3N/nUKFxZdm9deg2vXUD/9jH7OfsQTz7ywaSS5U1E1DYvRDWXKwozp/ob0Fgv074fj2mXi
wi4ySB3OVMd4P/L/hm/5nEVEmBRGf/gh8xYtCtC+dzqdNHvtNfRVq3o9IoIqxaooSgKaVg14ASXj
H/xGHqONy2Yb1Z+tzZ7du+X+Fywo98nlEsntjz+GWbMwJiYyY/LkXN2KEP4eQsT/AMPlclGtTh2O
nzwps9Ru3WR27cHOnSgLlvAXf5Gf/Jh9xOZjY2P5/fffM/82mUx06JCzyTaaRonixbl18ybOcuVE
F8gTF05Ph759JfzgkVyeNs2f9EEGh6FD5bk3d2YpExwGvADMQWb+3YCLiBFwxq9ffhF/18ywirqS
uQAAIABJREFUhgHs7YX0p4yW12vbVjSBxo4V8mnXTl43N6sVT0fwF1/IDFsuFkwcB8UcmcTvYig3
SKIHg5nPFD/yP895+tCHdMUqzlS5QYsWqOjo9ekgNEci+Z0aL2g6/tDrSQ1G+iCWnTNmwuDBOJ96
itO//0m739sRgVh5amgkkIAdO3obfLtqJYAf+XtIf/edO1g/+kiIOj1drp3P9SpYsCC7d++mVKlS
NHv1Vc6ePyTln0CE2czo4WOpX78+xYoVo0mLFuw8dAh3XJw014GEqCZOxJiezsHY2KBJ5hDuH0LE
/4DC5XLRqm1bTtls0gzTubN/OSJAy5Y49Hpuzp2H2+HGpEpTzurVq3m769toFbXMwhpdgo4lK5Z4
O3FPnxYC8FX7tNtJTkvFUbGiJP98G3giI0Wgq29fmV3/61+BpO9BhvsSBwZl2RCBEQMKPXCwGtiC
CET4wGZFgtxhoOigdDEoeAI6j/GWPZpMEBMjKqD9+wtx2+2iFrl1a6AJuwdLlsj7TUuTnwIFROFz
6lQo+bDMsPXJ4B4PDMfNJ9wAOtOLUhQGvQKmMM6647AMGSCDzz1Aa9EMy8YfKHLmDoeBIqi0DDNx
ulWrQNLPvGQR0KQJzJuHw+XCgYtEEgN2s2iAxcKKlSv57ocfMGTcO5vbjbVsWazDhsmOiYkyMF+5
4pfjuJ2UxGNPPomi06Epiqzq/vUveOUV9CdOMHTkSA7Uq4fRaGTTunW0aNOGHb/+6u0gTUwEq5W9
sbFU8XQJh/CPIUT8Dyhe69iR7deu4SxRQpKvWUnfg2bN4MYNSq86y5/xf9CpUye+Wf8N1nZWfxVI
N+xbsx9dTBTqH3/IstxgEN0VgGvX0KfcIUlnDCR9Dzzk37x5LiWgfcNO5zBRj+505Akepys9cJFd
n4AbSJESmWdekMqhYChUCObPF933b76Bv87BjAx/sKzkv2SJSBXY7TLr7dVL8hSffy6OXp4Zar58
0HcYwq3DcTOGROMGEivp4PUW8tzCnaF8ebHm3LpV7kEwXLokrbQevwBA0emYDTnUC2UDTbvrNfeQ
v69qLEajhGU8lUwGAwaXgkvzSeAbDJL/mDoVzTMAWa2S89m7F3eVKtwsUoQy5cqhaBpNX36Z5UuW
cPz4cT+Dm4oVK1KqVKl7fWch/A2EiP8BhMvlYv2336Jt2iT11nebQRUrxh9hP6JayrBs1TLxlb2m
wI4I7z4KqE+lg2KFIf3BrpMZ9eRxMGcaOGyEmTUcKLhzarqJjPTPDeSIZCJ4HAUFJ1fpTmdaICRZ
mUoc5WgujpEFHjlmD6Kjxe/45k0JKxW3w+ypIg/sW8f/++9eG0ZNkxn/woWSL/j5Z3ncMyhMGQ09
BoNzFxiMEH4VZnwbmHSeOFHuj04HL2cpt7x0ScpHu3SRQSIDZiA/9wF6/C29DGSG1YxGiQy6DWYY
0N+/mW7fPtzjJmCwG3DhEtIvWVI0iHy1H6KiZEXTvz9s2SKDW4UKaMDGs2d5snp1Th05QnROyfQQ
/jGEiP9BhaKInsylS7na3alagS7w6BC4ZIdfo6HvIG+DTWoqzJoGz1nhzxhgMRjbw+tAXlnyWzXg
BytMGg9Dh+esthkfL4ne7DSFzp0DvUI1QzE6utoSQQQlfLxk00jL1fvyg8slZJs3r+gCJSdLAvWj
jzJyD0jKQK/Cnv3kqENgNouHwODB/gnshQslFFK6ADR/QgaIdWHBy0xLloTp04X8//pLzgVkYFq1
SlYUjRt793e7UVNT/QS28rtcGI8cwdmwYaDapeecjh6V14+MlGvgtEuKxNeJ8TjSA+cOR1VL4jZc
FtJ/KUvpbJ06aCM+zCB/cOl0gaTvQZ48Uh7brp1o/Xj2qVePq199RaVnnuHU4cMh8v8/QIj4H1Bo
miYdtjqdTN9y3hkJ5hvgjgrXomHWfG/izYMSJWDIAFAdENYeOlkDfb3fAlbuzZ78PbPtK1e8VnxZ
yf/AAVGe/OgjYufMp+KVI7RTvQYpxznOeeLJ1qTcA73eO3A5HJjefQNz2i3MeU3wST9Ut0ZqiorN
CmanHj2RcjiDmXR3UvaHDkb6IP/v2lXI9ehRqRi6eVMG4OxQsqTkGrp1k+arq1eFJHv39k/Eu90w
ahQlExKo7fP0aU4ne3fu5GJEBI5evfzPR9OEeM+elXMND5cmqZ07Qc3Sg1AEUMKBzyCsD7z2eiDp
e1CnDto7b+NeshQizELoCQnwwQcygHkQHi73WK+XbVlWeVcfeYRXO3Zk6w8/ZH99QvhHECL+BxWq
KgRUrZp01FarFlzF0VNWaXcAN+GOAouCkD5AxYoweTr07gXt3IGkDxKWb2eHz/cJ+fkqK2aQV2ZC
+Px5yRW8845/+eW8eVLV89hjqK+2YMWnKzjmOAZIKeFRDqOyEBiIKKNlw9CKIk5OPXti+uscj5dz
MHExGI0SstE0WLQI1qyBjs63qEENeZ4NetMbe3b25ooSSPq+23r2hA4dhPRBQkAuV3DbS/DelzFj
5IT27pXk8+XLMig2bgyzZqGcOUNThwPfNG4MsM9mo/rGjZw/cADNN47vdsuse+5c72y7Rg0ZDNdt
gRZWqIA0fy0OB1cndLp3UN2KNFJt3epN0oZnaf6KiUFRdGg6nZB+/4zVga9pysmTku9xOCRc1KmT
d9vZszBmDIdyISMewv1HiPgfQBgMBio9/jinihaV7thVq6Q9fuZMf/K/cUNI6rXXYOFn6FiLmi9f
cNL3oGJFie0XyEFfNwyIdPl38HpI/+BBIUKDQcjQ4ZC6fQ+MxkzS9yC9fFH2R+tg31GgO9J6Wx6x
e+ka+Pp6vZRp9u4NRiOmT0bzWFkHpUoZA0LpTZtC61ZOtn2/kVa2VkQSyS1u4VJc2c/4dbrgpO+B
6B/I/4sVgzJl4OOPYMzYQPJ3OGTwq1oVZd8BonYcopG9McrXLiCZc5znxKdLsD9bGW3KFD7v14/S
SUkM8lnF6QC9oqA984zcSw9+/12Sz7dueYlfUaSyymaDdbvgfZsQv5qPPHm+xeCO4lFLBZRtFti1
jwTtNpdKr8M+c6I/+WsaquaG27ehY0cJ57zxhv97q1pV7vnw4UL8vp+9QoVg3DiSRoxg2bJlvPXW
3TudQ7h/CBH/A4oyDz3EKU+FhUfNsVcv0dnxhFvi4mTau+cXDPpilHYfI14rnN08956guFS0yZO9
DT82m8S7PQlSD+k3beqfPAyGsmWFxF9uBY7J6E3OzJi5phpQ7S6MhOHUuSFPlMTKx42TUsZBI7En
WShePIzNm8vidG7FK8qfzubNDWjQ4CxqzE1mXJ1EJ95nePhw6tWox7ad27I9pVxDr8dQJD9Rh3Zj
HTsC+0fjvOTvcMAHQ0ED5aGHiZq9mHnOGZTCW9miojIhbCp7Uq5gL1gQy/z5jOzRA2dSEm1UlRTg
dbOZiw0byqzbd0AqXVrCUh5BtDIZikCKIlLYR36DFBuchyhTGu50Nx+qH4mwnBNwyuuPvziFX/p9
4CV/TYMdO6BAjIS8bt2S8ttgeOopyWEsWybVZb6oWhWGDGHIqFEh4v8vI6R5+oDi6IkT/g+0bSvE
HxcnM32PM1WJEnApHpN2k05oRN4nP7ZwzYwpySqx/CtXJByQVabZ6RQT+OygaSK3cOCAzCqdaSjh
oD1fF/c7XXC/0wX1va4oJYpRMqwkLZRXJQl9Lh7avwktWsO5ykAY27aVxWbbi7TXRmf8FMNm+4Wt
W8uRkmLAzS8MMwzm4apl2Ba7UwjS8+NrIuN0Ss1+drDb5TwyEGZJplsnG485j2Jo+TJhLZsS1rIp
hlebUTr9FEWSThH1zY8BpA+gQ8eHjkHUuVgC88hPoEgRLPPnM/6hh3hKp6MmcK5aNdxZSd+DF1+U
sNPChUGuL+CEiN8jcKc7+chD+llef7hjMLUvFMc8dJQ8OGOGhKHmzZOw0d2MYAoWzD7PVLw4rqBd
wCH8kwjN+B9QGDw1eR4kJEj8uHlzUT/0xfLlsGwZeVRwJSbCkSOBszMPtvwsBLPTAM1dwW2kzoPt
uo1wwrFnW2uPzHh/+knCEO++679N0yTB++ef0LMnhk/n4zab0TVthLtnXz+S0xo04GKvnnDrMDh0
iDh+BlGrl4BvMkg/mLxzPmy2X7BRgssmB4nabWKPpMKnn/qVUfLVVzJrdTgkHDVkiMhNRET4H85u
F/E6vR42bJBkLzLJnzbeTnKy/+5584r6w+k5dSnl8pK+Awdun7VXW0cr9l0cL38UKUL64sXoO71D
g0uPsrlssZxDTw8/HMTTAOkyXguqxcLj2hPUpCY2bFh8muKMGMlDHvo5exAb105yMBs3SmIkQKjt
78EpBr8h/BcRIv4HFNExMVI/XauW1PEPGCBNSVlJH+SxbdvIHx/PRoeDl4YNw/nJJwHkr2z5mcjp
C3nH0Y05f8xF0xnhFac/+Z+HsO8gSjGTRi6+0DYbfPutzKI9zWAgtfGnTsHMmYRPnIgtKQldowYB
pA9Avnxoc+dxsXs3wq+HY2MJGt2AbcB6RL4hGOlnHgBFCeehOhbO7TdJLD49XZLTIGGl116T38uW
SU16WppUqkyc6CV/u10GhMKFJa49ZIgkl29fglpy2vlyOo0M7GMfIxnnl2IwEY7q8mloS0xEfycl
Rze1bGG3y2fDbkWXB55KEyK4yEWG0Bt87ls6bnozgDo8J/eoew95I76kf7eqsbtsT89p9RTCP4IQ
8T+giMqTBypVkqqKvn0lNBGM9DPgqlSJA/HxvA2UtSucGzYSZ5uW3nLIlFQi129jtn0KZSjDeecF
Nh7fiJYAurwyv7ZpoJ2CwUNg5nQb7ru6ymbAZoN162SGDBJWeewxmDaNsBUreOboUX4xGnG/1DT7
mW2+fGi1alFzTRKHGE0KR8iTZx2dO7dl9uy7n4emwZHTkdC9OxFjx1LG6cxUN052u7n56KNYp0wR
0/fVq8Ulav58abzyreN/6CGpzdfrpUs5Lg7n6OFs3m6gbl1X0MIel8ubdtnHPkYzHSc7gOrefVgG
ST1kxp03L/ToQSNrXfIRdfdmON/tdrsMSufPwTM29FaodA2OYWMIvZlGOm/6DDlxwAvMEj0f9ETZ
zCTqfJL2Tz4pCdw6deTzlhUpKRIaSk6WlYJvdt1mgzlziMpaMRTCP44Q8T+geL9jR37r0wdXrVoS
MrmLhZ29SxeWbdlCfkUh2q2nl/09biy/iaaIAJqihdGI6ZQWJxDyEM77TpWiF6UEXAdMASz55fuv
ot5bkthm8/6/USNJ5gLGS5e4fA/2e5FE0ojn2JxnJTt37aRAgQLMnr0C7mZvrgOHXSVi4ULGp6fT
z2eW6gJaxcWxbfBgrI8+Kg8qiiRT+/b1HmPTJslZeCp6IiOhalWceQpw3BLNR+MuMHaE3Y/8HQ74
foMBk3KBX7RfGMtM7GzEl/QFb8lb6DEA8ughOZmm7obc5jamtXOxN2wo+ZqssFqln8NgkLLeAwfg
UjxUSYMXVNgkRT2nOcun4Ef6ABWBHdipy3x0GIgkkkQtSUYqvV5Wk0OGSHhrwgR/8k9JkbzSE09I
iPGjj+Txl1+W+z1wINjtPBTsvEP4RxEi/gcU73TuzNq1a/nBbocePWDBgpyfkD8/lshIZplMFLpt
owxlaE7zHPujygAf+Py9RIGX+0nT7f2CKyGB62XLQvzFXO3/k+5nXHoVk91I7ZrPExYWhoIDTTcC
1HEEJX/9x2BwQYKV8ZpCvywzaAPwvcNBq7g4tl+/7i8L5zsoeeru/d6AC+x27F36cGTJp3zw8Wlq
V/POmLfuMXGj9NMohcKY8Os87MwkkPQ9eAusRyHfN1DmYfbH7edt3qZbyh0W9ByIfd40f/K3WmHA
ILh4BVQDnIqDcA2edUEdNfNSpAJvoJHderAisAQnfclHOm5J1k6cKKEuvV7q/Pv3l+qhcuW8A9+V
K7LasNslXzJ9ugzoGzbIud24Ac2aofiasYTwX0GI+B9gzJ83j13PPEOKosiXLzk5+4RcSgo4HFgm
TuTOwI9JsiXleOxk7viVhKmA3SSNm8uWBRbw/G1oGhQqhHL9Cvx6AC1YOAGESI4cwfXU45guXqNR
Ug1KqSXAARYsLFXnoOoIJH/9xxCzlDCrm4ft0C+bkc4AfOdwYLp5M/jqaeVKUfmcMcP7mMsFH32E
kp6OoXdvVOBsZARnT4VD3mhUg4G0xyqh9R0AmobzpXag3c1xqiAULgQGN18pX1FNq0ZLrTmkwIIe
A+DZaoCGEyfq2bNwvRY4jiPiPGtAewMquTMvgasQHNBBlbuE6aOBKCJJxy735JdfpGR2xAh5n+vX
y8y+RQvv9TGbhfCHDRPdnsGDJfz13ntQu7bkUX7+mdYeS8sQ/msIEf8DjJIlS/LHoUM8+eyzJEVF
eeu5s5J/Sops0zQoW5bUEf35ZMR4ClGIilQMOO43fM0pYvEUCKpAFwOk5pWowr34rQfFjh1Sflq4
MC6DQUJGk6dBn94oYUa09h3997daoX8/UDXCLl7njaRmvKG299ulBjXooQ5GNW6FsIwMq2oBw2m4
lYRT0WfG9LND5pclJr9IK3gIbudOUff89FOv3k4G6Rc9epQLNhtLdDomFSjAhJkzMWTEem7evMnQ
kSOxvHQKKlcWZcvc+IsbjKC5MUWb+Mj+ER/aPqSmVp2olAiubL/CZmUzN7Q0xKS3DmLaWxF4FdTm
cHEVZHjcaM9C8u/gzoWkk4pGOulQ/nFp1ho2TETk0tOF4EeNCq7PNHGihIO+/RZatZLPWalScPQo
LevX56MRI3LxpkO4nwgR/wOOUqVK8c2XX9KwZUuoXFkIfuxYbxem1Sqdo2XKiHCaXg9RUVj1Dgaq
A5mmTfMj/6/5ms0sJRY7JRHSfxf4VgV3yn0gfZCVSffuMGYM7r/ioVhhkT2ePQetT29ISYWKPjP/
r7+Gy39hKlSajkkvBZA+QAUqsJDp9NEGYm3fRo732yH4/nfgIJqWBLQAkgOeG4DwNBjaU968FSCj
yqVbNwn1aJok0zWN26pKtF5PvpgY9u/fH2AwUq5cOVp37Ihl9GgoWQzO3G2pZIeyj6AcO8Ks6bMo
Xrw4PTr3wOF0oGoqt5OtuNSyaJRC5CzWA/0zfteErFVACqi6AFeDAFiAa1zDWqSISEtYrfJea9QQ
aYZGjbIX5QsPh+eeky5fD378EUNUFAP797/LK4fwTyBE/P8DaNCgASMGDWLa0qVYq1bNrC3PRO3a
sH+/JOhOniRizBhq1q3Lnj176OXo5VdPnh8T6dh5FAn/a8AjpUpRPDycP//8EwATYaiKxA40TZye
3Kh4+wU1yMmPVlWlwWxAb3hWg98OwKFD0uk5Z67Eio8dJ/MFkpKgbFmUC9dorDbM9rDlKMeT+qc5
EBEBtxNg/Q7QdgFVgFiSRWg42y/FDTJk4TrZvTulA3uAwvWhU2dwudC91xWz0Ujnzp1JSkrixx9/
DEr6AI0bN2bNV1/R7PXXcb7VGc73APdTwMNBzmA3mOaiJFalNPDqq6+SL18+zl87j8VioX79V0g8
VgqnbTH4rV82Ac0R8s+CWD1c01iCSgOgVZBXvQC8hUJSmB7nisWSKM6TR8JaAwZIzD+30DS5v+XL
Yzx9mkJ3a/4K4R9BiPj/RzA2w2R9+rJlWMaM8SYhk5OlEalZM3A4iBg9mrUrV5KamsquXbsw5I3C
nZ6eeZxE3OhNkVC8OI569UCnI27lykxVRhMmuildaal5KeQsZ+lLfyyUB4oh6cTfCIhrhIV55Qzs
dqjshpeAR+0wejiMHJ9B/nNkH4cDhgyWWHLdunBh5V2vg+JwSBmmGgXqEoT0AWpwi2dpya+sxRrw
xbgO1EJHJGHYlrlwverTvKYCmgLR0ejavUm4y8GGjRupV68esbGxxMfH52gl2KhRI5ypqfD5Z5An
EpJqAAfwJ//dYGoFNZ/AsH8/W377jXw+TQEvv9yGY8dKYQsgfYAmwFKgObgqwhYFtisy/up0UPlJ
rFeu0PH6db7En/wvIOuERPQ4Hy7lrzVUqpQMwtkZ3WSFpsn+JUvCmTO0euUVKlSokLvnhnBfESL+
/yGMHTWK8IgIli1fDsCdO3dISUujePHi5I+Px3D5MhNWr+bFF19k/fr1uBUFt8EAn33mbct3u3FP
nIhb06SpKSwM6tWDLl0wpToCSB9kpj2LGfRlGBY+BF4DfgZakhlkCAsTAbjeveHECQyzZ+PyyLQ/
DLTOIP9KFchk3Os3Ic0CtZ/PuXPVB5qfEYuvpUkYFn5iB41pya+s8SH/G0BtIBKNvDg4e0nBNRvQ
G4FIUN2Qdx+Gy9cwpaew4ccN1KtXL1fn44foaMkNmJJBfVTep84A9hggATS3hFVeeIHmbdqwd/t2
YmIkGfzrr/uw2U4TSPrnILwb6NIAHShHwZhPYvMGg5ScnjkDFy9iNZvpYLNRGBP6jNVZAi7e4B2W
Kotx2WyBqe9SpaSk88ABWTkGuw8ul6zYkpPl2n/6KaSmsnbQIKbNnMnAfv3u/VqF8B9B0bS7dX+E
8L+G6dOnM3DoUCGFefMC68MzEpdomsR7jUb47DMar0xiKEOzPe5e9jKBb0lnDfAQsBVoAQanNGxN
mSJG5jNnepMFCmDWQxuXaKv5qvjeAi6VgnZvw2efYVbD6Hm7Ha9owW0mk0nmXXMvEga8BZMWgvs7
oG6WvWxE8DIWdgAaSsYpjAGGIz2trdCxA7DQAZBBFN0odOo4/vVUTfYc2ZN5tNjYWD788ENiY2Oz
vS6AmJvnzy+aRI0aeTccOCCVMDabVMx07Qp6PcYFCyhy+DBPPvUUAJu/34TbHQ+oYG6JzNVVIBWi
IsRzuWRJOeaqVbJC+/e/vQ16330nkh42G2GEUcVYhTRdGha3hWT3NcppDk4XL07qihWB5J6aKrmj
J54QtVff7S6XVP6cPStuZVOmeDudL18mondv0pNyriAL4f4jNOMPwQ8bN25k0McfC5nPmhVI+pom
Px9/LPo6PiQVTRtyQh7yIBZXzwLtgdnAy5BnmxDC8eMwcyZK165oHo9XEOmE0cNl1u9bZGQA4jWo
Xx9SU7EtX87c8M8xWo000vxj/ckk08M8gKTmz4t0xZcbId5GIMxYEFVORRlI6aJf80piIsMzGsyM
wPeotELHTr4hneXAYTDMgyCJ7cKFCxMXF8exY8eyNRGfPmOGJEDfegtatvTf+OKLEo6ZNElWRBmh
Fme3bvx14AB/ecJwus3gvi3hoOZVobVPY9nx4xLemjRJqm8ef1zu3/vve8m/dWtJ2H71FSWLFePp
Bk+zYcMGCkZEUOGiylcuqHnnDunz56P26OFP7nnySPPWu+9KhU+NGt5tW7Z4k/W1avlLO+fPjxqa
d/6fIET8IWRiy5YttOnUCc3jlfrdd/6OSgaDxN7/+MPr7KXTweuvy5f/89QcG74E5YEtSPC+j+R7
C+SXio9PPoGuXdFaZUkxVq0q8f3Rw+E1uywW0oBNenAlw/XrMhsG7F98wQz7LG67b1KSkpmH+My8
jBvNa+Lu9p6QVov6sKALOGIhoxvZHz+hKJ+hJbq4oWm0MZup7XDQR1UxArNRqYIDOAymRjCiL4wc
G3CUChUq8Omnn9K4cWN++umnAPJf8eWXDBk5UnIsWUnfgxdekGanLVu8EtaKAjVreuWu9XrQNYWW
taFrZ39ibtBABvKhQ73kP2aMdM7OnCmlliASyqtX43K52LRpEzt37qRSxYrYzWaqm0xcdblQ12yG
fb97zeWbPCf355OxKDYLyvbtqL/9JiEdnU4MgIYNk89HCP+fQYj4Q8jEnEWLsHTqJMSg04mDlK+5
xp9/wooVsHixaNKAtwfAbMbpZ+IaCGem+FdeMslfTRfy37hRcgVZSd+DqlWha2/YOB8KWOALIE0D
oybhhXnzhPzLlcN++jQrln2DTlOkkxSwP9MId4fXvYTYqrlUDi2vCezHn/x/AlqjLx7DpXbtuKQo
oKr88OWXXL55k7Gq6pUxM70AIwZDnTooQPxf8SQkJBATE8OQESNY67FdjIyk6vPP07lNG5588kkA
rt+4wYzPPsNdvbqEQXJCkSKBYmceQ3ZNk56E56oGkr4HdevK+/38c6mr1+tl5n/hgnefK1cwpDm4
mX6TEiVK0LBeQ9x6Paf79ZMBf87noI6CK/ngCoAN9gyBCAeUUdFed6JfbUS1WCRMqKqyWuvVSyqA
YrI0p4XkmP/PECL+EPwRFiZ1/hUqyKwwzEcR8plnJAE5aJBUZ5QqJX9PnQq9evEjm6hJDaoHkRy4
zW0+YRZWPCGIvMD3QFlQSgh5FSiQ87nFxKC/puCeBxQFklURBytQQMIM0dFCeg4HNntGyCGjmiko
mjWF79aA6ynQFwVNBYcT1KtQtwbOjz+WATAlhYhhw7AnJDBLp2N2xmrHgALP1xBrw1GjcKtubiTf
pGbNf/Fc/RdYtWcPlp49vfXtCQksGj8ew9Kl6Js1Q1MUHFOmiEBdbpBwR66TonhJ32PIvjijzDKn
JHeJEqKwGQznzhE5dz7V69SiYsWKaGi4NDervl9D6tWr8PV6cHwH1Pd/nlYd7HWhQiqcNOIqVVq0
oXzlqpculRWkL/k7HIRPnEjTV17J3XsP4b4iRPwh+OP4camLnzLFn/Q9aNpUYsHTpkmYAIRw587F
3rIl48LGMcIxwo/8b3Ob7gzkDl1QGeBzsAhAg4vx8HA5rz1gDijthMtWcMUDil7cnwYOlDCJJyE8
c6ZYHiYk5HwwhwMiwmR/m00SkQMHQvNWUvUCQvpDhvBO06bM/uMPScICly5domrVqlhjY6WcsWFD
SEzEuW4dZzdt4uzmzf5etx5MnYpr4EBczz4rGjce3E3aWNPgVgosWAzNGvmT/r3gyhV537739tw5
IvsPpNUrzVn65VJ0PpIU1ao9S9euPYGhSH3TRqAp3lrWp8G1CzbUgjIlAkkfvF67/fuwli/aAAAZ
pklEQVRLKa7ZDEOGULtkSVYuXXpv5x/CfUHIgSsEf1gsYs8YjPQ9qFxZyN8XGbPt9m+3Z1LkJDrQ
gY50ogPdeYuuGaQ/POBQOp2OCFM47Nh296W/2008opaJKn/zxx8iM+zxCi5eXBKI5cpJJUl2s+nU
VFnZvPSSzITLlkV36BBhHnNzgLQ0L+lPm5ZJ+gBWqxWnTifqnE2ayPGGDJHX1OuDkz6IeuXUqfLa
HlSpIlLPvvkUX9y+jbLwU3SOJHTf/YjSu7+EvjznmZAgCdTcyjOvXSsD5s8/Q7Fi5Bk2nJZNXwkg
/UWLFtHvg35Q3gXlZ0P5rpC3Leh74J/MeRrcLpgwJZD0PejUSe5L377w3nvozp1jyYIFmfIVIfx3
ESL+EDLR8513RHzrbrNPkGTs9ev+jykKm3ftYtuebVzjGnfMBbjGCqz8EpT0IRWDwUCrV1tjMppE
6Cyj+xcQYt+2TeL/q1bBpEkSP/aF3Q7Hjknicv16aejauxvmzYTkWzB/JrRsCqu+9hJfaqoIhj3x
hAiGZUCXnIzRd8D77TcqFy0aQPoAM+bOJblhQyHfxETpYH3+eeltKFUq59VLuXJy3j//LH/XrSvE
OGBAIPnfvo2hT3feaHqH8sX0VHOXo2ZSeXTmDC/jPXvgrQ6w+ydJxl/KRnQnLQ2++EIGxtu3RbHV
5ZIB22Zl1LhRAaTf54M+WDtaRfKnY6r8dEuH/MuCkD8yk88JUVFSBfbcc+SNiqLA3UJ7IfxjCA23
IWSicePGmMLCsOcm6eZySahh4EApp3S5QNP46+GHebV1a3r37s2CBcsxGNbico0JcoA76PWN6NGj
Ox06vMaGffuwX7rkjQWXLQsjJ8GhBNAqZ8h9vgxsxmhM8g9Ve8j/6FHQqSIl+ZAqTcIAWGH1Z/DV
lxAWLnHuhg2F/DyE7najHTiAxadLGU0jf0xMAOkDuFXVG68eOVK0aN5+Gw4fvvu1A8kdLFwoyVWP
aF7FiqL388gjgBkwwaU4sKXx3Wozek1PQvh5SmglUDRFSH/yOOjogBLAESf07wUz5orRugdpabIa
qVBBqmvWrJFVjs0WdJW1bt06If321kwxt0yEA+9a4PNlkFgA3ONy935BVkK3bxOzdy97d+4kPGTA
8n+GEPGH4Ic8efNij42F9u2DV5qoqoQKnnlGHL0GD5bHduwAsxn39u1cKliQNd9/z2OPP8wfv8/C
YCCD/D0Eege9vg7duzdh+vSJ/Pbbb2AwEFmzJo49e3D26QOGPGCpBNoehG08OIWm1cJkSvKXfna7
5dOcF6gEvOjzcgCPA4stUPxhOPWnzPavXvVuX7oULSkJs2bGvusX1DeDlXhmg2vXpKEtl93Dmdex
Vy+Ii4O9e6kaHk6tWrWo2K4defLkYeDAwSQkpBIdbWLngf0UzlD9dLlcdHi9A/r9v+DesQHa2YX0
gf/X3p1HR1lffxx/PzOTTPaFxQSoyKJiAKkWAcGfQBGhFlFcUVAQFKvIFokSdtBGBINWqLIFsbKJ
LEVQkRYqi5IeAYWfgIoQQIQEEkIQkslkluf3x00ymSwU/VVQn/vycDjMSSaT8ZzPPM/3e7/3cr0J
nIPhg6HVteApHRJ/6JCM0Rw2TK76a9eWD9acHBg4EFYHL4dty9yG67fVhH6ZcKBbEazcWBr8O+Ti
v6gouE6/otKeSlHffMO2zExt1XCJafCrIGtXrqR9ly4wYoRselYMf79fNn2PH5eSwPBw+feIEbK2
e9ttsHYtvqIijpkmx77/HmzF4JmGHNaSYDSMEp588klmzEivcjVtt9vxFAPuZsB6gkMfIAmvdxuG
0YGQkALAgc1ml6HudZGqzMqhDxAJDDRh3l5o00GqYL7/PjA4wAR/sYdraMmRxe9R4LDjT6x7/kHg
1d0ZJSZCVpbcfZSeqq1iyRLZfE6fBi2TsB/NIvTaa/F6iunduze1a9fm+PHjvPzyK2Rmbivv85Oe
ns5LL72EaZp4zuRBVzMQ+mWuN6F2IRT8Gw4CZ5Nko7p9e1mS2rRJXmNFJuzevZsrS0tfL0j5+7sD
6EJYhB1PSgq+GTOq1uybJvY5c4gvKmLDRx9p6P8M6Bq/CnLjjTdyRZMmcsry6adhwYLAnwkTgkMf
ZFniqackTDZulBm/q1fLpuq778KcORjRTl599XmOHdvHsWP7yM4+xMyZgXXzTVu24AsPJ9A9xAlM
pWrol0nC4xlAvXr1aNGiBW3atJHnKgFaUvOExUjgSiSYY2KkhUF0tCz9uLLB/BshZgSz3K8Q97d3
MXZ8TuYnnzAvI6PKU/Xs3p3w5cuD6+BBllAmTpT3oWxYe0Vvvil3R9e1hBgv1PkMX4dzZEZnkvHv
DNp3ak9eXh7jxo0LCv0XXniB1NRUTp48SW5urrxXNc1Zbwi0Qg661UuQ/5dl+xBXXy37KA0byh3K
/Pn4XD769+vP+vXra3jCmuRgt99KWloq//xgA4N69iTi2WdlD6WMaRKakUHjvXv5ateuGk8vq4tL
r/hVFb9t0YLsM2coeewxqTaJiZFeOi1aSNlk5dv5/Hxp9DV+vJwmrahxY8xXXyV5+HDq1q3Lgw8G
98p/fdYsJqan45o4Ub6/uBgJfgNw4XT2xm7/vPzrTTMcl2sRdruDwYOHM2qU9AZq0LQBx88d54Kc
yKm0MR2K1KcPxYWfy7iMWe5XmL9hIadpQcrwkRgmPDZINoIPHz7MsxMn4i4qCvSm2bVL9g1ArvTL
wr9LF1nP93qlTDYrC65Ngt2boZ8n6LPNY3o4+M+DNLmmCV6vNyj0J0yYgO/HHHg6fEg+tDdtktDf
sUP6/bz2GtSrR4PMTOo2vop2B9pxz933MC9jHvn5+dgL7EHtuKs4BRERp1i1dDndS9t23HTTTdif
fpp5Dz6IvbS6x/T5uLxBAzI3bdLN3J8RbdKmqigsLKRz9+7siY2l2OmUq9h77qn5G8aNkyv/gQNr
/pqPPiJq7lxWVqjb3r5zJ2kzZkjop6VBTg6hXhsGcbh5G6dzAjfcsJNHHw2UjmZlwUsvReHx9CIt
rQWpqTL1Nz4xngJ/gfQUrn+eX+59pB70i9K/yzmBZjgp5AF+zyMEpnx9y7c8G/4sCQ0SOOs9x7e5
J/A99JCcNP7uO2lulp0tfemjoqBRI+kyevAgbN8Oa9fKZK6OHeWQ1Yq58HBx9Tc0JnJw+DMwS0zy
8vJISEjAX7nSKgT5rGpf9SnKZQJbHOCMkpYNHo+E/syZhBkGk8aPZ+DAgcyfM595U+bRt6gvC6IX
4DE95Hny8LX1ybJZZXsh4h8RbNu8rdor+JMnTwZ9SNWpU4eQyrOI1SWlwa+qVRb+Ow4fllr3fv1q
/uLUVGjVCvr0qflrMjNh6lSibTZsdepAaCg+u51zt9widxUnThDqtdGEJpzBTb7TzQ035DF5ckmV
wU6ZmTB5sh0nDjp16MALM2Zwfdvr8Tq80BroXMNrcAPzACME4u1wxC+P4UDuMDyAHSfwAL15hP7l
33qEI4xwPENBuBv695MPwsOH5RRznz6yWVpmyRK5c+ndWwYQN28uHwSGISWrezLg1vNcTR8FFoHf
5efo0aNcUdYeo7IQoA8y9b6yLGCFQ5a/DCP4j93OfXfeyTuLF5d/+YSxE1j8l8WkF6UTTzz55DM4
ZDC57XLxt6nwoXMEYjbHsGXjFl22+QXTpR5VrcjISDatX8+IESPIWLRI+ve0r+bycu9eOe1b2n/m
vKKiOHvDDbLe7PVi7NlD6JtvEhsezimvnzpcRhYn8FObq5tmM3myWe00v/btYeRIHytf8dF80yZ6
detGlOkAt58z//ZjOpBRsxW5gQXAZVfD7b0kAI8ehZV/x+7uicFB/HyBHxdu4G2WsoLlpd9sUOLw
42l6BfzuuuDQ/9OfAks8ZZKSpDFZWpos9ZSF/g9ghBo8PvhxxqWeZx6tB1hC1fDPAlY5Ie1FuQtJ
Tg6cWzh2DMaOxVfp9TyXJiW3T7zyBImhsvlby1+LvO15RO2LKj9oFRMdw5qNazT0f+E0+FWNIiMj
mTdvHr1796b7HXfgHz8+OPz37pVlnnbtStfmz8PlktPA0dFw992Qn49t506GDhnCzOkziSKKbL7H
5EPgcxo1SsFur3n+bOPGYDfgRdPkk+xsYoF/AX3ssG4LmIUELfkYn4D9jAPv9IlyiKns8Tp1CZnz
Jve4b2cPJl+xDzcu3KX/AbJx/frr0sK4rE319OlSzlo59EF+zylT5JTqxo3y+zau7rK8Zma0yZIP
l3Du7Lnzf6EHWITMX3E4SrumGhL6ZVVF114rtfzh4ec9kf1c2nPcc/89FFU4JPeb3/yGyy+//Ae9
dvXzp8Gv/qOuXbvyj7Vr6dGrFz7DwOstXRw3TWmCFh8vJZ1JSdXfFWRlyWbiddfBl1/Kmnd0NLbE
RF5e+jZGqB1XCaWhfxPwedXnQLoh/G/pqN3cXMj3wEngMmSWVyywxgeLfDB3O7hKa9YigRgfbAtx
UGALLmQz7+qF2+dn8/wPeaP4NcYwni/YFQh9kINH8fFB30dxsSzh1CQ0VE7oFhTIe5OWFphNe9gO
bp9sK1Rnv7zooruLWL10NSDldzWep/aB4QNzzDhp/+B01lxPn5Nz3rsPvZK3Bg1+dUFuueUW8k+c
4MiRI7S+8UZc998Py5dLqNepI3+mTJEljorhn5UlywxPPSUboStWyJVzQkJ5a2Nz5078YydJGJY9
Vmnnac8emPgM3Ft6TivOhLZeWc6vWBVuB/oD/b3B3z8X2BpqBE7JnjkDn34qP8swyfPlcJrTvMDz
pJLKF3wRaCN9IS0sqmGz2Yjy+XABnmefLf2lbGB4ZQRuf6qG/yZgD1DPCW/ZKfYDERH4TRPD5aoy
7sBAapKMBg0obtfu/G0T9u2DtDSccXH8rmXLH/U7qV8HDX51wSIiIkhKSuKDd9+lx733UjRokFyC
Z2XJVWZcnNT4Vwyfc+ekrUOzZtK58fHHq54Ibt0a0ibB2LvA/SHQki1bbNx3n6yQlIX+4mKo3Ity
MvAa1RefVOa9/nq5Es7Pl5r2xESpwjFNin97DYO+GMrr7pfpQQ++4qtA8OfnyxyCpCTZiK5cslqD
kJAQnh83jmHDhrFlyxY6deoCvAnOQRBXLEs0bSp8w3fAbsARDnVaQ0qFKqkDBzCnT8fpdpdP1TWR
uwAjLo7i2bOrD/2CAvj6aynlnD4dR3Q0/Xv2ZMyomkdkql8/repRP8qmTZsk/O+8U0LfNGHzZlnL
nzAh0KUxLEzC/6mnZHrU0KE1P+mcufB2M2AisJjIyEFMnOjixQnVh36Z8cB8ZDZIdYsYJvCI3c7b
PXpQUtYM7fe/D7QLLmWseY/o1xfysPs+FrCAIio0hHM6ZSiNacKGDXL4KyZG7mZs1ZyDzM4mYuRI
lmdk8Mc//pH9+/fTrFlzZFF+ITj7w7XANwZE1oKrroZQJ5w8LXdPo0dTZWf744/hz38mzOvFbhj4
TRPT76c4Jkbe38r7DQUF8nhp507DMBjw0ENkzJpVbf8hZR0a/OpHy8zMZPGyZeX/Ligo4J1Vq/DE
xZVPvgJgxw7qxseTO3y49PipyYIF8FYTJPgBFuN0DqSZu4Td53kdpQsojAKmEBz+JjAcmF+vHkWv
vSYVLtWEfhljzXuEvf4GeL24zELw+8u7VkbWro0rNhaby0VJcbGslV93nYR0xfDPziYiJYUpo0cz
bMgQAE6cOEG9xKbYeRIv0wCnDJHv0EHaStts0l1069bAhKzqrF8vTdYmT5Z/v/SSnCd46y3ZRC7b
uDZNWLhQlt2ys2HbNubNnMmjjz6qoa90qUf9eO3bt6d9pc3cSePGMXbsWIorVPl0mzKF+cuWkfuD
f0J3/O7aOMgDztMzp9RMux23z8e9FR5bBLxls1FUUiJXvnl5NYY+gHnH7ZQsWoJxeUM4tB/buXOE
2Gw89thj5OfnM2DAAEJCQvj000/Jzc1l+dq1HBs3Dl+TJuWbpuH/+ldQ6AMkJCTw+mvTGDJkFA4T
vCSC0x0IfZABKQ0b1hz6IGtfphnot2OzydJZerqMVVyxIjCQpqQEli3DCAtj7l//ymOPPvof30Nl
DRr86r/qyiuvZFmFu4AyC955J7iHS3XOnEF2N0cBLpx0pAMtKCaTCwn+op49mbduHQsSE+WU6okT
eJ1OiuLipHPk8OHSOmH7djnJ2qpVtcs0PpsfBj4s5w2mTaNb584kJCQwc+bM8qvlzp07AzBp0iRm
z54d9EHX8t57ubN0+HtFTwweDFAa/o3wOnKqXyb6IUpKpEoqMVHOFsTESAXVqlWwejVOn4+5M2bQ
7+GH/38/R/2qaPCri2JiSgq9BwzAlZgoG72Vvfc+/PNDCDMw3FEYhkmEP5Z7GcKLbOU0EF/1uwDZ
Dw0BPGFhFCYkyDJISor0oO/WTTagJ0yQAfEej2zQ5uTIMk1yctXwNU0ZNB8RQXhEBL1796Zv377V
/WgiIyMZOXLkBb8PTwwejDMsjCmTJ3OgqMookwufogXSXTQnR9pl+HxyN/Pcc7BmDbalS6l72WVM
T0uj7/lOVCtL0u6c6qLo2bMnSzIyCB87VqpMKnrvPfjrTAh1Q6dibr3Nx4IFfqIiDJJI4ka604Uw
TlfzvLuB7kBbm02WWnw+Cf1Bg4JDf9w4qSqaNUvWxefMkSvkV14JLtc8e1ZaNc+aBUCjK66oMfR/
rAEDB7Jm/XrCHY7g1s6NG8OWLfK6quPxwOLF0h7i++/l9+zcWU4Hr1snG+vPPEODDRs49OWX5Bw6
pKGvqqXBry6aXr16sSQjA8eIEVKB8oc/SA//hQul9/+Nt8JnDj7dHpiTbmDwJCO4im50IYwdwK7S
P+uBjkAn4PPYWKm08Xik7LJVK3jgATk8dfasjGbs2TPQKjkiAqZOlZCdPVseO3tWvr5TJwnRM2eI
K6v7/y9r2rQp1zVvTtjUqYHwb91aWkCkpFQNf49H7mQKCqBrVxg6FNvx44SsX49zzBjW/f3v+P1+
/H4/R7/5hoYVJ3ApVYlW9aiLzu12s3DRIoamplL8/PPSB8hul2WM6VOxbV1PtB1shZEsLVmJEycm
JguYzadsCXquLE7iiI3GNXy4tFEo6xmUlQX33w8V19p375alkEmTAu0MDhyQx9LS5G+XS9bI+/Yl
1OHgveXLubW6tgz/BS6Xi649evCZw0HxqFGBTd116+SO46abAu/LgQPYs7O56uqrwTC4tWNHRqek
YBgGERERxMTE/CSvUf06afCrS2bR4sX8KTk56ECUeegQUfm5nHKdI6LQy5X+K3nROx1npSOuhRQy
jGEcDzlBcfJTMHeulJDGxsqJ3AED4K67qv7QXbsk+MvC/9Ah2fT1+aSiJjYWxoyB++7jhjZt2P7x
xz/pe+Byueh6++189vnn2EpbF3vdbsKcTmrFx5dvJjesX5/316whMjLyJ309yho0+NUltXXrVr76
6qvyf4eFhVG/fn3u6NOHol534vxgI1dlR5Pum1oe/oUUMpThfBd2Ek90mByuSk6WK+Vvv5Wh5cnJ
Nf/QDz+UKVhTp0rwP/ecrJNnZUkPnlatYNUqbuvUiQ9WrPip3wJ8Ph85QYNhoH79+lpvr34yWtWj
Lqmbb76Zm2++ucrjs9LTeSIlBdcLL7D/rWX8YUvwud2QHnfheXpIoCLH45ElGtMMNEOrSa1agQ3d
vLzAc5w5A4WFUh7Zp4+0ML4I7HY7Dcq6fip1EWjwq5+lsrrzJ0aOxNepE47OnfFu3y4bnK1bB1f1
ezxStRMbKyMgL9T+/dJY7umn5cp/3z55jhkzYOtWHOc7SKXUL5gGv/rZ6vfwwzSoX5//Le3FfLBF
C2ZPnIjvmWegrEe8aUqvfLcbHnkEli4NLpGsjs8nm7ipqbIk1LYtLFsm5ZSTJkFWFlHLljFh3bqf
9PdT6lLRNX71i7J582Z69e3LmXPnMOPiJMRPn5aum16vDCMpKpIKn2uuqfoEp07B4MFSujl6tAyR
GTNGzgCkpcHOnUS9/DIb33+ftm3bXvxfUKmLQINf/eKYpskzo0cza+VKijp2lKks33yDceIE4aZJ
nbg4vsvNxZ+eHhz+p05Jd9DmzWXwOcDq1bLE43ZjGAZRtWqx4YMPNPTVr5oGv/pFMk2TN954g4NZ
WeWPRUdFkZycTFhYGGvXruX+fv2wN2qEx+OhxOOBnBwM08QWEYFZXEzL5s35n3bt+Mu0aYSUllIq
ZQUa/OpX6+uvv+ZYaWXO4cOHMU2TpKQkQLplNm3a9FK+PKUuGQ1+pZSyGO3Vo5RSFqPBr5RSFqPB
r5RSFqPBr5RSFqPBr5RSFqPBr5RSFqPBr5RSFqPBr5RSFqPBr5RSFqPBr5RSFqPBr5RSFqPBr5RS
FqPBr5RSFqPBr5RSFqPBr5RSFqPBr5RSFqPBr5RSFqPBr5RSFqPBr5RSFqPBr5RSFqPBr5RSFqPB
r5RSFqPBr5RSFqPBr5RSFqPBr5RSFqPBr5RSFqPBr5RSFqPBr5RSFqPBr5RSFqPBr5RSFqPBr5RS
FqPBr5RSFqPBr5RSFqPBr5RSFqPBr5RSFqPBr5RSFqPBr5RSFqPBr5RSFqPBr5RSFqPBr5RSFqPB
r5RSFqPBr5RSFqPBr5RSFqPBr5RSFqPBr5RSFqPBr5RSFqPBr5RSFqPBr5RSFqPBr5RSFqPBr5RS
FqPBr5RSFqPBr5RSFqPBr5RSFqPBr5RSFqPBr5RSFqPBr5RSFqPBr5RSFqPBr5RSFqPBr5RSFqPB
r5RSFqPBr5RSFvN/TMb2loIdRAcAAAAASUVORK5CYII=
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
89ivXz9WVFRc9F6oxddut7NHjx7MyspyvXb69GmqLxil+jP6VgP8xYd9DgCM12hECFkg8AIhvo2E
zZs3s23btm4f+L7w8ccf02q18tVXX2VZWRnXrl3LlJQUpqWlcejQoVSr1VQqFIxRKPxK8Op61VU8
ceJEkK46MN59990a2b/BoqKign379uX9999/0Xuhnjf/9NNPmZycXON38d///pdWSQq4A5AAMLeO
OmCXStwSCC53hPg2AiorK5mWlsY333wzKMf7/vvvGRERQZPJxL59+/Kjjz5yJers27eP3bp1ow6g
ueph6lXIUamkNSKCt956K2NjY/n+++8Hpa2BMGnSJC5btqxOjv3nn38yNjaWH3zwwUXvhXLevF+/
flyzZk2N1x577DHGBDDf6xp9+yG+hOds7cZenlIgCCZCfBsBGzdu5FVXXeV2eZAvnD59mo8++iij
oqI4aNAgtm7dmhMmTHA98C5MrlkPMBpgf8BjgldfvZ46SeKsu+7iihUr2KRJE65cuZJNmzbl9OnT
efbs2WDcAp8pLy+nxWLh/v376+wcn3/+OaOjo5mXl1fj9fXr17N3WJjfouftvPmWLVuYmJh4kYHK
6NGjqZHLAx99AywIUufhcilPKRAECyG+DZzy8nImJyfzo48+8vsYR44c4Zw5cxgZGcmbb76Zv/76
K0myuLiYw4cPZ9++ffnEI4+4Ta6xAcwEmFH1ME6EIxypBmiSJD7zzDP86quvGBUVxby8PL7++uu0
Wq185513OG7cOLZp04bbtm0L1u3wms8++4ydOnWq8/M88cQT7NGjh0sAv/76a3bv3p06mazO582H
DBnCF154ocZrdrudcXFx7NqmTeCj70CEu1rY/HIrTykQBAMhvg2cVatWsU+fPn6Nevft28epU6cy
PDycd9xxB//444+LPlNRUcFrr72WVkm65BxvARxhyFw4EnGi5XKOHTOGJPnoo4+yT58+rKiocMw5
Wq3ctGkTN2zYQKvVysceeyzg+WpfmDlzJh955JE6P09lZSWvu+46TpgwgSNGjGBCQgJffvllbli/
vk7tJbdv387Y2NiLLDP37dvHuLg4rl+/PjCjj6pOl7/7OxPG6sNmUyBoDAjxbSC4S0ApKSlhQkIC
t2zZ4tOxfvrpJ/7tb3+j2WzmvHnzas32DdQKUStJLC0tZUVFBf/yl7/wiSeeIOlYSxwTE8PVq1e7
zD169eoVEucru93OhIQE1wi/Ljl69CgnTpxImUzG8ePH89y5c6736nLEN2rUKLfz2atWreK4ceMC
t7iEI+oRiPj+/vvvwudZIPCAEN965FIJKDfddBOHDBni9fG++uorDh48mDExMVy4cKHH9ZbVCUbh
hqSkJP744488cOAArVYrv//+e5Lknj17mJiYyIULF7KyspJLliyhxWLhmjVraozkg535+sMPPzA5
OTngOfLaOHPmDB966CFGRkZy1qxZ/Oijj2ixWPi///2vxuecc521uTz1VCp9muvctWsXo6KiXEYW
1bnppptc65r9HXVaAL4agPCWAdTK5Vy1alXIbTYFgsaCEN96wpsElG6SRKtOV+tD2W6387333mN6
ejpbtGjBF154wafqPcHIzDVJEiMiIjh69GguW7aMrVq14pkzZ0iShw4dYkpKCu+55x7a7Xbu3LmT
HTp04PDhw7ly5co6yXydO3cu7733Xr/2vRTl5eWuxLK//e1vNUbyzzzzDFNTU2uMfsmLXZ7i1GpG
KxTUKZXs2qYNw8PDL9qnNsaPH8/HH3/8otedI/49e/a4Xvvn3XfTAu+z1hO0WraIigr4NxEpSWzT
pMll5ZYmEAQTIb71QDDCkeXl5dywYQM7duzIjh07csOGDSwvL/epHcGyQlTBMfpt0aIFw8PD2apV
K46pmgsmyVOnTrF79+6cMGECy8vLuW7dOppUKnaXpDrJfG3Tpg23bt3q8361Ybfb+dZbb7F169bs
27cvf/zxR7efufHGGzl58mSPxykoKODChQs5atQo1yi/c+fO/OSTT7xqx759+2ixWNxGNXJzcxkT
E+Ma8R87doyJiYkcNnQodTKZVx7LTzz+OCMjI5muUvk/YgW4CAiK0UdD8gkXCIKJEN8QE2gCSklJ
CVesWMEWLVqwV69efPfdd/0OrwbLjSlKJuPq1au5YsUKRkdHs23btpQkiUOHDnUZbhQXF/Oaa65h
x5SUOs18/e233xgXF+dV9SFv+fbbb5mens727dtz8+bNtd7voqIiJicn13Aiu5AXXniBU6ZMcf29
ZMkS3nrrrV61ZfLkyXzggQfcvvfSSy9x7NixJB2j7YyMDN57771s2bIl33777Ys8lmNVKobJZC5b
0g0bNtBisTCzKioTyHzx7wCbBvi7IhpehSyBIFgI8Q0hgSbBRKjVjImJ4eDBg/nVV18F1JYzZ87w
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
Cgp49OhR1q5dm05OTszNzSVJHj9+nBqNhvv376dardYf++LFi2zVqhV79uzJ7Oxsnjp1ih4eHgb3
of9u3759rFWrlkEbQiGEqAgJvtWIKVqt1VKr6WRjwzALizInauXn53PgwIFs2bIlr127ph+PTqdj
37596erqSjc3N/7rX//irVu3DMb8888/08/Pj8HBwXzppZf0j69atYqenp5MTU2lr68vd+/ezWbN
mhncd50yZQrbtWtHhUJBkkxKSmKvXr0YFhbG//73v/rtZs2axXbt2tHR0dHg3Lm5uYyPj2dAQABP
nDhBHx8fpqamPvQ97tGjB//973+X8zsjhBCGJPhWE5mZmVTa2BgEy/J+/fve/dPyJGr96/33+fzz
z7Nr1668ffu2fjz79+9n/fr1aW1tzZkzZxo8R5IFBQWcPHky3d3dOXPmTHp6evLGjRskyU2bNtHN
zY2HDh3i8uXLGRkZyS+//JLNmzc3yDju1q0bg4OD6enpSbK4F++0adM4depUjh071uBcoaGhtLKy
euB7l5iYSK1Wy+eee44LFix46Pt8+PBhurm5GfQFFkKI8pLgW02cOXOGfkZccl4F0Pte8lV5ErW0
FhZs9+yz+ozmffv2sUuXLnRycqK7u/sDM4jPnDnDsLAwduzYkadPn2bt2rW5fv16ksUzYY1Gw927
d7OoqIgNGzbkxo0b6ePjw507dxocp2bNmlQqlWzZsiVJsmvXrkxOTua+ffsYFBRksO2BAwcIgH/+
+ecD37/du3fTxcWFAQEBD730TJIvvfQSp0+fXrZvjBBCPIAE32rCmOCbC9AdqHCilruTE7dv386O
HTvS29ubcXFx9PPzKxHodDodV6xYQY1Gw48//phFRUUcNWoU+/fvT5I8ePAgtVotN2/eTJJcs2YN
W7Rowffff589e/Y0ONaFCxfo5OREb29v9urViyTp7e3NM2fOsLCwkGq1munp6Qb7WN3LhC4tuKak
pNDKyooxMTElLo//1alTp6hWq/UZ2kIIUV4SfKuJ+5ed8ysQQFcCjDLicnWYlRU1Gg0XL17MZcuW
0cvLyyADmiRv3rzJuLg4BgQE8ODBgyTJHTt20NPTkxkZGTx58iQ9PDy4evVqksWBukmTJvz888+p
Vqt58uRJg+OtX7+edevWZfv27fnaa6/xxo0bdHR01F+W7tu3L5csWWKwj0qlYoMGDfj111+X+j7W
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
