# Configuration file for ipython-nbconvert.

c = get_config()

#------------------------------------------------------------------------------
# NbConvertApp configuration
#------------------------------------------------------------------------------

# This application is used to convert notebook files (*.ipynb) to various other
# formats.
# 
# WARNING: THE COMMANDLINE INTERFACE MAY CHANGE IN FUTURE RELEASES.

# NbConvertApp will inherit config from: BaseIPythonApplication, Application

# The export format to be used.
# c.NbConvertApp.export_format = 'html'

# Whether to apply a suffix prior to the extension (only relevant when
# converting to notebook format). The suffix is determined by the exporter, and
# is usually '.nbconvert'.
# c.NbConvertApp.use_output_suffix = True

# overwrite base name use for output files. can only be used when converting one
# notebook at a time.
# c.NbConvertApp.output_base = ''

# Whether to overwrite existing config files when copying
# c.NbConvertApp.overwrite = False

# List of notebooks to convert. Wildcards are supported. Filenames passed
# positionally will be added to the list.
# c.NbConvertApp.notebooks = []

# Create a massive crash report when IPython encounters what may be an internal
# error.  The default is to append a short message to the usual traceback
# c.NbConvertApp.verbose_crash = False

# Writer class used to write the  results of the conversion
# c.NbConvertApp.writer_class = 'FilesWriter'

# PostProcessor class used to write the  results of the conversion
# c.NbConvertApp.postprocessor_class = ''

# Whether to install the default config files into the profile dir. If a new
# profile is being created, and IPython contains config files for that profile,
# then they will be staged into the new directory.  Otherwise, default config
# files will be automatically generated.
# c.NbConvertApp.copy_config_files = False

# The Logging format template
# c.NbConvertApp.log_format = '[%(name)s]%(highlevel)s %(message)s'

# The date format used by logging formatters for %(asctime)s
# c.NbConvertApp.log_datefmt = '%Y-%m-%d %H:%M:%S'

# Whether to create profile dir if it doesn't exist
# c.NbConvertApp.auto_create = False

# Set the log level by value or name.
# c.NbConvertApp.log_level = 30

# Path to an extra config file to load.
# 
# If specified, load this config file in addition to any other IPython config.
# c.NbConvertApp.extra_config_file = ''

# The name of the IPython directory. This directory is used for logging
# configuration (through profiles), history storage, etc. The default is usually
# $HOME/.ipython. This option can also be specified through the environment
# variable IPYTHONDIR.
# c.NbConvertApp.ipython_dir = ''

# The IPython profile to use.
# c.NbConvertApp.profile = 'default'

#------------------------------------------------------------------------------
# NbConvertBase configuration
#------------------------------------------------------------------------------

# Global configurable class for shared config
# 
# Useful for display data priority that might be use by many transformers

# DEPRECATED default highlight language, please use language_info metadata
# instead
# c.NbConvertBase.default_language = 'ipython'

# An ordered list of preferred output type, the first encountered will usually
# be used when converting discarding the others.
# c.NbConvertBase.display_data_priority = ['text/html', 'application/pdf', 'text/latex', 'image/svg+xml', 'image/png', 'image/jpeg', 'text/plain']

#------------------------------------------------------------------------------
# ProfileDir configuration
#------------------------------------------------------------------------------

# An object to manage the profile directory and its resources.
# 
# The profile directory is used by all IPython applications, to manage
# configuration, logging and security.
# 
# This object knows how to find, create and manage these directories. This
# should be used by any code that wants to handle profiles.

# Set the profile location directly. This overrides the logic used by the
# `profile` option.
# c.ProfileDir.location = ''

#------------------------------------------------------------------------------
# Exporter configuration
#------------------------------------------------------------------------------

# Class containing methods that sequentially run a list of preprocessors on a
# NotebookNode object and then return the modified NotebookNode object and
# accompanying resources dict.

# Extension of the file that should be written to disk
# c.Exporter.file_extension = '.txt'

# List of preprocessors, by name or namespace, to enable.
# c.Exporter.preprocessors = []

# List of preprocessors available by default, by name, namespace,  instance, or
# type.
# c.Exporter.default_preprocessors = ['IPython.nbconvert.preprocessors.coalesce_streams', 'IPython.nbconvert.preprocessors.SVG2PDFPreprocessor', 'IPython.nbconvert.preprocessors.ExtractOutputPreprocessor', 'IPython.nbconvert.preprocessors.CSSHTMLHeaderPreprocessor', 'IPython.nbconvert.preprocessors.RevealHelpPreprocessor', 'IPython.nbconvert.preprocessors.LatexPreprocessor', 'IPython.nbconvert.preprocessors.ClearOutputPreprocessor', 'IPython.nbconvert.preprocessors.ExecutePreprocessor', 'IPython.nbconvert.preprocessors.HighlightMagicsPreprocessor']

