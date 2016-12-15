from .nsercGrant import NSERCGrant, isNSERCfile, parserNSERCfile
from .medlineGrant import MedlineGrant
from .baseGrant import Grant, FallbackGrant, isFallbackGrantFile, parserFallbackGrantFile
from .cihrGrant import CIHRGrant, isCIHRfile, parserCIHRfile
from .nsfGrant import NSFGrant, isNSFfile, parserNSFfile


"""#Creating new grants

mk is intended to be expanded as different researchers will require processing of files not in it currently. To add a new grant you need to write 2 simple functions and class. To see a basic example look at the `baseGrant.py` file as it contains the fallback grant processors and you should be able to reuse much of that code.

The way GrantCollections are created is when they are given a file or directory of files they check each file with the `detector` functions in the `grantProcessors` found in `fileHandlers.py` and if one returns `True` they use the `processor` function and added the `type` string to their `collectedTypes` set. The `processor` must return a tuple the first element being a set of all the Grants the second `None` or an `Exception` object. `processor` should not raise an exception, if there is an issue the GrantCollection should be given even a partial set of grants, GrantCollections have an errors attribute that contains all errors they encountered during the parsing.


The first function is to determine if a given file path is to a collection of grants of the needed type. Determining if a file is of the needed type is usually done by reading the first few lines and checking that they match a known header template. For example CIHR files start with the string `"Search Criteria,"` so the function `isCIHRfile()` checks that the first lines start that way.

One thing to watch out for is the encoding most grants are CSVs encoded with ISO-8859 which is what many windows programs, most notably excel, expect. Python will use that encoding (called `'latin-1'`) on Microsoft systems but on Mac OS and Linux will often use `'utf-8'` so you should always give the encoding as mk is intended for all 3 operating systems.

The next function is the parser, this is the function that is called on the file to create the Grants. It is given a file path that has been confirmed to be a correctly formatted grant by the detector.

The function must return a tuple the first entry being a set of all the Grants and the second an `Exception` if an error occurred or `None` if not. If an error occurs the function should attempt to return as many grants as possible, including the one that had the error (with its error handlers correctly indicated). The GrantCollectio will record the error and allow for the user/script to decide what actions to take.Note, often not doing anything is appropriate as errors have been found to most often occur at the end of the file so no data is actually lost.

The`Grants` in the set returned by the processor, should be a new class the inherits from `Grant` even if no new attributes are defined.

Once the `detector` and `processor` functions have been created and tested, they can be added to the list of grants found in `fileHandlers.py` called `grantProcessors`. Each file is checked in order so do not add them to the end as the last entry will tell the `GrantCollection` to stop and that the file does not match, so placing anything after it will not work.
"""
