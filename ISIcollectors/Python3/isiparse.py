"""
ISI flat file format parser.

Empirically, the ISI flat file format is *identical* to the plain text
EndNote format (.ciw), judging from what happens when you export from
the Thomson-Reuters Web of Science "To EndNote Desktop" vs "To Other
Reference Software". The only difference might be the file extension.

Run test(s) by getting a .ciw file either
manually or with isi_scrape and running
```
python -m isiparse data.ciw
```
"""

# TODO:
# [ ] rework strpisimonth to be strpisidate, returning a tuple instead of an integer;
#     I *thought* the PD field was only ever month and maybe day, but sometimes it duplicates the year (PY) field too
#     Once this works, write an assertion "not ('PY' in fields and 'PD' in fields and fields['PD'].year is not None) or (fields['PY'] == fields['PD'].year)
# [ ] Rename this whole thing to ciwparse? EndNoteParse (though this might get us sued :P)?

def is_WOS_number(w):
    """
    check that the string w is a WOS number
    You find these in the 'UT' field in exported .isi files.
    It is also called the "Accession Number"
    
    The format of this is "WOS:ddddddddddddddd": the 'd's are usually digits, but sometimes they are capital letters; sometimes they encode dates in them, and sometimes they seem totally arbitrary.
    """
    try:
        header, number = w[:4], w[4:]
        assert header == "WOS:"
        assert len(number) == 15
    except: #<-- ugh, lazy
        return False
    
    return True


class EmptyModule(): pass

try:
    import builtins
except ImportError:
    # hack around python2/3 (in)compatibility
    builtins = EmptyModule()
    import codecs
    builtins.open = codecs.open

import sys

from datetime import date
import time
from util import chomp

import logging

class ISIFormatError(Exception):
  pass


#class NumberedISIFormatError(ISIFormatError):
#	def __init__(self, line, *args):
#		self._line #^ this is meant to DRY up the line[%d] shit
#		super()    # but i don't want to think about it right now
	

def strpisimonth(d, fmt):
    """
    parse an ISI format "date" (PD field). This sometimes doesn't exist, sometimes includes a month, and sometimes includes a day, and sometimes includes a year.
  
    Known formats:
    Month ("%b")
    Month Day ("%b %d")
    Month-Month ("%b-%b") --- this gets coerced to the first %b, dropping the month range
    Season ("%s") --- this gets coerced to use the first month of the given season
    Month Day Year ("%b %d %Y")
    Month Year ("%b %Y")
    
    
    returns a tuple (year, month, day). This is like a datetime object, except that any of the three may be None to indicate missing data.
    """
    try:
        # handle the extension formats by a mixture of edits to the data and to fmt
        # then fall back on the standard strptime (whether or not we went through an extension format or not)
        if fmt == "%b-%b":
            # handle a month range e.g. "2006 APR-MAY"
            # which strptime can't handle
            l = d.find("-")
            if not (len(d) == 3 + 1 + 3): #four chars for the year, 3 for a month, 3 for another month
                raise ValueError("time data '%s' has wrong length for format %%b-%%b" % (d,))
            if not (d[3] == "-"): #four chars for the year, 3 for a month, 3 for another month
                raise ValueError("time data '%s' missing hyphen for format %%b-%%b" % (d,))
            end_month = time.strptime(d[l+1:], "%b") #this is a no-op, but it ensures that the format looks like we think it does
            d, fmt = d[:-4], "%b"
        elif fmt == "%s":
            # handle a season e.g. "FAL"
            # remap season to a month
            # this is a kludge, but at least it gives us *something*
            # each season gets three months out of twelve
            seasons = {'SPR': "MAR", 'SUM': "JUN", 'FAL': 'SEP', 'WIN': "DEC"}
            if d in seasons:
                d, fmt = seasons[d], "%b"
            else:
                raise ValueError("unknown ISI season '%s'" % (d,))
        
        return time.strptime(d, fmt).tm_mon
    except ValueError:
        # coerce any error to strptime()'s default message, to hide the real source
        raise ValueError("time data '%s' does not match format '%s'" % (d,fmt))