#------------------------------------------------------------------------------
# HTMLExporter configuration
#------------------------------------------------------------------------------

# Exports a basic HTML document.  This exporter assists with the export of HTML.
# Inherit from it if you are writing your own HTML template and need custom
# preprocessors/filters.  If you don't need custom preprocessors/ filters, just
# change the 'template_file' config option.

# HTMLExporter will inherit config from: TemplateExporter, Exporter

# formats of raw cells to be included in this Exporter's output.
# c.HTMLExporter.raw_mimetypes = []

# List of preprocessors available by default, by name, namespace,  instance, or
# type.
# c.HTMLExporter.default_preprocessors = ['IPython.nbconvert.preprocessors.coalesce_streams', 'IPython.nbconvert.preprocessors.SVG2PDFPreprocessor', 'IPython.nbconvert.preprocessors.ExtractOutputPreprocessor', 'IPython.nbconvert.preprocessors.CSSHTMLHeaderPreprocessor', 'IPython.nbconvert.preprocessors.RevealHelpPreprocessor', 'IPython.nbconvert.preprocessors.LatexPreprocessor', 'IPython.nbconvert.preprocessors.ClearOutputPreprocessor', 'IPython.nbconvert.preprocessors.ExecutePreprocessor', 'IPython.nbconvert.preprocessors.HighlightMagicsPreprocessor']

# 
# c.HTMLExporter.jinja_comment_block_start = ''

# 
# c.HTMLExporter.jinja_variable_block_start = ''

# 
# c.HTMLExporter.template_path = ['.']

# Dictionary of filters, by name and namespace, to add to the Jinja environment.
# c.HTMLExporter.filters = {}

# Name of the template file to use
# c.HTMLExporter.template_file = 'default'

# 
# c.HTMLExporter.jinja_logic_block_start = ''

# 
# c.HTMLExporter.jinja_logic_block_end = ''

# Extension of the file that should be written to disk
# c.HTMLExporter.file_extension = '.txt'

# 
# c.HTMLExporter.jinja_comment_block_end = ''

# 
# c.HTMLExporter.template_extension = '.tpl'

# List of preprocessors, by name or namespace, to enable.
# c.HTMLExporter.preprocessors = []

# 
# c.HTMLExporter.jinja_variable_block_end = ''

#------------------------------------------------------------------------------
# LatexExporter configuration
#------------------------------------------------------------------------------

# Exports to a Latex template.  Inherit from this class if your template is
# LaTeX based and you need custom tranformers/filters.  Inherit from it if  you
# are writing your own HTML template and need custom tranformers/filters.   If
# you don't need custom tranformers/filters, just change the  'template_file'
# config option.  Place your template in the special "/latex"  subfolder of the
# "../templates" folder.

# LatexExporter will inherit config from: TemplateExporter, Exporter

# formats of raw cells to be included in this Exporter's output.
# c.LatexExporter.raw_mimetypes = []

# List of preprocessors available by default, by name, namespace,  instance, or
# type.
# c.LatexExporter.default_preprocessors = ['IPython.nbconvert.preprocessors.coalesce_streams', 'IPython.nbconvert.preprocessors.SVG2PDFPreprocessor', 'IPython.nbconvert.preprocessors.ExtractOutputPreprocessor', 'IPython.nbconvert.preprocessors.CSSHTMLHeaderPreprocessor', 'IPython.nbconvert.preprocessors.RevealHelpPreprocessor', 'IPython.nbconvert.preprocessors.LatexPreprocessor', 'IPython.nbconvert.preprocessors.ClearOutputPreprocessor', 'IPython.nbconvert.preprocessors.ExecutePreprocessor', 'IPython.nbconvert.preprocessors.HighlightMagicsPreprocessor']

# 
# c.LatexExporter.jinja_comment_block_start = '((='

# 
# c.LatexExporter.jinja_variable_block_start = '((('

# 
# c.LatexExporter.template_path = ['.']

# Dictionary of filters, by name and namespace, to add to the Jinja environment.
# c.LatexExporter.filters = {}

# Name of the template file to use
# c.LatexExporter.template_file = 'default'

# 
# c.LatexExporter.jinja_logic_block_start = '((*'

# 
# c.LatexExporter.jinja_logic_block_end = '*))'

# Extension of the file that should be written to disk
# c.LatexExporter.file_extension = '.txt'

# 
# c.LatexExporter.jinja_comment_block_end = '=))'

# 
# c.LatexExporter.template_extension = '.tplx'

# List of preprocessors, by name or namespace, to enable.
# c.LatexExporter.preprocessors = []

# 
# c.LatexExporter.jinja_variable_block_end = ')))'

#------------------------------------------------------------------------------
# MarkdownExporter configuration
#------------------------------------------------------------------------------

# Exports to a markdown document (.md)

# MarkdownExporter will inherit config from: TemplateExporter, Exporter

