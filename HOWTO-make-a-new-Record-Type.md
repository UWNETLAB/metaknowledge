#Overview

The Records in metaknowledge all inherit from the `ExtendedRecord` class in `mkRecord.py` which is a `Record` that memorizes, it saves the results of the fields it processes. `Record` is a `Mapping` subclass which means it acts like a immutable dict. If you wish to create a new