def parse_month(m):
    """
    """
    # try all the formats, starting with the most restrictive
    # strpisimonth requires an exact match so order shouldn't matter
    for fmt in ["%b %d", "%b", "%b-%b", "%s", "%b %d %Y", "%b %Y"]:
        try:
            return strpisimonth(m, fmt) 
        except ValueError:
            # silence the ValueErrors from a failed strpisimonth()
            # however if everything ValueError's out, the else clause will fire
            #print("error parsing '%s' with format '%s'" % (d, fmt))
            #traceback.print_exc() #DEBUG; warning: enabling this will be verrrry noisy
            continue
    else:
        raise ValueError("ISI time data '%s': format unrecognized" % (d,))
    
    assert False, "NOTREACHED"

def parse_year(year):
    # parse out the year
    if not isinstance(year, str):
        raise TypeError
    
    if len(year) != 4:
        raise ISIFormatError("Invalid ISI Year '%s'" % (year,))
    try:
        _year = int(year)
        if not (1900 <= int(_year) <= 3000):
            raise ValueError("year out of range")
        return _year
    except ValueError:
        raise ISIFormatError("Invalid ISI Year '%s'" % (year,))
        
        


def records(isi):
	"""
	read records from an open ISI-format file
	
  	TODO: make into a method on isireader()
	"""
	
	if isi.encoding.lower() != "utf-8-sig":
		logging.warn("%s opened in '%s' instead of BOM-compatible 'utf-8-sig'" % (isi, isi.encoding,))
	
	isi = (chomp(line) for line in isi) #(lazily) autostrip trailing newlines
	isi = ((i+1, line) for i, line in enumerate(isi)) #number isi lines, so we can give good debugging output
	def partition_lines(isi): #this is longer than it needs to be simply because I want to pass 'i' through it for the 'sep' error message
				   #it would be shorter written as a simple map function, without an internal loop
		for i, line in isi:
			#print(i,line) #DEBUG (handy: can see *every line* go past)
			#import IPython; IPython.embed()
			
			# partition the line
			# (note: EF, ER, and the blank line between records break the pattern, hence the verbose if-chain)
			# ( also being stateful and ordering ops choosily means we can reuse 'line' without worrying stomping it before the 'sep' check)
			if len(line) > 2:
				sep = line[2]
				if sep != ' ':
					raise ISIFormatError("line[%d]: Malformed ISI line: '%r'" % (i,line))
			tag = line[:2]
			line = line[3:] #subtle: [3:] works even if the line is not that long, it just gives "". This is probably acceptable:
				# on pure-tag lines like "ER" line will end up as "" as expected, and on the blank line, so will tag
			
			yield i, (tag, line)
	
	isi = partition_lines(isi)
	
	# ---- parse very first line
	_, (tag, header) = next(isi)
	if tag != 'FN':
		raise ISIFormatError("Malformed header: '%s %s'" % (tag, header,))
	
	#TODO: pass the header and version upwards somehow (probably by wrapping yet another generator)
	# TODO: handle the case where the file ends at these next()s.	

	# ---- parse very second line
	_, (tag, version) = next(isi)
	if tag != "VR":
			raise ISIFormatError("Malformed version '%s %s'" % (tag, version,))
	if version != "1.0": #TODO: make this optional, via flag (yayyy feature creep)
		raise ISIFormatError("Unsupported version '%s'" % (version,))
	
	
	# ---- parse everything else
	
	
	def fields():
		"""
		a generator over the fields in an isi record
		each key is a two letter ISI code as at <TODO>
		and each value is a string of everything following it, possibly on continuation lines.
		Now, some fields are actually lists, and some are simply extended paragraphs.
		(and some seem to be jerks that don't fit either)
		For now, content is returned as a list of the lines, even content of only a single element,
			either interpret beyond that should happen at a higher level or be carefully special-cased in.
		
		Control flow here is a bit unusual:
		 fields() and records() work together to process *the same stream*
		when fields() gives up on the stream, records() goes back to nomming it,
		and usually it immediately hands control back to fields()
		"""
		
		# the (apparent) format of an ISI field is:
		# [two letter character code][single space][content][newline]([two spaces][single space][content])*
		# that is, continuation lines are given by a two-"letter" code of '  '
		# This is a perfectly difficult format to parse, for which a very stateful generator is a great answer.
		
		# output will be (field, content)
		# except to avoid the quadradtic string-realloc curse, we store content as a list until we're done

		field, content = None, None
		
		# short maps to convert content's output form to something resembling it's real content
		# all fields are flattened by default unless they are explicitly listed here
		# inferring from the data I have, *some* fields, if they overflow,
		# are implicitly joined by newlines(?)
		# and others by spaces
		# and .. uh.. yeah.
		
		# TODO: figure out if I can assume. that abstracts do not seem to follow this convention wigs me out.
		paragraph = lambda c: str.join("\n", c)
		semicolon_list = lambda c: str.join(" ", c).split("; ")
		newline_list = lambda c: c
		flatten = lambda c: " ".join(c)
		reformatters = {'AB': paragraph, #abstracts are just paragraphs reflowed
			'SC': semicolon_list,  #subject categories are a a list split by semicolons
			'WC': semicolon_list,  #ditto for web-of-science categories
			#....			
			'C1': newline_list,
			#'PY': parse_year, #TODO
			#'PD': parse_month,
			}				
		_outcount = 0 #DEBUG
		for i, (tag, line) in isi:			
			# figure out what type of line we have:
			if tag != '  ':
				# a new field
				assert tag == tag.upper(), "ISI field tags should all be two letter upper case strings"
				
				# return what's collected (if any)
				# putting this here is cleaner than dupeing this code above to do a do-while
				if field is None:
					# but only if there's anything to return, of course
					assert content is None, "invariant: field exists <=> content exists"
				else:
					_outcount += 1
					yield field, reformatters.get(field, flatten)(content)
				
				if tag == 'ER':
					# end record
					break
				elif tag == 'EF':
					# end file
					assert _outcount == 0 #XXX this should be an ISIFormatError
					return          #cut short the generator
				else:
					# common case: a new tag
					# reset the accumulators and continue
					field, content = tag, [line]
			else:
				# continuation line
				if field is None:
					raise ISIFormatError("line[%d]: Field continuation line seen before any field tag: '%s'" % (i,line,))
				assert content is not None, "invariant: field exists <=> content exists"
				content += [line]
		else:
			raise ISIFormatError("line[%d]: Record (and file) ended before 'ER' marker." % (i,))

	
	while True:
		# read records
		# this loop ends when we read a fake 'record' that consists of a single tag 'EF'
		r = list(fields())
		if not r:
			# end of file (NB: this isn't the same as EOF, the actual file might continue)
			break
		
		# sanity check
		if len(r) != len({k for k,v in r}):
			raise ISIFormatError('Duplicate fields seen in a record: %s' % (fields,))
		# coerce to dict form, now that we know it's safe
		yield dict(r)
		
		# every record is followed by a single empty line
		# TODO: maybe just scrap this; how important is it really to enforce the BLANK LINE RULE? seriously. autists ehre we come.
		try:
			i, blank = next(isi)
			if blank != ("",""):
				raise ISIFormatError("line[%d]: Missing blank line after record. Instead saw: %s" % (i, blank))
		except StopIteration:
			raise ISIFormatError("File ended before 'EF' marker.") #XXX awkward; DRY this with the one below
	else:
		# ensure that we exit the loop by 'EF' and not some other way
		raise ISIFormatError("File ended before 'EF' marker.")
	


class reader():
	def __init__(self, name, encoding="utf-8-sig"):
		self._file = builtins.open(name, "r", encoding=encoding)
	
	def __iter__(self):
		return iter(records(self._file))
	
	def __enter__(self):
		assert not self._file.closed
		return self
		
	def __exit__(self, *_unused):
		self._file.close()


def open(fname, mode="r", encoding="utf-8-sig"):
	"""
	utf-8-sig is the most widely compatible text codec. It handles both ASCII files (because of utf-8 backwards compatibility) and most Unicode files, with or without a BOM.
	If you happen to have a different encoding, you can provide it. See the codecs module for options.
	TODO: use the chardet module?
	"""
	if mode != "r":
		raise NotImplementedError("only have read-only support so far")
	
	return reader(fname)

if __name__ == '__main__':
	import sys
	with open(sys.argv[1]) as isi:
		for i, record in enumerate(isi):
			print(i, record)
			#import IPython; IPython.embed()
	