# formats of raw cells to be included in this Exporter's output.
# c.MarkdownExporter.raw_mimetypes = []

# List of preprocessors available by default, by name, namespace,  instance, or
# type.
# c.MarkdownExporter.default_preprocessors = ['IPython.nbconvert.preprocessors.coalesce_streams', 'IPython.nbconvert.preprocessors.SVG2PDFPreprocessor', 'IPython.nbconvert.preprocessors.ExtractOutputPreprocessor', 'IPython.nbconvert.preprocessors.CSSHTMLHeaderPreprocessor', 'IPython.nbconvert.preprocessors.RevealHelpPreprocessor', 'IPython.nbconvert.preprocessors.LatexPreprocessor', 'IPython.nbconvert.preprocessors.ClearOutputPreprocessor', 'IPython.nbconvert.preprocessors.ExecutePreprocessor', 'IPython.nbconvert.preprocessors.HighlightMagicsPreprocessor']

# 
# c.MarkdownExporter.jinja_comment_block_start = ''

# 
# c.MarkdownExporter.jinja_variable_block_start = ''

# 
# c.MarkdownExporter.template_path = ['.']

# Dictionary of filters, by name and namespace, to add to the Jinja environment.
# c.MarkdownExporter.filters = {}

# Name of the template file to use
# c.MarkdownExporter.template_file = 'default'

# 
# c.MarkdownExporter.jinja_logic_block_start = ''

# 
# c.MarkdownExporter.jinja_logic_block_end = ''

# Extension of the file that should be written to disk
# c.MarkdownExporter.file_extension = '.txt'

# 
# c.MarkdownExporter.jinja_comment_block_end = ''

# 
# c.MarkdownExporter.template_extension = '.tpl'

# List of preprocessors, by name or namespace, to enable.
# c.MarkdownExporter.preprocessors = []

# 
# c.MarkdownExporter.jinja_variable_block_end = ''

#------------------------------------------------------------------------------
# NotebookExporter configuration
#------------------------------------------------------------------------------

# Exports to an IPython notebook.

# NotebookExporter will inherit config from: Exporter

# Extension of the file that should be written to disk
# c.NotebookExporter.file_extension = '.txt'

# The nbformat version to write. Use this to downgrade notebooks.
# c.NotebookExporter.nbformat_version = 4

# List of preprocessors, by name or namespace, to enable.
# c.NotebookExporter.preprocessors = []

# List of preprocessors available by default, by name, namespace,  instance, or
# type.
# c.NotebookExporter.default_preprocessors = ['IPython.nbconvert.preprocessors.coalesce_streams', 'IPython.nbconvert.preprocessors.SVG2PDFPreprocessor', 'IPython.nbconvert.preprocessors.ExtractOutputPreprocessor', 'IPython.nbconvert.preprocessors.CSSHTMLHeaderPreprocessor', 'IPython.nbconvert.preprocessors.RevealHelpPreprocessor', 'IPython.nbconvert.preprocessors.LatexPreprocessor', 'IPython.nbconvert.preprocessors.ClearOutputPreprocessor', 'IPython.nbconvert.preprocessors.ExecutePreprocessor', 'IPython.nbconvert.preprocessors.HighlightMagicsPreprocessor']

#------------------------------------------------------------------------------
# PDFExporter configuration
#------------------------------------------------------------------------------

# Writer designed to write to PDF files

# PDFExporter will inherit config from: LatexExporter, TemplateExporter,
# Exporter

# Shell command used to run bibtex.
# c.PDFExporter.bib_command = ['bibtex', '{filename}']

# formats of raw cells to be included in this Exporter's output.
# c.PDFExporter.raw_mimetypes = []

# 
# c.PDFExporter.jinja_comment_block_start = '((='

# List of preprocessors, by name or namespace, to enable.
# c.PDFExporter.preprocessors = []

# Shell command used to compile latex.
# c.PDFExporter.latex_command = ['pdflatex', '{filename}']

# 
# c.PDFExporter.jinja_variable_block_start = '((('

# 
# c.PDFExporter.template_path = ['.']

# Dictionary of filters, by name and namespace, to add to the Jinja environment.
# c.PDFExporter.filters = {}

# Name of the template file to use
# c.PDFExporter.template_file = 'default'

# 
# c.PDFExporter.jinja_logic_block_start = '((*'

# 
# c.PDFExporter.jinja_logic_block_end = '*))'

# Extension of the file that should be written to disk
# c.PDFExporter.file_extension = '.txt'

