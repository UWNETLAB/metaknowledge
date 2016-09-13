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
<p><em>metaknowledge</em> is a python library for creating and analyzing scientific metadata. It uses records obtained from Web of Science (WOS), Scopus and other sources. As it is intended to be usable by those who do not know much python. This page will be a short overview of its capabilities, to allow you to use it for your own work. For complete coverage of the package as well as install instructions read the full the documentation <a href="{{ site.baseurl }}/documentation">here</a>.</p>

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
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">import</span> <span class="nn">metaknowledge</span> <span class="k">as</span> <span class="nn">mk</span>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">import</span> <span class="nn">networkx</span> <span class="k">as</span> <span class="nn">nx</span>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">import</span> <span class="nn">matplotlib.pyplot</span> <span class="k">as</span> <span class="nn">plt</span>
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
<p><em>metaknowledge</em> also has a <em>matplotlib</em> based graph <a href="{{ site.baseurl }}/documentation/metaknowledgeFull.html#contour">visualizer</a> that we will use, the module also contains the titular contour plot generator</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[4]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">import</span> <span class="nn">metaknowledge.contour</span> <span class="k">as</span> <span class="nn">mkv</span>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">import</span> <span class="nn">pandas</span>
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
<h1 id="Reading-Files">Reading Files<a class="anchor-link" href="#Reading-Files">&#182;</a></h1><p>The files used here are for WOS, but the instructions apply to any of the sources. fRecords can be loaded into a <a href="{{ site.baseurl }}/docs/RecordCollection#RecordCollection"><code>RecordCollections</code></a> by creating a <code>RecordCollection</code> with the path to the files given to it as a string.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[6]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">RC</span> <span class="o">=</span> <span class="n">mk</span><span class="o">.</span><span class="n">RecordCollection</span><span class="p">(</span><span class="s2">&quot;savedrecs.txt&quot;</span><span class="p">)</span>
<span class="n">RC</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt output_prompt">Out[6]:</div>


