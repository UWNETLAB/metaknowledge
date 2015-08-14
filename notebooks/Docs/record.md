# The Record Class


## Overview

The `isilib.Record` class is a way to manage the meta-data provided by WOS for a single piece of literature, e.g. a paper, book or conference. These records are obtained as plain text flat databases, which the `isilib.Record` class can read and analyze to extract useful information from, such as a list of the subject tags or the WOS number of the record. They can also be collected into larger groups in the `isilib.RecordCollection` class and analysis of their relationships can be run.


## WOS records

WOS provides records in a plain text form from the web interface, or their API. To get them from the web interface in groups of up to 500 by select the _"Other File Formats"_ and then _"Plain Text"_ options when you have done a search. The records can then be downloaded as a single file with an entry for each record. Each file (a utf-8 with BOM encoding) starts with the WOS header

      FN Thomson Reuters Web of Science™

      VR 1.0

The rest of the file consists of a series of records composed of WOS tags, usually starting with the 'PT' tag. Each record is terminated by a line with only 'ER' and a second blank line.


# TODO explain fields



A WOS tag is how the fields in the record files are identified each is two characters long and composed of uppercase letters and number. There is no published complete list, nor is there a definition provided for most tags, the best known official list is [here](http://images.webofknowledge.com/WOK46/help/WOS/h_fieldtags.html). So tags in this library have been compiled by hand, as have their meanings. Tags that have been compiled are in the `isilib.tagFuncs` module. Examples of tags are 'CR' for cited references, 'J9' for the 29-Character Source Abbreviation and 'OI' for the orcID, most tags are not present in all papers.

The beginning of a record is a tag followed by a space and then the value of that tag, e.g _"PT J"_.
# Bellow this for each tag, if applicable to the record, a tag and values pair occurs.
If the value occupies more than one line, the line after the first starts with 3 spaces and then the values for that line. New lines can occur to distinguish entries in a value, for instance the 'CR' tag gives each reference a line. Or they can occur because the value of tag contains new lines, e.g. the 'AB' (abstract). However, new lines can also occur for no distinguishable reason.

The last line of a record is the end of record indicator 'ER'. When all these are put together into a full file the result is similar to this:



      FN Thomson Reuters Web of Science™

      VR 1.0

      PT J

      AU Marghetis, T

      AF Marghetis, Tyler

      TI The Motion Behind the Symbols

      SO TOPICS IN COGNITIVE SCIENCE

      LA English

      DT Article

      DE Mathematical practice; Metaphor; Fictive motion; Gesture; Cauchy;

            Calculus; Conceptualization

      ID REPRESENTATIONS; GESTURE; REAL; TIME

      AB The canonical history of mathematics suggests that the late 19th-century arithmetization of calculus marked a shift away from spatial-dynamic intuitions, grounding concepts in static, rigorous definitions. Instead, we argue that mathematicians, both historically and currently, rely on dynamic conceptualizations of mathematical concepts like continuity, limits, and functions. In this article, we present two studies of the role of dynamic conceptual systems in expert proof. The first is an analysis of co-speech gesture produced by mathematics graduate students while proving a theorem, which reveals a reliance on dynamic conceptual resources. The second is a cognitive-historical case study of an incident in 19th-century mathematics that suggests a functional role for such dynamism in the reasoning of the renowned mathematician Augustin Cauchy. Taken together, these two studies indicate that essential concepts in calculus that have been defined entirely in abstract, static terms are nevertheless conceptualized dynamically, in both contemporary and historical practice.

      C1 [Marghetis, Tyler; Nunez, Rafael] Univ Calif San Diego, Dept Cognit Sci, La Jolla, CA 92093 USA.

      RP Marghetis, T (reprint author), Univ Calif San Diego, Dept Cognit Sci, La Jolla, CA 92093 USA.

      EM tmarghet@cogsci.ucsd.edu

      CR Alibali MW, 1999, PSYCHOL SCI, V10, P327, DOI 10.1111/1467-9280.00163

         Bell E. T., 1940, DEV MATH

         Byers W., 2007, MATH THINK USING AMB

      NR 45

      TC 4

      Z9 4

      PU WILEY-BLACKWELL

      PI HOBOKEN

      PA 111 RIVER ST, HOBOKEN 07030-5774, NJ USA

      SN 1756-8757

      J9 TOP COGN SCI

      JI Top. Cogn. Sci.

      PD APR

      PY 2013

      VL 5

      IS 2

      BP 299

      EP 316

      DI 10.1111/tops.12013

      PG 18

      WC Psychology, Experimental

      SC Psychology

      GA 126NA

      UT WOS:000317623000007

      PM 23460466

      ER



      EF


What is referenced to as a "WOS record" is everything between the 'VR 1.0' and 'ER'. If multiple records are present in a file they are seperated by the 'ER'