# List of preprocessors available by default, by name, namespace,  instance, or
# type.
# c.PDFExporter.default_preprocessors = ['IPython.nbconvert.preprocessors.coalesce_streams', 'IPython.nbconvert.preprocessors.SVG2PDFPreprocessor', 'IPython.nbconvert.preprocessors.ExtractOutputPreprocessor', 'IPython.nbconvert.preprocessors.CSSHTMLHeaderPreprocessor', 'IPython.nbconvert.preprocessors.RevealHelpPreprocessor', 'IPython.nbconvert.preprocessors.LatexPreprocessor', 'IPython.nbconvert.preprocessors.ClearOutputPreprocessor', 'IPython.nbconvert.preprocessors.ExecutePreprocessor', 'IPython.nbconvert.preprocessors.HighlightMagicsPreprocessor']

# 
# c.PDFExporter.template_extension = '.tplx'

# 
# c.PDFExporter.jinja_variable_block_end = ')))'

# How many times latex will be called.
# c.PDFExporter.latex_count = 3

# Whether to display the output of latex commands.
# c.PDFExporter.verbose = False

# 
# c.PDFExporter.jinja_comment_block_end = '=))'

# File extensions of temp files to remove after running.
# c.PDFExporter.temp_file_exts = ['.aux', '.bbl', '.blg', '.idx', '.log', '.out']

#------------------------------------------------------------------------------
# PythonExporter configuration
#------------------------------------------------------------------------------

# Exports a Python code file.

# PythonExporter will inherit config from: TemplateExporter, Exporter

# formats of raw cells to be included in this Exporter's output.
# c.PythonExporter.raw_mimetypes = []

# List of preprocessors available by default, by name, namespace,  instance, or
# type.
# c.PythonExporter.default_preprocessors = ['IPython.nbconvert.preprocessors.coalesce_streams', 'IPython.nbconvert.preprocessors.SVG2PDFPreprocessor', 'IPython.nbconvert.preprocessors.ExtractOutputPreprocessor', 'IPython.nbconvert.preprocessors.CSSHTMLHeaderPreprocessor', 'IPython.nbconvert.preprocessors.RevealHelpPreprocessor', 'IPython.nbconvert.preprocessors.LatexPreprocessor', 'IPython.nbconvert.preprocessors.ClearOutputPreprocessor', 'IPython.nbconvert.preprocessors.ExecutePreprocessor', 'IPython.nbconvert.preprocessors.HighlightMagicsPreprocessor']

# 
# c.PythonExporter.jinja_comment_block_start = ''

# 
# c.PythonExporter.jinja_variable_block_start = ''

# 
# c.PythonExporter.template_path = ['.']

# Dictionary of filters, by name and namespace, to add to the Jinja environment.
# c.PythonExporter.filters = {}

# Name of the template file to use
# c.PythonExporter.template_file = 'default'

# 
# c.PythonExporter.jinja_logic_block_start = ''

# 
# c.PythonExporter.jinja_logic_block_end = ''

# Extension of the file that should be written to disk
# c.PythonExporter.file_extension = '.txt'

# 
# c.PythonExporter.jinja_comment_block_end = ''

# 
# c.PythonExporter.template_extension = '.tpl'

# List of preprocessors, by name or namespace, to enable.
# c.PythonExporter.preprocessors = []

# 
# c.PythonExporter.jinja_variable_block_end = ''

#------------------------------------------------------------------------------
# RSTExporter configuration
#------------------------------------------------------------------------------

# Exports restructured text documents.

# RSTExporter will inherit config from: TemplateExporter, Exporter

# formats of raw cells to be included in this Exporter's output.
# c.RSTExporter.raw_mimetypes = []

# List of preprocessors available by default, by name, namespace,  instance, or
# type.
# c.RSTExporter.default_preprocessors = ['IPython.nbconvert.preprocessors.coalesce_streams', 'IPython.nbconvert.preprocessors.SVG2PDFPreprocessor', 'IPython.nbconvert.preprocessors.ExtractOutputPreprocessor', 'IPython.nbconvert.preprocessors.CSSHTMLHeaderPreprocessor', 'IPython.nbconvert.preprocessors.RevealHelpPreprocessor', 'IPython.nbconvert.preprocessors.LatexPreprocessor', 'IPython.nbconvert.preprocessors.ClearOutputPreprocessor', 'IPython.nbconvert.preprocessors.ExecutePreprocessor', 'IPython.nbconvert.preprocessors.HighlightMagicsPreprocessor']

# 
# c.RSTExporter.jinja_comment_block_start = ''

# 
# c.RSTExporter.jinja_variable_block_start = ''

# 
# c.RSTExporter.template_path = ['.']

# Dictionary of filters, by name and namespace, to add to the Jinja environment.
# c.RSTExporter.filters = {}

# Name of the template file to use
# c.RSTExporter.template_file = 'default'

# 
# c.RSTExporter.jinja_logic_block_start = ''

# 
# c.RSTExporter.jinja_logic_block_end = ''

# Extension of the file that should be written to disk
# c.RSTExporter.file_extension = '.txt'

# 
# c.RSTExporter.jinja_comment_block_end = ''