<div class="output_text output_subarea output_execute_result">
<pre>&lt;metaknowledge.RecordCollection object savedrecs&gt;</pre>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">RC</span> <span class="o">=</span> <span class="n">mk</span><span class="o">.</span><span class="n">RecordCollection</span><span class="p">(</span><span class="s2">&quot;.&quot;</span><span class="p">)</span>
<span class="nb">repr</span><span class="p">(</span><span class="n">RC</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt output_prompt">Out[7]:</div>


<div class="output_text output_subarea output_execute_result">
<pre>&#39;&lt;metaknowledge.RecordCollection object files-from-.&gt;&#39;</pre>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">RC</span> <span class="o">=</span> <span class="n">mk</span><span class="o">.</span><span class="n">RecordCollection</span><span class="p">(</span><span class="s2">&quot;.&quot;</span><span class="p">,</span> <span class="n">extension</span> <span class="o">=</span> <span class="s2">&quot;txt&quot;</span><span class="p">)</span>
<span class="nb">repr</span><span class="p">(</span><span class="n">RC</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt output_prompt">Out[8]:</div>


<div class="output_text output_subarea output_execute_result">
<pre>&#39;&lt;metaknowledge.RecordCollection object txt-files-from-.&gt;&#39;</pre>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="nb">print</span><span class="p">(</span><span class="s2">&quot;RC is a &quot;</span> <span class="o">+</span> <span class="nb">str</span><span class="p">(</span><span class="n">RC</span><span class="p">))</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt"></div>
<div class="output_subarea output_stream output_stdout output_text">
<pre>RC is a RecordCollection(txt-files-from-.)
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
<h1 id="Record-object"><code>Record</code> object<a class="anchor-link" href="#Record-object">&#182;</a></h1><p><a href="{{ site.baseurl }}/docs/Record#Record"><code>Record</code></a> is an object that contains a simple record, for example a journal article, book, or conference proceedings. They are what <a href="{{ site.baseurl }}/docs/RecordCollection#RecordCollection"><code>RecordCollections</code></a> contain. To see an individual <a href="{{ site.baseurl }}/docs/Record#Record"><code>Record</code></a> at random from a <code>RecordCollection</code> you can use <code>peek()</code></p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[10]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">R</span> <span class="o">=</span> <span class="n">RC</span><span class="o">.</span><span class="n">peek</span><span class="p">()</span>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="nb">print</span><span class="p">(</span><span class="n">R</span><span class="p">[</span><span class="s1">&#39;authorsFull&#39;</span><span class="p">])</span>
<span class="nb">print</span><span class="p">(</span><span class="n">R</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s1">&#39;AF&#39;</span><span class="p">))</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt"></div>
<div class="output_subarea output_stream output_stdout output_text">
<pre>[&#39;RIGNEAULT, H&#39;, &#39;FLORY, F&#39;, &#39;MONNERET, S&#39;]
[&#39;RIGNEAULT, H&#39;, &#39;FLORY, F&#39;, &#39;MONNERET, S&#39;]
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="nb">print</span><span class="p">(</span><span class="n">R</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt"></div>
<div class="output_subarea output_stream output_stdout output_text">
<pre>WOSRecord(NONLINEAR TOTALLY REFLECTING PRISM COUPLER - THERMOMECHANIC EFFECTS AND INTENSITY-DEPENDENT REFRACTIVE-INDEX OF THIN-FILMS)
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
<p>If you try to access a tag the <code>Record</code> does not have it will raise a KeyError unless <code>get()</code> is used</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[13]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="k">try</span><span class="p">:</span>
    <span class="nb">print</span><span class="p">(</span><span class="n">R</span><span class="p">[</span><span class="s1">&#39;GP&#39;</span><span class="p">])</span>
<span class="k">except</span> <span class="ne">KeyError</span> <span class="k">as</span> <span class="n">k</span><span class="p">:</span>
    <span class="nb">print</span><span class="p">(</span><span class="n">k</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt"></div>
<div class="output_subarea output_stream output_stdout output_text">
<pre>&#34;&#39;GP&#39; could not be found in the Record&#34;
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
<p>There are two ways of getting a tag, one is using the sources names, in this case WOS 2 letter abbreviations and the second is to use the human readable name. There is no standard for the human readable names, so they are specific to <em>metaknowledge</em>. They are: <code>'year'</code>, <code>'volume'</code>, <code>'beginningPage'</code>, <code>'DOI'</code>, <code>'address'</code>, <code>'j9'</code>, <code>'citations'</code>, <code>'grants'</code>, <code>'selfCitation'</code>, <code>'authorsShort'</code>, <code>'authorsFull'</code>, <code>'title'</code>, <code>'journal'</code>, <code>'keywords'</code>, <code>'abstract'</code> and <code>'id</code>'.</p>
<p>To see how the WOS names map to the long names look at the complete <a href="{{ site.baseurl }}/docs/metaknowledgeFull.html#WOS">documentation</a>. If you want all the tags a <a href="{{ site.baseurl }}/documentation/metaknowledgeFull.html#Record"><code>Record</code></a> has use <code>keys()</code> like a <code>dict</code>.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[14]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="nb">print</span><span class="p">(</span><span class="nb">list</span><span class="p">(</span><span class="n">R</span><span class="o">.</span><span class="n">keys</span><span class="p">()))</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt"></div>
<div class="output_subarea output_stream output_stdout output_text">
<pre>[&#39;PT&#39;, &#39;AU&#39;, &#39;AF&#39;, &#39;TI&#39;, &#39;SO&#39;, &#39;LA&#39;, &#39;DT&#39;, &#39;DE&#39;, &#39;ID&#39;, &#39;AB&#39;, &#39;RP&#39;, &#39;CR&#39;, &#39;NR&#39;, &#39;TC&#39;, &#39;Z9&#39;, &#39;PU&#39;, &#39;PI&#39;, &#39;PA&#39;, &#39;SN&#39;, &#39;J9&#39;, &#39;JI&#39;, &#39;PD&#39;, &#39;PY&#39;, &#39;VL&#39;, &#39;IS&#39;, &#39;BP&#39;, &#39;EP&#39;, &#39;PG&#39;, &#39;WC&#39;, &#39;SC&#39;, &#39;GA&#39;, &#39;UT&#39;, &#39;PM&#39;]
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="k">for</span> <span class="n">R</span> <span class="ow">in</span> <span class="n">RC</span><span class="p">:</span>
    <span class="nb">print</span><span class="p">(</span><span class="n">R</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt"></div>
<div class="output_subarea output_stream output_stdout output_text">
<pre>WOSRecord(NONLINEAR TOTALLY REFLECTING PRISM COUPLER - THERMOMECHANIC EFFECTS AND INTENSITY-DEPENDENT REFRACTIVE-INDEX OF THIN-FILMS)
WOSRecord(WHY ENERGY FLUX AND ABRAHAMS PHOTON MOMENTUM ARE MACROSCOPICALLY SUBSTITUTED FOR MOMENTUM DENSITY AND MINKOWSKIS PHOTON MOMENTUM)
WOSRecord(SHIFTS OF COHERENT-LIGHT BEAMS ON REFLECTION AT PLANE INTERFACES BETWEEN ISOTROPIC MEDIA)
WOSRecord(RESONANCE EFFECTS ON TOTAL INTERNAL-REFLECTION AND LATERAL (GOOS-HANCHEN) BEAM DISPLACEMENT AT THE INTERFACE BETWEEN NONLOCAL AND LOCAL DIELECTRIC)
WOSRecord(Goos-Hanchen shift as a probe in evanescent slab waveguide sensors)
WOSRecord(Transverse displacement at total reflection near the grazing angle: a way to discriminate between theories)
WOSRecord(GENERAL STUDY OF DISPLACEMENTS AT TOTAL REFLECTION)
WOSRecord(SPIN ANGULAR-MOMENTUM OF A FIELD INTERACTING WITH A PLANE INTERFACE)
WOSRecord(Numerical study of the displacement of a three-dimensional Gaussian beam transmitted at total internal reflection. Near-field applications)
WOSRecord(THEORETICAL NOTES ON AMPLIFICATION OF TRANSVERSE SHIFT BY TOTAL REFLECTION ON MULTILAYERED SYSTEM)
WOSRecord(MECHANICAL INTERPRETATION OF SHIFTS IN TOTAL REFLECTION OF SPINNING PARTICLES)
WOSRecord(Goos-Hanchen and Imbert-Fedorov shifts for leaky guided modes)
WOSRecord(ASYMMETRICAL MOMENTUM-ENERGY TENSORS AND 6-COMPONENT ANGULAR-MOMENTUM IN PROBLEM CONCERNING 2 PHOTON MOMENTA AND MAGNETODYNAMIC EFFECT PROBLEM)
WOSRecord(ANGULAR SPECTRUM AS AN ELECTRICAL NETWORK)
WOSRecord(TRANSVERSE DISPLACEMENT OF A TOTALLY REFLECTED LIGHT-BEAM AND PHASE-SHIFT METHOD)
WOSRecord(OBSERVATION OF SHIFTS IN TOTAL REFLECTION OF A LIGHT-BEAM BY A MULTILAYERED STRUCTURE)
WOSRecord(LONGITUDINAL AND TRANSVERSE DISPLACEMENTS OF A BOUNDED MICROWAVE BEAM AT TOTAL INTERNAL-REFLECTION)
WOSRecord(Optical properties of nanostructured thin films)
WOSRecord(PREDICTION OF A RESONANCE-ENHANCED LASER-BEAM DISPLACEMENT AT TOTAL INTERNAL-REFLECTION IN SEMICONDUCTORS)
WOSRecord(EXCHANGED MOMENTUM BETWEEN MOVING ATOMS AND A SURFACE-WAVE - THEORY AND EXPERIMENT)
WOSRecord(A Novel Method for Enhancing Goos-Hanchen Shift in Total Internal Reflection)
WOSRecord(DISCUSSIONS OF PROBLEM OF PONDEROMOTIVE FORCES)
WOSRecord(CALCULATION AND MEASUREMENT OF FORCES AND TORQUES APPLIED TO UNIAXIAL CRYSTAL BY EXTRAORDINARY WAVE)
WOSRecord(Longitudinal and transverse effects of nonspecular reflection)
WOSRecord(Simple technique for measuring the Goos-Hanchen effect with polarization modulation and a position-sensitive detector)
WOSRecord(INTERNAL PHOTON IMPULSE OF DIELECTRIC AND ON COUPLE APPLIED TO ANISOTROPIC CRYSTAL)
WOSRecord(DISPLACEMENT OF A TOTALLY REFLECTED LIGHT-BEAM - FILTERING OF POLARIZATION STATES AND AMPLIFICATION)
WOSRecord(CONSERVATION OF ANGULAR MOMENT WITH SIX COMPONENTS AND ASYMMETRICAL IMPULSE ENERGY TENSORS)
WOSRecord(SPIN ANGULAR-MOMENTUM OF A FIELD INTERACTING WITH A PLANE INTERFACE)
WOSRecord(Experimental observation of the Imbert-Fedorov transverse displacement after a single total reflection)
WOSRecord(INTERFERENCE THEORY OF REFLECTION FROM MULTILAYERED MEDIA)
WOSRecord(EXPERIMENTS IN PHENOMENOLOGICAL ELECTRODYNAMICS AND THE ELECTROMAGNETIC ENERGY-MOMENTUM TENSOR)
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
<p>The individual <code>Records</code> are index by their id numbers so you can access a specific one in the collection if you know its number.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[16]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">RC</span><span class="o">.</span><span class="n">getID</span><span class="p">(</span><span class="s2">&quot;WOS:A1979GV55600001&quot;</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt output_prompt">Out[16]:</div>


<div class="output_text output_subarea output_execute_result">
<pre>&lt;metaknowledge.WOSRecord object WOS:A1979GV55600001&gt;</pre>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">Cite</span> <span class="o">=</span> <span class="n">R</span><span class="o">.</span><span class="n">createCitation</span><span class="p">()</span>
<span class="nb">print</span><span class="p">(</span><span class="n">Cite</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt"></div>
<div class="output_subarea output_stream output_stdout output_text">
<pre>BREVIK I, 1979, PHYS REP, V52, P133, DOI 10.1016/0370-1573(79)90074-7
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">RCfiltered</span> <span class="o">=</span> <span class="n">mk</span><span class="o">.</span><span class="n">RecordCollection</span><span class="p">()</span>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="k">for</span> <span class="n">R</span> <span class="ow">in</span> <span class="n">RC</span><span class="p">:</span>
    <span class="k">if</span> <span class="n">R</span><span class="p">[</span><span class="s1">&#39;title&#39;</span><span class="p">][</span><span class="mi">0</span><span class="p">]</span> <span class="o">==</span> <span class="s1">&#39;A&#39;</span><span class="p">:</span>
        <span class="n">RCfiltered</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">R</span><span class="p">)</span>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="nb">print</span><span class="p">(</span><span class="n">RCfiltered</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt"></div>
<div class="output_subarea output_stream output_stdout output_text">
<pre>RecordCollection(Empty)
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
<p>One note about implementing this, the above code does not handle the case in which the title is missing i.e. <code>R['title']</code> is missing. You will have to deal with this on your own.</p>

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
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">RC70</span> <span class="o">=</span> <span class="n">RC</span><span class="o">.</span><span class="n">yearSplit</span><span class="p">(</span><span class="mi">1970</span><span class="p">,</span> <span class="mi">1979</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">RC70</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt"></div>
<div class="output_subarea output_stream output_stdout output_text">
<pre>RecordCollection(txt-files-from-.(1970-1979))
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">RCintroOpt</span> <span class="o">=</span> <span class="n">RC</span><span class="o">.</span><span class="n">localCitesOf</span><span class="p">(</span><span class="s2">&quot;Yariv A., 1971, INTRO OPTICAL ELECTR&quot;</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">RCintroOpt</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt"></div>
<div class="output_subarea output_stream output_stdout output_text">
<pre>RecordCollection(Records_citing_Yariv A., 1971, INTRO OPTICAL ELECTR)
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
<div class=" highlight hl-ipython3"><pre><span></span> <span class="n">RCfiltered</span><span class="o">.</span><span class="n">writeFile</span><span class="p">(</span><span class="s2">&quot;Records_Starting_with_A.txt&quot;</span><span class="p">)</span>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">selectedTags</span> <span class="o">=</span> <span class="p">[</span><span class="s1">&#39;TI&#39;</span><span class="p">,</span> <span class="s1">&#39;UT&#39;</span><span class="p">,</span> <span class="s1">&#39;CR&#39;</span><span class="p">,</span> <span class="s1">&#39;AF&#39;</span><span class="p">]</span>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">RCfiltered</span><span class="o">.</span><span class="n">writeCSV</span><span class="p">(</span><span class="s2">&quot;Records_Starting_with_A.csv&quot;</span><span class="p">,</span> <span class="n">onlyTheseTags</span> <span class="o">=</span> <span class="n">selectedTags</span><span class="p">)</span>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">recDataFrame</span> <span class="o">=</span> <span class="n">pandas</span><span class="o">.</span><span class="n">DataFrame</span><span class="p">(</span><span class="n">RC</span><span class="o">.</span><span class="n">makeDict</span><span class="p">())</span>
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
<p>To make a basic co-citation network of Records use <a href="{{ site.baseurl }}/docs/RecordCollection#networkCoCitation"><code>networkCoCitation()</code></a>.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[27]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">coCites</span> <span class="o">=</span> <span class="n">RC</span><span class="o">.</span><span class="n">networkCoCitation</span><span class="p">()</span>
<span class="nb">print</span><span class="p">(</span><span class="n">mk</span><span class="o">.</span><span class="n">graphStats</span><span class="p">(</span><span class="n">coCites</span><span class="p">))</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt"></div>
<div class="output_subarea output_stream output_stdout output_text">
<pre>The graph has 571 nodes, 17663 edges, 0 isolates, 25 self loops, a density of 0.108538 and a transitivity of 0.684276
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
<p><a href="{{ site.baseurl }}/documentation/metaknowledgeFull.html#graphStats"><code>graphStats()</code></a> is a function to extract some of the statists of a graph and make them into a nice string.</p>
<p><code>coCites</code> is now a <a href="https://networkx.github.io/documentation/networkx-1.9.1/"><em>networkx</em></a> graph of the co-citation network, with the hashes of the <code>Citations</code> as nodes and the full citations stored  as an attributes. Lets look at one node</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[28]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">coCites</span><span class="o">.</span><span class="n">nodes</span><span class="p">(</span><span class="n">data</span> <span class="o">=</span> <span class="kc">True</span><span class="p">)[</span><span class="mi">0</span><span class="p">]</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt output_prompt">Out[28]:</div>


<div class="output_text output_subarea output_execute_result">
<pre>(&#39;Zeroug S, 1994, J ACOUST SOC AM&#39;,
 {&#39;MK-ID&#39;: &#39;None&#39;,
  &#39;count&#39;: 1,
  &#39;inCore&#39;: False,
  &#39;info&#39;: &#39;Zeroug S, 1994, J ACOUST SOC AM, V95, P3075&#39;})</pre>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">coCites</span><span class="o">.</span><span class="n">edges</span><span class="p">(</span><span class="n">data</span> <span class="o">=</span> <span class="kc">True</span><span class="p">)[</span><span class="mi">0</span><span class="p">]</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt output_prompt">Out[29]:</div>


<div class="output_text output_subarea output_execute_result">
<pre>(&#39;Zeroug S, 1994, J ACOUST SOC AM&#39;,
 &#39;Zhang Sz, 1989, J OPT SOC AM A&#39;,
 {&#39;weight&#39;: 1})</pre>
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
<p>The <code>networkCoCitation()</code> function has many options for filtering and determining the nodes. The default is to use the <code>Citations</code> themselves. If you wanted to make a network of co-citations of journals you would have to make the node type <code>'journal'</code> and remove the non-journals.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[30]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">coCiteJournals</span> <span class="o">=</span> <span class="n">RC</span><span class="o">.</span><span class="n">networkCoCitation</span><span class="p">(</span><span class="n">nodeType</span> <span class="o">=</span> <span class="s1">&#39;journal&#39;</span><span class="p">,</span> <span class="n">dropNonJournals</span> <span class="o">=</span> <span class="kc">True</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">mk</span><span class="o">.</span><span class="n">graphStats</span><span class="p">(</span><span class="n">coCiteJournals</span><span class="p">))</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt"></div>
<div class="output_subarea output_stream output_stdout output_text">
<pre>The graph has 89 nodes, 1379 edges, 0 isolates, 41 self loops, a density of 0.352145 and a transitivity of 0.635939
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">nx</span><span class="o">.</span><span class="n">draw_spring</span><span class="p">(</span><span class="n">coCiteJournals</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt"></div>


<div class="output_png output_subarea ">
<img src="data:image/png;base64,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
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
<p>A bit basic but gives a general idea. If you want to make a much better looking and more informative visualization you could try <a href="https://briatte.github.io/ggnet/">R</a>, <a href="https://gephi.github.io/">gephi</a> or <a href="http://visone.info/">visone</a>. Exporting to them is covered below in <a href="#exporting-graphs"><strong>Exporting graphs</strong></a>.</p>
<h1 id="Making-a-citation-network">Making a citation network<a class="anchor-link" href="#Making-a-citation-network">&#182;</a></h1>
</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>The <a href="{{ site.baseurl }}/docs/RecordCollection#networkCitation"><code>networkCitation()</code></a> method is nearly identical to <code>coCiteNetwork()</code> in its parameters. It has one additional keyword argument <code>directed</code> that controls if it produces a directed network. Read <a href="{{ site.baseurl }}/examples/#Making-a-co-citation-network"><strong>Making a co-citation network</strong></a> to learn more about <code>networkCitation()</code>.</p>

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
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">citationsA</span> <span class="o">=</span> <span class="n">RC</span><span class="o">.</span><span class="n">networkCitation</span><span class="p">(</span><span class="n">nodeType</span> <span class="o">=</span> <span class="s1">&#39;year&#39;</span><span class="p">,</span> <span class="n">keyWords</span> <span class="o">=</span> <span class="p">[</span><span class="s1">&#39;A&#39;</span><span class="p">])</span>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">nx</span><span class="o">.</span><span class="n">draw_spring</span><span class="p">(</span><span class="n">citationsA</span><span class="p">,</span> <span class="n">with_labels</span> <span class="o">=</span> <span class="kc">True</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt"></div>


<div class="output_png output_subarea ">
<img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAeIAAAFBCAYAAACrYazjAAAABHNCSVQICAgIfAhkiAAAAAlwSFlz
AAALEgAACxIB0t1+/AAAIABJREFUeJzs3Xd8jWf/wPHPSUSSU1kIoYQaKbVaYq/E+EVJUkLVHlG7
NSrWU2o++sTuU5vWakqpoka1pfaMKmKU2CMIRYIMOTnf3x8n8iQkZJ3cSVzv1+u85NzzeyXH+d73
dV9DJyKCoiiKoiiasNA6AEVRFEV5nalErCiKoigaUolYURRFUTSkErGiKIqiaEglYkVRFEXRkErE
iqIoiqIhlYgVRVEURUMqESuKoiiKhlQiVhRFURQNqUSsKIqiKBpSiVhRFEVRNKQSsaIoiqJoSCVi
RVEURdGQSsSKoiiKoiGViBVFURRFQyoRK4qiKIqGVCJWFEVRFA2pRKwoiqIoGlKJWFEURVE0pBKx
oiiKomhIJWJFURRF0ZBKxIqiKIqiIZWIFUVRFEVDKhEriqIoioZUIlYURVEUDalErCiKoigaUolY
URRFUTSkErGiKIqiaEglYkVRFEXRkErEiqIoiqIhlYgVRVEURUMqESuKoiiKhlQiVhRFURQNqUSs
KIqiKBpSiVhRFEVRNKQSsaIoiqJoSCViRVEURdGQSsSKoiiKoiGViBVFURRFQyoRK4qiKIqGVCJW
FEVRFA2pRKwoiqIoGlKJWFEURVE0lE/rABRFSV14eDgrli3j/MmTPI6IoICDA25Vq9K9Z0+cnZ21
Dk9RlCygExHROghFUZILDg7mqy+/ZMsvv+AH1IyJwQ54BByxtWW9CK3ef5/Bo0dTs2ZNjaNVFCUz
VCJWlBxm0fz5jAsIYGR0NN1FcEphmwfAMp2Oqba2TJg+nT79+2d3mIqiZBGViBUlB1k0fz6BAQH8
GhVFuTRsfwHw0usZqZKxouRaqrGWomSzuXPnUrNmTWxsbPD3909cHhwczPAhQ4iPiqI60BK4lWS/
loAdYJ/wsgbaAr9GRTEuIIBNmzbRpEkT3njjDd555x127NiRfYVSFCXDVCJWlGz25ptvMnbsWHr1
6pVs+b8++wzj06dsA+4DpYGOSdZvxfSMODLhVQ9oD5QDRkRH49+jBzVq1OD+/ftMnjyZdu3a8c8/
/2RDiRRFyQyViBUlm7Vu3RpfX18KFiyYuCw8PJy9Bw/SAaiAqTvDWGAPcDmFY1wB9gJdE943EOHe
/fsMHDgQa2tr/Pz8qFq1KuvWrTNrWRRFyTzVfUlRcoAVy5ZRHlN18zPGhH9PAW89vz3QCHBNeH8T
cNTpWLd2LcOGDwegWrVqnD592nxBZzPVlUvJq1QiVpQc4PzJkzSNj2cV0A8oC0zEVGUVlcL2K4Ev
krx/DDiJcD4kJHGZvb09YWFh5gs6m7y0K9dPP+E2bpzqyqXkaqpqWlFygMcREdQExgN+QJmElx1Q
4rlt9wF3MDXUeqYA8BR49OBB4rKIiAjs7OzMF3Q2WDR/Pr4eHrhv2MClmBi+iYmhH9AZ0wXLt9HR
XIqJocaGDfh6eLBo/nyNI1aU9FOJWFFygAIODjwC+gPnMbWW9gMMQOXntl2RsE6fZFklIBywKVAg
cdmJEyeoVKmSGaM2r2ddufZGRTEklf7UAE7AUBH2RkURGBCgkrGS66hErCjZLD4+npiYGOLj4zEY
DMTGxlKucmUOWlvz7InuNaAPMARwSLJvDLAG6PncMcsDjhYWXL51i9jYWH766SdOnTpF27Ztycky
2pVrOlAFUzeusgnvy/G/rlzffPMNtWvXxt7ennfffZf9+/dnX6EUJZ1UIlaUbDZ58mT0ej2BgYEE
BQWh1+v558EDNgIfYaqOrgPUx/ScOKkNmO4AGz+3/D4Qa2VFnMGAk5MTn3/+OevWraNQoULmLk6m
ZLQrF5iekz8EfgHmYLpAKQd8EhXFwAEDGDlyJBEREQwfPhwfHx8iIiLMXRxFyRA1spai5BBd/Pxw
37CBIRn4LzlLp+NYmzaszKXdlcaOHcvNmzf59ttvCQ8Px7V4cbrGx7M4Yf0t4E3gIi+2IAcYnPDv
V8BqoLNOx+07dxJbU7/99tuMGjWKnj2fr0tQFO2pO2JFySEGjx5NoK0tF9K53wVgqq0tg0ePNkdY
2e5VXblSspf/PUt/NvrYimXLEteLCKdOpba3omhLJWJFySFq1qzJhOnT8dLr05yMLwCNdDo+nzIF
d3d3c4aXbZ515VqLKfFG8/KuXOMAAXokvK8LxInwy6ZNGAwGli9fzsWLF4mKSmlvRdGeSsSKkoP0
6d+fkdOn01CvZ5ZOx4NUtrsPTANqALdFuHbzZvYFaWbp6co1B/gO0/CfVgnLCgJDgb9OnsTFxYXf
fvuN5s2bU6LE83srSs6gErGi5DB9+vdn0+7dHGvThjI2Nvjb2jIfU8KZD/jb2lLK0pJxmMacFmDG
jBkcO3ZMy7CzTFq7cn0LTAX+AIo9d4ziQDtfX+7du8eKFSs4e/YstWrVMn/wipIBamQtRcmB3N3d
WbluHXfv3mXFsmUcDwnh0YMH2Dk5UalKFca2a0fjxo25fv06AEajkV69enHkyBGsrKxecfScIz4+
nri4uBS7cjWMjaUSKXflCgI+B3YBpVI47jZra+q/8w6RkZF88cUXuLq60rx58+wokqKkm2o1rSi5
1JYtW/D29k62LDAwkBEjRmgUUfpNmDCBCRMmoNPpEpcFBASw8KuvKBEby1VMVdL+wCTg2VZlMI2v
bY2pRkAHdAHmYaq2d7GwwLZAASwsLGjRogVff/01hQsXzr6CKUo6qESsmJUaqN+8OnXqxKpVqxLf
29jYEBISQrly5TSMKvNe565cyutHJWLFLF46UL+tLetF1ED9WSA8PJyKFSty//79xGWenp7s2LEj
2V1mbhMcHIyvhwd7o6JIzyXFBaChXs+m3bvzTCty5TUgipLFFs6bJy56vczS6eQ+iKTwug8yU6cT
F71eFs6bp3XIudry5csFUw1t4uubb77ROqxMWzhvnpTR6yU0lc/Q869QkDLq86TkQioRK1lKfXlm
P6PRKM2bN0+WiB0dHeXWrVtah5ZpC+fNEycLC5mWcPGW0mfoH5AZ6qJOycVU1bSSbk+fPmXAgAFs
376dBw8eULZsWaZMmUKhQoXw9fAgMCqKL4HrQG1gKf+bwB5gJPANpgY2vYCPMVUnrtiwgaVLl7J7
926ioqKoXLkyM2bMUN1O0uDy5ctUrlw52aAV7dq1Y+3atRpGlXl3797FxcUFa6MRAT7ANM72s8cc
wQmPObxbtmTw6NGqOlrJlVT3JSXdDAYDrq6u7N27l5IlS7Jlyxbat29P03r1+CQqikGY+nh6A2Mw
TWRwMGHfhcDPwLPp65thagE7IjqaeTNm0LhFC2bPno2zszNLliyhVatWXL16Fb1ej5K6t956i0mT
JjFs2LDEZX/99Rf//PNPjp/44WXWrVuH0WgkOuH9nqJFcfi//0vWlSuwRw/V8E/J1dQdsZIlKlWq
xJXQUP4dF8ePmCavB9OQhIWB44AbphmFemK6CwbT3fJiYDNQ1saG89euJftSdXBwYNeuXbz33nvZ
VJLcy2AwULduXY4dO4aNjQ07duygTp06WoeVKR4eHuzevTvx/eTJk/n88881jEhRsp4aWUvJtDt3
7hAaGkoLnY4rQLUk6/SYpqZ7Ns/u6efWV0tYVhBoo9MlG6j/+PHjxMXF5fquONklX758LFu2jODg
YObMmcOnn36KwWDQOqwMu3nzJnv27Em27KOPPtIoGkUxH5WIlUwxGAx06dKFcqVL0/zpUx6TfCJ7
MM2E8yjh5+fX2ycsA6gZHc35EFOldWRkJN26dWP8+PHY2dmZsQR5S6VKlahevTo9evTA3t6e//73
v1qHlGFr164laYWdu7u7uihT8iSViJUMExG6dOmCtbU1Vd3csAMKYBr/OKkITI1rSGF9RMIyErZ5
9OABMTEx+Pr6Uq9evVw1SlROotPpWLRoEVOmTOHSpUtah5Mhq1evTvZe3Q0reZVKxEqG9erVi3v3
7vHTTz9h7+jII6ASpufBzzzBNJn7s8H6KwEnkqw/nrAMTHfNent7WrdujaurKwsWLDBzCfK2smXL
MnLkSPr160duawpy+fJlDh8+nGxZ+/btNYpGUcxLJWIlQ/r168fff//Nzz//TP78+XGrWpUjNja0
wfTMdz0QC0wA3gXKJ+zXDZgJhGEaK3gmpsZbAIdsbDjw11/o9XqWJXlWrGTc0KFDuXfvHitXrtQ6
lHQREXr16oWFhekrqn79+ri6ur5iL0XJnVSraSXdrl27RunSpbGxscHS0jJxuTE2lhtxcfwFDMQ0
a05tYBnJ+xGPwtRSWgf0Br7ENFB/ceCpToder08cnlGn0/HLL79Qv3598xcsjzp27Bjvv/8+ISEh
FClSROtw0uzgwYP4+/szbdo0rK2t1exJSp6lErGSZbr4+VFjwwaGZuAjNVOnY1u9ejgUK8b27dvx
8/Ojd+/e1K5dO1ePmZxTjBw5kuvXr/P9999rHUqaDR48mEKFCvHFF19oHYqimJWqmlayRExMDPHW
1kzANPB+elwA/m1pycTp01m7di1///03b7/9Nl27dqVatWrMmTOHhw8fmiHq18e4ceM4cuQIW7Zs
0TqUNImPj2fNmjWqgZbyWlCJWMm006dPU7t2beLi4vh4yBAakfZkfAH4P1tb3nRzY8SIEdy6dYui
RYsyYsQIzp07x+zZs9m/fz+lS5eme/fu7N+/P9c1PMoJ9Ho9ixYtYsCAATx69OjVO2hsz549FCtW
jLffflvrUBTF7FQiVjJMRJg7dy4eHh4MGjSIyZMn8/3q1fh8/DEN9Xpm6XQ8SGXf+5iqoxvq9Yya
MYPjISE0bdoUd3d39u0zjctlYWFBkyZNWLVqFaGhoVStWhV/f38qV67M7Nmzk039p7xakyZNaNas
Gf/617+0DuWVVq9eTYcOHbQOQ1GyhxYzTSi53507d8Tb21tq1Kgh586dk0uXLknJkiVl2bJlIiIS
HBwsXfz8xNHGRnra2so8kJUg80A66nTikD+/dPHzk+Dg4GTH3bp1qxQpUkRmzZolRqPxhfMajUbZ
vXu3dO7cWRwcHKRz586ya9euFLdVXvTPP/9IsWLFZP/+/VqHkqqnT59K4cKF5fLly1qHoijZQjXW
UtJt27Zt+Pv70717dyZMmMDdu3dp1KgRn332GQMHDky27d27d1mxbBnnQ0ISB+q/eOMGlatWZfbs
2Ske//Lly7Rr147y5cuzZMkSChQokOJ29+/fZ+XKlSxatIj4+Hh69+5N9+7dKVy4cJaXOS9Zu3Yt
48aN46+//sLa2lrrcF6wbds2JkyYwMGDB1+9saLkBVpfCSi5R3R0tAwePFhKlCghf/zxh4iIhIeH
S4UKFSQwMDDNx9m/f79UqVLllefy9/eXd955R86ePfvSbY1Go+zbt0+6desmDg4O8tFHH8mOHTsk
Pj4+zTG9ToxGo/j6+sr48eO1DiVF3bt3l9mzZ2sdhqJkG5WIlTQ5deqUVK1aVdq2bSv//POPiIjc
v39f3n33XRk7dmy6jmUwGKRw4cJy5cqVV267ePFiKVy4sPz4449pOvb9+/fl66+/lipVqki5cuXk
P//5j9y+fTtd8b0Orl+/LoULF5bTp09rHUoy0dHR4uTkJDdv3tQ6FEXJNioRKy9lNBrl66+/lkKF
CsmSJUsSn8VGRkZKnTp1ZMiQIRl6PtutWzeZO3dumrYNDg6WUqVKSUBAgMTFxaU57oMHD4q/v784
OjpKu3bt5LffflN3yUnMmzdP6tatm6N+Jxs2bJDGjRtrHYaiZCvValpJVXh4OD4+PixfvpwDBw7Q
q1cvdDod0dHRfPDBB1SuXJmZM2dmaMANb29vNm/enKZt3d3dOXr0KCdPnqR58+bcuXPnlfvodDrq
1KnDN998w5UrV2jSpAkjRoygXLlyTJkyhVu3bqU75rymb9++WFhYMH/+fK1DSaRaSyuvJa2vBJSc
6ZdffpFixYrJqFGjJDY2NnF5bGystGzZUjp16iQGgyHDx3/48KHY2dnJ48eP07yPwWCQsWPHSokS
JTLU6tdoNEpwcLD07t1bHB0dpU2bNrJ169ZMlSO3O3PmjBQqVEiuXbumdSjy+PFjsbe3l/DwcK1D
UZRspRKxkkx0dLQMGjRISpYsmdgg65m4uDhp166dtG7dWp4+fZrpczVt2lQ2bNiQ7v02bdokzs7O
8vXXX2e421JkZKQsWrRI3N3dxdXVVSZOnCg3btzI0LFyu4kTJ4q3t7fmXcBWr14tXl5emsagKFpQ
VdNKolOnTlGrVi3CwsI4fvw4np6eieuMRiO9evUiMjKS1atXY2Vllenzpad6+vn9Dh48yJIlS+jS
pQtPnjxJ9zHs7Ozo3bs3wcHBrF+/nrCwMKpUqYKvry+bN2/GYDCk+5i51ciRI7ly5Qpr1qzRNI7V
q1erIS2V15PWVwKK9p41yCpcuLB88803L9wZGY1G6d+/vzRs2FCePHmSZecNDQ2VYsWKZbix0JMn
T6R79+5SuXJlOX/+fKbjefz4sXzzzTdSu3ZtKVGihHzxxRdy9erVTB83Nzh06JC4uLjIvXv3NDn/
w4cPxd7eXh48eKDJ+RVFS+qO+DUXHh6Ot7d3YoMsf3//ZI2vRISRI0cSHBzM5s2b0ev1WXbucuXK
4eDgwLFjxzK0v16vZ+nSpXzyySfUr1+fDRs2ZCqeN954A39/fw4dOsSWLVu4f/8+7733Hq1atWLj
xo15+i65du3afPTRRwQEBGhy/o0bN+Lh4YGjo6Mm51cUTWl9JaBoZ+vWrVKsWDEZPXp0qs98J06c
KFWqVEnsO5zVAgICZNy4cZk+zqFDh6RkyZIyatSoNHdxSosnT57IsmXLpH79+lKsWDH5/PPP5dKl
S1l2/Jzk0aNHUqpUKfn999+z/dzvv/++fP/999l+XkXJCdQQl7lceHi4aQjJkyd5HBFBAQcH3KpW
pXvPnjg7Oyfb9rfffuPx48e0bNmSkSNHsn79elasWIGHh0eKx545cyYLFy5kz549FC1a1Czx7969
m2HDhnH06NFMH+vu3bt07NgREWHVqlUUKVIkCyL8n9OnT7N48WK+++47atSoQZ8+ffD19c2S5+U5
xS+//MInn3xCSEhIltZ+vMy9e/coW7YsN2/eTHU4U0XJ0zS+EFAy6MiRI9K5TRtxtLERfxsbmQ/y
Hch8kJ62tuJoYyOd27SRI0eOSExMjAwdOlQAKVCggLi5uUm7du1eepe7cOFCKV26tNm7tTx9+jRL
R1IyGAwyevRoKVmypBw6dChLjvm8qKgo+e6776RRo0ZStGhRGTVqlFy4cMEs59JC586dJSAgINvO
t3DhQvnwww+z7XyKktOoRJwLLZw3T1z0epml08l9EEnhdR9kpk4nRW1sxPXNNwVIfJUrV+6l3Y9W
rlwpb775poSGhmZLeTp27CiLFi3K0mNu2LBBnJ2dZd68eWbtlnP27FkZNmyYODs7S9OmTeWHH35I
1u86NwoPD5eiRYvK0aNHs+V8TZo0kXXr1mXLuRQlJ1KJOJdZOG+elNHrJTSVBPz8KxTEBUSXJBFb
WFjIzp07Uzz+Tz/9JC4uLtk6BnFQUJD4+vpm+XHPnz8vVapUkW7dumVpa++UxMTEyKpVq8TT01OK
FCkiAQEBcu7cObOe05xWrlwp7777bpb0F3+ZsLAwcXR0lKioKLOeR1FyMtVqOgeaO3cuNWvWxMbG
Bn9//8TlwcHBDB8yhPioKKoDLYGkAzVGAD2AooALMAEoB+wF7BK2yZ8/PzY2NgwZMoT9+/cnO++2
bdvo168fW7Zs4Z133jFX8V7QokULdu7cSXR0dJYet3z58hw8eJD4+Hjq1q3LxYsXs/T4SVlbW9Oh
Qwf++OMP9u3bh4WFBQ0bNsTT05Pvv/+emJgYs53bHDp37kzRokWZOXOmWc/z448/4uPjg62trVnP
oyg5mtZXAsqL1q9fLxs3bpQBAwZIz549E5c3a9BACoCcBYkD6Q/SOMndbw+Q9iAxIFdAyoIsS1g3
IeFOeMWKFWI0GuW7774TJycnefjwoYiI7Nq1S5ydnTWbML5hw4ayZcsWsxzbaDTKnDlzpEiRIrJp
0yaznCMlsbGxsmbNGmnevLkULlxYhg4dKmfOnMm282fW5cuXpVChQlnSRzs19erVk82bN5vt+IqS
G6hEnIONGTMmMRHfuXNHrC0t5eMkiTcsocr5UsL7wiBHk6yfAtIo4edVIBY6XbJxfN3c3OTbb7+V
w4cPi7Ozs2zfvl2rosrUqVOlf//+Zj3HgQMHpESJEjJmzJhsH1/64sWLMnr0aHFxcZEGDRrIihUr
ckV17KxZs8TDw8Msz9mvXr0qBQsWzPXP1BUls1TVdC6xYtkyygPWSZYZE/49lWSZPLf+2To7wD7h
OInbirBz5058fHz49ttvadq0aZbHnVbPhrsUM/amq1u3LkePHmXfvn20bNmSe/fume1czytTpgxT
pkzh2rVrfPbZZ3z//feULFmSQYMGcerUqVcfQCOffvopT5484dtvv83yY69ZswY/Pz/y58+f5cdW
lNxEJeJc4vzJkzSNj2ctpuQaDUzE9AeMStimBRAIPAYuAEuTrKsLxInwy6ZNGAwGli9fzsWLF1m3
bh1ff/013t7e2Vqe51WoUAErKytCQkLMep6iRYvy+++/8+677yZOr5idrKysaNOmDb/88gtHjx7F
0dERLy8v6tWrx7Jly4iKinr1QbKRpaUlS5YsYfTo0Vk+daSa8lBRTFQiziUeR0RQExgP+AFlEl52
QImEbf6L6Y65PNAG6JRkXUFgKPDXyZO4uLjw008/kT9/flq0aEH79u2zryCp0Ol0eHt7s2nTJrOf
K1++fAQGBjJz5kxatmzJ4sWLzXonnprSpUszceJErl69yqhRo1i3bh0lSpRg4MCBnDhxItvjSU3V
qlXp06cPgwYNyrJjhoaGcuPGjVQHk1GU14lKxLlEAQcHHgH9gfOYWkv7AQagcsI2TsB3CetCgHig
VpJjFAfa+fpy4sQJQkJCsLW1pV+/ftlVhFfy8fHJ0GxMGeXn58fevXuZPXs2H3/8cZa32k6rfPny
4evry6ZNmzhx4gRFihTB29ub2rVrs2TJEh4/fqxJXEmNGTOGkydPZno872d++OEH2rVrh6WlZZYc
T1FyM5WIc6D4+HhiYmKIj4/HYDAQGxtLucqVOWhtzemEba4BfYAhgEPCskvAfUzPhn8BFgNjkxx3
m7U1RUuXxtPTk+LFi1OpUiWaN2+eTaV6tUaNGnH27FnCw8Oz7Zxvv/02hw8fJioqivr163P58uVs
O3dKSpYsybhx47hy5Qrjxo1j8+bNuLq60q9fP/7880/N4rKxsWHx4sV88sknPHz4MNPHU9XSipKE
xo3FlBSMHz9edDqdWFhYJL5GjBghDtbWUgmkAEgxkM9BjElaSa8BKQ7yBsh7IL8nWfcPiFXCsWxs
bKRDhw5y9+5drYv6grZt28rSpUuz/bxGo1G++uorKVKkiGzdujXbz/8yN27ckEmTJkmpUqWkevXq
smDBAomIiNAklr59+0rfvn0zdYyQkBApUaJEhqe/VJS8RiXiXKRzmzYyS6dL04haz79m6HTyppOT
DB482KxDPmbW0qVLpW3btpqdf+/evfLmm2/KuHHjclyiMBgMsm3bNvHz8xNHR0fp1auXHD58OFv/
ng8fPpQ333xTdu/eneFjjBkzRoYNG5aFUSlK7qZmX8pFgoOD8fXwYG9UFOXSsd8FoJaFBY18fFi/
fn2y+YZzmvDwcNzc3AgPD9esW8vt27f56KOPeOONN/juu+8oWLCgJnG8zO3bt1m2bBmLFy/Gzs6O
Pn360LlzZxwcHF69cyZt2LCBkSNHcuLECWxsbNK1r4jg5ubG999/T82aNc0UoaLkLuoZcS5Ss2ZN
Jkyfjpdez4U07nMB8LCwoHz16qxbty5HJ2GAIkWKULFiRfbs2aNZDC4uLmzfvp2KFSvi7u7OsWPH
NIslNS4uLowaNYrQ0FCmT5/O7t27KVWqFD179uTgwYPJWoE/ffo0S1uFt27dmipVqjB58uR073vs
2DGMRiPu7u5ZFo+i5HaW48ePH691EEra1ahZE9uCBem2cyeWBgMVgJRG6b0PzNPp6GZpSfHKlTl4
+DD58uXL5mgz5s6dO/z111+8//77msVgaWmJl5cXxYsXp2PHjjg7O/Pee+9pFk9qdDodZcqU4cMP
P8Tf35+wsDDGjBnDokWLMBgMuLm5sWDBAnr27ElMTAzly5fnjTfeyPR5GzZsSO/evfHy8krXXNWz
Z8+mWrVqmg4eo6RNeHg48+fOZdn8+axaupRft27l3IULlHdzy5LPkJKEphXjSoYFBwdLFz8/cbSx
kZ62tjIPZCXIvCTzEVdwdZVatWpJTEyM1uGmy/Hjx+Wtt97KMc+yz5w5IxUqVJDevXtLdHS01uG8
ktFolJ07d0rHjh3F3t5e7O3tE2fesrKykvbt28v27dsz/Qx88eLFUrNmzTQPFxofHy+urq5y8uTJ
TJ1XMa/0zHWuZA31jDiXu3v3LiuWLeN8SAiPHjzAzsmJ8lWqcObsWUJDQ9m2bVuuu3oVEUqVKsWv
v/5KxYoVtQ4HgEePHuHv78/ly5dZt24dpUqV0jqkNNm4cSOtW7dOcV2ZMmXo3bs3PXr0wMXFJd3H
FhGaNGnCBx98wJAhQ165/YEDB+jduzenTp3K8Y9IXleL5s9nXEAAI6Oj6S6CUwrbPACW6XRMtbVl
wvTp9OnfP7vDzHs0vQxQspzRaJThw4eLu7t74sxKuVH//v1l6tSpWoeRjNFolBkzZkjRokXl119/
1TqcNPn666/Fysoq8Y44pVe+fPmkbdu2sm3btnTfJZ8/f14KFSokly9ffuW2n376qUyYMCGDJVHM
LSNznZfR62XhvHlah57rqUScx0ycOFEqV64s9+7d0zqUTNmyZYs0bNhQ6zBStHv3bilWrJhMmjQp
x3VxSkkri/s7AAAgAElEQVR4eLhMmzZNypcv/9KEDEjp0qVl8uTJcvPmzTQf/z//+Y94eXm99FGC
wWAQFxcX+fvvv7OiSEoGzZkzR9zd3cXa2jrZFKtHjhwR+/z5pRSIHcj7CbO7PZ98n4JUACmZJBm7
6PXy888/i6enp+j1eqlYsaKmM7nlRqpqOg+ZNWsW8+fPZ8+ePRmqasxJoqOjKVq0KFeuXMmR3YfC
wsJo3749Tk5OrFixAienlCrxchYRYffu3SxevJgff/yRp0+fprqtpaUl3t7e9OnTBy8vr5cORRkX
F0etWrUYNmwYXbp0ITw83PS45ORJHkdEUMDBAYs33mD/gQNmn9RDebkNGzZgYWHBr7/+SnR0dOKs
Ws0bNuTQvn0EA+WAQcAZYNdz+/8b+B3TKH7XEpbN0umY4uRED39/Jk+ezJYtW+jVqxcXLlygUKFC
2VKuXE/jCwEliyxcuFBKlSolV69e1TqULOPr6ytBQUFah5Gqp0+fyuDBg6VMmTJy/PhxrcNJl7t3
78rMmTOlQoUKr7xLLlmypIwfP16uXbuW6vGOHj0qBQsWlHYtW6bYyKezpaXY5cunGvnkEOmd61wS
fn4HZFuSO2IBOZLwOUn6eKJRo0aycOFCjUqX+6h+xHlAUFAQEydOZPv27bi6umodTpZ5NkdxTmVl
ZcXs2bOZPHkyzZo1Y8WKFVqHlGaFCxdm6NChnDlzhr1799K1a1esra1T3Pb69euMHz+e0qVL4+Pj
w6aEqTST+vPIEXSRkdTdupVLMTF8ExNDP6Az0A/4Lj6eqwYDNTZswNfDg0Xz55u9jErapHWu80HA
l8DzQ7jcBBx1OtatXZu4rFq1apw+fRolbVQizqWezVu7fv16hg0bxq+//kq5cukZbyvna9WqFdu2
bSMuLk7rUF6qY8eO7Nq1i3//+98MGDCA2NhYrUNKM51OR4MGDVixYgVhYWF89dVXVKpUKcVtjUYj
mzdvxtfXl1KlSvHFF19w9epVFs2fT2BAAIcMBj6DFFvakrB8qAh7o6IIDAhQyTiHSMtc5+sxJWff
FPZ/DDiJcD7JYwd7e3sePXpk1rjzEpWIc6G1a9dSvnx55s+fT9++fdm6dWuqX565WfHixSlTpgwH
DhzQOpRXqlSpEsHBwdy+fZtGjRpx/fp1rUNKt4IFCzJo0CBCQkI4cOAAPXr0wNY2peFiTM/IJ02a
ROnSpRk6cCDxUVFUB1pimobzmZaY5sy2T3hZA22BX6OiGBcQQPHixdHr9djb22Nvb0+LFi3MW0jl
Ba+a6zwKGIlpvnMw1UMnVQB4Cjx68CBxWUREBHZ2dmaNOy9RiTiX2bJlC506dSIsLIyBAwfy5Zdf
Ur16da3DMpucXj2dlL29PevWraNdu3bUqlWLHTt2aB1Shuh0OurWrcvSpUsJCwtj7ty5qfabtgYs
RNiGaTS30kDHJOu3Ao+AyIRXPaA9pgZBI6KjiYyIYMuWLURGRhIZGcm2bdvMVzAlRa+a6zwUuAo0
BIphupAKwzS/+TWgEhAO2BQokHjMEydO5MmbA3NRiTgX+eOPP2jbtm3i8zkRYfjw4VkyP2xO5e3t
zaZNm7QOI810Oh3Dhw8nKCiILl268OWXX2I0Gl+9Yw7l6OjIgAEDuHz5MocPH+bdd99NNlSqAegA
VADyYZr/eg+Q0qzOV4C9QNeE991FiI6O5kGSOynFvDIy13kV4DpwHDgBLAFcEn4uCZQHHC0suHzr
FrGxsfz000+cOnWKtm3bZnfxci2ViHOJgwcP4uvrm+z5o06n47///S+Ojo4aRmZe1atXJyIigtDQ
UK1DSZcmTZoQHBzMzz//jJ+fHxEREVqHlCk6nY5atWrh7e1Nhw4dWLBgASWKF09TI59nVgCNgGfN
CQsCeqBHjx4ULVqUFi1acPLkSbOVQYHJkyej1+sJDAwkKCgIvV7PPw8esBH4CFN1dB2gPqbnxGBK
EkWSvAomLHMGdJhqQmKtrIgzGHBycuLzzz9n3bp1qutSOqhEnAs8mwDhyZMnyZbPnz+fLl26aBRV
9rCwsMDb25stW7ZoHUq6lShRgt27d1OiRAnc3d3zTB9aKysr+vbty/uennjBSxv5JLUS6Pncsn4i
tPfx4erVq3h4eODl5UVkZKRZ43+djRs3DqPRSHx8fOIrMDAQ75Yt+Vin4xGmaufJmJJsShrzvz7E
AMt1OnxbtWLfvn1ERUVx9uxZPD09zV2UPEUl4hzuzJkz/N///d8Ld1QzZsygb9++GkWVvXLTc+Ln
5c+fnzlz5jBu3DiaNGlCUFCQ1iFlmVc18klqH3AH0/PFpKoBUZGR2NjYMGrUKBwdHdm7d695A1de
MHj0aAJtbdM8veozF4CptrYMHj3aHGG9NlQizsEuXrxIs2bNuHfvXrLl48eP57PPPtMoquzXtGlT
Dh8+nKurd7t06cKOHTsYN24cn3766UtHtcotXtXIJ6kVCev0zy1/BNglGZVMp9Nl6dzJStpkdK5z
L72eCdOnq/mlM0klYo2Eh4czfepU+nTpQicfH/p06cL0qVO5e/cuYBpEoWnTpty6dSvZfgEBAXzx
xRdahKyZAgUK0KBBA3777TetQ8mUqlWrcvToUa5du4aHhwc3b97UOqQ0S6mRT9nKldlvZZVqI59n
YoA1vFgtfR3YnD8/Zd95h9jYWKZNm8Y///xD/fr1zV4e5UV9+vdn5PTpNNTrmYlplqWU3Adm6nQ0
1OsZqWZfyhoaj+z12knLXJ9t339fXF1dXxhqsF+/fjlmjt7sNnfuXOnWrZvWYWSJ+Ph4mTJlihQr
Vkz++OMPrcNJk/Hjx4tOpxMLCwuxsLAQnU4nBQsWFBuQSiAFQIqBfA5ifG6igFUgpVOYQGA/iIVO
J2+88YYULlxYmjVrJseOHdO6qK+94OBgKVe8uNiAfJQwx/nzc5138fOT4OBgrUPNM1QizkYL580T
F71eZul0cj+VqcXug0wDsU8Y6/VZEu7atWuumOnHXK5cuSKFCxdO8yT0ucHvv/8uRYsWlalTp8rd
u3elffv2cv36da3DSpHRaJQDBw5It27dxMHBQTp27ChTpkwRPcj0NE6b9/xrOkjHDz7QumhKCt56
6y0h4TvIBuT9Bg2kT9euMn3qVAkPD9c6vDxHJeJskpG5Pl0S/iO0bdtW4uLitC6C5qpUqSL79+/X
OowsdfXqVXF3d5eiRYsKIM7OzjnqLvnhw4cyZ84cqVKlipQrV06mJvkijo6OlmLFiol9wuc1PUk4
NOFis06dOvLkyRONS6kkFRERkawmzsLCQqKiorQOK09Tz4iz0NOnT/n4448pXbo0Dg4OVK9enW3b
thEcHMy4gADGRUXhg2lIuKYk7wIApmHkCmPqn7cE0+AHjhYWDBs2jIkTJ1K1alWsrKyYOHEir6Pc
3Ho6Na6urnh5eXHnzh0A7t69S7NmzZg6daqmjZaOHj2a+FnetWsXs2bN4ty5cwwfPhxnZ2diY2MZ
OnQo1tbWPNHpaAjpauTTEFNDrUOHDtGqVSseP35strIo6fN8X243N7dUhzpVsoZKxFnIYDDg6urK
3r17iYiIYNKkSbRv354pY8fySVQUgzDN53kfqIGpA/0zC4GfgRDgJLAJ+AMYI8K86dMpX74806ZN
w9vbO5tLlXP4+PjkuURsNBo5ceLEC8tGjhxJ27Zts7VP7ePHj1m0aBE1atTgww8/pGzZspw9e5a1
a9fStGlTLCxMXxc3btygcePG3Lx5k+LFi9O0eXM6DBpEQ72eWTrdSxv5zNDpcNfpuMP/xizetWsX
Xl5eubpVfF7y/OexWrVqGkXyGtH6ljyve+edd0RvZSWzQOonqZp7AmILci7hfT2QxUnWfwtSF+Qf
EEcbm8TqwC5dusiECRM0LpU2DAaDFC5cWK5cuaJ1KFkqPj5eJk6cKDqd7oUGem5ubnLq1Cmznv+v
v/6Sfv36iZOTk7Ru3Vp++eWXVNsj7NixQ1xcXGTChAnSoEED6dmzZ+K2wcHB0sXPTxxtbKSnrW2q
jXy2bdsmVapUeaGsNWrUkHv37pm1rMqr9e7dO9nfZcqUKVqHlOepO2IzunPnDqGhobTQ6biCafCC
Z/SYBr5/1vXj9HPrqyUsKwi00elYsWyZ+QPO4SwtLWnZsmWeuyu2sLBg7NixbN26FSen5JMInj9/
nlq1arFq1aosPWdUVBRLly6lTp06+Pj4UKxYMUJCQli/fj0tWrRIvPt9RkSYNm0anTt3ZvHixWzf
vh03NzeWLFmSuK27uzsr163j/LVrVJowgeNdu7LV25vjXbtSacIEzl+7xsp16/Dy8mLnzp3UqFEj
2Tn+/PNPPD09CQ8Pz9KyKumj7og1oPWVQF4VFxcnzZo1k4rly8t8kF4go59rsFIfZHnCz5ZJ7o6f
NWaxSPh5Hkifrl1F5PW+IxYRWbNmjbRo0ULrMMzm8uXLUr169RfuFgEZNGiQxMbGZur4p06dkk8/
/VQKFiworVq1kp9//vmVDQEjIiLEz89PatasKadPn5YGDRrIxx9/nOlW/A8fPpR69eq9UM4KFSrI
jRs3MnVsJWMMBoPY2tom+3uov4X5qTtiMxARunTpgrW1NVXd3LDD1EDr+ad9EZiGAySF9REJy0jY
5pGaoQYALy8v9u3bl2cb95QuXZr9+/fTq1evF9b997//pUmTJoSFhaXrmDExMXz33Xc0bNiQ5s2b
4+DgwLFjx9i8eTM+Pj7JZlN63tmzZ6lduzbOzs5s3bqVPn36ULFiRRYuXPjCXXN6OTg48Ouvv+Lh
4ZFs+d9//03jxo25evVqpo6vpN+FCxeIjo5OfF+oUCGKFy+e4ravGpRISTuViM2gV69e3Lt3j59+
+gl7R0ceYZqz83iSbZ4AF/nfUICVME0r9szxhGXw4jCArzN7e3tq167N9u3btQ7FbGxsbFiyZAmL
Fy/G2to62br9+/dTvXp1du/e/crjnDt3jmHDhlGyZElWrlzJ0KFDuXr1KpMmTUp1fuGk1q5dS6NG
jRgxYgRTp07lgw8+oFKlSixYsCDTSfiZAgUKsHXrVry8vJItv3jxIo0aNeLChfSOfqxkRkrV0jpd
8ukfgoOD6eLnx9ulSnF23DiqBwXRavNmqgcFcWb8eNxcXeni50dwcHB2hp67aX1Lntf07dtX6tat
m9g3clpgoPS0sZG7II4gP4HEgAxPaIz1rCp6Acg7IDdBbiT8vChhXU9bWwn88kuJjo6WTp06yZgx
YyQmJua1HeBj1qxZ0qtXL63DyBZHjx6VUqVKvVB9a2lpKdOnT39hpLXY2FhZvXq1eHh4SJEiRWTU
qFFy8eLFdJ0zLi5OAgICpHTp0nL06FGJiIiQunXrSt++fc32mYuJiZEPPvjghXIWK1ZMzpw5Y5Zz
Ki/617/+lez3P3To0GTr0zoo0UydTlz0elk4b55GJcldVCLOQlevXhWdTie2trZSoECBxJfeykru
g+wAqQCiB/EEufrcB3gkSEGQQiCjEpY9azXdoUOHZEMMWlhYyPLly7UusiZCQ0PFxcXltbkQuXfv
nnh5eaX43Lhdu3YSGRkpFy5ckBEjRkiRIkXE09NTfvjhhww9T759+7Z4eHjI//3f/8m9e/fk4cOH
UqdOHenfv7/Zf99Pnz6V9u3bv1BGZ2dnOX78uFnPrZi0atUq2e8+6XdMRgYlKqOScZqoRJwNOrdp
I7N0ugwNAzhTp5Mufn5aFyHHqVChwms11q3BYJAvvvgixWT8xhtviKOjowwbNkzOnTuXuM+dO3dk
WmCg9O7cWTp6e0vvzp1lWmBgqkMUHjx4UEqUKCFjxowRg8EgDx8+lNq1a8uAAQOybYxzg8Eg3bt3
f6GMTk5OcuTIkWyJ4XXm6OiY7Pf+7ALoyJEjYp8/v5QCsQN5HyQsyffUeBCrhHUFEv69nJCMXfR6
+eGHH8TDw0McHBykZMmSMmnSJI1LmrOoRJwNjhw5Ii7puJJMekXpote/VgknrQICAuSLL74QEXlt
7oxFRDZt2iT29vYvJKoCBQrImjVrRCRtE4t0btMmMbEZjUaZO3euODs7y8aNG0VE5MGDB1KrVi0Z
OHBgtk80Eh8fL/369XuhjPb29rJv375sjeV1cu/evWS/b51Ol1ir0qxBAykAchYkDqQ/SOPnEnHX
l9xMFHR0lLFjx4qIyMWLF6VYsWKyadMmLYubo6hEnE1UtU7Wefr0qcyaNUuKFCkibm5ur0UVfVxc
nGzcuFFatmwpDg4OUrhw4RTvjps3bZquZ3hff/WVdOvWTSpXriznz58XEVMSrlmzpnzyySeazfZl
NBplyJAhL5RPr9fLjh07NIkpr9uxY8cLtRAippoVa0tL+TjJZygM0zj4l9KQiP9JOF7SceI//PBD
+c9//qNVUXMclYiz0bOGDjNf8iX5D8gM1dDhpcaNG5fsC+PDDz/UOiSzuX79uowfP15KlCghderU
kaVLl8qTJ0/kyZMnL1Th6jBNFJKei73iOp3UdneXx48fi8j/kvCgQYM0n3LTaDTK6NGjX0jGNjY2
snXrVk1jy4tWr16drLalbNmyImJqcFrZ0lIGJvns3Ej4vP2cJBE7YmrfUjmh9iXpZ62khYU08fSU
uLg4+fvvv6VkyZLy559/alzinEMl4myW1mEAVXV06g4dOvRClWVmB7rISQwGg2zdulU++OADcXJy
kv79+yc+q5szZ464u7uLtbW19OjRQxYsWCD58+c3JShI9Rne+/zv2Z0dSH6QqgnJ2NnGRvR6vRQo
UEAsLCzEyspKdDqdzJw5U+PfhMmkSZNeSMZWVlayfv16rUPLc27evCmOjo7y4YcfSqtWrUREpHfn
zjIYpAhICEgUSB9MgxCtTvh8nQW5hWku6gOY5qZeneTzNxHErkAByZcvn1hYWMj48eM1LmnOohPR
cIqX19jdu3dZsWwZ50NCePTgAXZOTrhVqUK3Hj1wdnbWOrwczWg04uLikmzggO3bt9O0aVMNo8q8
27dv8+2337Jo0SIKFy5M37596dixIwUKFEjcZsOGDVhYWPDrr78SHR3Nt99+y5EjR2jeoAHGuDiC
MQ2dOgg4A+xK5VyeQDPgc2CWTsehVq24eOsWDRs2ZNCgQbi5uXHp0iVKlixp3kKn0YwZMwgICEi2
zNLSkqCgID766KNU9lLSa9u2bUybNo169epx8+ZNvv32Wzr5+NBq82YigVmYxjUYAvwH2AzUT+E4
gcBRYC0QDbgC5d99l31//snt27dp27Yt3bt3p1+/ftlTsBwu9SF1FLNydnZm2PDhWoeRK1lYWNCq
VSuWJRl/e/PmzbkyERuNRv744w8WLFjAjh07aNeuHT/++CPu7u4pbt+6dWvANKjCzZs3AdNoXLFG
I12BCgnbjQXeBC4Dbz13jCuYpthcnvC+uwhjtmyha58+zJw5k4kTJ9KoUaMck4QBhg0bhq2tLQMH
DkxcFh8fT6dOncifPz9t2rTRMLq848SJEy+MLV3AwYFHQP+EF0AoMJn/DUj0PB0kzq51GlMyrlKl
ChYWFhQvXpwOHTqwdetWlYgTqJG1lFzJx8cn2ftNmzZpOn9vet29e5epU6fi5ubGsGHDaNKkCVeu
XGHx4sWpJuHUrFi2jPJA0jG4jAn/nkppe6ARprsUME0s4mdpSbmyZdHpdKxcuZIePXqkr0DZYMCA
AXzzzTfJRnoqUaIEDRo00DCqvOWvv/6iYsWKxMfHYzAYiI2NpVzlyhy0tk6coOYa0AfTXbFDwrKf
gYcJPx8BvgJaJ7wvB8QCT+LjERFu377NDz/8oCaTSEIlYiVXat68OVZWVonvL168yPnz5zWM6NVE
hN27d9OxY0fKly/PmTNn+O677zh+/DgDBgzAwcHh1QdJwfmTJ2kaH89aTIk3GpiI6T93VArbrwR6
PresnsFAaEgIe/fuJTw8nLZt22YoFnPz9/cnKCgIS0tLSpQowePHjzl48KDWYeUZf/zxB3379iUw
MJCgoCD0ej3/PHjARkzzp9sBdTBVR09Mst9qTAnXHugB/AvokrDOCFhbWXEyJAQnJyeqV69O1apV
+fzzz7OrWDmeqppWciU7Ozs8PDz4/fffE5dt2rSJt99+W8OoUnb//n2WL1/OokWL0Ol09OvXj3nz
5r0w5WFGPY6IoDHwNuDH/57h2QElntt2H3AHeD7NPptYZMWKFbRt2xa9Xp8lsZlDx44dsbOzo1q1
aty5cwdvb29iY2P58MMPtQ4tV4uJieHRo0dER0e/MMb5zdBQ3DdsYEgqtU7fv+S4y3U62vj4sHLd
uiyMNm9Rd8RKruXt7Z3sfU6ap1hE2L9/P926daNMmTIcPXqURYsWcfr0aQYNGpRlSRiSP8M7D9zC
lJANvPgMb0XCuufT7CPA1t6etWvX5shq6ed5e3tTsmRJ3N3d+e233xg8eDArV67UOqxc7fTp05Qv
X/6FJAwwePRoAm1tSe8UHBeAqba2DB49OktizKtUIlZyrecT8b59+3ig8XSRDx8+ZM6cOVStWpWe
PXtSrVo1Lly4QFBQEA0bNnxhJpv0io+PJyYmJt3P8ABigDW8WC0NcCBfPh4bDBQsWJDGjRtnKsbs
VrVqVf744w/+9a9/sWjRIq3DybVSaqj1TM2aNZkwfTpeen2ak/EFwEuvZ8L06elu9/Da0bDrlKJk
2jvvvJOsf+mqVauyPQaj0SiHDx8Wf39/cXBwkPbt28uOHTvMMiDG+PHjX5j8Y8SIEeJgbS2VEvoK
FwP5PKFPZ9JBFVaBlE5lEBkbkPz584uPj4/ExcVledzZ4cKFC1KqVCmZPXu21qHkSp9++qlMmzbt
pduMGDZM7EGmgRqUKAupRKzkaiNGjEiWiDt16mS2c0VGRsr8+fPF09NToqOjJTIyUhYsWCDvvvuu
vPXWW/Lll1/K7du3zXb+l8nMxCLTQGyT/A4rVqwoGzZs0HxkrYy4cuWKlC1bVr788kutQ8l1GjVq
JL/99ttLtxk4cKCQ8HmxAelkaakGJcoCakAPJVfbt28fDRs2THzv5OREeHg4+fJlXTvEY8eOsXDh
QoKCgnjy5AkAnp6e/PXXX3h6etKvXz+aNWuGhYV2T3qCg4Px9fBgb1QU5dKx3wWgBhCZwrr69esT
GBhI/fopDdmQc4WFhdG0aVPat2/P+PHjM/044HUgIjg5OXH+/HmKFCmS4jZxcXEUL16ce/fuJS7r
0b07+Y1GNShRZml8IaAomRIXFycFCxZMdle8Z8+eTB/38ePHsmTJEnF3d09xcgVXV1e5efNmFpQg
62RkYpG3bG3Fq3lzsba2TrGcgHzwwQdy5swZrYuXLnfu3JGqVavK8OHDc+WdfXa7cuWKuLi4vHSb
rVu3JvtcODo6SkxMTDZFmLepxlpKrpYvXz7ef//9xPc6YGi/fnTy8aFPly5Mnzo12VCYr3Ly5EkG
DhxI8eLF+fjjjzl69GiK2924cQODwZDZ8LNUn/79GTl9Og31embpdKTWbO0+MFOno6Fez6gZM9j2
22+EhobSs2fPFO8eN27cSOXKlendu3fiaF45XZEiRdi5cyc7d+7k008/xWg0vnqn19jLGmo98/33
yTsptWvXLsUW1koGaH0loCiZNXnyZNEnPLPqCK+cf/d5UVFRsnz5cqlbt26qd4XPXsWKFZOxY8fK
1atXs7mUaRccHCztWrYUW51OuuTLl65neCEhIeLt7Z1q+W1tbWX06NHy4MEDDUqWfg8fPpR69epJ
r169xGAwaB1OjjVx4kQZMWJEquufPHkib7zxRrLPws6dO7MvwDxOJWIlV1s4b5642NrK9Je04kw6
/27SVpxnzpyRwYMHi5OT00uTr06nEy8vL/npp5/k6dOnGpY2bcLCwqRChQoyYsQImT51qvTp2lU6
entLn65dZfrUqRIeHv7KY+zatUtq166d6u+kYMGCMnPmzFxRNfno0SPx9PSUTp065doW4ebWtm1b
CQoKSnX9qlWrkv3933zzTXVhk4VUIlZyrYw8Ey2j10uvnj2lUaNGr7z7LVKkiIwaNUouXryodVHT
LCwsTN5++22ZOHFipo9lNBrlxx9/FDc3t1R/R6VKlZKVK1dKfHx8FkRvPlFRUdKiRQvx8/PLU1Nm
ZpVy5crJqVOnUl3v4+OT7O8+bNiwbIwu71OJWMnRks6/27Nnz8TlR44cEfv8+TM0/26BVyTgJk2a
yJo1a3LdF/azJDxp0qQsPe7Tp09lwYIF4uLikurvrFq1avLLL7/k6IZRMTEx0rp1a2nVqpVER0dr
HU6O8ejRI7G1tU21tuDevXuSL1++ZH/vY8eOiYipUdy0wEDp3bmzdPT2lt6dO8u0wMA01boo/6MS
sZKjrV+/XjZu3CgDBgxIloibNWggBTBNSB4H0h+k8Uvuhj1AJif8PBrEKoXq50GDBsm5c+c0LG3G
3bx5U9zc3OTf//632c7x+PFjmTRpktjZ2aWakD09PXN0/9GnT59Khw4dpFmzZvL48WOtw8kRDhw4
IDVq1Eh1/cKFC5P9jStUqCCHDx+Wzm3aiKONjfjb2KS7XYaSnErESq4wZsyYxER8584dsba0lI+T
JNowEB3IpRSS8GUQS5CrJB9JCpCGDRtKUFCQ2NvbJ17l5zY3btyQ8uXLy5QpU7LlfOHh4TJo0CCx
srJKNSG3b99eQkNDsyWe9DIYDNKjRw9p2LChREREaB2O5ubPny/+/v6prl+6dKmUKFEi8W/r6+0t
Lnq9zNLp0t0uQ0mZ6r6k5DpZMf9uW0tLhg8bxp49e3jnnXeIi4ujXLn0DIWRM9y8eRNPT0/8/f0Z
nU0D6zs7O/PVV1/x999/07FjxxS3WbNmDRUrVuSTTz4hPDw8W+JKK0tLS7755hsqV65M8+bNNR+f
XGuv6rrUo0cPunXrRseOHWni4UHI9u3sjYpiiAipTV3iBAwVYW9UFIEBASyaP98ssecVKhEruU5W
zIKQTb0AACAASURBVL9bPz6eiPBwIiMj6datG+PHj8fOzs68gWexGzdu4OHhwccff8yoUaOy/fxl
ypTh+++/588//6RZs2YvrDcYDMydO5dy5cpx586dbI/vZSwsLJg7dy7169enSZMm6eprntc8n4jn
zp1LzZo1sbGxwd/fHxFh1apVvP/++xw9cABjTAzVgZaYZvp6ZgKQH9OcxHYJ/+YDfo2KYlxAAMWL
F0ev12Nvb4+9vT0tWrTIvkLmcCoRK7nO44gIagLjMU3pVybhld75dx/eu4evry/16tVjxIgR5g06
i12/fh0PDw/69OmjeezVq1fn999/57fffuO99957YX2lSpVSHTZRSzqdjhkzZtCqVSs8PDy4devW
q3fKY4xGIyEhIVStWjVx2ZtvvsnYsWPp1asXAIcOHcLa2poVCxdifPqUbZgGhSkNPF8f0gHTcKmP
Ev4tDZQDRkRHExkRwZYtW4iMjCQyMpJt27aZu3i5hkrESq6TFfPvPgAOnDiBq6srCxYsMHPEWev6
9et4enrSv39/hg8frnU4iZo3b87Ro0cJCgqidOnSgOnOMyIigjp16rBr1y5N40uJTqdj8uTJdOrU
icaNG3P9+nWtQ8pWly5domDBgsnmx27dujW+vr4ULFgQMI2o5evry95Dh+gAVMB0pzsW2ANcTsN5
uosQHR392j8GSI1KxEqOZo75dw3ANAsLHAsWZNmyZeYuQpa6du0aHh4eDBgwgGHDhmkdzgssLCzo
1KkTf//9N1999RWjRo3i1KlTDBkyBH9/f1q1asXJkye1DvMFn3/+Of369aNx48ZcunRJ63Cyzaue
DxuNRtasWYNOJE3tMjYBhYEqQNLL24KYLoZ79OhB0aJFadGiRY78HGhFJWIlR5s8eTJ6vZ7AwECC
goLQ6/X88+ABG4GPMFUx1wHqY3pOnNQGTI1GGj+3fBtw3Wjk0qVLODg4YGdnh729Pfv37zd3cTLl
6tWreHh48Mknn/DZZ59pHc5LWVtbM2jQIP79739jYWFBx44dOXv2LF5eXjRv3pwePXpw7do1rcNM
5rPPPmP48OF4eHhw7tw5rcPJFq9KxGFhYbz11lvcDwt7ZbuMj4CzwF1gUcL6H5Icq58I7X18Ej/H
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
<h1 id="Making-a-co-author-network">Making a co-author network<a class="anchor-link" href="#Making-a-co-author-network">&#182;</a></h1>
</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>The <a href="{{ site.baseurl }}/docs/RecordCollection#networkCoAuthor"><code>networkCoAuthor()</code></a> function produces the co-authorship network of the RecordCollection as is used as shown</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[34]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">coAuths</span> <span class="o">=</span> <span class="n">RC</span><span class="o">.</span><span class="n">networkCoAuthor</span><span class="p">()</span>
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
<p>In addition to the specialized network generators <em>metaknowledge</em> lets you make a one-mode co-occurence network of any of the WOS tags, with the <a href="{{ site.baseurl }}/docs/RecordCollection#networkOneMode">networkOneMode()</a> function. For examples the WOS subject tag <code>'WC'</code> can be examined.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[35]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">wcCoOccurs</span> <span class="o">=</span> <span class="n">RC</span><span class="o">.</span><span class="n">networkOneMode</span><span class="p">(</span><span class="s1">&#39;WC&#39;</span><span class="p">)</span>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">nx</span><span class="o">.</span><span class="n">draw_spring</span><span class="p">(</span><span class="n">wcCoOccurs</span><span class="p">,</span> <span class="n">with_labels</span> <span class="o">=</span> <span class="kc">True</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt"></div>


<div class="output_png output_subarea ">
<img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAeIAAAFBCAYAAACrYazjAAAABHNCSVQICAgIfAhkiAAAAAlwSFlz
AAALEgAACxIB0t1+/AAAIABJREFUeJzs3XlYVdXewPHvOYjCUeZJQAREsTQ1TTLTUuqqOZVomhao
ZOZEqcVVyXKoDDW0sldJ7ysiYqSpOZv0mjnUNSBzpFAp0EQTRAQFHGC9f6A7RkUcDujv8zw+zzl7
r732b+9T/M5ae521dEophRBCCCGMQm/sAIQQQogHmSRiIYQQwogkEQshhBBGJIlYCCGEMCJJxEII
IYQRSSIWQgghjEgSsRBCCGFEkoiFEEIII5JELIQQQhiRJGIhhBDCiCQRCyGEEEYkiVgIIYQwIknE
QgghhBFJIhZCCCGMSBKxEEIIYUSSiIUQQggjkkQshBBCGJEkYiGEEMKIJBELIYQQRiSJWAghhDAi
ScRCCCGEEUkiFkIIIYxIErEQQghhRJKIhRBCCCOSRCyEEEIYkSRiIYQQwogkEQshhBBGJIlYCCGE
MCJJxEIIIYQRSSIWQgghjEgSsRBCCGFEkoiFEEIII5JELIQQQhiRJGIhhBDCiCQRCyGEEEYkiVgI
IYQwIknEQgghhBFJIhZCCCGMSBKxEEIIYUSSiIUQQggjkkQshBBCGJEkYiGEEMKIJBELIYQQRiSJ
WAghhDAiScRCCCGEEdUydgBCPOjOnDlDVGQkRw4c4ML589SzssK7ZUuGBAbi4OBg7PCEEHeZTiml
jB2EEA+i+Ph4PgsNZdOWLfQFfPLzsQBygDhzc75Rip7duzM2JAQfHx8jRyuEuFskEQthBIvCw5ka
HMzEvDyGKIVNOWXOAZE6HbPNzZkeFsbro0bd6zCFEPeAPCMW94Svry8RERF3tM5Ro0YxY8aMO1rn
vbAoPJxZwcHsys1l3LUkvANwK1XOBhivFLtyc5kVHMyi8PB7Gqenpyfff//9PT2nEA8iScTijvHw
8MBgMGBpaYmzszOBgYHk5ubetfOFh4czefLku1Y/wNatW+nUqROWlpY4OTnh6+vLhg0bqlxffHw8
U4OD2ZqbS+NS+3QVHNMY2Jqby9TgYBISEqp87jtp6NCh6PX6Mvdi/Pjx6PV6oqKiKlVP6WSfmpqK
Xq+nsLDwjsYrRHUmiVjcMTqdjk2bNpGdnc3evXtJSEjgww8/NHZYVbZq1SoGDBjA0KFDOXnyJH//
/Tfvv/8+GzdurHKdn4WGMjEvr0wSvpnGwIS8PD4LDa3yue8knU5H06ZNSyTcgoICvv76axo3vtWr
+4dSCp1OR1WfmBUUFFT53EIYiyRicUdd/wPq7OxM9+7dOXTokLYvJSWFjh07YmlpyXPPPUdmZiYA
vXr1Yv78+SXqadWqFevWrQOKWllOTk5YWVnRqlUrEhMTAQgMDGTKlCnaMevWraN169ZYWVnRpEkT
YmNjAYiMjMTLywtLS0u8vLyIiYmp1LW8/fbbTJ06lcDAQCwsLAB46qmnWLhwoXatH374IR4eHtSv
X5+hQ4eSnZ0N/NOyi4qKwt3dHUdHR9555x02bdnCEKXIB4YCtsAjQHypc58CXgQcAS/gc2CIUmzc
vJkJEybw0ksvMWTIECwtLWnRogV79+7Vjp01axYNGjTA0tKShx9+mO3bt2vxzpw5k8aNG+Pg4MDA
gQPJysrSjlu2bBkeHh44ODjw0Ucf3fT+9OrVi927d3P+/HkAvv32W1q1akX9+vW1Mn/88QfPPvss
9vb2ODo64u/vr92jwYMHc/z4cXr16oWlpSVhYWF06tQJAGtraywtLfn5558BiIiIoFmzZtjZ2dG9
e3eOHz+unUOv17NgwQK8vb3x9va+adxCVDtKiDvEw8NDbdu2TSml1PHjx1Xz5s3V1KlTlVJKde7c
WTVu3FgdO3ZM5efnq86dO6uQkBCllFIrV65U7dq10+rZt2+fsre3V1euXFFbt25Vbdu2VdnZ2Uop
pX7//Xd1+vRppZRSQ4cOVe+9955SSqmff/5ZWVlZaedPS0tTSUlJ6uLFi8rS0lIdPXpUKaXU6dOn
VWJi4k2v5ffff1d6vV6lpKRUWGbx4sWqSZMmKiUlRV28eFH17dtXBQQEKKWUSklJUTqdTr3++uvq
0qVLav/+/apWrVqqb+3aSoGaCOppUFmg/gL1CCg3UApUIajHQH0I6iqoP0F5gYoFFWhurrp26aLM
zc3Vt99+qwoLC1VISIh64oknlFJKJSUlKTc3N+0epaamqj/++EMppdSnn36q2rdvr9LS0tTly5fV
yJEj1aBBg5RSSh0+fFjVq1dP7d69W12+fFm99dZbytTUVLufpV2/9yNGjFBffPGFUkqpAQMGqK++
+kp17NhRLV26VCml1LFjx9T//d//qStXrqiMjAzVqVMnNX78eK0eDw8P9f3332vvU1JSlF6vV4WF
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
v/76a95//32io6PJzs5m/fr12NnZoZSid+/etG7dmlOnTrFt2zY+++wzvvvuO6Diz0v8QxKxEKJc
11vF3333HQ8//DAuLi537Vxff/017777LlZWVri6uvLmm29WWLZ27docO3aMs2fPYjAYePzxxwGI
iYmhS5cuDBgwABMTE2xsbGjZsmW5deh0Oj744ANMTU15+umn6dmzJytXriy37JUrV3g8P197PxZw
AqwpavXuu7bdFvAD6gB1gRDg+vAyn7w8ci9eZOjQoTz00EPo9Xpq166tLXYCcPjwYVJTU+nZs2e5
cWzfvh1PT0+Cg4NxcXGhU6dO2lSgERERDBs2jGeeeQYoWg+8vLWZFy5cSEhICN7e3uj1eiZNmsS+
fftKzDMeEhKChYUFbm5u+Pr6aq3exYsXM2HCBNq0aQNAo0aNcHNzIz4+noyMDCZPnoyJiQkeHh68
9tprfPXVVwCYmpqW+3mJf0giFkKUy9/fny+//JLIyEgGDx588wNuQ1paWokpNYuvalXa4sWLSUpK
4qGHHqJdu3baM9OKVuAqj42NDWbFFs9wd3cnLS2t3LKqsBCLYu+Lz/RtAK6vBZYHjAA8KErSnSjq
rlYUzR1ecPVqiZHgUDSt6/Vu8ejoaAYMGICpqWm5cbi4uDBv3jyOHj1KamoqdevW1T6Xyl57ZVay
Kr5oSfFV0io6R2pqKidPntTqtLGxITQ0VGu1R0RElPt5iX/IYC0hRLkaNmyIp6cnW7ZsKfGM8bq6
deuSm5urvb++3GJ5bjYo6frqT9d/KlR8VavSvLy8tOS1evVqXnzxRTIzM3Fzc9Pmzr6Zc+fOkZeX
h7m5OVA073iLFi3Kj12vJ6cSdYYBR4F4wIGibus2FCXiHIpW3yp9H5544glq167Nrl27+PLLL4mJ
ialU/K6urowZM4aXX34ZuPHqY8W5ubnx7rvvVmninIrO4ebmRqNGjSpcXrSiz+v6vRfSIhZC3EBE
RATff/99uX80H330UdasWUNeXh7Hjh1j8eLFFdbj5OR0w98UDxgwgNDQULKysvjrr7/4n//5nwrL
Ll++XFvT2MrKCp1Oh16v55VXXmHbtm2sWrWKgoICMjMz2b9/f7l1KKWYOnUqV65cYdeuXWzatKnC
Z5empqbE3WTpSShqGZsDlhRNxjKt2L54c3MMdeuWe5y/vz9BQUHUrl27xOCr4rKyspg2bRrJycko
pcjIyCAiIoL27dsD5a8+duTIkTL1jBw5ssorWb322muEhYWxd+9eAJKTkzlx4gSPP/44FhYWzJ49
m/z8fAoKCjh8+DAJCQlAxZ+X+IfcDSFECcVbbZ6entozwdL7xo8fj6mpKfXr1ycwMLDEqlmlyw4b
NozDhw9ja2tL3759y+yfOnWq1gJ/7rnnynSFFy/77bff0rx5cywtLRk/fjwrVqygTp06uLm5sXnz
ZsLCwrC1taV169YcOHCg3Gt0dnbGxsYGFxcXAgICWLhwIU2aNCm3bN169fiGohmzbtSuHwfkAvbA
k0CPa9szKVo1y7mCZ+wBAQEcOnSoxPKfpdWuXZuUlBS6dOmClZUVLVu2xMzMjCVLlgDlrz52vVeh
+L271ZWsir9/8cUXmTx5Mi+//DKWlpb4+fmRmZmJXq9n48aN7Nu3D09PT20hlezsbKDiz0v8Qyb0
EEI8UKoyWcjdXDUrPz8fJycn9u7dW+ln3OL+Ii1iIYS4ibEhIcwyN6/0Qh3XHQNmm5szNiSkwjIL
FizAx8dHkvADTAZrCSHETWirZgUHs7WS01xWZtUsT09PANauXXvnghU1jnRNCyFEJcmqWeJukEQs
hBC3ICEhgc9CQ9m4eTN+Oh0+eXlYUPQTpXhzc75Ril49ejA2JETWjxaVIolYCCGqoLqtmiVqLknE
QgghhBHJqGkhhBDCiCQRCyGEEEYkiVgIIYQwIknEQgghhBFJIhZCCCGMSBKxEEIIYUSSiIUQQggj
kkQshBBCGJEs+vCAOHPmTNEsQAcOcOH8eepZWeHdsiVDAgNlFiAhhDAimVnrPhcfH89noaFs2rKF
voBPfr42L27ctXlxe3bvztiQEHx8fIwcrRBCPHgkEd/Hrq8UMzEvjyEVrBRzjqKVYmbLSjFCCGEU
8oz4PrUoPJxZwcHsys1lXAVJGMAGGK8Uu3JzmRUczKLw8HsZ5g2lpqai1+spLCy8o/VaWFiQkpJy
R+sUQoiqqvGJuHPnztja2nLlypVKld+xYwdubm53OSrjiY2NxdPTk5GjR1MnN5eLlTzuL+DP3FyC
x44lISGhUsf4+voSERFR5VgrQ6fT3fE6c3Jy8PDwuOP1CiFEVdToRJyamkpcXByOjo6sX7++Usco
pW76x72goOBOhGcUQ4cOpb6NDXN1OlZDhS3h0qKAFkDdK1f4LDT0jsRSk++jEELcKzU6EUdFRdGl
SxcGDx5MZGRkiX2bN2+mefPmWFpa4ubmxty5c8nNzaVHjx6kpaVhYWGBpaUlp0+fZvr06fTv35+A
gACsra1ZunQply9fZty4cbi6utKgQQPGjx+vtbqvt6rnzp2Lk5MTrq6uJc6fnZ3N4MGDcXR0xNPT
kxkzZmj7li5dSseOHXnrrbewsbGhSZMm/PTTT0RGRtKwYUPq169PVFQUULQAef369Sn+GH/NmjU8
+uijFd6TWrVqcfDQIYYoxcNAw0rcx1xgFfAFcBFYu3Ej6enpAFy6dImAgADs7e2xsbGhXbt2pKen
8+6777Jr1y6CgoKwtLTkzTffBECv17NgwQK8vb3x9vYG4KeffuLxxx/Xjv/vf/+rndvX15d33nmH
du3aYWVlhZ+fH1lZWdp+pRTR0dG4u7vj6OjIRx99BMDff/9N3bp1OXfunFZ27969ODo6UlBQQHJy
Mp07d8ba2hpHR0cGDRqkldPr9fzxxx8A5Ofn8/bbb+Ph4YGNjQ1PP/00ly5dqvC6hRDijlM1WOPG
jdXy5cvVkSNHlKmpqTpz5oy2z9nZWf34449KKaWysrLUr7/+qpRS6ocfflBubm4l6pk2bZqqXbu2
Wr9+vVJKqby8PPXee++p9u3bq4yMDJWRkaGefPJJNWXKFK2OWrVqqWnTpqmrV6+qzZs3K4PBoLKy
spRSSgUEBKg+ffqoixcvqpSUFOXt7a0iIiKUUkpFRkYqU1NTtXTpUlVYWKjeffdd1aBBAxUUFKQu
X76sYmNjlYWFhbp48aJSSqnmzZurb7/9VovVz89PffLJJxXek5YtWqh6oFJAqUr+iwLV+Nrrl0E9
bGKiwmbPVkoptXDhQvX888+r/Px8VVhYqPbu3atycnKUUkp17txZLV68uMT5dTqd6tq1q8rKylL5
+fkqMzNT2djYqOXLl6uCggIVExOjbGxsVGZmplZHgwYNVGJiosrNzVX9+vVT/v7+SimlUlJSlE6n
U6+//rq6dOmS2r9/v6pTp476/ffflVJK9ezZU33xxRfaucePH6/Gjh2rlFJq0KBB6qOPPlJKKXXp
0iXtvwWllNLr9So5OVkppdTo0aOVr6+vOnXqlCosLFT//e9/1eXLl2943UIIcSfV2ES8a9cuZW5u
rv1xfPTRR9Wnn36q7Xd3d1eLFi1S2dnZJY6rKBF36tSpxDYvL68SCXDr1q3K09NTq8NgMKiCggJt
v6Ojo/r5559VQUGBql27tpYslCpKZr6+vkqpokTs7e2t7Tt48KDS6/UqPT1d22ZnZ6f279+vlFJq
5syZ6pVXXlFKKXX27FllMBjU6dOny70noaGhys3FRQ0F1QhU6rXk+r+g+t0gEf8L1DvXXn8DygLU
a9fOGRERoTp06KAOHDhQ5nwVJeIffvhBe79s2TLVrl27EmXat2+vli5dqtUREhKi7UtMTFS1a9dW
hYWFKiUlRen1epWWlqbtf/zxx9WKFSuUUkp99dVXqkOHDkoppQoKClT9+vVVQkKCUkqpwYMHqxEj
Rqi//vqrTNw6nU4lJyerwsJCZW5urg4ePFimzI2uWwgh7qQa2zUdFRVF165dqVevHgD9+/dn6dKl
2v7Vq1ezadMm3N3d8fX1Zc+ePTesr/QArrS0NBo2/Kdj193dnbS0NO29nZ0dev0/t89gMHDhwgUy
MjK4evVqmWNPnjypvXdyctJem5ubA2Bvb19i24ULFwDw9/dn48aN5OXlsXLlSp5++ukSxxc3b948
Hvb05F/A24AvkAr8CDxbwXWfALYD/a+9fw64AiQlJQEQEBBAt27dGDhwIA0aNGDixIk3ffbboEED
7XVaWhru7u4l9pe+H8Xvvbu7O1euXCEjI0PbVvx6r99ngD59+vDbb7+RmppKbGws1tbWPPbYYwB8
/PHHFBYW8vjjj9OiRQuWLFlSJs6MjAwuXbpEo0aNyuwbPHhwieueNGmSPPMWQtwVNTIR5+fns3Ll
Sr7//nucnZ1xdnZmzpw57N+/n4MHDwLw2GOPsXbtWtLT03nhhRcYMGAAUPEo3NLbXV1dSU1N1d6n
pqbi4uJy09js7e0xNTUtc6yrq+stX+f1OJ544glWr15NdHQ0AQEBFZa9evUqdQwGcoDRwGtAZ+AH
YHAFxywDFNADcAY8gavAiTNngKJnzu+99x6HDx/mp59+YuPGjdoz7MrcSxcXlzI/FTp+/HiJ+3Hi
xAntdWpqKrVr1y7xxaQiderUoX///ixbtqzMvXF0dGTRokWcPHmSL774gtGjR2vPha+zt7fHzMyM
5OTkMnWbmJiUuO4NGzZo1y2EEHdSjUzE33zzDbVq1eK3335j//797N+/n99++42nnnqKqKgorl69
ypdffkl2djYmJiZYWFhgYmICFLWuzp49S3Z29g3PMXDgQD788EMyMjLIyMjggw8+uGESvE6v19O/
f38mT57MhQsXSE1N5ZNPPrnhseomc6oEBAQwe/ZsDh06RN++fSss179/f/YnJbGtdm0KgMeBTKAO
Rcm1PFEMvxC5AAAgAElEQVTANGAfsP/av061a/NXWhrnzp3jhx9+4NChQxQWFlKvXj1MTU1L3MvS
ya20Hj16cPToUb766isKCgpYsWIFv/32G7169dLKREdH8/vvv5Obm8vUqVPp37+/lswrc28iIyPZ
sGFDiXu8atUqrdVtbW2NXq8v0YMBRV8YAgMDeeuttzh16hSFhYXs2bOHy5cvl3vdpY8XQog7oUb+
ZYmKiuLVV1/F1dUVR0dH7d+YMWNYvnw5AMuWLcPT0xNra2sWLVqkbW/atCmDBg2iUaNG2Nracvr0
6XLP8e6779K2bVtatmxJq1ataNu2LZMnT64wpuKtwM8//xyDwUCjRo14+umn8ff3JzAwsFLHlve+
b9++pKam0rdvX8zMzCqsZ+7cufTu3ZvVly9jDUwH1gKtgH5A6Y7Vn4HjFLWeHa/9qwX8otfTpEkT
YmJiOH36NC+++CJWVlY0b94cX19f/P39ARg7dixff/01dnZ2jBs3rtzYbW1t2bhxI2FhYdjb2xMW
FsamTZuwtbXVygQEBDBkyBBcXFy4fPkyn332WaXvTYcOHdDpdLRp06ZEF3d8fDzt2rXD0tKSPn36
MG/ePO23w8XrCAsLo0WLFvj4+GBnZ8ekSZNQSpV73ZX5IiaEELdKprisIZo0acLChQt55plnblrW
v29f2q5dy7gqfLSf6HTs9fNj2erVVQnzll1PcK+++mqV6/jXv/7Fyy+/fFt1CCGEsdTIFvGDZs2a
Neh0ukolYYCxISHMMjfn2C2e5xgw29ycsSEhtxyjsSQkJPDrr7/y0ksvGTsUIYSoEknE1Zyvry+j
R49mwYIFlT7Gx8eH6WFhdDMYKp2MjwHdDAamh4XRtm3bKsVaFbczheXQoUPp0qULn376KXXr1r2D
UQkhxL0jXdP3sXmffsqU8eOZotMRWMHCD5kUrb70say+JIQQRlHL2AGIuycrO5snunXj17p1+WDz
Zvx0Onzy8rT1iOOvrUfcq0cPNoSE3NOWsBBCiCLSIr5PnTlzhmbNmhEfH4+npyfp6elERUZy5OBB
cs6dw8LGBu8WLRg8dCgODg7GDlcIIR5YkojvU0FBQZiamvLJJ58YOxQhhBA3IIn4PnT06FGefPJJ
fvvtt0rNUCWEEMJ4ZNT0fWjy5Mm89dZbkoSFEKIGkBbxfSYuLo5+/fqRlJSEwWAwdjhCCCFuQlrE
9xGlFBMmTGDatGmShIUQooaQRHwf2bRpE+np6QwZMsTYoQghhKgkScT3iYKCAiZNmsTMmTOpVUt+
Hi6EEDWFJOL7xNKlS7G1tS2xvKAQQojqTwZr3Qdyc3Np2rQpX3/9NU888YSxwxFCCHELpEV8H5g3
bx7t2rWTJCyEEDWQtIhruLNnz/LQQw/x448/4u3tbexwhBBC3CJJxDXcW2+9RX5+/i0tkyiEEKL6
kERcg6WkpPDYY4+RmJiIk5OTscMRQghRBfKMuAZ79913eeONNyQJCyFEDSYt4hrq119/pUePHhw5
cgQLCwtjhyOEEKKKpEVcQ02cOJH33ntPkrAQQtRwkohroO+++46UlBSGDx9u7FCEEELcJknENUxh
YSETJ04kNDQUU1NTY4cjhBDiNkkirmFiYmKoU6cOffv2NXYoQggh7gAZrFWDXLp0iYceeoioqCie
euopY4cjhBCaM2fOEBUZyZEDB7hw/jz1rKzwbtmSIYGBODg4GDu8ak0ScQ3yySefsH37dtavX2/s
UIQQAoD4+Hg+Cw1l05Yt9AV88vOxAHKAOHNzvlGKnt27MzYkBB8fHyNHWz1JIq4hsrKy8Pb25ocf
fqBZs2bGDkcIIVgUHs7U4GAm5uUxRClsyilzDojU6Zhtbs70sDBeHzXqXodZ7cnCtTXEzJkzef75
5yUJCyGqhUXh4cwKDmZXbi6NKyhzAmgOnFeK3rm5dAsOBpBkXIq0iGuAEydO8Oijj3LgwAFcXV2N
HY4Q4j4WGRnJ3LlzSU5OxsrKij59+hAaGoqVlZVWJj4+nuc7dy6ThD2BxcAzFdR9DHjKYGDDjh20
bdv27l1EDSOjpmuAqVOnMmLECEnCQoi7as6cOYSEhDBnzhyys7PZs2cPqampdOnShatXr2rlPgsN
ZWJeXoUt4Yo0Bibk5fFZaOgdjbumkxZxNXfo0CGeffZZjhw5UuIbqRBC3Ek5OTm4uLgQGRlJv379
tO0XL16kUaNGzJo1i9TUVH755Re+3bSJOoWFNAWWAC2AwcBywAwwAaYA/SlqJV+lqNV3DggCYgBr
Gxs6d+7MmjVrOHv2LEOHDmX37t3o9XoeeeQRduzYcS8v36jkGXE1N2nSJEJCQiQJCyHuqp9++olL
ly7h5+dXYnvdunXp3r073333Hd7e3mzevJlOJibEFhbyKfACcBSIAnYBEYDvtWNTAV2xuvwBS+Bl
MzNaTZzIE08+CRS1xN3c3Dh79ixKKfbs2XNXr7W6ka7pamzHjh0kJiYySgY2CCHusoyMDOzt7dHr
y6YFZ2dnMjIyALCzsaH/lSuYAG8B+UDxtFlRF+spYCuwEOiQn8+xw4e1+RBMTU05deoUf/75JyYm
JnTo0OGOXVdNIIm4mlJKMWHCBD788EPq1Klj7HCEEPc5e3t7MjIyKCwsLLPv1KlT2NvbA2Bmasr1
pWZ0QAMgrRL1/wXYUtQitgByzp3T9k2YMAEvLy+6du1K48aNmTVr1m1dS00jibiaWrVqFVevXmXg
wIHGDkUI8QBo3749derUYc2aNSW2X7hwgS1btvDss88CkH/lCjnX9imKEuz1YaQ6KuYGZALZFE32
YWHzz6+O69atS1hYGMnJyaxfv565c+eyffv2O3FZNYIk4mroypUrvPPOO8yaNavcbiIhhLjTLC0t
mTJlCm+88QZbt27l6tWrpKSk8NJLL9GwYUMCAgIAOHvuHF+bmlIAfELR4Kx21+qoD/xRql5VbF93
YDSw28wMr2bN2LVrFwCbNm0iOTkZAAsLC2rVqvVA/e2TwVpGcqN5WVeuXEmjRo3417/+ZewwhRAP
kH//+9/Y29sTHBzMH3/8gaWlJX5+fnz55Zfaam89e/Zky8aNWAPewDcUjZIGmAS8AUwA3gX6UbKV
vAwYBazIz2fL7Nk888wzPPXUUxw9epSgoCAyMjKwsbFhzJgxdOrU6R5dtfHJz5fusZvOy1pYiA74
fPFiXnnlFeMGK4QQxUyfPp3k5GQKL1yg7dq1jKtC+vhEp2Ovnx/LVq++CxHWTNIivoeKz8v6eTnz
so7My2MORcP/g19/nYvZ2TIVnBCi2hkbEsLzW7fS6wbTW5bnGDDb3JwNISF3K7Qa6b7ohB81ahQz
Zswwdhg3VHxe1nGlkvCXwHPXXtsAbwO7cnOZFRzMovBwrdz06dO15zTVVWhoKK+//nqlyvr6+hIR
EVHuvtTUVPR6fbkjOIUQxuXj48P0sDC6GQwcq+Qxx4BuBgPTw8JkesvSlLipTp06KTMzM2VhYaEc
HBxU37591enTpyt9fFxcnKpvMKijoFJA6UAVgFI3+XcUVH2DQcXHxyullJo2bZoKCAi449f3yy+/
qMcee0zVq1dPNW3aVMXGxt6w/A8//KD0er2ysLDQ/j3//PO3fN7OnTurxYsXl7svJSVF6fV6VVBQ
cMv1CiHujYULFqj6BoOaq9OpzAr+jp0FNUenU/UNBrVwwQJjh1wt3Rct4rtNp9OxYMECsrOzOXLk
CFlZWYwfP77Sx1+fl9WTohGEOir+0Xtx92pe1qCgIHr27ElOTg5bt26lQYMGNz3G1dWV7Oxs7d+6
devuaoxCiOrn9VGj2LBjB3v9/GhkZsZQMzPCgWggHHjV3BwvMzN+9fNjw44d8qitAtUuEc+fP7/E
+1atWml/5MePH4+TkxNWVla0atWKxMREAAIDA5kyZYp2zLp162jdujVWVlY0adKE2NhYoGhVES8v
LywtLfHy8iImJqbScalrgxKsra3p168fhw4dAmDz5s20adMGKysr3N3dmT59unbM9e7VNRs2MEcp
ngU6UZSErSn6YfvPwFLgqWLnOgx0BeyAWUqxav160tPTy8S0Z88eOnTogI2NDa1bty4xN+utXKup
qSkNGzYEwN3dnYcffrjS96W00t3nN4qxuMLCQoKDg3FwcKBx48Zs2rSpxP7b+eyEEHdP27ZtWbZ6
NUeOH8dmxAg+tLFhc69e7AsIoPn06Rw5fpxlq1dLd/QNVLvBWsuWLWPMmDEA7N+/n7S0NHr27Els
bCy7d+/m2LFjWFhYkJSUhLW1dZnj4+LiGDJkCGvWrOGZZ57h1KlT5OTkkJuby9ixY/nll19o3Lgx
f//9N5mZmbccX0ZGBqtXr6ZNmzYA1KtXj2XLltG8eXMOHTpEly5daN26Nc8//7x2jGthIQco+tZz
GmhE0Y/arw/r/73Y6wtAF4qG/28ErgADTUyIiowsEcfJkyfp1asXy5cvp1u3bmzbto1+/fqRlJSE
ubn5LV2rj48PEyZMoE2bNrRu3fqW70lpOp3upjHa2dmVOGbRokVs3ryZ/fv3YzAY6Nu3r7bvTn12
Qoi7x8HBgedfeIF9+/fz5YYNxg6nRql2LeKjR49qP+yOjo7mpZdeolatWpiampKTk0NiYiJKKZo2
bYqTk1OZ4yMiIhg2bBjPPFO0IqazszPe3t4AmJiYcPDgQfLz83Fycrqllt8bb7yBra0trVu3xtXV
lTlz5gDw9NNP07x5cwAeeeQRBg4cWKbVN7SwEHOg+ESVFXVNbwScgXFAbaAu0OPSJY4cPFii3PLl
y+nZsyfdunUD4Nlnn6Vt27Zs3rz5lq71q6++Yvv27SxbtoxevXrx66+/ArBt27YbfoM9efIktra2
2NjYYGtry6pVq8qUuVmMxX399deMGzcOFxcXrK2tCSk1qvJ2PjshxL1x/vx5WaCmCqpdIh4wYADR
0dEopYiJidG6OX19fQkKCmLMmDE4OTkxcuRILly4UOb4EydO4OXlVWa7wWBgxYoVhIeH4+zsTO/e
vUlKSqp0XJ9//jmZmZmcOHGCqKgorUUXFxfHM888g6OjI9bW1ixcuFCbHB0ApWh4C9d/Aigdfel5
WaGo23vlypXY2tpqCfHHH3/k1KlTt3St8+bNY+LEifTo0YMvvviCHj168Ouvv/Ljjz9qU9qVx9XV
lczMTM6dO0dmZiYvvvhimTIVxXj69OkyZdPS0nBzc9Peu7u7a69v97MTQtwbWVlZkoiroNol4sGD
BxMdHc22bduoW7cu7dq10/YFBQWRkJBAYmIiSUlJfPzxx2WOd3Nz01rUpXXp0oXY2FhOnz5N06ZN
GT58+G3H+/LLL9OnTx9OnjxJVlYWI0aM0J4nA6DTafOywo3nYoWi+VhLR196XlYous7BgweTmZmp
JcScnBwmTJgAVP5ar169yuXLlwHo3bs3YWFhdO3alSVLlhAUFHTT67/htVQQ47///e8yZZ2dnTlx
4oT2PjU1tcT+u/HZCSHuLGkRV021S8Tt27dHp9Px9ttvlxj0k5CQQFxcHFevXsXc3BwzM7Ny5yId
NmwYS5YsYfv27SilSEtLIykpiTNnzrB+/Xpyc3MxNTWlXr16mJgUTcx2fVDV8ePHbzneCxcuYGNj
g6mpKXFxcXz55ZdlysQXWz3JgaKbXv5XBehF0XPkecBlip4Zb65TB+8WLUqU8/f3Z8OGDcTGxlJY
WEh+fj47duwgLS3thtdaWv/+/Xn//fc5cOAASim8vb0xGAzk5eWV/EJRBTeKsbQBAwYwb948Tp48
yblz50qsvnIr1yOEMJ7z58+XO3ZH3Fi1S8RQ1Co+dOgQ/v7+2rbs7GyGDx+Ora0tnp6e2Nvbl9uy
8vHxYcmSJYwbNw4rKys6d+7M8ePHKSwsZO7cubi6umJvb8/OnTsJvzZZxvHjx/Hw8MDV1bVMffDP
4KPyLFiwgPfeew8rKys+/PBDXnrppTLHfgNc71g2ByYDHShaEiyuVH31gO+A9RRNkt4Y+L+CAgYP
HVqiXIMGDVi3bh0fffQRDg4OuLu7ExYWRmFh4Q2vtbTg4GBeffVV/Pz8sLS0ZOTIkcydO5chQ4bQ
q1cvcnJyyj2uMm4U4/V7c93w4cPp1q0brVq1om3btvTr10/bdyvXI4QwHumarppqOdd0dHQ0ixYt
YufOnffkfDNmzMDR0fGudXf69+0r87IKIe57w4YNo3379rz22mvGDqVGqXY/X8rNzWX+/Pm3/Xzy
VkyePPmu1i/zsgohHgTSNV011a5r2tHREWdnZwYNGmTsUO4YmZdVCPEgkMFaVVPtWsTl/STpfnB9
arengoOZkJfH0HJWXwLIBCJ1Oj42N2d6WJhMCSeEqDHkGXHVVLsW8f2s9Lysr5qby7ysQoj7hrSI
q6ZaDtZ6EKSnpxMVGcmRgwfJOXcOCxsbvFu0YPDQoTg4OBg7PCGEuGVOTk4cOHCg3FkPRcUkEQsh
hLgj6tSpw/nz5zEzMzN2KDWKdE0LIYS4bfn5+QCShKtAErEQQojbJj9dqjpJxEIIIW6bDNSqOknE
Qgghbpv8dKnqJBELIYS4bdIirjpJxEIIIW6bPCOuOknEQgghbpt0TVedJGIhhBC3Tbqmq04SsRBC
iNsmXdNVJ4lYCCHEbZOu6aqTRCyEEOK2Sdd01UkiFkIIcduka7rqJBELIYS4bdIirjpJxEIIIW6b
PCOuOknEQgghbpu0iKtOErEQQojbJs+Iq06nlFLGDkIIIUTNpZTC1NSUvLw8TE1NjR1OjSMtYiGE
ELfl4sWL1KlTR5JwFUkiFkIIcVukW/r2SCIWQghxW2Sg1u2RRCyEEOK2yE+Xbo8kYiGEELdFWsS3
R0ZNCyGEqJIzZ84QFRlJ7IYNpCYn0+mZZ/Bu2ZIhgYE4ODgYO7waQxKxEEKIWxIfH89noaFs2rKF
voBPfj4WQA4QZ27ON0rRs3t3xoaE4OPjY+Roqz9JxEIIISptUXg4U4ODmZiXxxClsCmnzDkgUqdj
trk508PCeH3UqHsdZo0iz4iFEKKa8/X1JSIi4o7WOWrUKGbMmHFLxywKD2dWcDC7cnMZV0ESBrAB
xivFrtxcZgUHsyg8/LbjLW7Hjh24ublp7x955BF27txZpbo8PT35/vvv71RoVVLLqGcXQggBgIeH
B2fOnKFWrVrUrVuX5557jvnz52MwGO7K+cJvMTnGx8cz9VoSblzJYxoDrXJzGTF6NO6NGtGtW7db
jrMiOp1Oe33o0KE7Vq8xSItYCCGqAZ1Ox6ZNm8jOzmbv3r0kJCTw4YcfGjsszWehoUzMy6t0EgbI
Bf4PcAbe+fe/705g9wFJxEIIUU1cH7Lj7OxM9+7dS7T0UlJS6NixI5aWljz33HNkZmYC0KtXL+bP
n1+inlatWrFu3ToAxo8fj5OTE1ZWVrRq1YrExEQAAgMDmTJlinbMunXraN26NVZWVjRp0oTY2FgA
IiMj8fDwYPk33/CZUsTcwvWsBjyBacC+Q4dIT0/X9k2fPp3+/fszcOBALC0tadu2LQcOHND2e3p6
MnPmTJo3b46dnR3Dhg3j8uXL5Z6nePeyUoqZM2fSuHFjHBwcGDhwIFlZWVrZZcuW4eHhgYODAx99
9NEtXM3dI4lYCCGqmRMnTrB582batGmjbYuJiWHp0qWkp6dz6dIlwsLCABgyZAjLli3Tyu3fv5+0
tDR69uxJbGwsu3fv5tixY5w/f56VK1diZ2dX5nxxcXEMGTKEOXPmcP78eXbu3ImHhwe5ubmMHTuW
gQMGEGhmxh7g0Vu4jqXAS8AgQKcUoaWeSa9fv56XXnqJc+fOMWjQIPr06UNBQYG2/8svv+S7774j
OTmZpKSkSvUQzJs3j/Xr17Nr1y7S0tKwsbFh9OjRACQmJjJ69GiWL19OWloaZ8+e5eTJk7dwRXeH
JGIhhKgm+vTpg62tLU8//TS+vr6EhIRo+wIDA/Hy8qJOnToMGDCAffv2AfD8889z9OhRkpOTAYiO
juall16iVq1amJqakpOTQ2JiIkopmjZtipOTU5nzRkREMGzYMJ555hmgqEXu7e0NgImJCb/8/DOt
8/NxAh6u5LUcB34A+gMWwCPAd1u3lijz2GOP4efnh4mJCW+99Rb5+fns2bNH2//GG2/g4uKCtbU1
kydPJibm5u3xhQsXMmPGDJydnTE1NWXKlCmsWrWKwsJCVq9eTe/evenQoQOmpqZ88MEHJZ41G4sk
YiGEqCbWrVtHZmYmf/75J59//jl16tTR9tWvX197bTAYuHDhAoCWmKOjo1FKERMTQ0BAAFA02joo
KIgxY8bg5OTEyJEjteOKO3HiBF5eXmW2GwwGVqxYwaHERCYBvYGkSl7LMoqSb5Nr79sDR//4o0SL
t/jIZ51OR4MGDUhLS9O2NWjQQHvt7u5eYl9FUlNT8fPzw9bWFltbW5o1a4apqSl///03aWlpJc5p
MBjK7SG41yQRCyFENVHVaR0GDx5MdHQ027Zto27durRr107bFxQUREJCAomJiSQlJfHxxx+XOd7N
zU1rUZfWpUsXenfrxkygKTC8kjEtA45SNFDLGYgGLl+5wubNm7UyJ06c0F4rpfjrr79wdXUtd39q
aiouLi43PW/Dhg3ZsmULmZmZZGZmcu7cOS5evIizszPOzs4l6szNzeXs2bOVvKK7RxKxEELUcO3b
t0en0/H2229rrWGAhIQE4uLiuHr1Kubm5piZmaHXl/2zP2zYMJYsWcL27dtRSpGWlkZSUhJnzpxh
/fr1eDz0EHvr1KEeYHLtmFSKEsjxcuL5L/AHEA/sv/avl5kZrR99lKioKK3cL7/8wtq1aykoKOCT
Tz7BzMysxJeI+fPnc/LkSTIzM/noo48YOHDgTe/FiBEjeOeddzh+vCiy9PR01q9fD8CLL77Ixo0b
+emnn7hy5QpTpkyp8pefO0kSsRBCVAM3elZZmeeYgwcP5tChQ/j7+2vbsrOzGT58OLa2tnh6emJv
b8+/y/kZkY+PD0uWLGHcuHFYWVnRuXNnjh8/TmFhIXPnzmV2WBhLL13ie+D6r4+PAx6Aa5naIAro
AzQDHCmasOJbIHTmTDZu3KiNYn7hhRdYsWIFNjY2LF++nDVr1mBiYqLV8/LLL9O1a1caN25MkyZN
mDx58k3vz9ixY3nhhRfo2rUrVlZWPPnkk8TFxQHQrFkz5s+fz6BBg3BxccHOzq5E97exyBSXQghx
H4iOjmbRokVVnmHqZvz79qXt2rWMu5YyZlCUZCvTVf2JTsdePz+WrV6tbZs+fTrJycklWsjFeXp6
snjxYm0A2f1MWsRCCFHD5ebmMn/+fEaMGHHXzjE2JIRZ5uYcu/Z+MpVLwseA2ebmjC02AlyUJIlY
CCFqsNjYWBwdHXF2dmbQoEF37Tw+Pj5MDwujm8GgJeObOQZ0MxiYHhZG27Ztb+l81eFnRfeKdE0L
IYSotOurL03Iy2NoBQs/ZFK0+tLHsvpSpUgiFkIIcUsSEhL4LDSUjZs346fT4ZOXp61HHH9tPeJe
PXowNiTkllvCDyJJxEIIIaokPT2dqMhIjhw8SM65c1jY2ODdogWDhw7FwcHB2OHVGJKIhRBCCCOS
wVpCCCGEEUkiFkIIIYxIErEQQghhRJKIhRBCCCOSRCyEEEIYkSRiIYQQwogkEQshhBBGJIlYCCGE
MCJJxEIIIYQRSSIWQgghjEgSsRBCCGFEkoiFEEIII5JELIQQQhiRJGIhhBDCiCQRCyGEEEZUy9gB
iOrhzJkzRQt8HzjAhfPnqWdlhXfLlgwJDJQFvoUQ4i7SKaWUsYMQxhMfH89noaFs2rKFvoBPfj4W
QA4QZ27ON0rRs3t3xoaE4OPjY+RohRDi/iOJ+AG2KDycqcHBTMzLY4hS2JRT5hwQqdMx29yc6WFh
vD5q1L0OUwgh7mvyjPgaX19fIiIi7mido0aNYsaMGXe0zjtlUXg4s4KD2ZWby2dK8WsF5WyA75Ti
7dxcZgUHsyg8vMT+1NRU9Ho9hYWFAPTo0YNly5ZVOa7Q0FBef/31SpWdPn06AQEBAJw4cQJLS0vk
e6UQoqZ5oBKxh4cHBoMBS0tLnJ2dCQwMJDc3966dLzw8nMmTJ9+1+jt37oxer+fgwYMltvv5+aHX
69m5c2e5x8XHxzM1OJitubk0LrVvOjC41LbNQDCwNTeXqcHBJCQklNiv0+n+Kbt5s5YcqyIkJIRF
ixZVuvz1c7u5uZGdnV0iFiGEqAkeqESs0+nYtGkT2dnZ7N27l4SEBD788ENjh1VlOp2Opk2bEhUV
pW3LzMxkz549ODo6VnjcZ6GhTMzLK5OEb6YxMCEvj89CQ6sWcA11vbUvhBB3wwOViAGt69LZ2Znu
3btz6NAhbV9KSgodO3bE0tKS5557jszMTAB69erF/PnzS9TTqlUr1q1bB8D48eNxcnLCysqKVq1a
kZiYCEBgYCBTpkzRjlm3bh2tW7fGysqKJk2aEBsbC0BkZCReXl5YWlri5eVFTExMpa/nlVdeYcWK
Fdp1xcTE0LdvX2rXrq2VKR7HmTNnWLdpEx+X04W7FfgIWAFYAK2vbfcFrnfaByjF1+vWYW9vT+PG
jdm0aVOJOop38ScnJ9O5c2esra1xdHRk0KBBWrnDhw/TtWtX7OzscHZ2ZubMmUDJ7ubr3d7/+c9/
cHV1xdXVlTlz5pR7H0p3kfv6+jJlypRyP0+AAQMG4OzsjI2NDZ07d9Y+s+v3a/To0fTs2RMLCwvm
zp1L/fr1S3R7r1mzhkcffbTcWIQQ4lY8cIn4uhMnTrB582batGmjbYuJiWHp0qWkp6dz6dIlwsLC
ABgyZEiJ55779+8nLS2Nnj17Ehsby+7duzl27Bjnz59n5cqV2NnZlTlfXFwcQ4YMYc6cOZw/f56d
O3fi4eFBbm4uY8eOZevWrWRnZ/PTTz/d0h94FxcXmjVrpiX1qKgoBg8eXOGz0qjISJ4CTMrZ1w14
B/QI9MsAAB7ZSURBVHiJolHT5T03XgWYFRYyeuRIEhISWLVqVYWxvffee3Tr1o2srCz++uuv/2/v
zuOiOO8/gH8WRGBhYXflWnQF5NIYDEXwQgmQolUxClaLcgRi+LV4VLTEiKlnogS1sZ6oqUXRxFRN
ooIXxiutmoAv6xHT4AECQhEiiCC7XPv9/QFMWG4SdW38vl8vXy9mZ56ZZ55d9zMz+zwzmDNnDgCg
srISAQEBGDduHP773//i9u3beO2114RyLS8vnz17Fnfu3MGJEyeQmJiI06dPt7m9luXaez+Bht+y
79y5g+LiYnh4eCA0NLRV2cWLF6OiogJz5syBhYWF0MYAsGfPHkRGRra774wx1lUvXBBPmjQJcrkc
Pj4+8PPzQ3x8vDAvKioKjo6OMDQ0xNSpU3HlyhUAwOuvv45bt27hzp07ABq+hH/3u9+hR48eMDAw
QEVFBb777jsQEVxdXWFtbd1qu3//+98xY8YM+Pv7A2g4I3dxcQEA6Ovr4/r161Cr1bC2tsaAAQO6
tU8RERHYtWsXsrKyUF5ejqFDh7a77M1r19C/pqZb629uP4DxRLiflwepVKrVfi0ZGBggNzcXBQUF
6NmzJ0aMGAEASEtLg0KhQGxsLHr27AkTE5MOh0YtW7YMRkZGePnllxEVFdXlKwbtvZ8AEBkZCbFY
DAMDAyxZsgRXr15FRUWFMH/ixIkYNmwYAMDQ0BDh4eHCwVhpaSlOnDihdYbPGGM/1QsXxIcOHUJp
aSlycnKwceNGGBoaCvNsbGyEv8ViMSorKwFA+CLfs2cPiAh79+4VLp/6+flh9uzZmDVrFqytrfGH
P/xBKNdcfn4+HB0dW70uFovxj3/8A0lJSVAoFJgwYQKysrK6tU9BQUE4ffo0Nm3a1GlHqcrycoi7
tXZthQBsAVSUlQEA7Ozs2l12zZo10Gg0GDJkCNzc3JCcnAyg/bZoi0gkQp8+fYRpOzs7FBYWdqls
e++nRqPBwoUL4eTkBKlUCgcHB4hEIvzwww/C8kqlUmtdYWFhSEtLg0qlwr59++Dj49PmARdjjHXX
CxfEP3V4S0REBPbs2YNTp07BxMRE66xz9uzZuHTpEr777jtkZWVhzZo1rcorlUrhjLqlgIAApKen
o6ioCK6uroiOju5W3YyNjTF27Fhs3boVEREt+zwDJiYmQu9wU3Nz/LeDdXXW51iBhjCWyBpGHefm
5ra7rJWVFbZv346CggJs3boVM2fORHZ2dodt0RIRIT8/X5jOy8uDra1tl8q25+OPP0ZqaipOnz6N
hw8f4u7duyAirc9Gy8vcvXv3xrBhw/DZZ59hz549P6tnOGOMNffCBfFPNXz4cIhEIvzpT3/S+hK+
dOkSMjIyUFdXB2NjYxgZGUFPr3WzzpgxA8nJyThz5gyICIWFhcjKykJxcTEOHz6MqqoqGBgYwNTU
FPr6Db/gNnVAysvL67R+CQkJOHfuXKszOQBwd3fH0aNHUVZWBhsHB6R2MMTHGsBdAO0drkwFcFQk
gnXfvigrK0NiYmK76zpw4AAKCgoAAFKpFHp6etDT00NgYCCKioqwYcMG1NTUoLKyEhkZGe2u5733
3oNKpcKNGzeQnJyMkJCQNpfr6kFWZWUlDA0NIZPJ8PjxY8THx3dp2FN4eDhWr16Nb7/9FsHBwV3a
FmOMdeaFCuKOvmy78kUcERGBb7/9FmFhYcJrjx49QnR0NORyORwcHGBhYYG33367VVkvLy8kJycj
NjYW5ubm8PX1RV5eHjQaDT788EP07t0bFhYW+Oqrr5DUeNOMvLw82Nvbo3fv3p3W2cbGRvgNtuW8
8PBwDBo0CPb29vj8iy9Qqa+P5gNymu/5FDSEcC8Anm3MnwxApaeHzUlJ8PT0xOTJk9utU2ZmJoYO
HQozMzNMmjQJGzZsgL29PUxNTXHy5EkcPnwYNjY2cHFxwdmzZ9vcRwB49dVX4eTkhICAACxYsECr
Y1d72+7o/YyIiEDfvn3Ru3dvvPzyy1rt1pHg4GDk5uYiODgYRkZGXSrDGGOd4VtcdsOePXuwffv2
dm+U8aStXLkSVlZW3b5U3Zmw4GB4HjyI2J/w1q8TiXA5KAi7P/vsidapLbm5uejXrx9qa2vbvMqg
C87Ozti2bZvQ6Y4xxn4ufvpSF1VVVWHz5s2YPXv2M9vm07or19z4eLx+4gQC27izVkduA1htbIzU
DnpKP2nP03Hi559/DpFIxCHMGHuino/TjOdceno6rKysoFAofhFDVry8vLB87VqMEYtxu4tlbgMY
IxZj+dq18PT07HT5J+V5uWWln58fZs6ciS1btui6KoyxXxi+NP0Ca3r60gKVCpHtPH2pFA1PX1rD
T19ijLGngoP4BXfp0iWsT0hA2tGjCBKJ4KVSCc8jzmx8HnHguHGYGx//TM+EGWPsRcFBzAAAJSUl
SNm5EzevX0dFWRkkMhlc3NwQERkJS0tLXVePMcZ+sTiIGWOMMR3izlqMMcaYDnEQM8YYYzrEQcwY
Y4zpEAcxY4wxpkMcxIwxxpgOcRAzxhhjOsRBzBhjjOkQBzFjjDGmQ/z0JcbYL15xcXHDneOuXUNl
eTlMzc3hMmgQ3oiK4jvHMZ3jO2sxxn6xMjMzsT4hAUeOHUMwAC+1WriXekbjvdTHjx2LufHx8PLy
0nFt2YuKg5gx9ovU9HSxd1QqvNHO08XK0PB0sdX8dDGmQ/wbMWOs27KysmBgYKDrarRre1ISEuPi
8M+qKsS2E8IAIAMwjwj/rKpCYlwcticldWn9Tk5O+Oabb55YfZu89tpr2L9//xNfL3u+8RkxYy8o
iUQCkUgEAHj8+DEMDQ2hr68PkUiEbdu2Ydq0ae2WzcrKgpubG2pqap5VdbssMzMTr/v64p9VVXDq
RrnbAEaJxUg9d+6ZPPIzPj4eDx48wPbt25/6ttjzjc+IGXtBVVRU4NGjR3j06BHs7Oxw5MgR4bWO
Qvh5tz4hAe+oVN0KYQBwArBApcL6hISnUS3G2sVBzBgDEaHlxTGNRoP33nsPjo6OsLKyQnh4OB49
etRm+bKyMrzxxhtQKBSws7PDihUrtOZv2bIFAwYMgJmZGV555RXcuHEDAHD9+nX4+PhAJpPB3d0d
x48fF8pMmzYNsbGxGD16NCQSCfz9/VFcXIxZs2ZBJpPBzc1NWA8AKBQKrFixAnsPHsRiIswCUAQg
AIA5gPEAKhuXPQHAucU+KAAMIELa0aOYO3cuwsLCMH36dJiZmcHd3R3Xrl3T2taFCxcAAPX19Vi+
fDkcHR0hlUoxdOhQFBcXAwBmzpwJpVIJc3NzDBs2TLicfejQIXz44YfYtWsXJBIJhg0bBgAYPnw4
PvnkE6H9ly5dCjs7OygUCrz11lt4/PgxgB9/Gti5cyeUSiWsra2xdu1aoX4XLlyAh4cHzM3NYWtr
i3fffbfN9409J4gx9j/h/v37tCYxkaJDQ2laYCBFh4bSmsREKi4u/tnrtre3p1OnTmm99sEHH5CP
jw8VFRVRdXU1RUVFUVRUFBERff/992RgYCAsO3bsWJo7dy6p1WoqKioiDw8PSklJISKilJQUsre3
p6tXrxIR0c2bN6mgoIDUajX17duX1q1bR3V1dXTixAkyNTWlu3fvEhFRSEgIKRQKun79OqnVaho5
ciTZ29vT/v37SaPR0Ntvv01jx44V6mBjY0P9HBxouqEh5QMkA2gIQDcAUgM0EqDVABFAxwFybvy7
6Z8NQOcBijI2Jn8/PzIxMaFTp06RRqOhefPmka+vr9a2zp8/T0REK1asIA8PD8rOziYioitXrlB5
eTkREe3evZvKy8uprq6OVq1aRUqlkurq6oiIaOHChRQdHa3V5sOGDaOPP/6YiIg2b95ML730EuXn
51NFRQUFBgYKy3///fckEolo9uzZVF1dTZmZmdSzZ0/KyckhIqJf/epXdODAASIiqqyspIyMjO5/
KNgzw0HM2HMuIyODQoOCSGpkRG8aGVESQHsASmoMDamREYUGBf2sL9u2gtjBwYEuXLggTGdnZ5NY
LCYi7SC+e/cumZqaCgFDRJScnEzjxo0jIqJXX32VPvroo1bbPHnyJNnb22u9FhQURImJiUTUEMR/
/OMfhXlr1qwhDw8PYTozM5MUCoUwbWNjQwE+PpTUGKzjAZrfLGjXADStC0G8BSD3gQNpwoQJwrov
X75MMplMa1tNQWxnZ0cnT57ssH2JiDQaDYnFYrp58yYRdR7E3t7elJycLMy7evWqVvvr6elRaWmp
MH/QoEF06NAhIiIaOnQorVq1ih48eNBpvZju8aVpxp5j25OS8LqvLzwPHkS2Wo0dajX+ACAUwB8A
/F2lQrZajcEHD+J1X98u9/rtivz8fIwbNw5yuRxyuRweHh4AgNLSUq3l8vLyoFKpYGlpCblcDplM
htjYWOHybH5+Pvr169dq/YWFhejbt6/Wa3Z2digoKBCmra2tAfx46dzU1BTnz5/HF198gbS0NJSW
lmLu3LmYNm0aSktL8e9LlyBpLGsMwLrZuo3x46XpjkgAVKvVsLGxEV4Ti8WorGy7dEFBQZv7BwAJ
CQno378/ZDIZ5HI5qqur8cMPP3ShFg3tY2dnJ0zb2dlBrVajrKwMAKCvrw+Z7Mf+4M3ruGvXLly9
ehUuLi4YPnw40tPTu7RNpht8Zy32zOTn52PgwIEoLy8Xeus+K5988glSUlK0foPUhaioKCiVyla/
obal+RCcjjoeNQ3BmVBVhTFxcQCA/4uJQUxMDPr06fOTfx9sKrt8+XLk5+drzSspKRH+ViqVkEgk
rQK6+fw7d+7A399feI2IIJVKkZ2dja+//hrFxcUoKSnBwYMHUVhYiAcPHuDMmTM4d+4cNm/ejJKS
Eujp6UFfXx9xcXGwsrJCjx49QESwt7fHkCFDkJ6ejpddXVFx8WKn+2YCoKrZdC2AptpXADA0Muqw
vFqtxrx58/DNN9+gT58+uHPnTqsw/vLLL7Fp0yacPn0arq6uICJIJBLht/jO/g/Y2toiNzdXmM7N
zYWxsTFkMplwkNMeV1dXfPrppyAi7N27F8HBwXj48CF69OCv/OcRvyusFXt7exQXFwtfdCKRCJGR
kdiwYcPPWq9SqWy3s8/TNn36dEyfPv2pbyc3NxcODg4wNTUFAKH9duzYgSlTpnR5PZmZmVjaTgjv
AvA3AP9s8boTgBNVVRgVFwcPLy8k/cyz49///vfYtm0b6uvrATTcJjIjIwOBgYEAIATKxo0b8fjx
Y4jFYvj4+GDFihW4evUq7t69C3Nzc5iYmGD+/PnYtWsX1Go1rl27htraWmE7I0aMgKWlJdzd3XHv
3j2IxWKMHj0a9+7dw8CBA7Fw4UJYWlpix44dOHLkCI4ePQoAuHHjBtLT0zFv3jwAQFxcHAa6uyPj
3//GTLUav+lg3wagIXjPABgFYCmApq5qmcbGkFtZtSpDzTqzGRkZYd26dQCAGTNmYNGiRXBycoKD
gwOuXLkCBwcHVFRUoGfPnujVqxeqq6vx3nvvobq6WliHtbU1MjMz263jtGnTsHbtWrz22muQSqVY
vHgxQkND26xPS7t378b48eMhl8thZmYGPT29Z37wy7qOL02zVkQiEY4cOYJHjx4Jw1l+bgjrUlOQ
PCsikQjl5eVa7dedEAY6HoJDANr7Sm0agvPXVau6XeeWYmNj0b9/fxQXF8PExASDBg3Cpk2bsHDh
QixatAj19fXo378/1q9fD319fVRXV+PkyZMYMWIE4uLicP78eRQXF+PVV1/FxIkTkZOTg//85z8w
MDDAkiVLQES4du0avL29UV1djaKiIqxcuRLm5uaIiIiAra0tevfuDaVSCaN2zlCb11skEmHs+PH4
orF9OoodKYD1AKYDUAKwBWAB4BGAL4jwsptbp9tqsnDhQowfPx7+/v4wNzdHTEwMampqMGHCBIwa
NQqOjo5wcnKClZWV1n2tQ0JC8PjxY8jlcowcObLVemNiYhAcHIwRI0bA2dkZFhYW+Mtf/tLue9Z8
Oi0tDa6urjA3N8e7776L/fv3Q19fv4MWYTqlk1+m2XOtrY47TXbu3EkjR46kuLg4kslk1K9fPzp2
7JgwPycnh3x8fMjMzIwCAgJo1qxZFBYWRkQNnXpEIhHV19cTEZGvry8tXryYvL29SSKR0JgxY7Q6
l1y8eJFGjBhBUqmU3N3d6ezZs8K88vJymjFjBikUCurTpw/9+c9/Jo1GI9TR29ub5s2bR7169aLF
ixcL9W4iEolo69at5OzsTDKZjGbNmiXMq6+vp/nz55OFhQX169ePNm3apFXvjty9e5f09PTaXTYy
MpIWL14sTKemppK7uztJpVLy9vama9eu0f3790lqZETXAQoGyBIgC4DmAPQfgIwA6gGQaWPPYAIo
EqAYgMYBZAKQiYEBhYSEaG3rwIEDNHDgQDI1NSVbW1t65513aN26dRQYGEhSqZR69OhBhoaGZGlp
SWZmZmRgYEC9evUiAwMDCggIoNDQUIqNjaVVq1bRRx99RIcOHaKNGzeSUqmkhw8fCu3fGV9fX9qx
Y0eb886ePUtKpVKYLiwspMmTJ5OlpSX169ePNmzYIMyrr6+nlStXkqOjI0kkEvL09KT8/Hyy6tWL
RI3tIAFoH0BnAeoDUGJjp6yIxnbbDpATQL0AmgjQMoDCgoOJqOPPSMvP07fffksBAQEkl8vJxsaG
EhISutQWjBFxr2nWhs6CuGfPnrRjxw7SaDSUlJREtra2wvzhw4fTggULqLa2lv71r3+RmZkZhYeH
E1HrkPL19SUnJye6ffs2qdVq8vX1pfj4eCIiunfvHvXq1YuOHz9ORERffvkl9erVi3744QciIpo0
aRLFxMSQSqWikpISGjp0KG3fvl2oY48ePWjz5s1UX19ParWadu7cSaNGjRLqKRKJaMKECfTo0SPK
y8sjS0tLOnHiBBERJSUl0cCBA6mwsJAePnxIv/71rzsM1+aa9rF5D+Lmmgfx5cuXycrKijIzM0mj
0QjDfD5YtYoiDQ3pFYD+BJAKoOrGHr0E0E6ARrXo8RsJkBSgi43TIXp6JJNKSalUkouLC0kkEgJA
MpmM3NzcyNvbm8aNG0dz5syh8PBwev/99+nzzz+nzZs3k7GxMX311Vek0WhaBWNLBQUFZGZmRlFR
UU88iDUaDQ0ePJjef/99qquro5ycHHJ0dKT09HQiIlq9ejUNGjSIbt26RURE165do9LSUsrIyCAA
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
<h1 id="Making-a-two-mode-network">Making a two-mode network<a class="anchor-link" href="#Making-a-two-mode-network">&#182;</a></h1>
</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>If you wish to study the relationships between 2 tags you can use the <a href="{{ site.baseurl }}/docs/RecordCollection#networkTwoMode"><code>networkTwoMode()</code></a> function which creates a two mode network showing the connections between the tags. For example to look at the connections between titles(<code>'TI'</code>) and subjects (<code>'WC'</code>)</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[37]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">ti_wc</span> <span class="o">=</span> <span class="n">RC</span><span class="o">.</span><span class="n">networkTwoMode</span><span class="p">(</span><span class="s1">&#39;WC&#39;</span><span class="p">,</span> <span class="s1">&#39;title&#39;</span><span class="p">)</span>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">mkv</span><span class="o">.</span><span class="n">quickVisual</span><span class="p">(</span><span class="n">ti_wc</span><span class="p">,</span> <span class="n">showLabel</span> <span class="o">=</span> <span class="kc">False</span><span class="p">)</span> <span class="c1">#default is False as there are usually lots of labels</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt"></div>


<div class="output_png output_subarea ">
<img src="data:image/png;base64,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
WrVq0dHRUSefnWfPnrFnz5709fVVWrSkDzIzMzlgwACOGDFCcbPes2eP2uEGdahbMRwZGcl+dyYP
0gAAIABJREFU/fqpHVIqXG1dSFZWFsVicZlcVlURHx/PkBD1HlKFFKbBfJNBgwbx4sWLOrWZl5fH
xYsXUywWMzIyUhESWxbi4+M5efJkpX2rVq1i+/bt9ZZg/sWLF/Tz86Ozs7PGtKKCCOgHITroHWJk
ZIQqVaootjczZGVlZSEsLAyhoaGKbf/+/Xpp+9tvv8WxY8fw66+/4vz58wgPD4eNjQ02b94MqVSq
9rxt27bB1dUVXl5eCA0NRdWqVfXSn0JMTEwQFhaG1q1bw8HBAYmJiQgKCsLMmTP1Un+HDh1Qv359
LF68WOXxypUrIy8vT/HZ2NgYbm5uWLNmjV7aL0Rbb507d+6gcePGSvtyc3Px+++/q/URUkfFihXR
r18/7Ny5E1evXoWtrS0yMjKQm5urUz1FWbduHbp27Qqg4Pfap08f3L59G1FRUXj//fdLXS8A5OXl
Ye7cuXB1dYWFhQWioqLQokWLMtUpoAV/twoJFJCZmUnzNm1oZWxM30qVFFt9Y2OuWb1ab+3I5XJO
mTKF7733Hk+dOsW5c+dSLBYzODhYaYz/wYMH9PDw4Pjx499JXmGywE/+gw8+4NSpU0su/AaavINk
Mhk7deqkNq7e3t5e6U0hNzeXIpFIr9d94MABBgcHl1hu5cqVxSKbtm3bptNCM3U8efKEX3/9Na2s
rEq1XqBoEpvk5GRKJBK1uQ50QS6Xc/PmzRSJRFy9erVW6zxkMhnXrVtHQ0NjAkc1vAmcYpUqNYU5
AQ0IIvAPoFAAulapQukbv+JrgN6FgCwYJqlVqxYjIyMplUq5bds22tra0sfHh8HBwbSwsOD58+f1
2mZJrF69mpMmTeLYsWPZq1cvndIwzpgxQ6N30MuXLymRSHjnzp1ix3r37l0su9rq1at19vrRxMGD
Bzlr1qwSy3l6ehbrS2lyNqgjJCSEa9euZffu3dmrVy8ls7+SiIiI4KJFi7hp0ya9pH4kyYSEBFpb
W3PGjBlKnlDqyM3N5cqVKymRSDhz5kxGRUW9tmVRJQSnaGxcV+cItvKGIAL/ADo5OKgUACUhMDHR
uznciRMnWL9+fY4YMYL5+flMSUmhSCRiy5Yt6e7uzmPHjr3VVbRFuX37Nq2trRVj8fv376dIJNJa
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
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
<p>For any number of tags the <a href="{{ site.baseurl }}/docs/RecordCollection#networkMultiMode"><code>networkMultiMode()</code></a> function will do the same thing as the <code>oneModeNetwork()</code> but with any number of tags and it will keep track of their types. So to look at the co-occurence of titles <code>'TI'</code>, WOS number <code>'UT'</code> and authors <code>'AU'</code>.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[39]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">tags</span> <span class="o">=</span> <span class="p">[</span><span class="s1">&#39;TI&#39;</span><span class="p">,</span> <span class="s1">&#39;UT&#39;</span><span class="p">,</span> <span class="s1">&#39;AU&#39;</span><span class="p">]</span>
<span class="n">multiModeNet</span> <span class="o">=</span> <span class="n">RC</span><span class="o">.</span><span class="n">networkMultiMode</span><span class="p">(</span><span class="n">tags</span><span class="p">)</span>
<span class="n">mk</span><span class="o">.</span><span class="n">graphStats</span><span class="p">(</span><span class="n">multiModeNet</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt output_prompt">Out[39]:</div>


<div class="output_text output_subarea output_execute_result">
<pre>&#39;The graph has 108 nodes, 163 edges, 0 isolates, 0 self loops, a density of 0.0282105 and a transitivity of 0.443946&#39;</pre>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">mkv</span><span class="o">.</span><span class="n">quickVisual</span><span class="p">(</span><span class="n">multiModeNet</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt"></div>


<div class="output_png output_subarea ">
<img src="data:image/png;base64,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
JSVYt24dPDw8cOvWLWzYsAFpaWkIDw+Hubk5U1Dk1atX8PX1RXp6OszNzdG3b194enpCV1cXbm5u
rVQRpaWlmD9/Po4cOYK+ffuib9++8PHxgYuLCzp16gRjY+M29bidOnXCuHHjsG/fPqYM5ddAREhN
TUVERATS09OhqqqKNWvW4NChQ+BwOLh06RKEhYURGxuL9PT0VjrXqVOn4v79+9DV1UVKSkqrKmaC
goIgInA4nO8ipC+Rmpr6j3l97N27FxMnTmSM74qKinBxcQHwMcgqPT0djx49wunTp1FUVIQuXbpA
QUGBIYa+ffsiOTkZ06dPBwCUlJQwqsGkpCRs3rwZYWFhGDt2LJ48eYJDhw6hpqYG5ubmiI2NbdNA
Xltbi2vXriE+Ph45OTlQUFCAgYEBPD09W81bXl4eoqOjcevWLVy4cAEnT56EgIAAlJWVwWKxICIi
gqSkJOTk5EBUVBROTk4QERGBkpISBg8ejKqqKgwdOhSlpaXQ1dWFsbExgP94Hbm4uKCmpgaTJ0+G
lpYWJk+ezKj3REREICoqis2bN2PJkiU4e/Ys3+Zg1KhROHXqFK5cuQITExPIyMjg/PnzaGhoQFZW
Fl+N6Z8l9v9p/N8VRP77ERkZSV0kJQlHjhBOnyZIDyMIOhGw89MRQBCSJbgsblddJNa/PykpKdHt
27f5xl66dCmtW7eONDQ0aOXKlZSQkEAsFosKCwuptLSUTExMqLKyklxcXGjGjBlkYGBAJSUlTP/q
6mrS0NBgRPyWc6qqqlRWVkbJycnEYrHozJkzrd5rx44dtGLFCuJwOOTg4EChoaHtzkFWVhb5+vqS
mpoaubm50aNHj4jH41FhYSHp6enRiRMn+Nrn5uaSgYFBK7VBSkoKeXp60rVr18jX17fNe61atYrS
09Pb/0C+AcbGxtTQ0PBTYxAR3bt3j8zNzb9L9VNXV0d37tyhPXv20Lx580hHR4dGjhxJixYtosuX
L5OmpiZxOBzatGkT2dnZtak2q62tpSlTppCSkhItXryYHj9+TNnZ2bRnzx4yMjKiWbNm0d69eyk7
O7vDZ3n79i1NmjSJrK2tydDQkC5cuEBcLpeIPqrj3N3dSUNDg/z9/amwsJDpFxoaSpqampSQkEDT
pk0jb29vWrZsGZmYmJC+vj7p6+vTnDlzaPXq1bR37146c+YMHTt2jNauXUu6urpkbGxM6urq1KNH
D9q/fz9lZGSQmpoaJScnt/uspaWlJCoqSp06dSJnZ+dW1xcvXkxZWVnt9ufxeNRfQoKsIUwWEGMO
LwgR5zMVkU3Xrh1+1/+N+EUC/wAiIyNJtFcvQo/+hE5eBPDos+8VAbkEkSHtEkE3GRlKT08nY2Nj
ioqKYsY9cuQInTx5koiI4uLiqH///qSiokKHDh0iPz8/On36NNP2xo0bpKioSPLy8pSUlESNjY1k
aGhIt27d4ntWe3t7SkpKYv5vaGggDw8PsrGxodLSUuLxeOTj40NeXl7M4sbhcMje3p6OHTvG9Hv/
/j3t2bOHtLW1ydHRkRITE/lsEzdu3CAWi0UZGRltzpm3t3cr8mlubiYDAwOaP39+uwtYTEwMY6v4
Uejo6PxUfyKisrIyUlVVpfLy8p8eS11dnW7cuEGBgYEkLS1Nffr0IUVFRdq6dStdu3atzXu8ffuW
pkyZQvPmzaMBAwbQgAEDaMmSJVRcXPzV+7XYliQlJWnOnDn0+PHjdtuy2WyKi4sjS0tLMjY2ppMn
T1JDQwM9f/6clJSUSFlZuc1+1dXV9OzZM4qPj6f9+/fT2rVrydTUlEaNGkU9evQgUVFR+u2332jE
iBGkoaFBGzduJHV1db7vWAuysrJo4MCBJCkpSYMGDaLFixeThYUFn71AV1eXIbDPUVtbSyEhIaSq
qkqiwj1JAHMI+Is5xDCFTCFKHICuAdSna1d6+vTpV+fw34RfJPAPYdiwcQSB1W0QwOdEIEvYvp2f
BIKDSbR7d/rw4QOx2WxydXUlPz8/4vF4dPfuXfLx8aGCggJSVVWl7Oxsqquro7CwMOrduzfZ29tT
cnIys1jX19fTypUrafDgwSQnJ8dHEkQfDbxr165t8/kfPHhALBaLjIyM6I8//mh1ncPhkLW1NS1c
uJCMjY3J3NycTp061WpHzePxyN/fn2xsbNrcxbagrq6OVFVVqbGxke+8trZ2h4t0Tk5OmzvBb0Vx
cTHNmzfvh/sTfTRszp49mx4+fPhT4xB9JFNra2siIkpMTKTevXvT06dPqbKykpKSkmjHjh1kZWVF
Ojo6ZGJiQlZWVqSurk4aGhqkpaVFmzZtIh6PR3V1dXT06FHS0dEhV1fXNhf2hoYG+uuvv2jatGk0
aNAgevTo0Xc9a1lZGe3fv5+0tbVp4cKF5OTkRBoaGuTj49Ohc0JxcTGtXbuWtLW16fTp06SlpUVp
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
QkAIIVzY/wOCa78XEy/HnQAAAABJRU5ErkJggg==
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">tags</span> <span class="o">=</span> <span class="n">mk</span><span class="o">.</span><span class="n">commonRecordFields</span> <span class="c1">#All the tags, twice</span>
<span class="n">sillyMultiModeNet</span> <span class="o">=</span> <span class="n">RC</span><span class="o">.</span><span class="n">networkMultiMode</span><span class="p">(</span><span class="n">tags</span><span class="p">)</span>
<span class="n">mk</span><span class="o">.</span><span class="n">graphStats</span><span class="p">(</span><span class="n">sillyMultiModeNet</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt output_prompt">Out[41]:</div>


<div class="output_text output_subarea output_execute_result">
<pre>&#39;The graph has 925 nodes, 14217 edges, 0 isolates, 39 self loops, a density of 0.0332678 and a transitivity of 0.33469&#39;</pre>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">mkv</span><span class="o">.</span><span class="n">quickVisual</span><span class="p">(</span><span class="n">sillyMultiModeNet</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt"></div>


<div class="output_png output_subarea ">
<img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAYEAAAEACAYAAABVtcpZAAAABHNCSVQICAgIfAhkiAAAAAlwSFlz
AAALEgAACxIB0t1+/AAAIABJREFUeJzsnXd4FNXexz+zfTcVklASepWIKEVpgiBSlS6goCggCihy
Ra+AegUEr3oVFa6CeuUVFRURFSkiSBMFKYJ0EZBOaIFASN3s7u/948xuNskmVMXAfHjOQzJzdubM
7uZ8T/kVTUQEAwMDA4NrEtOVboCBgYGBwZXDEAEDAwODaxhDBAwMDAyuYQwRMDAwMLiGMUTAwMDA
4BrGEAEDAwODaxhDBAwMDAyuYQwRMDAwMLiGMUTAwMDA4BrGEAEDAwODaxhDBAwMDAyuYQwRMDAw
MLiGMUTAwMDA4BrGEAEDAwODaxhDBAwMDAyuYQwRMDAwMLiGMUTAwMDA4BrGEAEDAwODaxhDBAwM
DAyuYQwRMDAwMLiGMUTAwMDA4BrGEAEDAwODaxhDBAwMDAyuYQwRMDAwMLiGMUTAwMDA4BrGEAED
AwODaxhDBAwMDAyuYSxXugEGfy0ej4fMzMzA72azGZfLdQVbZGBgcCUxZgLXEElJSdxQtSplSpYk
ISqK0pGRxIaFEW4yEWE2UykujnpVq/LkkCH4fL4r3VwDA4O/AEMErlJEhP379/PWf/9LXGQkkRYL
VRMS2HfgACaPh/oi7Ab2An+IsMLnw52czC179rDsgw+4u2NHNm3aREZGxpV+FAMDgz8RTUTkSjfC
4PLi8/kY0r8/Mz/9FEtODmbAC5QEKqGU/2vArtfPBkYDM4GzQATgA7BYiKxQgaVr1hAbG/sXP4WB
gcFfgSECVxlbt27lno4dsR84wDKfj0j9uAD3A6uA38grAF30Y9ejxMEW9JpnLBbmG0JgYHDVYiwH
XUW8OH48jevU4fS+fTT1+XgVOK2f04DeQBSwGVgHrATuAnYCN5JXAPyv+bfHQ9s9e7j5+utJS0v7
qx7FwMDgL8KYCVwlDB08mDnvvMNjQcc2AruARUAY0AbV4cfr59OBo8AZIJO8AhCMANWB+55/njFj
x/4JrTcwMLhSGCaiVwHjnn+eue+8w2qgbNBxAYYBdwDlUUtAfwCOoDqvAmOAY3odgCzgPZQwBF/r
rVdeoVrVqtzXt++f8RgGBgZXAGMmUMx55pln+Oill1hHXgHwI8ANQBlgHnkFwM8rqE5/DRCO2iMQ
4KagOh8BLYBVMTHsT06+bO03MDC4shgiUIyZO3cu93TtygCvl0lF1LMDySirn8JoBowCJgElgI/J
O03cBzQH0hwOTmVmFni9gYFB8cTYGC6mzJs3j75du/Kw13teH2Jh6/1+coA3CC0AoExLVwC2rCzm
zJlzoc01MDD4m2KIQDFERBjSpw8fe71UvEzXNAObgH9Q+EZRJeAe4Pfff79MdzUwMLjSGCJQDHli
8GCyUlNJQJl8rkZZ+hSGACeLOO9DmZKez5dBO+9WGhgYFAcMESiGTPnf/yij/9wa1YnfhNrgfQNl
GpoB/Be1yesAWgLHQ1zLBwxEWQJZz+PeJpPxlTEwuJow/qKLGfPmzcPr82ECjgC3AzWAtsABlOfv
rShfgG9QSzgDgTigMXmFwIfyIt6FciCrhnIiK4wcYL0RddTA4KrCsA4qZiRWqMCugwfph4r1Mwx4
Iuh8FMo5rCfKJLSZflyAx4HJqDV/DSUCNpTDWDiwA2gFvAg8mO++OcDdwMGaNfl50ybsdjsGBgbF
H2MmUIzYsGEDBw8dQgOWoZy7JqBG+5WABOABlHPYTKA7cFB/rYZaHtoExAJfofYJslACAHAd8Drw
GMpUdFVQ6Q2sN5kY8tRThgAYGFxFGB7DxYjRw4fziggbgU+A9sAGctfyM4COqFH8NKACaomofNA1
aqP2CfaioooGL+ysAYYC/9GLR3+tBqSZTJRLTKRXr15/xqMZGBhcIYyZQDEiLTWVCsBh4DbgM/Ju
5rqAuUAS0A8VIfSjQq61D7WpfNZqRQsLQ4uIoFF4OOlOJy+ZzVRB7Q98CySazYTXrs2ilSuJiCjK
5czAwKC4YewJFBMyMzOpFBnJOI+HsahOvDBrngygNFATtRE8GOUN7GcQ8AHgLlcOTp+G7t2hQgV1
UgSmTkU7fhyr14tJ04iNimLb/v1ERkZiYGBwdWEsBxUTUlJS8Hm97EAtzxRlzulChYpIQnX2dwJP
oxzC3MAvgLtkSUhOhiFDoGPHvBdo0AAZPATT2VQqly+PxWIxBEDn1KlTbNu2LfC7yWTi5ptvxmY7
l0+2gcHfE0MEihFuk4l3vV4SzqNuNtAHFT7aP9VzowRhu8sFbjcMHFhQAACiomDKZLIeGsihQ4eI
jo6+TE9QPDly5AhjRozg1IkT/LhsGTavF7vZTGm7nQNuN24gJjYWTVOudG3uvJPX3n7b8KkwKBYY
IlCM0Ewmmni9/IHq2Avz3vXo/z8XVGcNKmT0yvh4Ms+cAa8XmjQp/GZRUWg1ryP75zVkObIuS/uL
E/Pnz6dnt25kuN24gIdQCXju0s//1+MhLjubnahYSwmHDgEqjedjH33EoPR03pk2zRACg789xje0
mGCz2cjS00WWQlnxhNrM8QD3Ak2BGJQvgKBmAD+ZzWTWrAkZGWrt/xxYMINPLXlcCwnnk5KSaN24
MVVKl6Z3x4584XZTEyWmE1Hmt/7yPfA7ykmvDcrqqjYqQ9u3GRlsmD6dCtHRtG3alEO6QBgY/B0x
RKCYEBsbS7sOHcgBFqLW9R8jrxB4gL5AKipVJCgroQjgtNlMtsUBK3aCXNgEUNM0/vjjj0t9hL81
SUlJtGzYkDJr13L2+HG+F+ENlKCOClG/BCo95ybg83znIoBlIjjPniVh9WpaNmxoCIHB3xZDBIoR
NzdsyCFUqsiFwHpU2sdKKEug6igHsNmojeGHUOEgALjhJnzZEeBdCdhA02DRosJvdvw4snUrGiYs
FgsbNmz4cx7qHOTk5JCenh4obrf7st/DLwD9jh5lq8/HO8AtwAmgcxGvK4Ey1T0R4lwEUAXo5fPx
8LFjhhAY/G0xRKAY0axZM5LMZu5DCcFy1Ih/Cmr0H4PKF3wX0BCVSnIM4LHZYOtRVLzRioALMjPh
009h+vSCNzp+HAYPpubZspg0Mx6Ph40bN/7pz6dufZyOLVvS6LrrqFu5MmUcDuLDw4mLiqJUdDRx
UVEsWbLkst5zzIgRdDxyBIfHw2HUctvl5J9eLz2OHWPEY4+du7KBwV+MsTFcjLDb7ZQPC+NMaio9
yM0CVgJ4G+iPygfQCKXutwKzAK8IeO+GQPaBOcAdkJ2uRODkyVw/AYDp09FST7PLl4bbacaakfGn
5xBIT09n9+7d3NOxI52PHKGLxxM49yWw0OtlKbDd4+HuTp34bM4cWrVqdVnunZWWRobXy9eo0fuf
QQOvlx1nz/5JVzcwuHgMEShGhIWFcTAnh5kob996qNg/DlT8n49RYSP8/IByFMuOjIQULWgDoRGw
mIAQzJsHuhWLyQSaNwerRRCLG7PPjtvtZv/+/X/ac23dupXbmzYl++xZHhPhRf24D5UnIRHV9Nv0
Z5qVkcHdnToxc/58WrRocUn33rdvH8uWLsWNWk7bQa51VSmUAN1UyGtPomI4NQtxbgnwK1D1klpn
YPDnYywHFSNq167N4yNG0N7lIhF4CbXmHwY8BXRAmSh6UUtFnVG+AWRkqD2APDRCdVWNwXMjuKtg
8Xmwa26eGi6Yzcq81AJ4vV5SUlL+lGfaunUrrZo0oVZqKt1FeBTl45CBsropjQqM9y4q5HVbVKf7
YkYGb7300iXde9++fWovIDWVqcBIoBMq9PZxVMiNL4EXQrz2JMoCKxIVXTWYJagN5Vmo8NwGBn9n
jJlAMeOZ0aMBmPLSS6zKzmYOajTaGhUq2o8LJQAegOxs8P2sHwn2bG2IihEKKh3N8wwblsaGDeDz
QVYWWK0+RITMPyG5/I4dO2jWoAHu7Gy2oXIhLEBtqsahRtFnUZ7OoLKf3YZa8moGiNd70ff2C8Dw
5GSGBh2/E3gWaIJ6Z5aicjYkA3WC6v0HFbrjAEp8y6I2432ojflZQHO9bgbwlstF47p1L7q9BgZ/
FkbsoGLKm6++ytQpUziwbx8LRAh2+5qHyieQt9t2obrOORRMO/8+VuvjDBqUyW+/wcqVat8YlI+A
yWTC4XBw/PhxnE7nZWn/vn376NW9O0kbNvB/QBpqBH4qqE5p1KLV9UHHTqNmCGUAa6tWfLl48UXd
v03jxrRau5YRPl+Bc4ISgv+h9gi8qBAcWShxKA3cgBLdFFSH/wXKXPRplCD7l5AygDs0jb1RUaxY
u5bq1aufdxtTU1P5/PPP8ej7I0eOHOH48eMkJOT6jHft2pXatWtfwJMbGOTFEIFiznfffUfPLl2w
Am63GxHBA7g1DRFB0/9XuFDbxc8FXWEtmul5YktlIR4faWlqBhCM2WzGZrOxatUqbrqpsBXy8+fL
WbPof++9lPJ4CEd1lIdQORDaB9X7BNWphhKCGKDT7bfz9UVaCjWsWZNJO3fSsJDzgsq65l/ueRq1
LPUVuTMTP6mo9J27UBndOumv96FmEjU6diTd52PXrl288847tGzZ8pztS01NpV2zZkTv2kUFEY57
PCzxeHiQ3PwP6cD7mkZMdDQ31atHbGwsvfr3p02bNuf/RhgYiEGxJy0tTZKTk+Xll1+W+Ph4MZlM
4nK5xGw2C6o/CipOgWhVtBKCFilYLILVGqKuKpqmic1mk3ffffeS2zrriy+ktNMpG5TPsqwFiQOZ
p/+ev3wEUhZke77jJpCPpk276HbcUqOGrC7knv4yDOTf+s/pIHeA3APiCapzBqSufu4nkE9AXga5
FSRa/wxat24tWVlZ8q9//UuqVKkiEydOLLRdhw8flloVK0oYSD8QH8hGkNIgM0O0cRZICZA2IHeB
uCwWue+++2TGjBkX/d4URnp6ukybNk3+97//Bcq6desu+30M/loMEbiKSEtLk5tuukmcTqe4XC4x
mUyFduwXWkwmkwwZMuSS2jd/3rw8AiAg94K8eY7O+F8gj+U7ZtY0ycnJuei2nK8IlAPpD3I/SE+Q
aBAnSDiIQ/leSxhIAkgNkFomk1QxmaRibKw0bdpUpk2bJjExMRIXFyd79uyR2bNnS9WqVaVv377i
drvztOnw4cNSo1w5qQUySBeAs0UIgL98pbfnCZCRIE+DVLXbZfzo0Zf0eQWTnp4urRo3lhYulwzQ
S3+XS+JcLvn2228v230M/noM66CriLCwMNq1a4fFYiErKwtfiPXui8Xn87Fz585LusaX06fzXGYm
wdujPtQae1GU1uv5cUPQEtfF4QWmaBqFvUNHge+AbijT0a/1koUyqfPpP3tQyzKHgZS4OKq0b0+F
5s2JrViRypUrs2zZMh544AGuv/56atWqRXJyMnPnzmX9+vW0aNGC5ORkQHkt16tRgz6HDpEMjEVZ
Z53W25MJvImyOroXZbH0GjAd2IpS6l3ANyjT1BrZ2bw1bhw9u3S5pPcJICMjg0533EGZX39lcUYG
7+tlakYGczIyuL9rV6ZNm3bJ9zG4MhgicJUxdOhQSpcuHQhrfDnZvXv3Rb82JyeHVT/8wKVmJ3YD
3ex2wi2Wi/ZdGPvcc6QdPMivIgyGAkJwFGUR1BsYhsq7nAHkoDr+dP33YKKioihZsiTbtm0jPT2d
1q1bs23bNrZu3UpUVBRms5kRI0YwZMgQhg8fzvLly3E4HNx6661s2bKFHl270jI9nefzXfd31Kb5
POBHlHidQJnMLkMlCDqrt7MOaut/Mypf9ACfj0XffEOH9u1JSkq6qPcK4L6uXSnz6698mJVVYD+k
ETAvO5uh/frx6n/+c9H3MLiCXOmpiMHlp3fv3pdtGSi42Gy2i27T0Icekmpms0wAaQ9SRy+lQHqD
vB5Ufsu33PEmyBCQbNTae4SmSdvbb5dy5cqJ1+u9oHaMefZZSXS55CjIMZAyIF1R6/j+Ullf2rlV
X/55GqQkiFbI+2KxWKRWrVqyZcsWGTdunJQuXVrq1KkjXbt2lbvuukvq1q0r/fv3lw4dOsgLL7wg
JUuWlLi4OPnjjz/ksccek5iwMIk3m+Wf+vPG6W3bqi8FTc/3fvj0ZZ8IkK9DLA+9pZ9rDNICpB5I
jNMpW7duvajPrmJMjOw5x9LZPSCRVqvM+uKLi7qHwZXDmAlchdSqVavQc5cyQ3C73QFzxQtl24YN
VPR6eRMVcvkj4EVyR+H7UTb3O4EWKHNLUEsdY1C5jivr50eLELNsGdmnTl1Q4vstW7bwzuuvszQj
g9LAO6jQz9ejTFNPoTyGuwP/RdlQNdfbNh+IxsSt3Eo96uHChUV3s4mIiGDOnDm8+OKLnDp1iuXL
lxMdHc2qVas4ePAgjRs35pdffuH48eMkJyfTsmVLEhMTSUxMpGzZsmhuN7293sB7YUeN+lujZiF9
8j2HBvwbNQsYgDJHrQvUBz4F2qGcBw8A01CBBt/MzKRV48Z5sqJdCOf61liAp3NyeLRvX+bPm3dR
9zC4QlxpFTK4vOTk5BRq4RPq+IXW6dOnz0W1q0a5chIG8qQ+kt0NUgFkSohR5Rf6CHiWPlMYBbIQ
pBHI80Gj4cdMJok0m2VaEVZC06ZOlTYNG0qbW26RJtdfL/Fms3yjX+MJkAlFjG4no4kZq5gIFwfh
YiJCnJSUd3lX2tBGoogSGza59dZbpUePHvLbb7/JkiVL5Pbbb5epU6fKzJkzJSEhQapWrSq33367
tG3bVmrXri39+/eX2267TYYNGyZWq1XKmUwSB/IP/b4L9BlI3XOMvn0gVpDVIBtAvgWJ1N+zKvr/
LtSmcQm9RDudsn///gv67CrGxMjec7TlPpQl12SQfj17XtR3xODKYIjAVUaNGjUuernnfKyJNE2T
1NTUC2rTxx9+KBEgA1DmlY+gllZMQeUREG9Qp/I5ygqnrN6ZldQ7sQiQEXoH6AMZYjZLtMUix48f
L3DfdydPlgoul8wG+U4vn+sC8+U5RGAymriIEdiV79RkAadoaKKZNTFbzVIpvpIsXLhQevfuLYMG
DZKDBw/KpEmTpHXr1rJ06VJ54IEHJCYmRmrVqiX333+/JCYmSoMGDaRXr17Svn17iUAtc4WDrCB3
CazmOTpeAbGBZAX9vgG1nDRL/z1Jv84zKHPckiDDhw+/oM+vapkyMr+INmSjBHoGyFSQfj16XND1
Da4sxnJQMcXn85GZmRko2dnZzJ8//5IseETknMtFIkKnTp3O+5qfffIJIwYNohPKy3YIsAXlaevW
SwqwHXiY3OWhniiHsM6ojdqTqOWaPSirnWf0eg96vYQ7nbRs2TKPxdB7U6bw4lNPsTQjg86omENt
9esu0Nuxq5A2/w+NpyhJBqspGP1nMDABwYG0Fbx1vSQlJzFy5EjCw8Np3749jzzyCCkpKbz77rt8
/vnnaJrGjBkz8Pl8LF68mLCwMMLDw9m0aRO/b9hAf1S4itaopagfgcaAE7WkE1zOZe9VV39/+uq/
l0VtIM/Ujy8HPn7rLT6fMeMcV1Kb+ZMmTSKybFnut9tZEaKOG+iFCvPR9ZxXNPhbcoVFyOAiOHny
pDSoVUtsJpPYzGaxmc1iMZnElG/UPnHixPNa4gEkPDz8vGcMmqbJwYMHz6utDa+7Tr4DeQikGUhT
kNQQo8mz+vkB+ghfQCqhNkfz1z0BciPIc/roNgokMTFRnnjiCRER2bdvn5Sw22V3EaPXDSg7/0b6
vYPPVSVSYOk5BuG9BRNCD8R0i0ni4uNk+fLl0rVrVxk6dKh8+OGH0rJlS3n33XdlzZo10q5dO3nl
lVdk/PjxEhMTI5UrV5ZOnTpJaYdD5oK8AfI4yPcgsSD19ecqBVJeL3EgnfSRt4D8oc8E3Pka50HN
tA4HHVuvzwJOg6wEqRATU+hn5vP5ZM6cOdKyZUv54IMPxOPxyPfffy/hmiZzQHbo5TeQLiAdg9r0
Gkj/Xr0uy/fc4K/BmAkUM06dOkXrJk24YfduSvl83OD1UsfrpY7PRwwqrDTArl27eOihh4iKijrn
NTVNY/ny5cTFxZ1XG0SE1q1bn19dnw8zamN1E7kB4vITjtr8nQ0c1I85Cb0hGYuyh387qP27du3i
ww8/5IcffiAtLY2ydnuRYZzr6tevihqFp+U5q6ECRvjJQoWQ85ez6rwP+BJ8bX2csZ0hJSWFr776
il69ejFz5kwaNGhAeno6I0eOZNCgQSQkJLBkyRImTpxIhQoV+OmnnzDpM69jqFH1HaiRuwk1MzhM
7izgECpkxd2oDeyWqNzH1hDPp+nn/XnYXKiIUW1Q+SdSU1PxhgjAt2nTJjp37sy6deuYM2cODz74
IIcPH+arr74iTYQ+qBlVJ9QsLQIVO8mGmmm8EhbGI8OHF/HOG/ztuNIqZHD+nD59WurVrCn9rFYp
p6+/5h9NNwCpHmQ6OWjQoHOO7O12u4iIHD9+XOLj4897RnA+IQMaVKsmtfUZQEzRQ2sRkIoge/VR
bEl9tBuq3knUHsEY1D6BxWIRp9MpcXFxsnr1akmMjDznvSJAHtZnFQ300fgbIDFECfyiV9suNltJ
cTgcgWI2WwVuz30v/oXYr7PLV199FXhun88nixcvlrZt28rIkSOlaf36Uik6WpokJkpiQoJUKVVK
XnjhBYmzWmUuyky1LioMRWuU2WxOiDZng3TW35u3C3kuD2qfpSRq1iT6qL0myvP6VtQG8oNBI/Yj
R47IwIED5YEHHpADBw6IiMjOnTtlwIAB0qNHD+nbt68AEhsbK+GaJgvz3XMBSFxYmKxatepyfuUN
/gIMEShGfPHFF9LY6QwpAPmFYEi/fiKi/rgtFkuRnXmFChUC90hLS5NKlSqdlwiULl36nG2uXbGi
VAXZj1rOOB8RWI1a/nipiHon9U7cRe6mtqZp4nK5pFq1alLd4RAB+QG1Yekvi4Ku4UKFfUDvNG16
0YgU+FFgu9jtJWTECE2WLSNQ/u//kLCwoLhM/0KohERERMhHH30kPp8v8Pw5OTnSslEjaWYyyXwI
lHEmk5Sw2eTGGjXkTrNZntdFoBFIfCECECwEEahN31DnR6OELSZIBNbqInBCF4eyICZNk4yMDHnx
xRelXbt2smbNGhER2bx5s/Tp00fuu+8+2bx5s5w+fVqcTqcAMmzYMEF/n8Kt1kApYQhAscUQgWLE
zJkzpZHDIR3P0ZEeACkVERF4XaNGjYrszHvlW8N1u92SmJh4XkIwa9asItv8zyeekCogk1Bmj74i
2u3TO6d4VMyeop7xIIg9RHs01Cg3HORR/To9g0pVvZP8FGV9VDtITHKdwcwCpcRujyogAHmFIEgE
yudaV1ksFunSpYvs3btXenftKq1dLskI8QyTNE1KR0RImchIqalpMhK1xh5/jmcX1H7Bp4UIQCLI
0SAROAhSDWSi/nsYKmaTCaRFixYyc+ZM8fl8snbtWunRo4cMGDBAdu7cGfgM+/TpIyaTSUwmU2BA
8dxzz0lqamqgZGVlXd4vu8FfhiECxQi/CHQ/RwdxFCTG5ZIzZ86IiMjGjRuL7MhDBQDz+XwFxcPp
zFscDgkLC8sz8s3Pxo0bpbLNJiVArifXTyCUADyOGqXWQs0axhXyfCn6tWwhBKAEatPyHyhT0L35
XnsM5Q3sRG1Wv6eXd1CbsLmb65p07Fiw8w8uL76IhEUgtEU0m5qF2Gy2PJvxN0JIAfCXl0Gqly0r
dpNJHtfbfi4BFHLNZgejlngeRi0p+QXgAErYtuoC8Jr+Or8IZOjPmpmZKT/88IN07txZHnvssQI+
BHv37pXw8HAxmUzicDjEZDKJzWa7YE9tg78vRmaxYsb5+utmZWVxyy23YLVaiYmJwW63k52dHbJu
qPj2mqbx888/07ZtWxYtWgR2Ozz3HJQvryqIwNtvk75pE6+88gojR44stC1uk4mKqLSLrYF/Aq+S
u+krwAjg/1Aewg8Bu1HpMyFv9oPTqIwIu8jd9PQTrV93JLAOWA1UylenFMoE81aUyerAoHNtgVtQ
5qg+hPBwiiQsDDQXlPi1BI+PepzFixeTlJREeno6mqZx9uxZmmRkUFQanlbAxNOnyQHeRxmkCipG
UP44PX5y9PI5KhsbqK3q/6E2mLNQMX3s+v9jgCf1epuBKPSEQ5pGt27dqF27Nu+88w5lypQpcK+B
AweSk5ODz+cjJycHgEGDBmEyGTYlVwtGUplixKFDh7ixVi1qpaXxI4W78m8Hbo+IYPGqVfz2229s
2bKF2bNns2XLlpD1f/zxR2688UYiIgra7SxdupQ2nTrhHT8e8ieU8Xjg2WfRNm8m9cQJwkP0mm63
m2Y338zpzZv5HWXr31pve3ByFA8qJMQe4GZyLYRcqBzK/mfNINe/ID89gBUoi597IE/ayPzMQEUF
/Tzf8X1APZTvwr33wsMPF36NTZvgX89r9L1/CC6Xi8zMTA4fPszmzZs5fPgw2dnZDBJhchHt+AVo
azKRYbPh8XiwejzURIWy+JCCQpCjP5sbZSHl74pF/3kD0BHlJ/AoymrHb/O1ChVSQlCZ2Uo3aMCc
hQtZtWoVGzduDNzDbrfzyCOPsHXrVu68806ysrLIysrC4VC2Z6dPn8Zuv9RQgAZ/FwwRKGasX7+e
lg0a0B+VFTi/EBxEZQ6+Z+hQXp80KXBcRDCbzeT/uE0mE9WqVSM1NRWTyUSJEiW4/vrradq0Ka1b
t6ZN584c6tcPGjcO3SCPBwYN4vaKFVlSSJavVatW8WDz5uzUTRLPouLZBFMf5dhUAzW6zZfc7LyI
Qc02RqNMLR8rou7nqFDM60KcawH8AHTrBkOLUJK1a2H8eA2HIzYwMnY4HISHh5OQkMCBAwe4fceO
gClrKH4B2mgasdWqceTIEdLS0rCjRvGt9Xb6hSBYAGbpdfz4RaAMyty1Pir0tF8k9qEypd2rX+9j
TWPlpk2sWbOGsWPH0rdv34Cj4G+//UZSUhKZmZns3r2b9PR0rFYrZrOZ7t27M336dEBliBvcvz9u
fYYAcEtDb4GhAAAgAElEQVTduny5cGHIAYXB3xNjOaiYsX//fs4CU1FLBpPIFYKDQEuXi7vuuYdp
06cTFRPDaD0xvaZp3H///Xz00Ud5rte9e3dmzpwJwMmTJ9mwYQPLly9n3rx5vPnmmxw+fhwqVCi8
QRYLJCSwbNkyzpw5E9IvoVy5cpy0Wtng9VIPZVveIl+deSiz++1A6EWr/Lj0/zXASzhZLEEFhDt2
Xq9Xyz6FoWka8+cL9etDkyYFzx89ChMmWOnV6z6qV7+ONWvWkJOTw5133knXrl0JDw/n5jp1mIda
ziob4h6C8nXIEWH//v1ER0cr72+vl2yUT0UMyg/A35nfQkEBACUQ/mtORqXB7KYfc+qv11CpMCcC
n4qdujfWJbpEND+v/jlP7mMRYdCgQcyYMSOwhOh0OvF4PLz9tpK0L2fN4tG+fZmbmUkNcjdmRq5f
T/vmzVmwYoUhBMWFK7gfYXCBHDx4MM9GqAvEajKJ3WQSi77R99rLL4uI8ipOTEyUhg0bSkZGhoiI
ZGZmioYmVqyBcm+PeyU5ObnQe5aqWFGYPl1Ytqzw0ry5ANK2bdtCr/P1119LKadT1ofY5JyrP0ts
RMR5ejiHCTwjyozzE4GnpAbK89aHCqH8+Dk2VsejPJJDnbtNv4/ZbBa7XW0AB28If/YZEh/vkkmT
3szzjGfPnpUZM2ZIr169pHLlylJH02QcyjTzMMqk87BeDoEMRFkxBT9zQkJCgec165u5o8gbX8lf
3CDdUFZON6K8jVvo5RaQG/QN4R0oL+kqOOQ2mkuZEmXyWAEF4/P5pF+/fhIWFiYmk0mio6OlQ4cO
IiLy5axZUtrplF9RqS9LoTbl/SUMpE6NGnL27NlzfqdPnTolJ06cCJRLyRZncHEYy0HFhOzsbMqX
L8+JEycCx+Lj4/njjz8A+Oabb+jbty/Tp0+nR48egTpDhw5lxowZzJs3j+/mf8eUcVO4m7sD5/da
93Kg4gGWr15OTExMnnumpqZSrkYNzk6YAAkJhTfu+efhxx/RNI3du3dTpUqVkNVmz57NI71780xm
ZmAkmwK8ER7OvCVLOHjwIJMmTSIpKYl9+/YVErY6DI1/YLb9jMe+HmrXBgSTCM49f9D31CnMHg8z
URvET4S4wkeozemqqHXyYA6iQjOftVoDG6E2G0TqDsSaBqmpULJkGeLjE3A4HDgcDpxOJ06nk8zM
TDZv3ozD4aDKnj0s8HgYhwpNnY1aowc1crehRub+mY+maQWW6/xYUKP/f6E20f3koDx3l+t18i8T
CmomMhc1g6iLgzvpSHnKk3JvCv/36f+FvB/Ajh07uOWWWxARTCYT27Zto1y5clQvW5b/HT1KCdRm
+lsQ9I1Snt+9gCdHj2bMmDEhry0ijHziCd56+22cFrUg4ROhapUqLFq5khIlShTaLoPLiyECxQAR
oW3btnz//fd5jq9evZqGDRsG6kRFRVG1alV+/fXXPPUWLlxI9y7dKeEtwcSciZSkZO61EabaprKp
wiaWr15OVFQUixYt4tNPP+Xs2bPsO3qUnZGRZI0cCeYQ9iq//QbDh0OWWsWvXbt2oRvQ/rZ8/alu
4Q5oJhMPDR1K/fr1Adi7dy+DBg0iPj6eOXPmkJKSEugYVfz+pmBLxxf2B75Jk6BcudyLp6XhevRR
Eg8epJoIa1Hh3noH3X8B8DwqFv8q/Xc/B1HLLSfQrXPM5jyhFex2O5qmYdUFwmw243a78Xq9IVN5
tkKFUrhfv+Y8csN6eFEd9ldAhsl03qlAXUB5cvcJUsld1noAtRSUf5/ILwTTgHLcwsu8zHzmc+re
U+clApGRkVSqVImffvoJgCqlSvH2iRP0o6AA+PkWuM9u57sVK7jlllvytkeEEf/4B4unTmVxenrg
2yjAkzYbK6pU4ftVqwwh+IswROBP5OzZs6xZsybPsQYNGhAdHX1B13n11Vd5+umn8xwrXbo0R48e
zXOsV69efPPNN6SkpOB05homzp49m2F9hvFGxht5BMCPILxrfZdf4n6hcmJl2rRpQ+/evUlISCAz
M5M2HTuy3mQic8SIvELw22/w5JOQmZnneqtWraJxYRvJ54Hb7WbUqFEkJSWxdetW9uzZQ0ZGBg1o
wBbbQXLC3AUFwE9aGo5HHiEqKYl+wPdAcGLFksDjqBlCRSyUxYQZH3fgYRKqQw21KW1Crc0H2z+l
Ax6LBYfDgYhw44030rJlSxo0aEBycjLfDBtGZEYGJ1ExkRz5rulFJYyZS8F0lRdKBHCGwi3GBLW/
0IQ7eYqnmMe88xYBi8XCJ598gsVi4Y8//mD08OG00fcC/lVEm94E1nfpwsdff53n+Kjhw1n43nt5
BCC4nX4hWLZ2rbGv8BdgbAz/SaSkpNC6SRPMhw8ToVuOZPh8pMbEsHTNGkqVKnVe11mxYgXPPvts
nmOapvHBBx8UqPvCCy8we/ZsJk6cmMdu//Dhw9T31Q8pAAAaGq1zWrNe1heYbTidThbNnUubjh35
6dFHcVatisfjIcfthtWrAzOAYLp168aRI0fO6/lCYbPZmDBhAnPnzmXChAnExsby46ofSXWnEllC
48Rd3UILAEB4OFmPPUbiuHHMysxkAGo24OdH1FJFBs34jS78hgYcZDHvYre4yQqxBGVCdaCrgeCF
rk+Ahz0ecrKyiIiOJikpie+//55169axb98+jmRnk4Na8sovAKBG858ACeSKgEP/Z9K3grPJJocc
3CGNYnPRKDr7V/5zDhxs2rSJzMzMPAOGYFatWoWI4PF4WLBgAZUqVSI1NZVstxsvuaanhREH+EIE
qZv09tvscrtDfhs1YILbTZNDh1i5ciXt2rU7x10MLhXD4+Mys3btWmIjIylfsiQNd+xg9dmzLD5z
hsVnzrDy7Fm6Hz7M7Q0bcvz48XNe69ChQ3Tr1i2wNu0nOjqa9u3bF6hfs2ZNSpYsGbDguFCs1lDx
KJUQPD9iBKVSUvhvt248WLEilp9+CikAAEePHmXGecSrPxcdO3bko48+wm63Iz7Bh49SpUurhfmi
0DQyTSbGAO+hHMT8pQf+Dnc9yjPhH8DroL2GmCMCtvB+ChMAUNY3LwKax8PJ5GT27dvH2rVrWbRo
ETt37uSs3gGGEgA/ZnItfezY6UQnvuIrvtT/zWIW1aiGLbCbcPF4ANEzErSkJTF7Yriz1Z1k5pvJ
AXz++ec88cQTeDxe7rrrLpYuXcrIkSMZO3Ysbq+Xny+lISIUFdtWA6JCLT0a/CkYInAZWbt2LXfe
fjuxZ88yELVeGtxdacCYnBwlBI0ahfzj85OVlUXr1q05eTKvIaOmabzxxhuFvm7IkCEcO3aMw4cP
X9Kz5Gf8+PGMHDmSAQMG8PDDD58zsczAgQML3eS8ECpUqMDcuXPRTBouXKgFg3OTBHyA8jCGXAez
XNnKAD5GzRMEkcHk5LyIyRSOy+UK1IoAPqOgACShNpDfQIVmjkU5tdlRn9GF5nK2YqUznRnEILSg
b40DBxOYcE4hcKP2BwojHWWCu4qlbGQjZsyMyBqB5VcLd7a6k+XLl/PDDz/www8/8PbbbzOgf3/e
e+897rijFd988w3bt28PDEYyUQG1c4q4H+dx3uDvgSECl4mff/6Zdrfdxuvp6ZxEJQgP1Q34hSDj
+HEOHToU8loiQu/evdmxY0eBc+Hh4TzwwAOFtmPYsGGYTCbGjh0bOFaiRAm2m7aTUcTK81rWYrKY
QnbcOTk5bNmyhaG651S1atXyeIyaQ4za0tLSeOmllwocPxc+n4+nH3+chjVrBkqLevWw2W1sN23H
qpkxn2up6dAh6vl8JKA6rMIXUvxCMFm/9wPk5KTToUMHXBYL4ag/kLB8r0pCxep/EJWEPgk4jtpY
rgxYVUwudU2K9nvw6e0rSckCAuDHgYPXeK3IJSFBhcIIJQTpQAvsWDFzFzmMYlQeIYj7NY4nujxB
r869uLtzd14b+QwPZ2Tw1Ucf8fXXX1O5cuWAhVBUVJTaELdaGa1pFGYCsBP4l9NJx3vuyXM8KSkJ
r9dL4cMfReZ5bpSfi6ysLE6ePBkoaWlp537RNYYhApcBt9tN386deT4ri9aoKf651mfN+kjx4MGD
fPbZZ4EyY8YMxowZw9y5cwu+TtMCzl+FERkZSY0aNZg5c2agI7rnnnu4redtjHKNCikEs5jFh3xI
Yv1E2rdvz/Lly/Ocf/3116lXrx4W3ZQvOjqaM2fOBExKQyUnARgzZkyh8YpC4fP5GNyvHz9Pncqb
O3cySS+Pb92KKS0LT2UP+w/so8yOHVjzOb0FWLYM8/vv82ZmJrs4H8/jDGBvniPNmzenmdnMFNQS
UjDJ5ArAqHznSqAsjqoALrMZp9OJVdO4k9BC4ENZCKUCLlwhBcCPo8hFJXX9nSghSEEt/Xj0a7cA
tnATVuzMROMZnmEMY3iapxnFKPZm7SX5TDINzzTkwzMfkZUG5QBPdjYWi4WEhAQiIyMpV64cFSpU
oEqVKkx55x206GhamM0FhGAn0MrpZOykSdzTuzder5cFCxbQpUsXWrduTWyJEnS22Ugv5Fn+bbFw
LCqqgFXR+eDz+RgzahTdWrXijoYNKRURQeVSpageH0/1+HhKlyzJB//3f5w+fZqsQpYzrzWMjeFL
xO1206tjRzh5koLht4p+3ajnnmP+woV4ExPBasViNiNpaWRv3YqE2KC02WwMP4+sTWPHjqVnz56s
WbOGRo0aYTKZmDJ1CoMZzOPTHud+7g/U3c1uvuALfFYfX375JaNGjWL+/Pm8+eabPP/889SrV493
332XTz/9tMB9XnjhBR599FFAzVDyj7JycnIYMmQIU6dOPWeb/QKwfdYsvs3IyJN9rCFQWoQ7/4DT
FU+jpWiUWrGCYyJ4OnTIrfjrr/D662jZ2bTFxUmyOHdW3tBUB+5DLekFP9VPQAWUAOSgLHz8WFFC
sBCoY7FwOiODnJwcqsXH0yMjgy8yMgLr/34B+AIlQ0UJwPniF4Jgbw8NuOUm8G7diNvjw4KJZjSj
MpVJCrKbsmGjDnUwYSIKF758c4qnn36aHTt2sG7dOlq1asXLL7/MhNdfx+lwcNsDD1DWrWYpLqeT
/cDLkybRrkMHxo8fz8KFC7HZbPh8Pl5//XWqVKlCo5tu4ja3mx/IO9P6t8XCR2XKsGztWkqWDG3I
UBj+79C2WbO4OyODF1FzvPuAJW433VAd3qMDBjDskUewORx8u2TJRYnNVcVf6pp2FdL37rulg8Mh
5XXvzyhUnPtYkK8K8UhNQ8W8JyxMeOop4b33xHzPPWLRizkxUbBaAx6jVv3np59++rzalJOTI2Fh
YdKiRYs8xwcPHiwWLOLCFSitm7UWm80mYWFhEhUVJWazWdq1ayd//PGHPPzww9KxY0eJjY0t+Nx9
+8rRo0fzeLZGRkYW8HY1mUxFeiT7WbBggSSGhYXMP+wv36FCQGvXa1IitoTEVagg9qgosUdFiSU8
XDQ98YkTp7zMy1KVqno7IgQig4o9Xzuf1G/xtTidJeS6SpWktqZJX5AmIAkQyFf8NSqz10zd+9Ye
VKqgQlcn6+387NNPJTU1Vbp06SJNbrpJInXvWn8YaFdQG+KJl6UslWUsC1nmMvc8PKnzFpsN6dED
mT8fmTBB3c+GtdB7+EtNysh/QLq1aiUiIm3atJHmzZtLrVq1pEWLFlK3bl355ptvAp/dhAkTAve8
7777ZMqUKXL33XdLt27d5L777pM2bdrIggULxOfzybZt2+T6669Xn5OmSRmHQ66LiJDrIiKkeni4
1CxfXpKSks7rex6M1+uVh/v2laYul6xH5aWYrn9mi1GhyX/I932aCxIXHh5IpnOtYojAJVK1VCmp
D9IP5BQq1n0KyM+oePb5hSANlfnLbrEoAZg8WZwlS8pzzz0nr7zyirzyyisyevRocUVGCjab/sds
E4vFIh6P57zb1blzZ3E6nZKdnR04FqqjmDlzprRu3VqioqKkVKlSkpCQIFarVapWrSqHDh2S9u3b
S82aNWXgwIF5ksuPGzdOVq5cKTExMYFrRUdHh7yHX4xee+klqRQbm6eMHjVKfD6ffPXVV9LlHCkh
T+gdLzYEC2IxI04zUtakQiSU0AXgHd7RO7OaAuEC8wTW62WtwPUCNr19DoHxAnPEjEvqobJ7VUWl
b3xbF2y/EHytf36lUSETgts3CRWKYgMqgU4pm02aN28uderUCQh5YcWBQxJJlNKUzlMe4AGZy1yp
TGWxUvQ1QIVs6KuXB0BaWZE6VZF585Avv0SsWIoUm2Usk6qUksoOh0x87TVZsGCBuFwuqVKlitSu
XVsaN24sS5cuzfNdmzZtWiD0RalSpWT06NHy1FNPSZs2beTbb78N5JtYv369NGzYUKxWq5jNZpk0
aZL8/vvvsn379kA5n1AToZg+fbrUc7kkFZVY5x/6Z7JMF4DF+mf3eVDZGiQEv/zyy0Xd92rAEIFL
IDU1VUpYLDKA0DFdNqBGfTNRKQFT/AIQHy+UKRsQgLlz5xa49sKFC8XlckmJEiUEkAcffPCC2rZp
0yaxWCwyffp0EREZMWJEyM56wIABkpycLOHh4ZKQkCBVq1aVWrVqicvlkri4OImIiJBTp07J+vXr
pUuXLjJ8+HA5ceKEzJgxQz788EMZP3584FqapkmzZs1Cdk7DH39cqjmdskHvTPfof4Q3uFwy6skn
5csvvzxvEXCBtEfFzAk+H4VV3uItWcYyGc94sREjsC7EpVJ0IXAKJApMkHCcspbcBDfDQeqhhP1n
XQgcqNledAgBCBaC8qgZ4TyQClFR8sEHH5yz8zZhkpKUlD70kW50C5TSlJaSlBQLRacI9QvATyCn
QaahUpD+D6S5GalRHpkzB0ms7JC76FCoEAxmoIThkJFPPikLFiwQZ6RTsCDOEiWkSZMmsnbt2sB3
zOPxyLx586RevXqBNlSqVEnatGkj8+fPz5Ns6Mcff5QWLVpIRESEhIWFSfXq1YtMRnSh/Pe//5Uh
druILgKj9c/jHpD/ohLuNADpoZe7dXFYiooj9eiAAZetLcUNQwQugWnTpkmTQgTAX5agAntZ9eIE
sUTGiqVUObGXKBFSAPwsXLhQnE6naHou2AslNjZWqlWrJj6fL09nUapUKTGbVY7cxMREERHp37+/
VKxYUapVqyb169eXJk2aBIKHvfDCC4E/2OXLl0vbtm3lkUcekX/+85+SnZ2d59rR0dGBfLTBnRPk
BhgzgYwN6thvcLnk7k6dpHNExHmJQCgBEBAXFvmWb2UZy8RGuMDqIi6XIlBa4nFKW8JlXb4KfiFo
gErc/jNqyec61OixqHbej8rw9RNIQliYVKlSJWSnrWmaVK9eXW5IvEGiiZYwm0USEpCE8qqEhSM2
l0lcZpeYzjEL8AtACsjNIG1Rs9N+qFlBJEhiZWTuXKRaOYd0CCEEDzNQnNilcvmqcscdncThdArx
ZqF1C9GaNZOb9GCEBw4ckDFjxkjLli3llVdekTFjxgRmAhUrVizQuS9atEg6dOgg8fHxEhsbK2Fh
YbJ169YL+i6np6fL3r17ZcmSJTJ16lQZM2aMDBw4UDp27CiNGzeW2NhYGaC//88FicDdqJldR9RA
LPhzWqa/b5VABvTufcF/X1cLxsbwRSIiTJ82jXIUbWJVAbVRtxc4BFTHQcezzfnOvh673c5dd91V
6GvbtGlDREQEN954Y6FenUXx0EMPMWHCBJ566qnAMYfDQWxsLCkpKXi9Xo4dO4aIMHnyZMqUKUN8
fDygrIz8JoETJ05kzZo1fPbZZ9x22200b96cmTNn8vjjjxMfH090dDSnT59G0zTOnDnDgAEDeP/9
9wEV66YNMJNcK4TjKAsbHyrr1dKMDGp+9x2YTKxDJZXJjwDjUHb4T6M2YYvCgxtlyV8Y0WiU40PW
c0eIsxoq30AEysSyERCJCvoWE6J+MHEoc9EFKIuuPXv2FKhjNpvp1asXmzZtYvu27TjsGs+O9uRJ
23DqFAwZ5iPlTBZkaOC1ECq3nBloikpE00Zv60TyWqgtAO7eCwcOwBtTshjSfyn9T2zHSQyg4cHN
AQ6RzWD2Hszh6MG3yQHMmcDRFaBpbK1Zk3LVqtG6WTMefvhhhg0bxltvvcVnn30WCH6Xk5OTx0di
9uzZfPzxxxw7dgyPx0NGRgY9e/YkIiKCZcuWsW/fPg4cOEBSUhJHjx4lOTmZU6dOkZaWRnZ2Nj6f
Lzd2lMWCzWbD6XRit9txOBzYbDYsFosyYdXv+Q3gNxfYjAoUOAsKeFm0QMVz6gzMnTOH06dPX3BI
l6sBI3bQRfKf8eOZMm4czdxuXkEFCQv2AS6FskBPBxqgkpe8jZn9dKQTnRjkehJXhI2UfPF/8lOm
TGkSEuJYsWINYWH5LdaL5tixY1SoUAG3O9e+vGnTppQpU4a5c+fidrsJCwtjy5YtVK5cmTFjxjBz
5kxiY2Px+XysW7eOnj17snbtWk6dOkW5cuX49NNPqVWrFgAdOnSgd+/ejBo1KuDzoGkaUVFR1K1b
lzXLltGWvALgxy8EPVFJYGpERDD8P/9h9PDhzM/MpEFQXUHF+vmqZElOnzrFHArmIwAIw8Is5uDE
SSva6hYuhWfAMtGAhYWIgJ9IlHhHogK3lUZFBC0qMtITwERNQ/wpGEUgyO7d4XDQtGlTli9fjtVq
RSSL0aND5+1RQgDJqeBNt4I3rwuWFX9MIBWk7kaUh/K3eZ5TBc0LB/o4YPwEWL4YZs8BHy683gF6
zRTgNDbm0QEVdK6+fmY70NRuJ8Nu56fFi/n+++9Zvnw5jz76KOvWreOll17C5/Nhs9m45557SEpK
4vfff+fkyZN4PB7cbndAHJxOJyaTCYvFgtlsxmazBTp1p9OJy+UiIiKCuLg4oqOjiYyMJDIykqio
qMDPwcciIiIYOnQoqz77jNWoQUQaysnvfuBnVNrOYP4LLNZ/3oEyJQ6rVIlVv/56zQmBMRO4SDav
W0drt5ujqM7sXqBr0Pmv9ePvo/4oJwM5mChPeSpRiVvdN7PBHSqvVV5EICVlGw0a1GbFirXExZ0r
YksupUuXJiwsLI8IuFwuGjZsyLx58wDweDysW7eOypUr8/zzz/POO+9Qvnx5tm7dSnh4OF6vl/bt
27Ns2TKOHDlC9+7dGTt2LD169EDTNPr06UPbtm0DsZA0TSM1NZWcnBycqBHZx6jRalcImH6WQmUB
K4cSgcyMDJYsWcJtd91F29mz6evzoYng8/nYC/xgseB1uwvNuwtQCQvv8z6PFZlT7OLx/7EUHcUH
3GYz8uCD0KOH6sWHDoWUFPD5iIqKIi0tjaVLlwYSudSosbPQxG0lS8KzT8Oof0N6tjevTSpq1jEe
mI8aaNREZSv7NKi9R1Fmkm8C1bPg6X+A2Q5T3oXDhzNYtGgqO3/NolKGjyooYbEC7VGfXVsgEViZ
nU3T7Owgk0qN779fqf/sAHy43VnMmDEjMIL3R1q1WCx4vV7CwsICs1rRHdC8Xi/p6emkp6cHjvsJ
9XOoY1lZWdyM+ptz689+n/5/fuPb8aiYTf8mdxZ/CHhm3z7Gjh1bpEf+1YghApdADOqP7Z+ojiyY
Oqg3tzPK5jzYWl1DY5jnUXql92Ljxo3clD93r862bdtITT2DzwfZ2Qe44447aNWqFUOGDKFatfxj
m4KICCkpKYHfTSYTe/fu5Y477mD06NFomobP52PlypX07NkTk8nEv//9b15++WWSk5OpXbs2Bw8e
RETo3r07c+fO5dixY4wdO5aff/6Z2NhYjh8/TunSpYmKiuLMmTOBkMgbfvqJOwF/F3EQeBcVWjlY
CPzvi93h4P777yciIoI6deqwceNG9u3bx/r1KhGlWQRfejphKIesFiGety9ZvMYPWLGSQBWSGIeX
cYR23VuGj+0FnMGCOYrqUEz6c/gzlvXT2xDKL+Q7YJrVCo0agd0OZcvClCkweDCkpHDmzBni4+Np
1qwZK1asIDk5meuvL6IRqORthVEbFbJil97OrSg/hcigOtfrx9qibPLdOXD7bRAVBQ4HpB/P4I6c
XLH28x4q2F4LlFgDjEVFDk1FQ/0FBHelB4BXcfuUP7Dm0/B6vWiahsfjwWw243K5AjMA//9msxmT
yRRI0Wk2m7FarVgslkAd/+9WqzXPz/7/t2zZQqO1a8kG/of6bh2h4BKQXwCWUfDzqwD0nTyZPn36
0KBBA64VDBG4BJahPEfzC4CfZ1Edhz+6/2/A9Xrsmwgi+Kf7n7Rs3pJFSxZx00035Qngtm3bNlq1
akqlStmEhcHOnT5SU/dQv359Ro8eTWZmJgMHDqRt27aBP5785E/o0axZM7Zv384NN9yAyWRC09Qf
qb+jBejfvz/PPfccNpuNG264gZycHE6dOsWmTZt44IEH+OSTT0hOTmbhwoW43W7WrFlDp06duPvu
u5k6dWog+clsyLPM4kNF6WlHXiEAmKxppHi9zJo1C03TAuvK+/fvz329PrJMQwVti6RgDmEHUI+6
bGADZYjmJO+SiQ9RYd6Cai7DZLqLKGcmA7NhiSdviGggMMN7FtiEEvMXUfkGxqHW3VeTtyP5Duju
cJDx6qsQLNJxcTB5sspcjwqd8PnnKsW9pagePgjtLNiyc4cSPjQ8+nepPbn7F/kFwE8dvX03o5zc
Fq2wsPxXO9bUTNrm+AoIwArUctBIct+bdJQIqF2JGGANBaMqVQHTYIjMRFIkMHPRNA273U5GhvJY
Fz20RvCoXtO0QMcf3MHb7XYiIiKIiooKLBWFh4cTFhaG1WrFZrPh8Xj48NdfGZWTgxnlzHc/Kq3n
HtS+wEqUQKwhtIB3BD5wu+narh0Hk5ND1Lg6MfYELpKObdrw0/ff8zpqZFgYH6CWhE4Ah8waLl80
b8okJtnf4xf3SvVnrPdP7e68k8EPPURmZibDhj3CQw+doUULeOEF2LULsrNLcOONN7J582auu+46
6l1igxkAACAASURBVNSpw++//06nTp148MEH86xl+nw+7HZ7nuxcX375JYMHD+bYsWNERkaSmZmJ
1+ulTp06rF+/PhADqH79+uzevZvbbruN6OhoEhISOHnyJElJSdx7771MnjyZ9PR0Tpw4gcPh4OOP
P1bhBMqXx45aCgu1zu4Xgj2oOP/ZqPy3MS7X/7N33uFRVdvf/5zpk14IJBB6k46ggArSlSL2ggoW
VESKFb1XUeFe7IogTVQEK6CCBcFGFQUBFREBka5ARHoIKZMp6/1jnZnMTCYJ3ut9f6hZz7OfZM6c
uufs9d17le/iqmuv5eCePaF9rU4nsz/4IPTZZrPh8/mIAzqhgDqMSNv8MKAmfbiVW1nOcvLI420W
kE8HDGpgYCD48PEaFouHQKAlTvbQjCMsIBBR7awXOsvugir/N1Cna1AuRBVlffO58i0W9jqdFD71
lFntLEr8fujZU+17UdKlCzRqCCdyS7alZcAll4LFAmvWwOyxsMLkWTgCdMYgB6GbeW/t0GzldTH6
PXQLqJlH3G6YNg1q1SL+wgvZlJdH7bD9VqCFYmajhXHCZRlwAVDAm5SU61mEmxchRO63l0Lnd5BW
rM4fv65CHQ5HhOIPzv7dbjepqalkZGSQkZFBcnIybrcbwzA4duwYhw8f5siRI+Tm5lJUVITX68Xr
9YYmBsHzFJw4gaW4mHFo0SAfOiFJRx3AB1FfwCfl9FEeUN3pJO9vRClRuRL4D6Xo+HFanuS+W4Bb
gY9dQq2ux7hpyRBo1hp57BMIzv5PnOCzO29n/fCrqV/Lym235dG5s37Vv79WcDx69CirVq2iY8eO
VK9enY8++gi/389XX33Fp59+Sp06dRg2bBjNmzfn4YcfLlWecdOmTSGgCCd9czgcbNmyhWbNmlFc
XMzPP/9M7dq1ad26Nd988w05OTm0bt2aJk2a8Oqrr/LAAw/w5JNPYrVa+fnnn7n//vux+HxkojPO
shytFuBxVHF6gcvQWebxggLWvvQS94TtuxKNLAoyHQUBoDfwFkrcNhQtyAKqiPcAxewgjjguRFlO
+9KXpSwlQAAQNrCJtfhpGjiDVKoi1GAX66nLXnQ4+DAoMXCkmdfrGvUs81ES6kXACGBkVhaFEyZA
lSplPH3Z8vXnIF9ArzB7/3tO+HkrXHglPDMWJueXzPCTgDUI7c1+GgKcTom5qkJ55BFwu8EsVRq+
RsoFLkbpLKIBALQfFgC9uQUPvYHVuBjAYAayi1348eMlmeUeKG6EkhflE+EUdjgceDye0Dan04nX
62Xv3r3s3LkTr9eLx+MJmZKC5qC0tDQaNGhAgwYNaNSoEU2bNqVFixbExcWRm5vL6c2bM9jsD1AQ
MIAZKHAN1FupUGLVQPgrSyUI/IdiM4xynZTh0hq1nH4msOVnB4FWTfD9e3QJAAAkJBCYMJFj944g
PXNvCACCEpxAFhcXs3TpUmrWrEmNGjWoX78+O3fuZMuWLRw7dozRo0fj8Xj4+OOPiZZJkyaFKn6F
m5CKi4tZu3YtzZo1Y9q0aTRu3Jhp06bRvXt37rvvPgoLC1m9ejV79+5l6NChjBs3jkcffZQHHngA
t9utZptffuEJoKIqAkGFczFqcumG6okPieSQuQpIAcZhcusYBokivIWaLepRekZ3FKjObkYxikd5
FBs2UkjhUi4F4GM+4hu+4QIuYlgUY+dqVjOGZ/BwC/AcCRRyDWr+iJbF6OrgOKp4nwK8Dkf5AFAG
K6Yb6CCw0B8ZxzTcAz0/h3uWwlS/9ke4ZKJmjRpofeHb0Vl6eRKcp6c88EDos7840s19HP0dYgFA
ULoCCRh4+AAX9/AEDzPHPQdrUyuNGjUC4Gq5mncXvEuePw+LxUJqaiqJiYnk5eWFfEeGYYTqNyQl
JWGz2cjNzSUvLy/kO6hatWrI51RcXMz+/ftZunQpCxYsoKioCJ/PF1pd+DwegpWwD5jPICgAzED7
sH0FfQTgj1nb+q8rlSDwX0gddHl5EcSsknQEeAKlM34QKAzA7gNufK8/FgkAQUlIoOjpSSy49GKG
3KSTtaBE1ZVhz5497N27l23btlGvXj1atGhBSkoKq1evjnDQBqVp06b8+OOPNDdNFcGVgMViobCw
kK+//pobb7yRKVOm8Nxzz9GiRQtatGhBTk4OmzZt4rzzziM3N5cpU6YwduxYRo0axaRJk+jRowdV
0tKoJVLKrl6WFKFgcCPqWF9EabpmgH+jJqMpQL4ILigXeIO1uLx8z6OMoj+DQt9tZztTmEIf+oQA
IIccnuRB8kyytCp4Oc7TFBNPuzLIjj9DS0JOQu3NoMyiV+bkwAcfwEUXlT7I71ebntMZUYjHgfoW
FlI6kDUBWFSsq6ocYkum+cw+NHR1M5oPULrckCrD+9GV2vowZtdMdKVaq4xrlCdWhvMEjzLHPYfs
7tnMfm92hI/j9nW306VLF4r8RaSnp3P8+HFyc3Ox2WzUrVuXpk2bsn//frZv38727dsJBAJYLBac
TicpKSnUq1ePrKwsPB4PB0zq9ePH9beKj4+nSZMm1KtXj9q1a0fQlh9AJxeXoiA9DzUfJqOlhDaj
0U6xZCb6uyxZsoTu3cuDwr+OVILAfyEXoEvzHujsMBwI1G6rL+GjwKvAQQFc7tgAEJSEBJPXv2RJ
unUrxJqciAhHjhwJOdvS09OpWrUqOTml1UZ2djabN2/ml19+ARQEgvZUj8fD9u3b+fnnn8nNzeX8
888H4PXXX6dly5bMnz+f5557DrvdzpAhQ3j44YeZMGECd999NxkpKRzavp0m6ODZjSr5soiPt6AK
/z3UmdmZ2AAQlAuBlwyD/JNwXR1AVw9f4WEw3/MY93AcVXRuAhRTxK3cGgKAkQzlXo7TK6xQzQzg
efJKxZVDCQC8h1I2h8sqj4dznn9ejU7hQOD3w5gx8PXXEEWr7UTNhGVlMiSgYY6lq0qUlgw0Sao3
assPBwJBE+wWoOU1w+U1dIa8AE04O3kJ4MDNwriFZHcrDQAAbdq0Yfny5XTp0oWcnByKiopwu92c
c845WK1WPv/8c44fP47L5eLMM8+kT58+HDt2jMWLF7N3716+/vpr/H5/CBgSExOpX78+7du3p3bt
2uTl5bFnzx5effVVioqKsKMrmW6oqXEMuuLshq6Y3kPHaTdgKaWBYDK6qssGrrzwQn7Yti2UPPlX
lkoQ+A+le79+3L56NavNz53NFpRlaOyxHViPKpAWHiiuKMg8ShYvVh9eWbT8IkJhYSHx8fHYbDbW
r18fc79NmzYBMHv2bHr16hWKDgpG4xQXFzNq1Cj69u0bstVWr16dXr16MWHCBE477TQaNGjA5MmT
ue+++3jsscd49tlnOa9dO24WYSsKhs3QgRersPo6VDnNpOKM33CxWCzg9+NFFVpZpMvF5vdOoDke
vsLDRgiZCOwYEQAwiuMMi6pU9hRgRZhtfr4VCKqBq1BFGw0AoGaGlR4PZz//PHELFyJWq/oz8vLg
0KGyf8D/QgRdCXiwMhmhAwHSgevQ1Wl4nsC3aPRQNJSeh/o8+qCrsgzUL1BW5jbmuU5QiBU7263b
WfjUwjKjnNq0aUPfvn156623cLvdpKens2HDBg4cOIDL5eLSSy+ld+/ezJw5k0ceeQSPx0NycjJd
unRh8ODB5OXlsWTJElauXMmBAwf46aef2LRpExaLJZRctnv3bkD9TE+hv88Y8/rzUKW+HA2lbY+u
4HugPp3wPIEPULPtI0ANm41Dhw79LUCgkjvoP5RAICA2kOYgv6GshJPM9k+UQGwOSA5IA5Sk6nMQ
o2pVYelSYdmy2G3xYrE4bDJhAnLnnYjTefLUwRaLJeZ2l8slZ5xxRojfpWHDhuJwOMQwjBBJ3UUX
XSRpaWkRTKEiIrm5uVKlShX56aefpGvXrvLJJ59I//795cUXX5QHH3xQGlWrJs+hrJrfg/wEUh3k
XPP/bWZbQgkJWxWzJZtcPCcoIdzrjVt6EB9qN2OTZPM54kBuRnl9ovl6PCDnoBTCh0xOmL1R+9gw
ZBGL5DzOkdEYZXL/BEBuMs/RAGSfud0eg38murUFaQ/iOInfK9F8R8o73ySQYWXc4xCQdAyxcLVY
qS21QQ6A/ADyfFh7AeVd+gdIrzKu0wnl0Glo9mESlOJTEpBvzPuG5hJPvNRNrCs//vhjuWPl6quv
jnhH4+LipEqVKtK5c2dp0KCB2O12SUhIkMsuu0x2794tU6ZMkdatW4vb7RaHwyHZ2dkydOhQ2b17
t2zcuFGmT58u11xzjbRo0UISEhJK9WufsPcp3Xz26Of4EOQekBvMd/IekBUo+V8NkOoOh3z//ff/
SxVyykjlSuA/FMMwMCwWOgUCtEEjXuLRWeo3aKLNlea+K1BnWjrgOH4cz/TpcPPNpQumB23HNisP
POBD5PdNIKP9AOGybt26EL9LkMdFRPB4PBQWFrJ9+3asVivZ2dkRxyUlJTFo0CBuvvlmnnjiCWbM
mEHLli0REXJzc7FYLDREuWq6oyahe1Cn5fnmOYpQ564PXY43MrcLOhs7H53BXYSDa7iZ6ubcXRBe
4nk85AA+CtDZKmj/Guis9WM06uhX1IcwC10N1Ai7zl3oDP9S+uDDx1cIeahJKnplYQAtUF/FzWiY
6EXmeSoSMZ/9ZMSLrhCvjHEPoCGdi6CUd0LQcNiFQC4XELB/C/G/0vOYzuQz0PDWaOlP2eGRWeY5
gw7oD4G+6Mw4PE/gftRE9Tq/4idQbsnLoIQ/WyAQoKCggKKiIr755puQf+Dcc89l9erVNGrUCLvd
TvfuWts4MTGRZ555hrfeeitUnKhOnToMGDCAcePGkZWVVep6gr5r96JJY7Hc9ReYDdR8dhM6Rhuh
kVFnFRcz67XXaPnMMxU+359e/o9B6E8tM19+WapYLHIGyCiUOngBsWmGn0FZKduC2BIThWuuiVwR
LF4snHuuGE5l4DQMQ5xOZ5mz+9/T0tLSxOFwRHDaB88bZBM1DEPi4+PlpZdekvz8/Ijn9Hg8kpmZ
KWvXrpURI0bIp59+Kv369ZP169dLdlKSzATZga4GJpUx0xwNUhddGYVv96GMly6cMprRpaiN5zNf
alErgko5DqUBzjRnrGeCnAdysTmTSzRngMEZ83B0xfEzSg19BGSPedwIYq8sJoC4DV0FvGPev5WK
VwJtfudvE2feX/Q9+ECuAknHJfEg3dAZbh+UFVOZMV2CvZrQziH0Qm62ln9v34G0KuO7Cyi9KvkY
5EqUtTXT7PPbQdaAJBEnl3O5JCYkyrx588ocI16vV8444wypU6eONG7cOLQaDf8bHx8v6enpUrVq
VenWrZs8/vjj0qZNG3E4HBIXFyd9+vSR7777Tq7o00faNWokdVJSJN1mC7HTRrcuKF302SgLbHl9
IiA28515AqUKF7MvLujU6X+tQk4JqQSB/1Iu7NVL0tGCFeW9aEEQ6GAYqnhdLqF6daFWLTFq1xaq
VhVLfLw4nU5xOByhQjLBFzs4aH5vczgcUqNGDTEMQ2w2Wyma5/Bms9mkWrVq0rRpU7nnnntk586d
oeecOHGiNGvWTI4fPy5dunSR7du3S9euXeX111+XeNTMMLqCPhhOSbGPYAuAVMEloxhVZpGT+cyX
DDJiKtChYQp0LgpEi1Bz0/doYZX6KM2yL+raQdrlWEAwHsSRiXS0l2xrCvJUOc+3kshqYYC4XEh8
fElzuWIDwS2UTCIWoBTIcSCtaCVZJMr0sO8WghwHSbIbQjubMBqh938OAk+bfbS/jOM2oqai6ai5
SEHALbdzuyRglfi4OFm8eHGpseH1euWKvn0lJS5Opk+fLo8//rh069ZNmjdvLoZhiGEYocmIxWIR
t9st1apVk6pVq0rt2rVl+PDhMmvWLGnTpo3Eoya6FWHtnhj9DWqKaw7yBScHAk50EnPM/H8uat69
4vzz/3+qkv8zqcwY/i+luLiY+qmpTCoo4OJy9huHmok+BLIbN+a0004DlOlzx44dHDt2DK/Xi8Vi
CSXHiAh+vx+/34+IlGvuKU9cLhciQsuWLcnJyWHfvn2h74ImIlAHbHp6Ojabjby8PKpUqUKTJk24
66676NatG/Xr12f8+PG4XC4WL15M9+7dWbhwIV988QV7f/iBqajJoSyZgobnTQnbdq/dzlS/nVcD
r1Il5sIdfuEXHuAOjnMstK0YdWbOQ80NO1CnXzBKqyVqfvOjDtHj5vdvEumUPoYyTH4LoazZ5WjG
7OFqkHoIxvjV4X0I+AdqNrk36h5XAedhIT8UtKm8PJ07Q3gZ5FWrNJI0PCHVjp00nGSGkVQHsPMT
v9CABuTzG9M4HHpuzCtcBspZYgAboOGH8LVXQyFjyb/N/lkRtu0ZA/4tGi0Tiy1H0MiidygJ7f0A
6IGbK7iaBbzJGDzcHxfHjNdfp2lTjbkREUbfey/5y5axtqCAXLudmjVrcumll7JhwwaAUPixYRhY
LJZQBrDD4SApKYn4+Hg1Vx46xJVeL9MobTZ7ADVFFkRt74lG5LVGqSIuLKNPnkYz+jejzKM10STF
a4E955/P25+Ul1/815BKn8B/KQ6Hg7O6dOG7jz4qEwQEjRBaaLPx5ty5uN1uVqxYwbp16zhy5Ag2
m420tDTi4+NDL/7BgwfJz88P2e6DmZMipTlXKpIiU+MEY6ztOHDh1NBEARs+cinEg2YlBwIB3G43
+fn5fPHFF3z99ddkZGTQo0cPhg8fzuDBg1m8aBG5x46xcdMmCgoKyKxRA8LA5WQkFwWExIQEouqa
h+QXfuFehnE7J6iPRroEgAlY+AgLc/FxBaqg66O27W7AHUQmehWhSvNaIoEgBQ3zDQbkzgRuIh6h
GfyWw1H83EEWTjRPwcsWnqOQzQTzBAz8wBQM8rERVNNxLujSFUbeG+n6adkSHA545x0FAgcO6lGP
cYxjKlNZyMKI59/FLgYxiKt4nloEqGtuP6GXLtGKLeCXXdBpI3wRAwieAJ6xgGGBOubDB5chfbvC
Ve/Dl76S3Ifg9w+jfERfo+HOnYBbAA+FvMEbZBDPAXx8WFDAsOuvpzjsYdv6/bQrKGA54PV62blz
J8888wwOhwO73U5xcTFJSUl4PB6KiopCYODz+Th06BB5eXlY/H4uLAMAQH0Wx9HQ3mjfSRbqN+lr
fr4Q5X0aS+TSoQ/6+x9Do4U+QfM3LjpJXqc/u1SuBP4A2blzJ906dOCeQ4cYEdWdgjolZxoGM+fO
5dJLL415jvz8fLZs2cJXX33F6tWr2bx5M7m5uRQUFBAIBEIDxev1/m4QCBe74SYgTfCHzWVtfEUK
08mngCLDCBHZBVcgwVT/oqIiLIWFXAicZh57HHgZHTx1USdcbfPz4rDrWlDO+zhKVgJHgXpuN05H
EpNzJ5daCQQB4EnyuRqhtx3W2MBq037NDwDF8LpXZ/NDUWV/BSUhguESBIIkCIWAgjqQOzmdHBFh
cbET4XGUkT8HDfYN55dfgo0LETz4ORt1m/5o7qsA4LLCOR1h1OjSvv+gTJoE8+dDDV9tpjKVSUzi
V37lcR7HjWYJFlLIvdzLLrbTAT8L8YXCbn2AwwAZHXZSAed8aLQRHghLLlxnGEwVKLYLZ58dGZOQ
lqbxCNdeCemFCp7BW96IkuQtQZ3NwW0dUQAHBbEM4rmF44yO4rl+DM2RiZ6lByUYiiwioZVAtMRb
4MmArr7KkjnAEIuFXEsgVHOnB+pUB12B90Vn+bnA52HP40UZkIrRHJf+KPA5gS/XruXMM8sKlP3r
SCUI/EESBIIRhw/TI+xlftlq5cO0NF5880169uz5u89bVFTE1q1b2bhxI2vWrGH9+vXs27ePQ4cO
UXjiBE6/P2KGlE8pyvmQWHECzfDzOdG8mTbGkMLT5FNAQkYGx44dC6X2Qwl3z1A0kseghPahH5Hc
Oi+gyuMTVOmDRu5chEbCvGBuC4JAowYtaPpjU673XR9xT4O5lpH8yvUmAKyuDYVXU5I2LMB8MDYa
TPQKU9EIrfKqNBShVA3hL322w8H5Awbw+uvvEwhchs02C6+3NoHASiIBIChL0HllkGjaT7DX44Ce
dqh5K1x2Wdn3sXw5PPYYdPUqLd0e9jKOZ0IAEJRCCrmHOzmDXbyKN/Rb+wGnAf4RRGYpCtiXg2sf
EADLHgtGwEqx304BBTidynLdqpV5Hj+8/baT4mInfk8xDr+f1ECALn4/qagpKLqCxcPobDooNmw4
8dGCkreqEFhvGFgTEykoKMDn84WoSsoza4abJ51OqF8dhu6qGAQeJIO9HMeDhtPFoVFj55r7DEcj
sb5As6vDpRj9NfehZkEHEG+zceDYsd9dyOnPKH+P9c7/B6lXrx7L1qzhhssv57XDh0Pba9apw7fv
vktaWixiiYrF5XLRsmVLWrZsyTXXXMOmTZvo2bEjqUVFxPn9zKOElrkATZXfT2wg8NMAYgAAgI8x
HMNDApNwOp2kpaWFeOCPHTtGAjCY0gBwNcovHy490DDCf1CSNNYQHYA9UcAI+g58gQDvf/o+Xc7q
gpFjcJ33utB5TpDH+Qh9YwEA5o1cCILwyEYo9MYOjYzoz6jPj9psJFSrRrVq1QgEmpOe/iaGYeO3
32YSGwBAg2GvRtdAJeJGq6iVZm0qWwop5Fu+ZS5zSwGAntPNOCZwNZeyD2+I198KjAf+OR0KbqYE
CAzwdgWvB1xzXGCDuwrv4gVeoIACPB74YgWs+UK9olarlWpZVXnoyX+RmpoKwIply/hk+nReLCjg
vbB7MdDCQAbqPxKREB/Q1FdeDU0Ygpz/zZs35/vvv+eLL75gwYIF7N69G6fTSXx8PFarlcOHD5cC
hPA5aUaGAsHJSC65hBuMfKiZ5yM0E/p5dK0WDQCgSn8+Gha8DjUF/af+tz+jVILAHyh169bl8zBu
/j9aNm3aRI+zz6bL8eOsQmfadYjkj1+L0goftdu5rH9/Vq9ezY4dO8yXugexACAoPi7CyzTOPvts
PB4Pv/32m6bj2+3k7d/PnSKhYXYnugKIBgDQl+oNVGE8izrvQBX0J6iD9m3Utm+xWhk9ahTLv1pO
q8Yt2efdR01qAuChmOPAigB4owEgKCYQHN0KA7y69D9ZedRm4/WsLJatWcPNNw8iPf0rpk71MmJE
EhUNDStWLKg5ISgBlNr6ZEFABDawDRvOmAAQFDdu4rATIJLeeIQAhXDXdPAPpGTZ5QdjrkHgcIDO
ns78yGZyTae6AaQL/ENMlenzszUnh6fGjGHZmjVkZmZy8cUXk5+XR6+ZM7mcksIsB1EnbC9USbZv
356pU6fSoUMH7r77bg4cOIBhGBw+fJjdu3ezatUqvv32W9atW0dBQUGIPdRzkskvhgEJaUrncC2x
ITkfmIqTupzGZraHVgK3oEVyLqMkHyAWAAQlWDs6AExDfUbOk0WgP7lUgsCfRGbNmsWtN95IYnEx
76M2y3PR5KhhaJSDgVIcrAUaer089thjZGdn07JlS9q2bcsrr1R8HUGrkT399NM0aNCANWvW8Nln
nzFt3LgIAqM8SpbascSGzsD2o0vtXaHz64DrZt7rqIICbnvrLUYBmXWSsNb4jMIU01b8rkAxWAzK
Z44zwGszSyBigksZuwbrrLUD9iclsWbNGrKyssjJ2cWNN3pJr6iKvClWFMy+pbTNu7EPpn4A550H
iYmljy0qUsdwIAC5WEgqk2mpYhkh8GYhbJxRoqwLgIxADer6szjG53SkmNPN7z5AfTd3Etalfj9j
c3Lo2r49y9asYd++fbw/dy5voia8oAgajDQNSEtLC1GWu1wuDh8+HEFP/kdJ81bw8qo4zqWYFfgi
gCAf6IOTBM6iH30YG2akSkcV+Wx04nGyNu/30QlMdvXqJ13w588uf4+n/JPLvLlzGXHDDVTxeumO
ZssGldwR1MRyL5FAkGKzhWZcx44do0aNGpgxJeWKD1i0aBFt2rQhKyuLhg0bcs455yjl74mKjy91
7yiX0KNh25ah0SpL0QzN7IICPn3rLYqcXoYMgaZNdcj+sAbm/Bx9xhhyQgP970NNMgPRWWA0EBxF
DTmXoNFEB826xgMGDMBiMULOUjVd/1ruJYVfuRytOhYtwwV2/gr3DYOnpkQCQVERjBwJ27cH2aUT
CXAUQSKorSOvJfiIbZ4IAAkC07xqghPgUiz8gOBjPcvwRhD0jURnxoPQiJqg2n7I5yOQk0O/7t35
Zc8eXszLI5oP1UAjrrzAxCNHQhm8/yvJy9PVkpcqgIvO/EyfsAzlpThI5yzu4UHWsx4JU/WC+jL+
iTp8QU2k5cFUHhpO+gowpjySx7+YVILAKS7z5s5l6MCBZHu9tEbt7H2B7ZS80E40FM4KPGluC9pW
CwoK8Hq9NG7cGKfzCTyeI8QmvhYMXsFnhlcEAgH27dvHvn37+PLLL4kLBPgStYT/HskEJhIZ3hd0
IAbZHPcArxUUMDxKBz70JNx1K3iPo9676IKxAnxmg/UWsNgJxEO+38/7Hg8DRHiDEiA4ioY3dkbN
CyOAL4qKGDx4MK+99hp7fimpanbbbccZO/ZqPJ5lQNsYTzWKVJZwNZGlRW0oDcVjwLM+4FcYeRu0
O7fkdld+BXv36qLKCjix4aMGzzGNO6JqHOgxwgQmUAV/qZKIAbSAigcFWkHfj88I0IR9MSm641DG
0L4oUVr4/V/v8/H83r3Us1hKAUBQDJSi48kyvgciyAmDYZ/hzWq14nA4yM3Nxev1UrduXdq2bUtm
pj7hnDlzOHbsGAUFxSxZAgkJObQ5cS2ZXMJBSso+nkMSfemLNYZqX4COi63oRORplLp8JrGB4FmU
RO5ySjvC/+pSCQKnsKxbt46h11/P4KIixqNx2vPRgehBQ/U2o2FvahvVcMfb0fDOIH97fHw8AwYM
4OuvN/Dii13weJYTHVJiMAJ4nUCMgD6fz8dxlF/Fhc6k66AzyfOIzQh6FJ2NjyB2fPcg4DAaJiv3
JQAAIABJREFUtfELOoNPEti/H8x8IzIy4NlpcMON4H0dfAMpAQIBPrXB4Rrw9mRIMH0dIhSMn8AH
Cz7CLWAxYcBHADs1SWI/hWZOBEBhYSGLFy0iwQE5ZprDOefAgw/m8cgjXfF4lqApRyoG/8LOVJLx
MQsLhM3Q81GbOZQAQat9sG+2OiVfBHx2Qm4Zvw8KTgAs4VO6QRQQKAA8z2d8hp0i1gGNwx7/XjQ4
dS4lADAHZf8cQNkU3XFobeylZXxfFktrtNSvX5/U1FRSUlJITU3lgw8+wO/3c99993H22WeTnZ1N
9erVSUlJweGIRnCVW2+9ldmzZ2O1Wrn77rsZNGhQqKqYzeZk714fyck+Pj7xEVN5nnRK2+u8eJnD
HLymh8aFKrYOqE+gJ2qa7EdsIHgWnRjciK6Er4+LY/jQoSfZC39+qQwRPYVl7ty5PHvddfxYWMiL
aPw76IC/AbX9v0dJxMsxVEGfhdp+v9m8maVLl/LWW2+xYsUKRIQ77riPF1/8FI/n1rArfYXF+IDq
NVLYu3dvuffkRrOfa6EzySyUijgcCIKz7nQ0+7YspfIJcD0KRy+jA/BSFzzwKLRpU7Lfb7/BPfep
IpUBKBB8ZoODNeDZMADYsYOEmTOx+nzw2wE4VkhR4WV4PGNRtRCHiyuow6fspiCUAZuOKs/rnNB/
GPTrp6f78kv497/t+HwaayUCmdTBiZ9udGMJH/IbR/BEmWrigYuxUMfcHgAmYaXIaeC7yaesZqCo
MckNRY8D1+GiG+kU4TCdxMUUcpjDFHECKCQ+rJ+Dfg9vWP+mohODOFQB3lxGv4Nm0y41/wZlN9Ah
KYl6hsGq3NyYxwXFChT7fBF+gDlz5nD99ddTo0YNduzYEYoWqkgmT57MyJEjQ1nxQdDIz8+nsLAQ
m82P3wNJ/nSeZ2oEEHjx8gAP8AM/hJzCTnSC8TBqGg2WLS1AgeAwJVOgAnS18J3ZF08ZBg+PHct9
o0ad1L3/FaRyJXAKy9q1a/m+sJBX0JT+W9BBvwGN1LiTkqStoHyOKgAf0KpVK5o1a8a556o9wjAM
RowYzGuvzcTjuReFEwPD8FOnbjY1atTAZrORk5NDcRmFD/yoCcFlHv0TGi3SLWyfWWgN4P5UPKvM
AvbhpD820oCUIj8PjSri4THQsKHuY7fDmW1g0XLwPAsWGxQXBGDehAgAcN9/P48++CBNmjQB1CT2
z3+OYfPme/F41JNSxDtsIZngJN4GfInOsJd74Kwpaqrp2BEaN4Y33/Ty+TILc2ck8YxnEi/yIj58
9Kc/venNUIbi5YhZwxjiiONGBlFEETlmoO5uduNxfonvJm8JAICixeBCmHI/+KGIL9jHd2E9/TAl
ZXrUoftDOX05jJOroVuWLDIMkpKS2HfkCMcoO0D2R8BimnrCpX///tx7773s37+fadOmcdttt1V4
zRMnTrBihRJZFBcXY7Va8Xg8xMfHc8kll3D33XfTsmVLnE4nkhhgeN5wOvs7A7pS2shGdrAjBACg
QBlrFRSHmk1XU7J++xIFz0wUFNOqVPlbAQBAJYHcKSobN26UeJtN7gXZCVIb5H6QmWabAdIE5F8x
CLF+RpkRMVt6erqsWrVKtm3bJikpKaUIt4ItIyNDzj777HL3STDJxhaAfGb+vRrl3r8SJYizocRt
j1RA3PUxSDUMOZuzZBrTQu0qrhS3E0l1IOkOJM6BxMVZpGlTu7z9NvLee4jFbhE+/VQZWKdPF3dG
hsyaPbtUP+bl5cnpp3cUp/MmAb9e2pIk1Eew670WhN3TVpBaLvT6TrekO+OlnitLnud5aUc7aUUr
+ZRPQ+R2b/O2xBEX6p944uUpnoogwOvg6CBchDCmjNYWAbdAK4E2Zqtnbivp+2SQwjL68nuQVJAx
IHeADCQ2O6qY228msk7BTJB0t1tGjhwpDWrXkqaGEuxFH7sZpLrbLS2aNYv53q5YsUJcLpekpKTI
iRMnyn3HV61aJdWrVxer1SoJCQmh2gBut1smTpwoIiJPP/10qXcwPj4+5rsZrFUQZAK9m4pJDV8D
6QfSF+Qs/j6kceFSCQKnoBw8eFCyUlKkj/ki1waZHOMF/rUcIHDHGCBWq1WwITRHqItQB6EmgiWS
SbQsxlIrWjDmA5TJMti+RpklM9BiHckgL4PUQwEp1uDLR4uv1CFTFrO4FHPoQzwoaTilI1qgph4J
kuKwSnIiUi0DwVoCAgmNG8vLM2aU2Z95eXnSsGEjcdJY4IhAknA5QnxpEAi2V0Gq4pQ0HOLGIck4
pDrx8jiPl7rXmtQsFwTaO9oLl5UDAufEBtzoloLSOkcDwfco1fMZKAPmUZQtdDClgSBgKv9GpgJ8
F+RxTHpum03cyXYxOhriaI00teu5N5vtc5Asl0tee+UVufnmm2X37t0x+ztY7GXAgAExv/d6vTJs
2DBxOp1is9kkPj5eEhMT5fTTT5dFixZJw4YNpWbNmjJmzJhSrLdJSUlyySWXRLyjVatWDf1ft25d
saO00HegFNEflvEOfotSjrcFuQzkdZCrevf+Q8bwn0kqzUGnoOzZs4d0v59NqON3OMrDMzJsHwtq
k1+K2oHboWaZoEjUOQOBAFjBVRUsm8FqWENp/A1bN2fzlp/M9P5A6Gir1YrfX5J77EZNUrcBrcLO
/S3KC3QJmrFsQZfYw9Hs4GVEFjIvALoasE3cTGV8KLpjN7v5F/eRSx4AfgJswGAtQmNO4C+GrcUQ
yINWFvAXFSkbW0EB53bqVGZ/JiQkcFarlmRve481nEUBxXoT5tsfK/jyOuA608TQAw0/fRw7tpOw
oAZNQ7/wC9OYxm7vbuKXxMNX4K3upbh3caRnMgWifMylxEBdIW40wqlJ2HefoA7Qd9B+LkDJ9Gah
5sPwiK63Uf/H6cC75jY7GnBwi89HnVzYtBUKroUdNuj4o3lCMUhJTqJu06YMvP567E4nS5YsYdCg
QaXudd68ebRq1YoPPviArVu30qhRo9B327Zto1u3buzbtw+bzYbNZiMjI4Nnn32Wiy++GMMw2LJl
C+effz7PPfcchYWRtHDff/89H3/8MR9++CE+M2/lxIkTxMfH483Px75rF0PR/BSb2Q8D0Nj/C8LO
sw4NF26Mjp/HgGEOBykZf7fYIKhcCZyCsnLlSqlisUgLdInfDeWXzzNnrQUo/3k9kHEgA8xZXfgs
xxU9k7QirkyknYHsRoul7EM55rOsNhk2ZIjExcUJZAgYMVcD1dDCMLvDrnMQLdhyJVpY5wHUbJWJ
FuZ41jzmVpAbQW4yDGlhsUjtalWla6euUiOuhsxmtsxkplQlQV7GkAMQahNAapnPG/58NzgcYjRs
KHz0kSTUrCnbtm0rt09vuPxyeRlkKIYkWgyhL0KyzoAvp3StgWCbZT7LHpAuxMvTPF3mSsDlckmN
ajWkurW6TGSiVKGKDGGIPM3TodbM3kwcpzmEh8JWAqMRqpe9ArBYLJKWliZnNGsm56KrlJlh7XbU
HFfV/I1SUU59w5zhJ0e1vmj9gsHm7x981t3mb3Um5krSaghWl2A5WwwjQZo0aSKDBw+W5cuXy2+/
/SbXXHNNmf3do0cPSUxMlFatWomIlmMdO3ZsqEaG3W6X9PR0mThxoni93pjnSE5OjuiHxMTE0Hdn
nHFGxHfntm8vzdGaAOG/3zGQdmjxoUxz5p+KrhDepWR1NNxulzObNpWjR4/+ByP2zy2VIHAKyogR
I+Q8dHmfiC5Vi2MoqJ/RerDNo0BgtKkUwgeJy6IAcCLGeXaYCiQ5wS4JCVr8xOGIUkTmIIoGgBam
4o82O2wASUNr13YEcdjt0r17d5k0aZK89tpr4vP5ZNWqVTL01qGSbE+WJJzyWBmKeEoMIPCDxNnt
Ym/Y8KRBYIZ5n5cbCE0QElQhpREbCIIA8APqK8jAKS/xUgQAjGe8OHFK48aNZfLkyXLkyBG57dbb
xIFDOtJRBjFIBjFIbuM2+YiP5BM+KQ0E/RF7nF1sNlupSnJ2u13cbrcMGjRIOnfuLD3OOUdqgZxh
sUh7m02amr/11Bi/aYb5uwXPlYRWfnvBbI+av/u3Yce9i5rpLge5EpfEkSUQL3Xq1JGsrCzp3Lmz
dOvWTXw+n5x33nkSCARi9vfBgwclLi5OUlJS5MUXX5Q6deoIEKprfccdd5SqYBcue/bsKQWG999/
f+j7yZMnh7bbQFrbbKUAIBwIWqIAmYZWZ3sD5H2zDQJpVqfO3xIARCpB4JSUm266SRqB9ERn+7EA
INh2moMg6IR92FSYCVEDqBqxASD8PFYDueceZORIpGbNyCL3CSCvRB3TEZ31l+WA3GAqHqfTKSNH
joxQGA8/PEqysuKkQ4dkad7MIq1PQ9JcWsox1rnuQyuTBT/PRauHWex2SUxMlGHDh5epkLZt2ybZ
aWmyzDz23yCkGoI9WVJRMO2AVg7rhToK+0QBQDVsMpJ7SgFAkj1JJkyYIOedd55cdtll0q9fP0lw
poiNGgIPhJqdPnIabUNAUN9eX53F/ZH4lHjp0KGDPPXUU+J0OiUtLU369+8vAwcOlNq1a8srr7wi
jRo1koceekh69uwpI0aMEJvFIommUnu+jD4LAoGBrgC+j7HP+1FA8KEJAlegoJiBOmpdLpd07txZ
UlNTpW/fvvL888/L3XffLT/88EOZ7/F1110XYdO3Wq3Sp08fOXToUIVjoE+fPqVAoHXr1vLqq6+K
iK6Wg9vjUR9UWe+2oIEUzdDV5a0gF5rtHJAUq7Xc5/irSyUInGISCASkcXa29Af5BF3KlvdyF4HY
0RXDWabSnWj+DR9ATSs4j5jKYskSZNky5P33I4EggdImp2og21Enbz6xHazno7PZaACoVy9O5s3T
awXbSy8hVeJiA8FUkCFhAFANNWXEo6UGs+Li5I4YQLBt2zapmZ4uLxpG6Fz/BnFgE+gmncxtBeiK
IxWkP1q28nFTwaaD2LHKBVwgAxggAxgg/ekvbsMtbdq0kVatWsmAAQPkoYcekuzsOgJZAj9HPYJP
HAwMAUFf+orFZhGrwyqvv/66FBYWysCBA+XBBx+UtLQ0ady4sSxfvlx27dolXbp0kaeffloaNGgg
o0ePlj59+kgVi0UeBLkGpDtaFjHYwpXibPNzLAAIB4IqptIPBwEByQbp1KmT1KpVS+Lj46VevXqS
kJAgDRo0kGqJiZLidErVxESpmpgo3dq1C82m8/PzQ7N/QFJTU2X79u0nNQYKCgoiSqsC0rVrV6lW
rZqcfvrpct1110m1pCRpgwZNZKAr0i4gXdFghVggUAPkH5RMWj4EyUhIkDVr1vxxA/hPKJWO4VNM
fD4f2/fuZRPqUD0ZNnMDzR79HOXrn/4H3EdyshY+GTJEs3ijU+2Po9HrzSihZvAB96MFXSIiyC0l
BUTGjXuKN94Yz9NPFxDNrt2gATz+HNx2ByQXaKZnuKxFndLvoc7Q1uZ1WgMXFhQwf8YMcvbvp3mL
FgCICC9PmsRDR45wi0joPAJ0x8dylpsuaHW4no3mY6wLu2YCyo1vcdrYUW8Hfr+fvLw8jh49Slpa
GocPH+bQoUPs27ePEydOUFSUbN5puCscwEoxM9nJDTzCeDKdiTwx9gmuvfZahg0bRn5+Pq+88gpj
x47l4osvZuHChQwaNIiJEyfy5ptvMnDgQHr37s2bb75JtWrVuNIwSEYJ885Dy5YG+3wncL75v928
k5aULcE6Dz40/+QQGmgQLi1atOCGG25g4MCBWCwWft2+nXlm32NyVD22fj3nd+zITbffzpAhQxDR
UpEOhwOLxXLSrJz//ve/Q07foMyfPx/DMGjZsiXvvvEGMwIBdqBZ6y9SkkR3CE2knEGkIxiU8PBl
YAuQYBh8FhfHgiVLaNcu+mn/XlIW2WKl/B+KYRgRdVPKk2DsTib6Yz6JZkAKqsAqApEAWvrya/OY
n36CYLJocjKcbtJP+lCOH1AA6I1GAxWEtb0ohcGY8PsOL4EIfPLJe9x8c2kACEqDBtDvKlgalWUW
MJ+nEQqOraOOswCDCgrYP3cuL48eTcHo0fjHjGHS4cMRALATVQS3AB+giuQJYAIaBdQH7cMnUY6c
QvPcfr+fgwcPUlxcTHp6Ou3atSMrKwu/388ll1xCv379SE9PxzCuoDQABMVKMbezjvV851nO7Jde
Ii8vj3nz5nH48GFuvPFG7rnnHnr06MGZZ56JiDBkyBBWrFjB22+/zZYtW2jSpAnbtm2jOBDgJZRG
fAEaBVPP/LsMLXszmsh6whXJF2gCYrL5/GbhNjZs2MDWrVtp2rQpM2bMwCgoYCEKNNXC2oTiYk7f
tIm7br0VEWHKlCkUFhbicDhwuVwMGDCgwnsQESZOnBixLTMzk4SEBH799VfyDx6MAIDlKAh2NdsV
Zn8MMv+CvovfoEFYVYDV6em0eeYZlq1Z87cHAIBKc9ApJsXFxWIzTRe/msvxl8pYxntBrgK5AORF
NI58uvl3u9meRCM93DHMOT6QG1AfQlOQRhakRRySmYS88YaaaHr3LnG+ZaLRKGejdlV/jHv6zTzX
GJBckNoGYrFaJCcnR0REevToIE88EWkGim433YT804j0V9Q2n21lWLvT3H7Y/JuFOq5vRHMLon0g
O8xnDXeifmaaUBKJbYb6DY2YCSbfGYYhSUlJ0r59e7nmmmvk2muvlUaNGklqaqqZxDSsAqvbWski
Weaj5qZku10ee+wxERFZtmyZdO3aVTZs2CCrVq2SLl26SKtWraRq1aoyZcoU+fjjjyUzM1NATUA1
zOfcTUm01/cgdVAH8LeoeatJ+TckgkYTJYK0QU1jftQsFgfSqlUradu2rQwdOlQy4+LK9NsIamrp
bbGEkr1ERKZNmyZpaWlSpUoV+eyzz8p9/+fMmRNhBgJk6dKlIiIya9YsuSIhQX5AzYH7yrmPtea9
F4M8iAZPHABpYrOFzlcpKpUgcIpJcXGxWEzlIyA/oU69aCAIAsD5aPLQVHO/Kmh46BqzbQcZD2LB
Lm5s8hpGBAB0iaEsnzdKgCAIAnaQ1ahvoBmxASDY9pgDsAWI045YrXapWbO25OTk/G4Q2IkC4RNo
AlRr1PfRxlTOp5sD3GkqsuqUAEEz1GZ+k9lqUjqKRtAImjfLeZ7fUOdptHICTa7LyMiQxo0bS0ZG
htjtd5aja4sE/iVVcct0FNTuB3Ebhgy4/noREdm/f79ccMEF8sILL8j48eMlPT1dk/yirlsFtd3H
cvbvMp/1GrNPkkF+LOf5Pjb3u5JIAEgwI5WqVq0q1atXl969e0uW2y3flHMuAbnD4ZDx48eH3ulA
ICA1atSQ7OxsqVevXpkhoSIiGRkZEc9ptVpD382aNUv6JybKair2lYn5zt5DCQAISJukJPn666//
Z+P3zyiVIHAKStNataQxJUBwC+rc64JGDPU0FWIQADabys+BzvwaobHeZ6JOzTnmYACnuLFJDxKk
PjbpUIYSCQJBtUQkI0MHoxPNWk4076O8wZdvDkAnCIZNoL7YbPdLzZqnybnnniEjR5YPAv36qYLv
i0uq4ZAEbJIFMpLISCQ/miMRjITKABmLzoRbo2BYAwXQl0AWlXG/FnTVVd4zdSE2CIS3888/X9zu
zgKeMgCgq4AjFL8fbLeAJFit0qhpU+nYsaMkJyeXChWNblXL+e2CQGBFo8s6oaukWEDwsfluxZnv
SjoKGnEgbdu2FUASEhKkc+fOEggEpE39+r8bBEREFixYIKmpqVKjRg155JFHYr73mzZtKvWct912
W+j73wsCVjQnIggAc0GqJSXJ/v37/6fj988mlT6BU1Aa1quHD81k/A113GUDG9Hsz5Eob/0HaMWu
HmixD0Htuj+hrsm1qH34TtS2HY+HQqwspjb7UJ71snwGQwQanyjxD4BSFY+mNK1/LBEI43T8GJ/v
MX799QZWr97BpEnwdRnV4Oe+BWs/U0K6LxAGMIIM0rgWS6i+cVAsKPPjxSg5WDXgQTQTdA/q5M1G
2TRvNvupLBkKXGO2j07i+WJJixYtOPfcNOLiLoew4ifaE71RurJihEhfyuuAz+Vi6+HDfPnll+Tm
5lZY4zaV8v09ddC++g79BRqgfToDzZ59A/WDXIY6/a9A2V8Po9TkRRYLzZtrxeYTZjGhYPauVNAP
sb7v27cvmZmZWK1WJk+ezMGDB0vtc/nll5faNnny5ND/FouF/YFAhdcP7Y9mRWeg7/qwpCQ++fxz
qlUrr9Dk308qQeAUFKvdThWU7rY6Sn+bgjoq/4lW6RqLOsQ6o47N/miafLOoc7UAPkMpBdSJ7EHj
I3wVKnObgNcsoiuocmxOpHqLJcXmvThA52CmuvL5/kFx8RE8npU89JCTNWu00lawzZ0DC2bCGo9G
OE3EwzxeRTjOUwRiMpIGgUAocZK/hyq1dmjxnXUxjgvKbNQReikaTdIN5ZV/v4JnjCVWq5X58+fQ
qZPNBILPzdYDBQBvzOOKgKL8fDCjmv5IcaOUEE7Umb4Ujax6DX2HnkUjun4iEmADgUAEZYPVaiUv
L4+O3bpxX1xcjKoTKmuBOTZbTIfrm2++SW5uLklJSQwePDjiuxMnTvDjjz9GbKtTp06I2gSgT58+
FNWrxxSHgx2oU7gsmQIkAoOBG53OEAC0bh0dUlApleagU1BWrVol6VarTDLNGY+jNuDP0ASs5WFt
o2kiuR1NfClraRz0GQSTd1xoxm95y+luIAlxyuxooH6IA6aJ4dkyjikwzQ+XYJqDiBPYF2PXhyTO
gbisJa2RMzIjeTdINeKlIXGhbTtRh2ew7TK3x6P0FYKaxO5EM2LnUTorNthmo6ak6Bj6b8xj3jM/
bzH7jgraGWecIYWFheLxeOT6628Tg1RJo54YxCbkK9WiqBDKa40r+O0CqDkkmGj4PWoyHIz6RzJA
vjC/exX1L1jM/gjSS1R1OiXOvF6nTp1k69at4vP55KoLL5SzLBbJj7rmGpCqcXHy4Ycflvlud+zY
UerWrSuZmZmyevXq0PZevXqVesatW7eWOj43N1c6tGgh/ex2qQKhBMDod70qmg9S0+WSf/7zn7Jl
y5b/yVj9K0glCJyi0rN9e5ltKqB0NGM2HQWC6ME+HKQByJFylMJ0IqkkXOa5BbWtbwRZH9aOgrTH
Lg6cESAgaIZtLCAoQKNWaoLcSzgI/BTjll6XC0koV5EFQaABbhGUxiENdQYHWxpq6403n+lDIkFA
KAGCcWgi3UQ0szqdsoHzG1MRrkSjokpxMcVoLpdLOnbsKIWFhSIiYsMmj/CIGCdxbBAErNaT29dN
6Qzu8HfiLlSxB30oP6ARVNPMFg58r6Kg4gZ5CmWFDbaBqH+gUaNG8s0330h+fr707NlTLu7VS1rG
x8t5IOeBXJ6YWCEAiIj88ssvkpiYKNnZ2VKtWjW58cYbZdCgQTGfsSzJzc2VTm3aiMW8t3+gEUAP
gtxGCcXIBpA0l0t27Njxh47Nv5pUgsApKhPHjZN6hiG/mQo3E+Xxj6ck4mUw6vjKIjbVdDQIxIUN
MKtdZ4a/gFyLU9ykShK1zVZL3MRJKk5pS1tpRrMIEAgHglZopE4b8x6botmmCahzGOyi3PgH/yMQ
iDfPNZ4SGofwfdah4YLBEE43mi09jsiokI9RsAy2oaizd3g51882z30rpWk4KgKCd999V6xY5QEe
EIyKjzMMxJroFpfrJAHDfM5Xo+45CABnEDkp+AGNlor1nEEq6SkxvvODXAeSaLHI/PnzpX///rJo
0SLx+XzyzjvvCCAOh0Pefvtt+e677yp8r4uKiqR2Roa0MwwZbPbtrejKpEHYO1qW8zhcVq5cKSku
lwxA6dT/hc7+d6EAkOl2y5wYNSYqJVIqQeAUlibZ2dIYnaWtRGkS3kJDO+NNhdscneE9U44yEzTE
MqLGQEPEZbNKvBEnbtoI5EUdMl6SyZLZzJZlLJMUHKWucRSdMU83laobnV33QKORSq4XCwhWSCp2
2VrG/QZQYrpz0aI1yZQGgHAgCKfJSEBnwSPRMNVos5cHnb1eZP5fVp/VQE0L0zh5EADlSkpMTBQr
Vrmaq4Uy6jNEHoOkV1HyvpO9Tm90JdQTnQxciZrwogFA0BVSqxjPuANdOZVXAMiP5qI0bdJEXnrp
pdD7uWbNGgGkSpUqJ/U+FxUVSb/u3eUil6sUH9ZWFHSvQN/t9evXn9Q5V65cKRnx8TKOElbVF6gE
gN8jlSBwCsvD//iH1LHZJBVkU4zBGyzqMh4N3YzFmSIg8yldZMad4JbOnXuJ3d4hBgBoszBRUqgu
85gnt3CLpJnXCt9pErqi6GEqip7ojP0qdKVQck27aKWsNDFIFxupkoJNapgKIHg+n6l4u6Kz8AdA
OlN2wlz4fYQ/owstFjISBcqHzPYgJmkY5QOAmPf/DgoALperwrDN6ObAIQ6SBeMcIaz6WHSz2ZDm
zZFZs/T/kz1/a/Mex6MmuK5oOHA0m+ZK8xmmx3iHMlCA/aSCvhgL0rB+/Yj384UXXhBATjvttJN6
nwdddZVc4naXSYgYBIKbQZKsVtm1a9dJnXf16tVywxVXyPWXXRZq77/33u8dbn9bqeQOOoVl9GOP
8dv+/bzz6qtEl/2uZzZQqoOFwFVo0fc+Yft9aG4PL81htVq5fdjtTJr0Il7vJpSQobQEGEEx89nM
ZpJJpitOJuLhR5Sm4mu03vFKNCQxKDlAFwjx8qh4zVZIIjAeDXd9A43IGYJqtvdwkE8tWtOWLLTC
7k98gMOss1uWOImMbikCNqFUFk7gJfP8RWjEyCY0nLZ7Gef7Ag2XvAHo1KsXP//8Mx6Ph0OHDpGf
nx9RbKcs8VmKkUB9kOXAKvSXia4C7CQQKOaZZ4SAacA/WdkFfIUWmBmE0jisQPszGIC5EbgcDQO9
G3jJYsFvhp9uRX+jpJO8Xt26dSM+f//99wBkZWWd1PE/fPcdkwsLQzw/0dIQ5TCqDqTd/RyWAAAg
AElEQVT5/fTq3JmV69aRnp5exhEq7du3p/3bb5/UPVRKaakEgVNYLBYLU2fMYMuWLVyyZg1focXG
o2Ucyv+TVbMmA48c4URREQG/H0EHf3RIp8ViIS0tzSwmXz6pVyBsyFrQgMdXgO9RAPiSSAAAHcTL
0YL3cQ4HcUlJ5OXl4TGJxgy03nqwUlkGGqefiAM3DZjAOFy4Quc7wM9oefDfJ0XATWYLSh00xv4C
VDnOpjQQfIGq62LDwG+x8Mknn0R8H11gvSxRXZuJDrNz0SDb6yAC0Fpit6/A6fQQVUSrQvFRosCT
gE/RuP+mYft4UdK9V9BqW2sqyD8oT44ePRrxedeuXQBkZ2f/x+csS/xA9V9/5bXXXuOuu+76w89f
KSVSmSdwiovFYmHpqlX0vf56Otnt7Ir6/klgjGHQpG1b1m7YwPY9e3DGxYHNhp/YMf0iwtatW/H5
Kp7NFpkK6wzO4AucLAQeAtKBUZQGgKBUR/MZLMXFHD16NAQAoAP8BhQIqqJKqhALCdTniSgAALDj
4EgF93mE2NUZD6Hx8aebLdXcfi5Kdnc58BTwvNnGAX0Ng0KrFS/ETNqSiqbrhgFxcViwYI+Y956L
rm32h7VZIVApKn+xU/o+oj4nAYvQVUCw9UIZRAMQirlPSUmJOK4ILVVa1uX3AdOAA4cOhbaF90vt
2rVP6n510nFyYgN+8npLsYlWyh8vlSuBP4FYLBZefuUVprRpQ9O778ZqmiL8gNUw6NS5M09PmsSW
LVvo2LEjbre7wsGTnx80SxxF09JiiYBpiKpGNcbwFHczJGR2qWgGEfw+3HQSjzKBvkNJ5vFh4HwC
ZFG7FAAA9OVK/l975x3fVLn/8ffJbNNdyq6AgIiAKCoiVlBEFAQuqAz9eQXxuuXiFbeieFUEEReI
igooKMPJUNmIKDJUBEHZWjrYtbvNPOf3xzdpkyYdLJXb583rvCDJGTkJeT7P851PsoE2OLkywnU+
B541gzOCpn2BJEONhbBkswNI6tzTlAuIATgNA2pg7gnGarWi6zo+w4D4eHjwQfTVq9GXuKo5Uq5c
VAT33w8mk1zaZrPRsmVLmjZtSk5ODjk5OZSWlmI2m3E6ncTGxnJ4715Kq5nZlyIZyUVAVFQUJSUl
FBQUhOzjQqps9kBEJPgbyEaS7g4CUUEi8Ntvv1GvXj1AqnxGwjAMfvrpJ+bOncvixYvZt38/PxFe
pjqAFzFfNUIyqasTfsWJQa0ETiGanH46sVYrMxCjQjTQ0DD4ZdUqep1zDt06dyYmJqYszb8yvF4v
n332GRaLCbEgH4iwlwGMQGMn53IuhRQylueIxcwoJCu3JsTFxmKxyFwjBrFfr0L8Gan+7RzE2PMT
y/mMj8PO0Za2PMV4BmJhaYXXPgeGRkOb82UArcgVwCJECNKDtpnACMQnYUIGy1Iqnw1Xh8fjQdc0
EYA33oCLL4YhQ8C6kco/LQ92+820bWtixAjIyoKkpHrExcXh9XrZtm0bS5cuZf/+/QwbNoytW7eS
kZHBoUOHWLZsGW3bt6efyURuJWd/DfHXrLPbcZnNlJRInm+k1Y0TEYLOiGkusF0AHEImHIHjQfwB
SUmyrqob1Jzd5/OxevVqbrnlFlq3bs3gwYNZt24d//jHP7isb1/uQ/xWFfECQxHz1YdIlnzNjG6K
40WJwCnCwoULuXXwYL50OtmGpP//AuwCMoBMXWcK4Kkwy6sMl8uF11uCuHE7ESoEIgAwDTteiinm
3wwnm30U4eMBxAlZ0TRVkd+AvKIivF4vUYj7eSWSzl+RZsAavLzBG3gilFc4m7O5gn9wjRkcQdtN
0fDsizL2NmgAUUHTWAdS/uFnxGzWEuiIOK3HIzb0NhUvVAkmk4moqKiyJimJiYm0atWKzp07lw2C
hsUiAhCYGTdqBP+5A/gn4ULgAfrh9a5iy5YSsrLA69X4v//7P7755hucTiclJSXMnj2bJk2aMG7c
OBo2bEizZs0YPXo0ycnJrN24kcuGDeMyqzVMCCYCjwFus5lcl4smTZpgMpmq9Gc4Ed/SG0HbAcDn
P8aQaEIANm3aVCYmMTExLFiwgD59+tCyZUuGDRtGdnY2bdq0ISoqim3btjFjxgx27NgBJhN3Io76
n4K2mxAnfjFwPhI4YACdO3eu4TekOFY0o1oDp+LvQGpyMrNyc1mP/DjXAJFiMmYgkTZH52MMWAWD
W9lYgBJMgAUbBgYePNgQW/+1SBOPR/3Xq8h7yEzSaTKVDRYXIBFFVWHHxEIWYatQ2cjA4DnLf6nT
7xuG/qt8Jmu1Qmkp3HEHXHihPF64EMwucQi/QvmMcgfiBH4OmXWCVFG6kIqRTOGYTCYsFguapqFp
GhaLhZSUFFq0aMGFF15I/fr1eXTiREqnTg0/+KVXYeEy/ycQ+LkdQMrcyTdlt9v56KOP6Nu3b6Xv
YdeuXUyYMIH58+eTm5tLdHQ0l156KfFRUSxZsIA4xO6u6zp5gNdmIzY2FofDQXZ2Ng6HI8gMeGxk
ZmaSmppKnz59yMnJYd26ddStW5fY2FiSk5PJz8/njz/+IDo6mmbNmtGoUSNKSkrYvXs3Xq+XvXv3
gtdLPDIZCExZDGRGehMiABuAK+128o/WUaI4apRP4BTB7fHQCqly+QmRBQDETLQImFPFuex2Ox6P
h8aNG3Po0KEgp225H8GMmwQCZhJx6DVr1oz09HSeRgTgK//fPiS0L8AC4BGHgx9//JEzzjiD+Ph4
SksqKzkWihHm7pTnJvAC2xLW8+bNOtHR5a8VFsI994gvtnVr6XRo1aUC64uELnVbIx23uiHCMATY
W4P31KRJEzp27EhaWhpdu3bF4XCQnp5ORkYGWVlZ7N+/nzVr1uB2VWL/H3kv2Oww/yvwaogXpPw+
LRZLtQIAcMYZZzBlyhSmTJmC0+lk1qxZvPLKK+zcuRPDMEhs2pQ7hw7ltNNOY+rUqWzevJn8/HwK
CwtJTEwkNzcXk8mEbhgQGwttgtZBu3dDXl61vpA77riDzMxMtm/fXrYqcDqdaJpGTExMmTCmpqbS
sWNHzj//fGbNmkV0dDSbNm0q81W5gDMRH0DFAOWNQG+bjRlzIxmOFCcatRI4RagbG8vVxcUsApYj
ER97EHPQz0jMtxmxtc9HZtwVXcMWiwVd12nUqBGff/4555xzDtOmTWP48OEhFSMD2AmUg5ZZWy/E
ubjb6WQrYtpJQkpdH0CGtVIgOSmJecuWsXnzZu6+/XZcPh8acB5id64MA3EWD2AQF3NJ2fPLrV/y
a/1V5Luc9O4NTfzdGw0D5syB9HSw26FzZ/B6weeGI5nQ+gDMdYfPdCRiXyOFePbixlvNuknTNC68
8EJSUlIAcQLXq1eP+vXrU69ePbxeL2vXruXjNWvQ33+/8hN9Mh8mv8uZrZrhdrv5/ffdgJuLL76Y
NWvWVPkeqmPr1q089dRTrFixguLiYpKSkujevTtFRUUsX74cp9OJKZAjkJAAr78OwfH9+flw111w
6FCVQqBpGna7HZ/PJ45wn49rr72Wrl270rFjR84991wcDgcgvqfbb7+dffv2kZ6eLuagIGIRYZ5K
+Ro0G/in3c7bc+fSr1+/4/pMFDVDicApQpLDQUKpJFp9gJgvrkFKOzuRRttZSJhgKrAeia4I/JxN
JhPx8fFMnz6d/v37h5x7wYIFfPPNNxiGga7rWK1W1q1bx5YtWygsLMTh9bIaceAG+BgpudwYEQa7
3c5vLhdPjR/PwcOHeX7MGOy6zipEsOxIvf9xyAy8IgaSzPQloGOnmGSKKAJNp1ETHxNec5KfD+++
W17eGsSZun8/vPwytGpV/rzbDU89CA23hwvBHuBcEiliARLwuoHqDGiappXZvQsKClixYgWLFy/m
l19+weVyUVxczO7MTDxPP13emLkiS5aQ9O67HMzIwGw2E2u1YtV17DYbnTp1wu5wMO6112jZsmWV
76U6SktLeeWVV3jnnXfIysrCbDaTkJDAwUOHMOLjwwUgQA2EQNM0brnlFsxmM3PnziU/P5/S0lKi
okKjukpKSrjxxhvJysrijz/+ICcnh/z8iimPMOL221n+ZXkHB7PZzDOvvqoE4E9EicApwsXnnkvJ
5s3oiA3+KSSyJThkshhJgmqGhPnN9D9nt9sZPXo0Dz/8cEh99qooLCykQYMGWEpKwgQgwDZkQN8C
nNe5M7GxseTl5bFt40bsPh9Lkdk/SBz6NESwKgqBAdwPzAKeBB4nGpcZjORS0jrALz/DwIFw7bWh
1x8/HlatgldeCRWAAAEhaLMD3gmy1IgI1KOIg8ha5ypqIgQA55xzDs2aNSMhIYGMjAyaN2/OsGHD
SEtL4+uvv+bqa6+l9IknwoVg8WKip0yhY/v2zJw5k6cfe4ytc+fyeFAo7xaTiTeTkli5bt1xC0Ew
3377LU8++SSr163DN2yYfJiV8fXX8sFWYr7TNI0XX3yRdu3a0bdvX1wuF7quhzicc3NzGTBgAHv3
7sXn86FpWlliWTDZ2dk0atTouO9PcXwoEThFWL58OSOvuoprdJ0XkY5JkWLmA0LQFjEHLa5Th+1Z
WWEztZrQv39/UubP550q9vkJibYpMpno3LkzuzZupE5pKS8AvSvs+wwwHRlqO1OeJ7APMWc9CTwI
pNiakHFRBsk74eNZcPAg3HcfNG8uZh+QMWrHDonEfPDByt/frl3w6n2wNcgfugO4oEwEAJxgaQHG
wdCDzWZRkgqcddZZDB48mGXLllFSUlLm+O7YsSNz586l0O2WgdbqTxQrKICFC+mWlsakSZPo3b07
jfLyWOpyhdnD3zKZePYkCAHAXSNG8KauQ4QOXmVUIwIAN9xwA6+88gqNGjXCMIyQPJB9+/bRr18/
srOzsVqt2O129u7dG5Yo9vrrr3PXXXcd9z0pjh/lGD5FcDgcOGJjSS0o4BoiCwBILP5rSPmAFcBC
n++YBACge/fubJk/v8p9AvM/XdfZ+t13jDYMxiCZwBV5ArH9Po04j0FWAXb/JklbZnRNhxQw/y4O
3wYN4LXXwF+qBpCxOWN3uS250vdXISKyELiBaLxcgSTCxYNlNNS3witzICam/AIPPwy//x4mBNu2
bWPs2LEhWdAgsfMaGmBgmTuXhx56CJ/Px/PTpwOwfv16xo4dS0phYUQBALhd1ynNzeXm667j2+Ab
/huxY8cO6tWrh2EYISvLnTt30r9/fw4cOIDNZiMpKYlOnTrx1ltvhRzfsWNHJQB/I1SewCnC6aef
zl5N43uIkFMbSnUD49FgtVXfUdgUFEeeQdXv7zHEJDQCCdXUkBWLB8lqNWElh5yw4+rUgcsvl61z
Z1j6GTTJo9JiZJEoRNpx/mrRccYsA2tTsNwI9efB5FchJQWio2VLSBBHw+mnQ4TPIFgAbDbRDtkM
HA64vFs3xjz7LOPGji0r0+B0Olm5ciXne72VlOwTLtd18vPyjuLOaobdasW0b1/VO2VnB4oeVcr+
/fvxeDwhIvDDDz/QvXt3MjMzMZvNDBo0iEWLFoUJgNVqZcOGDcd1H4oTixKBU4SGDRuyZPVq5kZF
hUX9nCxsNhu7zWaciA0/NWhrioShbgeat2wZMiMMDOxVEfy6BzFjFaNRwj2UYoAGbqdE+1Rk5UpI
2gvtfbCnmjErMxMydWgCnGY2s7VjR1xLvoTPP4T/Pgx8BJPHy6BfkehoEYIqhNBqhaZNxYLywgsw
/gV44AFYvXopw4YN47333uNsf+9gXdfZv3//UdXQOZE8cN99NNi0CXNloZdLlsCMGdUWMcrPz+fA
AUkuNPkL7F155ZUcOXKEpKQk5s2bx8SJE+kQwUGekxMu8Iq/FiUCpxDt27dn5COPkE548bBgspHV
wI9A9DGaggD++c9/4mzThrNNJvKQ0Mp1/m02cC+SdLVx1y569uwJSMG6eki55sp+7ssQAbkk7BUD
mA56GvwMzmR44ulwIfD5QPPBTCtsz4HnXogsBD/+KINzo6bQ8BIrZ6ZZsP/2M9pifzRKmzaSYhxJ
AAIEVgbIrtagpYfVCs2awauvyqnOOku2bt1g7FiYM+ddHnjgAX7++efKz/8nkpqayvrVq6m/ZAnm
2bPh8OHy7YsvRPAi5DqYMGHBgtn/x1XiYsigIWXRZP3796e4uJjevXuzfft20tLSePXVVzl4MNTH
smTJEuLiIuWLK/5KlGP4FCM/P59LL7iALunpTPR6w+qr/ITE898OvBkTw6eLF3PJJeHDbU3weDwM
uPpqSleuZKGuhxWd3ooM5IHAP5OmEWUYdEFqwy9B6t0HV4NfBtyI1IcZj5SmDnVBakACWPOwNLVg
NnvpUA+eeRL8JYiYMAEWLwPfzXJy+xy45Ey4dWj5WXbvhjHPwpOjRUSmvCTioetQXALG6c0pef55
+Ne/oBq/B4MGweHDdOgAW7eWh6jWrw/TpxOSvBbMhg0werSGx2MKcZ7WRwS6cYRjDGCkzcbOiy7i
i6+/rvp9HSPZ2dlc2a8f+7Kzycvzt6DRtIgrABMmkklmIhNJRMxaPnyMsY7hJ89PuHDhcDiYM2dO
WbJbYWEh8fGhXQquv/56Zs+efVLuR3F8KBE4BcnLy+PKtDQ6797NGLe7TAh+RSJybgBmH6cAACxe
vJhHBgxgfXFxpV0HfgC6EFp4LRa4D6k8+SmSwBYwqGxHKoiORwrJVRaUaSeaeGssefXzMLs8+PJB
MwE6uDVE6c717+yCqHn+CwbQQSuFu4fDW6/C/V5ZoWiIcD0IrGrSBOcff8CCBeEe5GAGDICcfC6/
XGflyvIlx3nnwYsvVn5YXh4MHgw+nzlEBMyIEGwgVAgM4D9mM/MSE5k2dy7du1fW8ubEkZCQEFZV
NEBAAF7ndepSN+Q1Dx4e4RF+4ReyDmeVJdIBtGjRgt9++63scSBbWfH3RJmDTkESExNZumYNP7Vt
S32rlTomE8lAV00jsWFDNrZvz2dLlhyXAICsBE4zm6tsO9MSsEdF0aVLl7LnioCXkBXAW5RX0P/F
YqEgJoYr4+JYGhdHqcNR6eDropQCTwFnZ53N0MN3cJP7Fv7PeTNutxQYC/EI28E5GJwjgraLICoG
XnrNjq/dubx4wQU8fMEFPNC6NQOiongX6JqVhWaxSOhRZXOhmTOlznNZHJNgPQqPdFjVTrOZIoeD
TogYBrbrgZk+H//IyeGGfv2OO4u4JlTsLRCMgRFRAACsWBnHOOKJ59lnny3zc0ybNi1EAIAy/4Hi
74kKET1FSUxMZPXGjX/12yhj9erVPPjgg0yYMAEQR++rSMayDuTZbGC34x42DJL9/Qt8PnhtEjZn
PobXCMkEBnDh4ld+xcAgnnh0f+39yrofVCS3yIT27+GU9OlT/qRh8PvEiVy6eDFfO51cWlrKjtWr
Mfl86PfeGypKM2fCrFl+O7kFr1eEwmaDM84IrVhaFcGL7UAVUrPbzRlI45fAFVsiqWu7gWnFxVxz
1VV8tmQJaWlpNbzjoyclJYWMjIzI7xuDFFIivgYiBHHEMWPGDGbNmsXVV1/Ne++9F7LPxo0bsdur
mkYo/mqUCCiqpDpboQGU+guINW3alEGDBvGhv99rCYDFgi0qCpPZjPOxx6TUZzBt2uC55y6iPflA
uBA4cfITP5U9dgC/GURumRaMG2jbDiNYAAA0DfeIEfwOdFu8mKa6zq68PMxLlqD//DM4HLIq8Hgk
tKjMTm7mmw0a1KmDUTeBPW4X2uZ97NhhcOaZET4XA2bMDO9x4Ha7sbjdXIuUU664DvIi3c4mAjOK
i+nfsye/7NlT1sDlRJNQlVO8htSvX586derwwQcfhDx/7733RowQUvy9UCKgqJQ2bdqwQdf5gvDs
X5BZ/l2IZcYN7N27V0oFB7DZsEdFoRlGZAEAaNAAY/IblNx6K7FRktZbUQiCKUEjy50Mi3LEsB6p
6sAe4FsNXr4j8kn8QrBzwQIa6zqn05wMbwbxOTkYR47g8bc1DO7OptnNGM1awMvj8djtePbuhR9+
4N773+T+e3107AgBy4phwKQ3LSxarON0hoctxRFZAEB+kB8jNaCmAPVMJg4fPnzSRKAqcxCAjo65
iswTHZ3t27djsVhCPq9A6Ojbb7/NkCFDKl0NHDhwgDcmT8Yb9KWnde3K1VdffZR3ojhWlGNYUSXr
16+n7xVXML2oKEQIfMCtUVHsPusssvPySE9PD++926UL1h9+wOt0YixfHrn1V4C7/4V5329QAr4q
REBczNPRGIph80qz4mAh2IPEryalwIcfVXlv5iuu4CqfifXEU0AB5ihzSL+AuLg48vLyKPZ4MJ1x
BvqECWC3Y3n7dexLFhKfbAGfF5wuCgqkhEViImRmwaYjp+H0mKXEaRBWpAx4dSWsE5AIq6K4OD5Z
u5a2bdtWc8SxMWzYMN59992Ir0URxUVcxChGRRSC+cznDd7ARXhYaVpaGk6nk9zcXLxeL/379+eR
Rx6hYcOGFBUV0b9HD77esEHqDiHO8p5Ix4U3oqN5YcoUbrzpphN5q4pKUCsBRZV06tSJhcuX0/eK
K+hGeXZwtq5jbtOGxV99RUxMDB999BFDhw7FYrHgdDrxeDxiX69pr16fhu8qJK40vNhkEG7gVgye
APczMNVLSP8ZN6JQturt0AawCg8u8sAMZqTaZnJyMm63m5ycHMxmM/h86KNGlQlA/Q2fM3mai4SE
8sFvxQoJs+/SBX78JQrP+5Ol4FHF20QiqcYGPdcE6RMRvDIw+5//rrIeBSeIuLg4NE0LF3DEFLeW
tTzLs2FCUJUAaJrGd999h91uJyYmhpiYGJYsWcJnn31Gq1atyM3K4pz0dIp0vSwyZTNSxu87wFJa
yp1DhvDIiBF8+OWXqrvYSUaJgKJaOnXqxDc//MDGIEe02WymT58+ZbXjBw4cyIABA7jhhhv45JNP
sNvtuPLzq3cqBDA0+NUMZ/hgo0mKt5VfrEIMeylSi/Tf4JsMpeUOAgf+wfTgQfTRoym9/nrJ4KrI
wYPohoETEzo+TIaJBg0aMHv2bKZOncqKFSvQNI1mzZqxdfdudLMZy3vviAC86AzLL+veXTRv0iQw
RVmhkqSoKCTbOljnnkPyO8Yj4XoliJadDyzzeIgJ1DM6CcTFxWE2m0NMOcG4cLGWtQxjGLH+Yhc6
Oumk4yqLmNL971wEISAoFouFoqIiSkpKMJlMeL1e8rKz6avrvEN5aGIuUhn3JuCBoGt/n5dH3+7d
WbhihRKCk4gSAUWNOPPMMzkzkgc0CE3TmDNnDs899xyjRo2CnBw0zURcnToULFkCvXpFPnD3bjh0
GLBDagnWpCQ8b71VFodpnjqVhCVLsDidHAF/jFApEoBqIeAljkd6CdsAvF7+WL2aJzdsoPTFF0O7
aB08CHffDVAWcaTrOvvS0+nRpQua32xls9kYOHAgW8eNk8erljL68XABCHD55fDtt/B1QQtJV87K
Cnk9CjF3LCG0vtL9wEX+579Bmqyfhgia2WymWbNmkS94AkhISKi2vLgLF5lkYrVa8fh8skzRENXT
NaweOwZJeDkMuDCbJS+iqKgIk8lEvXr1sFgs5B46RHNdZyahAtAD6Ip0ggteDaUC0aWl9OvRg/nL
likhOEmoPAHFCWX58uUsWrRIyiDn5OB2n4arqEhqKyxZEn7A7t3w0EPwn/9A3WTMOrTIy8PxzDOS
ihsXh+/eeym66ipi7HaSCB4oignkG8cjA+idwC3+7QHgE6eT6JEjYd06+OMP+P13THffjZaXF1Jr
woEMwoVeLwVuNwVuN+8WFTHx+eex22xyLNXnB1jsJvSmzWHUqJASDHakyX2wABhIT+hpiDloP5I8
5kL6N2ggg+5JJD4+HqvVWmUDek0Du90m9Z7qGzBAh+t0uNYHXX14LCXE4MZCXcBe1kMgNjYWXdc5
cOAAR7KySHG7aUbooDMd6X9RUQAC9AQmFBfziF+0FScetRJQnDB27tzJk08+KdVEMzL8CVixuCwO
KM6Fd96BjAxISpIDdF36Q44YAZddBu9PxXIARvp8jN6+nZI9e+DMMyWap1cvfl+yBGtMTLmFyeUC
r5doRADaR3hPvYBPXC6uefRRbDabDE4eDwW6TpF/HwcyG33Xv12KDD59gGlFRQyyWuHhhyCuhvVZ
v/wyLPnMjmQpBwvAA0i576v8z92MlNXIAs7yv5eTKwESHWS32ympon+A3W7HZ9Iwkl1ws0FI9uCZ
Bjg08hcdJsFblxI0PIhJqKioqGy304HuiM1/hv+5M5DigS2ILAABWgKek+wbqc0oEVAcFbm5ubzw
3HOUFpd3aWnXoQPXDhjArbfeisvlYvPmzUFlEnZDdDKU5EmNhYULpR9kgIcfhk6d5N9ug64F8C9g
fLBPYOdOePRRePxxPMFZ0Lt3w7//TWOnM6IABOiFWDD2u93EIG03z0Qymx1IW8v6/n29/sf3AI8g
jW5GeTz816mDT6ewsOrPp6DQ7wyvIs41IACrgK+QPs0BioBuSL+Fm4HtNewEd6wkJiZijbC8CXYW
x8bGcoQceUOR/O3nG+DVyF9xiCi3g0h3HoUI9RlIj2yAh5F7Pa0G7/OvqrxaG1AioKgxubm5XJmW
xlm7d9PB48GF1A6abbXy+GOPYbHbyc7OrnBUERT4ID5eakDfc0/kk3/zDZaDh5nu85sLikvgvkdh
6GCYOxdGjoSKZTBatoQHHsB49tmjuo9kIBHw2e1Mcrm4scLrlyNNewKV8OsCLVObsPNwBqNG+Zg8
GVJTw8874wMTmzbqmPSA36Kc4DXEJEQAlhMqACB1l77yv4d0IKVCIbYTTXJycpkpyGQyhbWKBIiJ
ieVI4h9gr8LLf7pR6XQ+Cgl5/RIIrrX3M5AGVJLNUYYBZFfwryhOHMonoKgRAQG4ZM8e3vN4uB2x
bxcBgz0erj1yhD7Z2YQPWQa4SqHEBfPmSaf4inzzDdYxY1jrdpcVVPMSA6UvwB0KVjoAABh4SURB
VNSZ4lCurA7SaadhHENZgv3AaxEEAMSstBQJ5XwPMdF0SevC4GuuxxVl5Z4RYT5fZsyAWe/rjHvu
JUqKixkzZgx16tQpc7r6kBLcIEX0/kW4AAQIFOBbBYybOPGo7+1oSEpKKhv4TSYTJpOpbAVQ037U
oYSbwXTk3pMREbga8eS0R2pMvYMIQiSKgf9AxNWF4sSgVgKKGjFs4EBa7drFcq+XJkiXLjPQGngU
aODfbzih5aUFQzrEYMCHH8KOHZji47EDhteLdc0aVrlcZU3pH8PCIeoAg8C3BhxV2OLj4tjv8/Ez
kX0CAIuR2Wiw0aMYccZWRnvELv8v//311zRmTJtBykMpfDbvU26+OROTGTRk8ExNbcTuXd+R6l8i
PPbYYzz66KPMmzeP+++/n/2//86rUGVHsYqYNI0LLrjgKI44eurUqVMmAsG+AbPZXFb47ljzSU3I
CuAbxOSTjwz2E5BooHHAP4F5iL9gFlAUdLwLWTU1Ana4XCxatIhelUWYKY4ZlTGsqBFtmzThSGYm
45AfbIBpSG+AlZQLQcU+A5GwIoPsbcAViJiACMCrpFLCeqAemB6BW3Lgxkhzdj9TppA0Zw6rCBeC
xUhXtAVIGGbguV5Un8LQBRG124GPly6lR48eZa+VlpaGlIeOiorCYql8TpUUHc3/OZ3MANohMfFV
xbvMBt5o357VJ7nPsMvlIjU1laKiIqxWK8XFxei6HlIGwmq14rF55IOIFB5rAF+aJOPLLcJhQqrI
rkNKiR9E7P+xyOqgBChA/s90QDKoVwAXUi7WR5AV2y/A58BHl17KglWrTvAnoFArAUW1/PLLL2Rk
Z/MmhJlPnkKcqS0QO/YnyCB3tf/flbnzPEi1zLHAJKyAAw86B6lTLgAgA0x1kSGtW1PXZuNKt5v/
Up5A/AeSN1BRAIbExECQY7s64uLjQwQAILqyTjKVEBUdTQOnk8bANiRK5i4qj4pZp2mcEZzbcJKw
+Vtn2u12dF2P6BPweDyYNTO+t32i2sFCYACLTLDJAE+5rMYgItAf+a4PAv8G/ht0qI6E8s5DROFl
5PTBp74bidT6D1Re7ltxXCgRUFTLkyNH8qSuR7SfAzyL/MhXIzNsD5CB2LzdSFpXpK61JUBJXBy4
O4IrUEjhLKTEmh9jAHx4JbRrF7kAXUYG0RMmMNrtJg4JP1yFmKqcyCzzXWCGyYRhsfCJ1cr8Zcvo
3aMHi4qLqcy4sAfYicxKbSegFPI/rrsO3nmHKGSWPwQZFCcRLgRPAp8mJvL9yy8f93WrI1AryWaz
UVJSgsViwWQyhUXj+Nw+zPiFoFPQm96vwc5QAXAgq7unEPPOdcBlyDc7G5nVf+rf10BWDRUFAP8l
XgdGAGOA05UInBSUCCiqxeN0UlmusAv5IZ+OOP22IYPvDOQ/l4GEAv5IZCHAZAJTImIIiMQF4JoG
T94AT/83VAgyMoi+5x5eLyoqs++nAd2io2lz9dX839ChrFy5Ek3TSE1NxWw2s7xbN9q3b8+Xy5fT
t3t3ZpSUhAnBHmRVMxIY5XBw+/DhVX08NaJ+gwbkIiuSiUhUVR9kgLshaL/PgdeAmdOn06BBg7Dz
nAw0TcPhcFBYWIjZbMZqtUYMyfS5faLqK4OejJAPcS5wK9Lr+mVkVWADPgO2IP8vMhDT0AYkY7qy
CCEN+bxsQDMlAicHQ6Gohr5duxrz5edetulgPASGBQw7GDb/v7uD0RyMeWBM9m8vg3G6fx8qblar
gSXegMVGhUv4N7cBPQ0Nu4HNZpCUVLZpNpsxGYxS/3YAjPMcDmPk8OGGruvV3tfatWuNFIfDmAjG
HP/2PhhNwBgHxlkOh/HfUaNOyGe4fft2o2FiovEuGIPA6AnGPjCuA6Ozf+sARqKmGdOmTTsh16wp
9erVMzp06GDY7XYjISHBiIqKCv+earBZwEgB40owevi/8/PBKPT/fxkORicw8oK+4HVgXBj5iw/Z
zGC8P2PGn/q51BaUCCiqpW/Xrsa8CgLwoH/Qygl63gvGjWAkg9EAjJvAuMu/DQEjtpLBIxaMBDQj
gYZGAi0MB30NKC4TAIg8KJnBMPn/NoNh1TTjwREjaiQAAdatW2f84/LLjXo2m1HPbDbqmc1Gis1m
JNhsxtNPPHFCP8etW7caDRMTjff8QnCB//O6Hox+YNSx2YzPPvvshF6zJtSrV8+44oorDIvFYjRo
0MAwmUzHJACpfmEzwHgAjC5+ATDAyAYjsYIAHK0IuFyuP/2zqQ0oc5CiWi667DIeWb2aroid/1Ek
0Wk5oa0ezcAoxKTxFOFL/C7AvUjMvAtZ4puRUMGLMJBYEBjH73xJQ0r8lfetVif16kFBgaQLxMTI
yOB2w9Kl5X7jnbt307x586O6t06dOjF/xQpKSko4fPhw2fM2m42GDRse1bmqo23btiz79lt6dOlC
cVERXsPgF8NAB+4cPpzHb7yRjh07ntBr1pSAozsqKqrMOWzU0PxiR9z465FeCSCO7+cpD4n1+f+d
gKjGp8i3nYGY394FhhLZUR5IyaiqvpHi2FEhoopqMQyDOJOJM5HEqTpADuG9fosR598TSFmGDyu8
PgSJEw8IQRySLFSxdYgPabr+JeAyS6khtxtuuw0qdov85hsYMwbcbi28ofvfFJfLRWlpadljm81W
VpL7r6BBgwb06NGDOXPm0KJFC3bs2IFF0zAHDQ2BYtHBaIiQ25DQ3MaIH+VcxDcz3v83QCZwMTLo
jwY+QkKNDSSQYDXih5lMqBBkIZOHpFat2Lhjxwm7Z0U5aiWgqBZN0zAhg3MgoSsgAEVIqCfAAWSG
fxrSJ/dByssEFCCO0PH+x22Q8MBIvaPMwBykdMO3uoXiI1aio+GDd2DZAoPR45xlveq7dIHHH4dn
xxhs376d1q1bRzjj3wu73f63ar5uNkszHU3TyMnJwQY0NQxGBO2zFul58DlScmMqIuDjKC+JsR8J
51xUyXW8SOTTPGTQrxv0Wj6SQHar/5wakifQB8k5cR/lCk9Rc5QIKGqE12Jhv9fL2ZS3RjyEzN4M
JJQyMA+/HokE6VbhHOcBg5EVwRZkxlgZZv/+buMi7uZuiTMthUVFCxl596e89LorRAjiEzQuvfJK
tvzww0nrx/u/isViYc/OnUR5PJQeOUIzxJxTJ2ife5AonoFIpvVrwBokESyYlkiYcGMkUexTZPIQ
MAF+CHxLqACAmIlWIyuHM5CBSUOK+O0BXNX0QlYcO6p2kKJGtG7enAQkHwBkmX45MuP/BdiEmHoy
keX7JMITxXoCc5HyADUx3JjQaE1rGgb9ucV3O5cduY6Rd9sDJf4FzcSh4mLOT0vj0KFDx3yftRFX
SQlbVq3ifqTr2Swkrj8laGuNlNBohXRC+4pwAQC4Bont34uYfUD6BbRAVoj3Ei4AARKAxxEROYJM
Mo4AH9lsJ72GUm1GiYCiRnyxahX5Vit3IT/qDkgS0FMV9rMhmcI+JLu4osOpJ6GrhqrQKsmnvdl3
G+2OdOOTD4P++0bZoU0bsvLzmTRpUg3Orjh48CB33nYb5OTwrceDA7HbX4s059ketD2K9Fxojsz2
qzLO9EU6hj2PNIv5D1KqO7OG7+sIUkLiPiTfpM1ZZ1G3bmXSoThelAgoakTDhg2ZMHUqDyICkExo
CYBgbIjjL2AKiEQr4AUqLyvxOzALK81oFvH103zN8HpEJA4dgqJcD9x5J3TowMeff16DO6rdpKen
c2G7dkx75x3WGQaHkEzrzxATzD2ErgRuRvw5rxMu7JHQ/OcAyRIeiWQR14TdyGpjMZBssdD23KoM
h4rjRYmAosb07t0bzGaWUr0zyUbldXE8SC0yDbExVxSC34E0zFzLbaSVxZdE5tAhuOs+O+4bh0Hj
xtCzJ3nVdX6p5aSnp9OtUyfuzsnBgdR964uY9IYhNY0i8U+gHzVdxQkrEAFYhmST/0TVIrIRMT2t
QPoxm1q25OUpU2pwRcWxokRAUWMSExPpdP75nF1FtczqWIsM+gOQ4nEaYmb4D2IvvgsprXABV9Gf
6yo9j4HB4cNw93ATef2Gog+6odJ9FeXk5eXRrVMnRh45wm2GgQup2fMlEt5blZlHR0xDu/1/V8Yc
yju1bUTMgu38j1cjvoJIQvAi0r+hk//1bE3jnvvu+1tFUv0voqKDFDXGZDKxcOVKLunYEee2bfgI
7ZgVTB7hP/S1iE/AgZiSOgNnA4eBL5AQ096AFRM/8ytFFBEboQL/AQ7wIXMp/cHAfWO4ADhiYo79
Jv/HSU9PJ87p5B5dpxfin1kEnI/Y+qtiOrKKex6J8V9BeQnwAO8j/oSvgp4LrAqsSC2h+5Bw0cFB
+3yBlCXvg4Sg/htIT0lh0KBBR3V/iqNHiYDiqIiJiWHFt9/StkkTbiwu5gPChSAPie2+EnESg+QJ
PI5En+Qg2cRjkSzRwOyzDvAq0AidzRzkHh5kMi+ECMEBDjDcfBdFcTqeqR9RFicaYN06mjdtegLv
+H8PzTC4FTG7XY8IAMhgXZWp5w8kaugOpElPd+Q7Dc4TeAMZVDKJXBIwGRGPIcjAH6AOIhwvIHkE
vwG3Dh9OogoNPekoEVAcNcnJyfyamcnlnTpx465dIUKQh5h3WiDlBD4NOq4/0rYxyv/Y7N//iP/x
NCT09D7gJkrZRza38m/OoBkaPsBgMz/jjHLjeWN6uABMm0bMypXM3LLlhN/z/xKHS0v5DXHcbgt6
visSBXQ1UhW2IgWUO/qHIhnfS4JeNwGv+M9xE5ITkIdkkhtI4uBGJP9jcYTze5DSE0eA1Kgole/x
J6HKRiiOmZKSEq5MS2PDpk1l3aDcQCqSMxDUFYAJwJtIktG9SCnlZoBhMhGjadgBn89HI8R5WF5U
IQ6JTbGCtg7idkK7VuDxhNaQ+PlnolauZOfmzZx22mkn5X7/F9iyZQsXtG9PNvAx4gx+M+j1ychs
/CtChWAfcA4yuL9UxfnXIaWxb/Y/9iCloLsgET89kdVeRSOPBzEPrQAujo4m5rLLmD1/PlarFcXJ
RYmA4rjQdZ21a9fS69JLKfT5sCOO3Z2UN1LXkR/5R0iEyUDEFHC4Th027tzJ2rVr8Xq9DBo0KEId
ew20BGjQAKIdUHAILF5ZBQTq7xQVQVER6776ik6dOv0Jd33qous6DquVI7rOXCR8cwmhJr3JSKOg
s5FeACAz+E6IQ3gV4XWjQGb7I5A+AsErwDXI4J/mf30Y8AyhGePjEOFfDfTq1UsJwJ+IEgHFCSE/
P5+eXbpg2rmTX10uRiJJRwGikDDEXsAaqxXrOeew6KuviI0tt/dbLJaQvr0hREeD2SzlQ71e8Plk
AwKNTV5//XXuuquyAEdFgFi7nQNuNybkO2mMOH2DheBFJFHrKf/jOshs/iFktl6xgqyBhIKu9r+W
RChrkO8+UEXUiZiP6iOrjKuQ8NN7oqLYX1CgBOBPRImA4oRRWFjIJ598QlZWFhPHjcPh9WLoOh6P
hwJAs1iw2mz83/XXM/HttzGZyiOUDcMIeXwstGvXji3KH1AtsXY7O9xuGiMtPgNC8CTlkTwfIvb9
rYSWeTAoF4Jbg55fC/xKZAEIcAky47/E/9iJrBDi/ecaFhXFoq+/5sJIbUQVJw0lAoqTQkFBAQcO
HCh7bLPZaNasWaX75+fnH3MkiI3ycNRATPmtw4bx0uuvqxr0EXjioYeYN3EiX7lcpCBCcBPiHzAQ
x2xjxPyzAfgaEYI8RBhKERHYCbRFcgDeQ+pKVSYAECoCTmSluA4JBBgPjJ00ieEnoJWn4uhQIqD4
S8nNzWVw795s376d3NxcDGRQD4QqGkhUSoz/OYPyCJUk/78TkMqUAcNSMdA3Koq2/fszfdYsJQQV
MAyD24YOZfXMmXyHlIUA+WzvRkxD+cj38A9khj8OSfJqT6gtfxqyethJ9eUkAhVoLYiPqDciJnUA
Z/36/LRtG0lJVcmI4mSgREDxl5Gbm8uVaWmk7dlDZ7ebh5BZacDW3BqxE49A+g+8j8xY6yCRKwEX
8gLgbWTACpCPzDjbXXMNsz75RAlBBQzDYFD//sxfsAAHYp/XkTLOjSlP5noICRn9GIn6eYPQciDZ
SNG5w4gp6OJKrrcPKQMxGxEDEJFJBVIaNeLbH3+kQYMGJ+4GFTVGiYDiLyE3N5fuF11E5507GYTk
ELyFDEIgs8rHkFn+v5AByYo4mAPR43WQWWsWMqt8h3AhaAx8vGgRPXv2PLk3dIpyZqNGPLB/f1mB
jgREDG6gvKDcBKQM9CQi14PKRgT3DyT7uKIQ7EN6S9yM5BCArNYuB9IdDjbt3n3CW3kqao5KFlP8
Jbz88ss09QvAdchMs3uFfT5DxOENZHXQGwkxDfA5Mrh8hYSc9kaSkALdzxKQEgQ3DRzIuk2baNGi
xUm6m1OX8zp0IHb//rBe0bOBRuDv8ixlPipbSzVGyj34kJXbq5QLtQcpI3ELoQJwlc1GavfuLJsz
h/j4+BN4R4qjRYmA4k8nJyeHtydPZhhSvGw64QIAMuufh5Q1OBtxSgYPRB0Rk0JACLoDOygXAZAB
raOu8/333ysRiEBsUhLfWa1c7/GEfLZWRERrigsR5RJk5RAQFQMx+TxFeelxA/jXwIG8NWPGcUeE
KY4fJQKKP505c+aQXFCAhkSJnFPFvlGIb+AaIs9EH0fMEE9Ucnwx4FEWz0p57uWX6b52LU9kZvJM
BSGAyvtBROIPpCxI1wrPFyJ1pPaaTAy87TZemjwZs7my0oOKPxslAoo/HZ/PR9xRDMxmKjdFgMz8
vyS8L8Hj/uPy9JpUwK+d1K1blxXr1tH9ootwZmZytcdT9locUugtFvEPVNbapRgpA3IxsrL7gvJQ
USfQT9PISU7m9ttvZ/SYMcpJ/zdDrcUUfwn1TCbe5ehmmlXhQxKbAsXpnkAcmZcDhYahZp5VEBCC
vd2782yHDoxs2pTBmkYq0gHOg2QQR2rtUoz4A1ohvYkbI2GkLRFnclu7nYuGDWPPoUM89dxzSgD+
hqiVgOIvIdVkYgDSTOYZZICJNCP5EYklf6ia821AkpWmIL6DXUjZYxPgq1+fXr16nZg3/j9K3bp1
+WjRorLH78+YwcN33smbpaW8hfR6eAgJBe0QdNwzSD0hAwnVtWsaydHRFPp8vDdjBgNVP4C/PUoE
FH86F198Mc+azVyP9BR4GIlLn0qoEPyIOHtjqLzjVQEyS01AQkVH+J9fgPQuWKNp3P/YYyE1ihTV
888hQ7BYLDw/diyGrhNfUoLd7Wa2xcKnZjOZGRnouo7XZMKwWGjSsCFvffABjRs3BqTvREpKSjVX
UfwdUHkCir+EL774gsF9+vAlYje+AyktfSYyq9SBuf59LUihsTWEFi0rAC71778KaOA/12LEln0z
8GHduqz56aeywUmhUISiREDxl2AYBj26dmX9t99yDjLQ70Hq1tyL2JbPQ8oPb0FaUTZBCo4F+Bqp
b/Mq0sfWjcSkD/E//jAhgTWbNlVZs0ihqO0oEVD8ZXi9Xvr36sX3K1bQzTAYihQUm4w0PY9BIoN+
RUoNf4CUI77If3wKktl6HVLFMhY4hPQwdppMfP3995x3XnDWgEKhqIgSAcVfitfr5brevVm5dCmj
EP/AZqQ38XjwN5WUUM8U/9+tKa99fwDxB7iQiJRE4IuUFJavWUOrVq3+1HtRKE5FlAgo/nIMw2D9
+vXc0K8fww4f5nL/f0kvUqXyN0QIzEh28W9Bx3qQtoXbAYemYa1fn6+//57U1NQ/9R4UilMVJQKK
vw2ZmZnceeON/LZrFwcPHCAGMf28gjQpHwbsJ7Rj2Txgl9VKm7PPZvxrr9GuXTvi4uLCT65QKCKi
REDxt8TpdHLTtdey9KuvwDBwuVxlvQRMgKZp9OzZk67dunHvffdhsahoZ4XiWFAioDgl0HU9pP+w
pmlq4FcoTgBKBBQKhaIWo2oHKRQKRS1GiYBCoVDUYpQIKBQKRS1GiYBCoVDUYpQIKBQKRS1GiYBC
oVDUYpQIKBQKRS1GiYBCoVDUYpQIKBQKRS1GiYBCoVDUYpQIKBQKRS1GiYBCoVDUYpQIKBQKRS1G
iYBCoVDUYpQIKBQKRS1GiYBCoVDUYpQIKBQKRS1GiYBCoVDUYpQIKBQKRS1GiYBCoVDUYpQIKBQK
RS1GiYBCoVDUYpQIKBQKRS1GiYBCoVDUYpQIKBQKRS1GiYBCoVDUYpQIKBQKRS1GiYBCoVDUYpQI
KBQKRS1GiYBCoVDUYpQIKBQKRS1GiYBCoVDUYpQIKBQKRS1GiYBCoVDUYpQIKBQKRS1GiYBCoVDU
YpQIKBQKRS1GiYBCoVDUYpQIKBQKRS1GiYBCoVDUYpQIKBQKRS1GiYBCoVDUYv4frJrExo5q8ZUA
AAAASUVORK5CYII=
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
<p>One of the features it lacks though is pruning of graphs, <em>metaknowledge</em> has these capabilities. To remove edges outside of some weight range, use <a href="{{ site.baseurl }}/documentation/metaknowledgeFull.html#dropEdges"><code>drop_edges()</code></a>. The functions all mutate the given graph, so if you wish to keep the original keep a copy. For example if you wish to remove the self loops, edges with weight less than 2 and weight higher than 10 from <code>coCiteJournals</code>.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[43]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">minWeight</span> <span class="o">=</span> <span class="mi">3</span>
<span class="n">maxWeight</span> <span class="o">=</span> <span class="mi">10</span>
<span class="n">proccessedCoCiteJournals</span> <span class="o">=</span> <span class="n">coCiteJournals</span><span class="o">.</span><span class="n">copy</span><span class="p">()</span>
<span class="n">mk</span><span class="o">.</span><span class="n">dropEdges</span><span class="p">(</span><span class="n">proccessedCoCiteJournals</span><span class="p">,</span> <span class="n">minWeight</span><span class="p">,</span> <span class="n">maxWeight</span><span class="p">,</span> <span class="n">dropSelfLoops</span> <span class="o">=</span> <span class="kc">True</span><span class="p">)</span>
<span class="n">mk</span><span class="o">.</span><span class="n">graphStats</span><span class="p">(</span><span class="n">proccessedCoCiteJournals</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt output_prompt">Out[43]:</div>


<div class="output_text output_subarea output_execute_result">
<pre>&#39;The graph has 89 nodes, 459 edges, 1 isolates, 0 self loops, a density of 0.117211 and a transitivity of 0.20841&#39;</pre>
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
<p>Then to remove all the isolates, i.e. nodes with degree less than 1, use <a href="{{ site.baseurl }}/documentation/metaknowledgeFull.html#dropNodesByDegree"><code>drop_nodesByDegree()</code></a></p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[44]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">mk</span><span class="o">.</span><span class="n">dropNodesByDegree</span><span class="p">(</span><span class="n">proccessedCoCiteJournals</span><span class="p">,</span> <span class="mi">1</span><span class="p">)</span>
<span class="n">mk</span><span class="o">.</span><span class="n">graphStats</span><span class="p">(</span><span class="n">proccessedCoCiteJournals</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt output_prompt">Out[44]:</div>


<div class="output_text output_subarea output_execute_result">
<pre>&#39;The graph has 88 nodes, 459 edges, 0 isolates, 0 self loops, a density of 0.119906 and a transitivity of 0.20841&#39;</pre>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">nx</span><span class="o">.</span><span class="n">draw_spring</span><span class="p">(</span><span class="n">proccessedCoCiteJournals</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt"></div>


<div class="output_png output_subarea ">
<img src="data:image/png;base64,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
hRBCCCf6/++oTZE1rtn4AAAAAElFTkSuQmCC
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
<p>Now you have a graph the last step is to write it to disk. <em>networkx</em> has a few ways of doing this, but they tend to be slow. <em>metaknowledge</em> can write an edge list and node attribute file that contain all the information of the graph. The function to do this is called <a href="{{ site.baseurl }}/documentation/metaknowledgeFull.html#writeGraph"><code>writeGraph()</code></a>. You give it the start of the file name and it makes two labeled files containing the graph.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[46]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">mk</span><span class="o">.</span><span class="n">writeGraph</span><span class="p">(</span><span class="n">proccessedCoCiteJournals</span><span class="p">,</span> <span class="s2">&quot;FinalJournalCoCites&quot;</span><span class="p">)</span>
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
<p>These files are simple CSVs an can be read easily by most systems. If you want to read them back into Python the <a href="{{ site.baseurl }}/documentation/metaknowledgeFull.html#readGraph"><code>readGraph()</code></a> function will do that.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[47]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span> <span class="n">FinalJournalCoCites</span> <span class="o">=</span> <span class="n">mk</span><span class="o">.</span><span class="n">readGraph</span><span class="p">(</span><span class="s2">&quot;FinalJournalCoCites_edgeList.csv&quot;</span><span class="p">,</span> <span class="s2">&quot;FinalJournalCoCites_nodeAttributes.csv&quot;</span><span class="p">)</span>
<span class="n">mk</span><span class="o">.</span><span class="n">graphStats</span><span class="p">(</span><span class="n">FinalJournalCoCites</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt output_prompt">Out[47]:</div>


<div class="output_text output_subarea output_execute_result">
<pre>&#39;The graph has 88 nodes, 459 edges, 0 isolates, 0 self loops, a density of 0.119906 and a transitivity of 0.20841&#39;</pre>
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
