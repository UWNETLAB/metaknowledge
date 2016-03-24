from .backend import getj9dict, abrevDBname, manaulDBname, addToDB

from ...citation import Citation

abbrevDict = None

class WOSCitation(Citation):
    def isJournal(self, dbname = abrevDBname, manaulDB = manaulDBname, returnDict = 'both', checkIfExcluded = False):
        """Returns `True` if the `Citation`'s `journal` field is a journal abbreviation from the WOS listing found at [http://images.webofknowledge.com/WOK46/help/WOS/A_abrvjt.html](http://images.webofknowledge.com/WOK46/help/WOS/A_abrvjt.html), i.e. checks if the citation is citing a journal.

        **Note**: Requires the [j9Abbreviations](#journalAbbreviations.getj9dict) database file and will raise an error if it cannot be found.

        **Note**: All parameters are used for getting the data base with  [**getj9dict**()](#journalAbbreviations.getj9dict).

        # Parameters

        _dbname_ : `optional [str]`

        > The name of the downloaded database file, the default is determined at run time. It is recommended that this remain untouched.

        _manaulDB_ : `optional [str]`

        > The name of the manually created database file, the default is determined at run time. It is recommended that this remain untouched.

        _returnDict_ : `optional [str]`

        > default `'both'`, can be used to get both databases or only one  with `'WOS'` or `'manual'`.

        # Returns

        `bool`

        > `True` if the `Citation` is for a journal
        """
        global abbrevDict
        if abbrevDict is None:
            abbrevDict = getj9dict(dbname = dbname, manualDB = manaulDB, returnDict = returnDict)
        if checkIfExcluded and self.journal:
            try:
                if abbrevDict.get(self.journal, [True])[0]:
                    return False
                else:
                    return True
            except IndexError:
                return False
        else:
            if self.journal:
                dictVal = abbrevDict.get(self.journal, [b''])[0]
                if dictVal:
                    return dictVal
                else:
                    return False
            else:
                return False

    def FullJournalName(self):
        """Returns the full name of the Citation's journal field. Requires the [j9Abbreviations](#journalAbbreviations.getj9dict) database file.

        **Note**: Requires the [j9Abbreviations](#journalAbbreviations.getj9dict) database file and will raise an error if it cannot be found.

        # Returns

        `str`

        > The first full name given for the journal of the Citation (or the first name in the WOS list if multiple names exist), if there is not one then `None` is returned
        """
        global abbrevDict
        if abbrevDict is None:
            abbrevDict = getj9dict()
        if self.isJournal():
            return abbrevDict[self.journal][0]
        else:
            return None

    def addToDB(self, manualName = None, manaulDB = manaulDBname, invert = False):
        """Adds the journal of this Citation to the user created database of journals. This will cause [isJournal()](#Citation.isJournal) to return `True` for this Citation and all others with its `journal`.

        **Note**: Requires the [j9Abbreviations](#journalAbbreviations.getj9dict) database file and will raise an error if it cannot be found.

        # Parameters

        _manualName_ : `optional [str]`

        > Default `None`, the full name of journal to use. If not provided the full name will be the same as the abbreviation.

        _manaulDB_ : `optional [str]`

        > The name of the manually created database file, the default is determined at run time. It is recommended that this remain untouched.

        _invert_ : `optional [bool]`

        > Default `False`, if `True` the journal will be removed instead of added
        """
        try:
            if invert:
                d = {self.journal : ''}
            elif manualName is None:
                d = {self.journal : self.journal}
            else:
                d = {self.journal : manualName}
            addToDB(abbr = d, dbname = manaulDB)
        except KeyError:
            raise KeyError("This citation does not have a journal field.")
        else:
            abbrevDict.update(d)