# 
# c.RSTExporter.template_extension = '.tpl'

# List of preprocessors, by name or namespace, to enable.
# c.RSTExporter.preprocessors = []

# 
# c.RSTExporter.jinja_variable_block_end = ''

#------------------------------------------------------------------------------
# SlidesExporter configuration
#------------------------------------------------------------------------------

# Exports HTML slides with reveal.js

# SlidesExporter will inherit config from: HTMLExporter, TemplateExporter,
# Exporter

# formats of raw cells to be included in this Exporter's output.
# c.SlidesExporter.raw_mimetypes = []

# List of preprocessors available by default, by name, namespace,  instance, or
# type.
# c.SlidesExporter.default_preprocessors = ['IPython.nbconvert.preprocessors.coalesce_streams', 'IPython.nbconvert.preprocessors.SVG2PDFPreprocessor', 'IPython.nbconvert.preprocessors.ExtractOutputPreprocessor', 'IPython.nbconvert.preprocessors.CSSHTMLHeaderPreprocessor', 'IPython.nbconvert.preprocessors.RevealHelpPreprocessor', 'IPython.nbconvert.preprocessors.LatexPreprocessor', 'IPython.nbconvert.preprocessors.ClearOutputPreprocessor', 'IPython.nbconvert.preprocessors.ExecutePreprocessor', 'IPython.nbconvert.preprocessors.HighlightMagicsPreprocessor']

# 
# c.SlidesExporter.jinja_comment_block_start = ''

# 
# c.SlidesExporter.jinja_variable_block_start = ''

# 
# c.SlidesExporter.template_path = ['.']

# Dictionary of filters, by name and namespace, to add to the Jinja environment.
# c.SlidesExporter.filters = {}

# Name of the template file to use
# c.SlidesExporter.template_file = 'default'

# 
# c.SlidesExporter.jinja_logic_block_start = ''

# 
# c.SlidesExporter.jinja_logic_block_end = ''

# Extension of the file that should be written to disk
# c.SlidesExporter.file_extension = '.txt'

# 
# c.SlidesExporter.jinja_comment_block_end = ''

# 
# c.SlidesExporter.template_extension = '.tpl'

# List of preprocessors, by name or namespace, to enable.
# c.SlidesExporter.preprocessors = []

# 
# c.SlidesExporter.jinja_variable_block_end = ''

#------------------------------------------------------------------------------
# TemplateExporter configuration
#------------------------------------------------------------------------------

# Exports notebooks into other file formats.  Uses Jinja 2 templating engine to
# output new formats.  Inherit from this class if you are creating a new
# template type along with new filters/preprocessors.  If the filters/
# preprocessors provided by default suffice, there is no need to inherit from
# this class.  Instead, override the template_file and file_extension traits via
# a config file.
# 
# - markdown2html - markdown2rst - citation2latex - comment_lines - add_anchor -
# get_lines - indent - posix_path - strip_dollars - wrap_text - path2url -
# highlight2html - ansi2latex - html2text - strip_ansi - add_prompts -
# ascii_only - ipython2python - filter_data_type - highlight2latex -
# strip_files_prefix - escape_latex - ansi2html - markdown2latex -
# prevent_list_blocks

# TemplateExporter will inherit config from: Exporter

# formats of raw cells to be included in this Exporter's output.
# c.TemplateExporter.raw_mimetypes = []

# List of preprocessors available by default, by name, namespace,  instance, or
# type.
# c.TemplateExporter.default_preprocessors = ['IPython.nbconvert.preprocessors.coalesce_streams', 'IPython.nbconvert.preprocessors.SVG2PDFPreprocessor', 'IPython.nbconvert.preprocessors.ExtractOutputPreprocessor', 'IPython.nbconvert.preprocessors.CSSHTMLHeaderPreprocessor', 'IPython.nbconvert.preprocessors.RevealHelpPreprocessor', 'IPython.nbconvert.preprocessors.LatexPreprocessor', 'IPython.nbconvert.preprocessors.ClearOutputPreprocessor', 'IPython.nbconvert.preprocessors.ExecutePreprocessor', 'IPython.nbconvert.preprocessors.HighlightMagicsPreprocessor']

# 
# c.TemplateExporter.jinja_comment_block_start = ''

# 
# c.TemplateExporter.jinja_variable_block_start = ''

# 
# c.TemplateExporter.template_path = ['.']

# Dictionary of filters, by name and namespace, to add to the Jinja environment.
# c.TemplateExporter.filters = {}

# Name of the template file to use
# c.TemplateExporter.template_file = 'default'

# 
# c.TemplateExporter.jinja_logic_block_start = ''

# 
# c.TemplateExporter.jinja_logic_block_end = ''

# Extension of the file that should be written to disk
# c.TemplateExporter.file_extension = '.txt'

# 
# c.TemplateExporter.jinja_comment_block_end = ''

