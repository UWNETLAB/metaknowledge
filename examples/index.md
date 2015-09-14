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
  <a href="{{ site.baseurl }}/examples/#The-RecordCollections-object">The RecordCollections object</a>
  </article></li>
</ul>

<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="Getting-Started">Getting Started<a class="anchor-link" href="#Getting-Started">&#182;</a></h1><p>{% comment %}</p>
<h1 id="Notes-for-those-who-downloaded-the-notebook">Notes for those who downloaded the notebook<a class="anchor-link" href="#Notes-for-those-who-downloaded-the-notebook">&#182;</a></h1><p>The notebook should just work as long as you put the sample file (savedrecs.txt) in the same directory as this file.</p>
<p>The one issue you will have is that the urls will not work. To make them work you will need to replace <code>{{ site.baseurl }}</code> with <code>http://networkslab.org/metaknowledge</code></p>
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
<p>You will often need the networkx package as well:</p>

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
<p>I am importing these next couple things so the graphs will look nice:</p>

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
<h1 id="Reading-Files"><a href="{{ site.baseurl }}/docs/RecordCollection#RecordCollection">Reading Files</a><a class="anchor-link" href="#Reading-Files">&#182;</a></h1><p>The files from the Web of Science (WOS) can be loaded into <a href="{{ site.baseurl }}/docs/RecordCollection#RecordCollection">RecordCollections</a> by creating a RecordCollection object with the path to the files given to the initializer as a string.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[4]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span class="n">RC</span> <span class="o">=</span> <span class="n">mk</span><span class="o">.</span><span class="n">RecordCollection</span><span class="p">(</span><span class="s">&quot;savedrecs.txt&quot;</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="nb">repr</span><span class="p">(</span><span class="n">RC</span><span class="p">))</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt"></div>
<div class="output_subarea output_stream output_stdout output_text">
<pre>savedrecs
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
<p>You can also read a whole directory</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[5]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span class="n">RC</span> <span class="o">=</span> <span class="n">mk</span><span class="o">.</span><span class="n">RecordCollection</span><span class="p">(</span><span class="s">&quot;.&quot;</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="nb">repr</span><span class="p">(</span><span class="n">RC</span><span class="p">))</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt"></div>
<div class="output_subarea output_stream output_stdout output_text">
<pre>files-from-.
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
<p>metaknowledge can detect if a file is a valid WOS file or not and will read the entire directory and load only those that have the right header. You can also tell it to only read a certain type of file, by using the extension argument.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[6]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span class="n">RC</span> <span class="o">=</span> <span class="n">mk</span><span class="o">.</span><span class="n">RecordCollection</span><span class="p">(</span><span class="s">&quot;.&quot;</span><span class="p">,</span> <span class="n">extension</span> <span class="o">=</span> <span class="s">&quot;txt&quot;</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="nb">repr</span><span class="p">(</span><span class="n">RC</span><span class="p">))</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt"></div>
<div class="output_subarea output_stream output_stdout output_text">
<pre>txt-files-from-.
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
<p>Now you have a RecordCollection object composed of all the WOS records in the selected file(s).</p>
<h1 id="The-RecordCollections-object"><a href="{{ site.baseurl }}/docs/RecordCollection#RecordCollection">The RecordCollections object</a><a class="anchor-link" href="#The-RecordCollections-object">&#182;</a></h1>
</div>
</div>
</div>
{% include docsFooter.md %}