# 
# c.TemplateExporter.template_extension = '.tpl'

# List of preprocessors, by name or namespace, to enable.
# c.TemplateExporter.preprocessors = []

# 
# c.TemplateExporter.jinja_variable_block_end = ''

#------------------------------------------------------------------------------
# CSSHTMLHeaderPreprocessor configuration
#------------------------------------------------------------------------------

# Preprocessor used to pre-process notebook for HTML output.  Adds IPython
# notebook front-end CSS and Pygments CSS to HTML output.

# CSSHTMLHeaderPreprocessor will inherit config from: Preprocessor,
# NbConvertBase

# DEPRECATED default highlight language, please use language_info metadata
# instead
# c.CSSHTMLHeaderPreprocessor.default_language = 'ipython'

# 
# c.CSSHTMLHeaderPreprocessor.enabled = False

# An ordered list of preferred output type, the first encountered will usually
# be used when converting discarding the others.
# c.CSSHTMLHeaderPreprocessor.display_data_priority = ['text/html', 'application/pdf', 'text/latex', 'image/svg+xml', 'image/png', 'image/jpeg', 'text/plain']

# CSS highlight class identifier
# c.CSSHTMLHeaderPreprocessor.highlight_class = '.highlight'

#------------------------------------------------------------------------------
# ClearOutputPreprocessor configuration
#------------------------------------------------------------------------------

# Removes the output from all code cells in a notebook.

# ClearOutputPreprocessor will inherit config from: Preprocessor, NbConvertBase

# DEPRECATED default highlight language, please use language_info metadata
# instead
# c.ClearOutputPreprocessor.default_language = 'ipython'

# 
# c.ClearOutputPreprocessor.enabled = False

# An ordered list of preferred output type, the first encountered will usually
# be used when converting discarding the others.
# c.ClearOutputPreprocessor.display_data_priority = ['text/html', 'application/pdf', 'text/latex', 'image/svg+xml', 'image/png', 'image/jpeg', 'text/plain']

#------------------------------------------------------------------------------
# ConvertFiguresPreprocessor configuration
#------------------------------------------------------------------------------

# Converts all of the outputs in a notebook from one format to another.

# ConvertFiguresPreprocessor will inherit config from: Preprocessor,
# NbConvertBase

# DEPRECATED default highlight language, please use language_info metadata
# instead
# c.ConvertFiguresPreprocessor.default_language = 'ipython'

# 
# c.ConvertFiguresPreprocessor.enabled = False

# An ordered list of preferred output type, the first encountered will usually
# be used when converting discarding the others.
# c.ConvertFiguresPreprocessor.display_data_priority = ['text/html', 'application/pdf', 'text/latex', 'image/svg+xml', 'image/png', 'image/jpeg', 'text/plain']

# Format the converter writes
# c.ConvertFiguresPreprocessor.to_format = ''

# Format the converter accepts
# c.ConvertFiguresPreprocessor.from_format = ''

#------------------------------------------------------------------------------
# ExecutePreprocessor configuration
#------------------------------------------------------------------------------

# Executes all the cells in a notebook

# ExecutePreprocessor will inherit config from: Preprocessor, NbConvertBase

# DEPRECATED default highlight language, please use language_info metadata
# instead
# c.ExecutePreprocessor.default_language = 'ipython'

# 
# c.ExecutePreprocessor.enabled = False

# An ordered list of preferred output type, the first encountered will usually
# be used when converting discarding the others.
# c.ExecutePreprocessor.display_data_priority = ['text/html', 'application/pdf', 'text/latex', 'image/svg+xml', 'image/png', 'image/jpeg', 'text/plain']

# The time to wait (in seconds) for output from executions.
# c.ExecutePreprocessor.timeout = 30

# If execution of a cell times out, interrupt the kernel and  continue executing
# other cells rather than throwing an error and  stopping.
# c.ExecutePreprocessor.interrupt_on_timeout = False

#------------------------------------------------------------------------------
# ExtractOutputPreprocessor configuration
#------------------------------------------------------------------------------

# Extracts all of the outputs from the notebook file.  The extracted  outputs
# are returned in the 'resources' dictionary.

# ExtractOutputPreprocessor will inherit config from: Preprocessor,
# NbConvertBase

# DEPRECATED default highlight language, please use language_info metadata
# instead
# c.ExtractOutputPreprocessor.default_language = 'ipython'

# 
# c.ExtractOutputPreprocessor.enabled = False

# An ordered list of preferred output type, the first encountered will usually
# be used when converting discarding the others.
# c.ExtractOutputPreprocessor.display_data_priority = ['text/html', 'application/pdf', 'text/latex', 'image/svg+xml', 'image/png', 'image/jpeg', 'text/plain']

# 
# c.ExtractOutputPreprocessor.output_filename_template = '{unique_key}_{cell_index}_{index}{extension}'

# 
# c.ExtractOutputPreprocessor.extract_output_types = {'image/svg+xml', 'application/pdf', 'image/png', 'image/jpeg'}

#------------------------------------------------------------------------------
# HighlightMagicsPreprocessor configuration
#------------------------------------------------------------------------------

# Detects and tags code cells that use a different languages than Python.

# HighlightMagicsPreprocessor will inherit config from: Preprocessor,
# NbConvertBase

# DEPRECATED default highlight language, please use language_info metadata
# instead
# c.HighlightMagicsPreprocessor.default_language = 'ipython'

# 
# c.HighlightMagicsPreprocessor.enabled = False

# An ordered list of preferred output type, the first encountered will usually
# be used when converting discarding the others.
# c.HighlightMagicsPreprocessor.display_data_priority = ['text/html', 'application/pdf', 'text/latex', 'image/svg+xml', 'image/png', 'image/jpeg', 'text/plain']

# Syntax highlighting for magic's extension languages. Each item associates a
# language magic extension such as %%R, with a pygments lexer such as r.
# c.HighlightMagicsPreprocessor.languages = {}

#------------------------------------------------------------------------------
# LatexPreprocessor configuration
#------------------------------------------------------------------------------

# Preprocessor for latex destined documents.
# 
# Mainly populates the `latex` key in the resources dict, adding definitions for
# pygments highlight styles.

# LatexPreprocessor will inherit config from: Preprocessor, NbConvertBase

# DEPRECATED default highlight language, please use language_info metadata
# instead
# c.LatexPreprocessor.default_language = 'ipython'

# 
# c.LatexPreprocessor.enabled = False

# An ordered list of preferred output type, the first encountered will usually
# be used when converting discarding the others.
# c.LatexPreprocessor.display_data_priority = ['text/html', 'application/pdf', 'text/latex', 'image/svg+xml', 'image/png', 'image/jpeg', 'text/plain']

#------------------------------------------------------------------------------
# Preprocessor configuration
#------------------------------------------------------------------------------

# A configurable preprocessor
# 
# Inherit from this class if you wish to have configurability for your
# preprocessor.
# 
# Any configurable traitlets this class exposed will be configurable in profiles
# using c.SubClassName.attribute = value
# 
# you can overwrite :meth:`preprocess_cell` to apply a transformation
# independently on each cell or :meth:`preprocess` if you prefer your own logic.
# See corresponding docstring for informations.
# 
# Disabled by default and can be enabled via the config by
#     'c.YourPreprocessorName.enabled = True'

# Preprocessor will inherit config from: NbConvertBase

# DEPRECATED default highlight language, please use language_info metadata
# instead
# c.Preprocessor.default_language = 'ipython'

# 
# c.Preprocessor.enabled = False

# An ordered list of preferred output type, the first encountered will usually
# be used when converting discarding the others.
# c.Preprocessor.display_data_priority = ['text/html', 'application/pdf', 'text/latex', 'image/svg+xml', 'image/png', 'image/jpeg', 'text/plain']

#------------------------------------------------------------------------------
# RevealHelpPreprocessor configuration
#------------------------------------------------------------------------------

# RevealHelpPreprocessor will inherit config from: Preprocessor, NbConvertBase

# DEPRECATED default highlight language, please use language_info metadata
# instead
# c.RevealHelpPreprocessor.default_language = 'ipython'

# 
# c.RevealHelpPreprocessor.enabled = False

# An ordered list of preferred output type, the first encountered will usually
# be used when converting discarding the others.
# c.RevealHelpPreprocessor.display_data_priority = ['text/html', 'application/pdf', 'text/latex', 'image/svg+xml', 'image/png', 'image/jpeg', 'text/plain']

# The URL prefix for reveal.js. This can be a a relative URL for a local copy of
# reveal.js, or point to a CDN.
# 
# For speaker notes to work, a local reveal.js prefix must be used.
# c.RevealHelpPreprocessor.url_prefix = 'reveal.js'

#------------------------------------------------------------------------------
# SVG2PDFPreprocessor configuration
#------------------------------------------------------------------------------

# Converts all of the outputs in a notebook from SVG to PDF.

# SVG2PDFPreprocessor will inherit config from: ConvertFiguresPreprocessor,
# Preprocessor, NbConvertBase

# DEPRECATED default highlight language, please use language_info metadata
# instead
# c.SVG2PDFPreprocessor.default_language = 'ipython'

# 
# c.SVG2PDFPreprocessor.enabled = False

# An ordered list of preferred output type, the first encountered will usually
# be used when converting discarding the others.
# c.SVG2PDFPreprocessor.display_data_priority = ['text/html', 'application/pdf', 'text/latex', 'image/svg+xml', 'image/png', 'image/jpeg', 'text/plain']

# Format the converter accepts
# c.SVG2PDFPreprocessor.from_format = ''

# The path to Inkscape, if necessary
# c.SVG2PDFPreprocessor.inkscape = ''

# Format the converter writes
# c.SVG2PDFPreprocessor.to_format = ''

# The command to use for converting SVG to PDF
# 
# This string is a template, which will be formatted with the keys to_filename
# and from_filename.
# 
# The conversion call must read the SVG from {from_flename}, and write a PDF to
# {to_filename}.
# c.SVG2PDFPreprocessor.command = ''

#------------------------------------------------------------------------------
# FilesWriter configuration
#------------------------------------------------------------------------------

# Consumes nbconvert output and produces files.

# FilesWriter will inherit config from: WriterBase, NbConvertBase

# Directory to write output to.  Leave blank to output to the current directory
# c.FilesWriter.build_directory = ''

# DEPRECATED default highlight language, please use language_info metadata
# instead
# c.FilesWriter.default_language = 'ipython'

# An ordered list of preferred output type, the first encountered will usually
# be used when converting discarding the others.
# c.FilesWriter.display_data_priority = ['text/html', 'application/pdf', 'text/latex', 'image/svg+xml', 'image/png', 'image/jpeg', 'text/plain']

# List of the files that the notebook references.  Files will be  included with
# written output.
# c.FilesWriter.files = []

# When copying files that the notebook depends on, copy them in relation to this
# path, such that the destination filename will be os.path.relpath(filename,
# relpath). If FilesWriter is operating on a notebook that already exists
# elsewhere on disk, then the default will be the directory containing that
# notebook.
# c.FilesWriter.relpath = ''

#------------------------------------------------------------------------------
# StdoutWriter configuration
#------------------------------------------------------------------------------

# Consumes output from nbconvert export...() methods and writes to the  stdout
# stream.

# StdoutWriter will inherit config from: WriterBase, NbConvertBase

# DEPRECATED default highlight language, please use language_info metadata
# instead
# c.StdoutWriter.default_language = 'ipython'

# An ordered list of preferred output type, the first encountered will usually
# be used when converting discarding the others.
# c.StdoutWriter.display_data_priority = ['text/html', 'application/pdf', 'text/latex', 'image/svg+xml', 'image/png', 'image/jpeg', 'text/plain']

# List of the files that the notebook references.  Files will be  included with
# written output.
# c.StdoutWriter.files = []

#------------------------------------------------------------------------------
# WriterBase configuration
#------------------------------------------------------------------------------

# Consumes output from nbconvert export...() methods and writes to a useful
# location.

# WriterBase will inherit config from: NbConvertBase

# DEPRECATED default highlight language, please use language_info metadata
# instead
# c.WriterBase.default_language = 'ipython'

# An ordered list of preferred output type, the first encountered will usually
# be used when converting discarding the others.
# c.WriterBase.display_data_priority = ['text/html', 'application/pdf', 'text/latex', 'image/svg+xml', 'image/png', 'image/jpeg', 'text/plain']

# List of the files that the notebook references.  Files will be  included with
# written output.
# c.WriterBase.files = []

#------------------------------------------------------------------------------
# PostProcessorBase configuration
#------------------------------------------------------------------------------

# PostProcessorBase will inherit config from: NbConvertBase

# DEPRECATED default highlight language, please use language_info metadata
# instead
# c.PostProcessorBase.default_language = 'ipython'

# An ordered list of preferred output type, the first encountered will usually
# be used when converting discarding the others.
# c.PostProcessorBase.display_data_priority = ['text/html', 'application/pdf', 'text/latex', 'image/svg+xml', 'image/png', 'image/jpeg', 'text/plain']

#------------------------------------------------------------------------------
# ServePostProcessor configuration
#------------------------------------------------------------------------------

# Post processor designed to serve files
# 
# Proxies reveal.js requests to a CDN if no local reveal.js is present

# ServePostProcessor will inherit config from: PostProcessorBase, NbConvertBase

# DEPRECATED default highlight language, please use language_info metadata
# instead
# c.ServePostProcessor.default_language = 'ipython'

# URL prefix for reveal.js
# c.ServePostProcessor.reveal_prefix = 'reveal.js'

# An ordered list of preferred output type, the first encountered will usually
# be used when converting discarding the others.
# c.ServePostProcessor.display_data_priority = ['text/html', 'application/pdf', 'text/latex', 'image/svg+xml', 'image/png', 'image/jpeg', 'text/plain']

# port for the server to listen on.
# c.ServePostProcessor.port = 8000

# The IP address to listen on.
# c.ServePostProcessor.ip = '127.0.0.1'

# URL for reveal.js CDN.
# c.ServePostProcessor.reveal_cdn = 'https://cdn.jsdelivr.net/reveal.js/2.6.2'

# Should the browser be opened automatically?
# c.ServePostProcessor.open_in_browser = True
