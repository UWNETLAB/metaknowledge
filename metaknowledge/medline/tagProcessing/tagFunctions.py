from ...grants.medlineGrant import MedlineGrant

def IR(val):
    """Investigator"""
    return val

def FIR(val):
    """InvestigatorFull"""
    return val

def PROF(val):
    """PartialRetractionOf"""
    return val

def PUBM(val):
    """PublishingModel"""
    return val

def CN(val):
    """CorporateAuthor"""
    return val

def MHDA(val):
    """MeSHDate"""
    return val

def LID(val):
    """LocationIdentifier"""
    return val

def EDAT(val):
    """EntrezDate"""
    return val

def OCI(val):
    """OtherCopyright"""
    return val

def SB(val):
    """Subset"""
    return val

def DA(val):
    """DateCreated"""
    return val

def PMCR(val):
    """PubMedCentralRelease"""
    return val

def PG(val):
    """Pagination
    all pagination seen so far seems to be only on one line"""
    return val[0]

def GS(val):
    """GeneSymbol"""
    return val

def VI(val):
    """Volume
    The volumes as a string as volume is single line
    """
    return val[0]

def UOF(val):
    """UpdateOf"""
    return val

def OWN(val):
    """Owner"""
    return val

def ORI(val):
    """OriginalReportIn"""
    return val

def MID(val):
    """ManuscriptIdentifier"""
    return val

def PMID(val):
    """PubMedUniqueIdentifier"""
    return "PMID:{}".format(val[0])

def PMC(val):
    """PubMedCentralIdentifier"""
    return val

def RIN(val):
    """RetractionIn"""
    return val

def RPF(val):
    """RepublishedFrom"""
    return val

def CIN(val):
    """CommentIn"""
    return val

def FPS(val):
    """FullPersonalNameSubject"""
    return val

def TT(val):
    """TransliteratedTitle"""
    return val

def PHST(val):
    """PublicationHistoryStatus"""
    return val

def EFR(val):
    """ErratumFor"""
    return val

def PST(val):
    """PublicationStatus"""
    return val

def SPIN(val):
    """SummaryForPatients"""
    return val

def AU(val):
    """Author"""
    return val

def FED(val):
    """Editor"""
    return val

def NM(val):
    """SubstanceName"""
    return val

def SO(val):
    """Source"""
    return val

def IP(val):
    """Issue"""
    return val

def OABL(val):
    """OtherAbstract"""
    return val

def CRDT(val):
    """CreateDate"""
    return val

def DDIN(val):
    """DatasetIn"""
    return val

def MH(val):
    """MeSHTerms"""
    return val

def DP(val):
    """DatePublication"""
    return val[0]

def GN(val):
    """GeneralNote"""
    return val

def CRF(val):
    """CorrectedRepublishedFrom"""
    return val

def TI(val):
    """Title
    only one per record"""
    return val[0]

def CRI(val):
    """CorrectedRepublishedIn"""
    return val

def OT(val):
    """OtherTerm
    Nothing needs to be done"""
    return val

def ROF(val):
    """RetractionOf"""
    return val

def OTO(val):
    """OtherTermOwner
    one line field"""
    return val[0]

def OID(val):
    """OtherID"""
    return val

def PT(val):
    """PublicationType"""
    return val

def RPI(val):
    """RepublishedIn"""
    return val

def AB(val):
    """Abstract
    basically a one liner after parsing"""
    return val[0]

def EN(val):
    """Edition"""
    return val

def AD(val):
    """Affiliation
    Undoing what the parser does then splitting at the semicolons and dropping newlines extra fitlering is required beacuse some AD's end with a semicolon"""
    retDict = {}
    for v in val:
        split = v.split(' : ')
        retDict[split[0]] = [s for s in' : '.join(split[1:]).replace('\n', '').split(';') if s != '']
    return retDict

def LA(val):
    """Language"""
    return val

def TA(val):
    """JournalTitleAbbreviation
    One line only"""
    return val[0]

def JT(val):
    """JournalTitle
    One line only"""
    return val[0]

def IRAD(val):
    """InvestigatorAffiliation"""
    return val

def PS(val):
    """PersonalNameSubject"""
    return val

def IS(val):
    """ISSN"""
    return val

def PL(val):
    """PlacePublication"""
    return val

def CTI(val):
    """CollectionTitle"""
    return val

def FAU(val):
    """FullAuthor"""
    return val

def VTI(val):
    """VolumeTitle"""
    return val

def DCOM(val):
    """DateCompleted"""
    return val

def BTI(val):
    """BookTitle"""
    return val

def CI(val):
    """CopyrightInformation"""
    return val

def STAT(val):
    """Status"""
    return val

def DRIN(val):
    """DatasetUseReportedIn"""
    return val

def RF(val):
    """NumberReferences"""
    return val

def UIN(val):
    """UpdateIn"""
    return val

def LR(val):
    """DateLastRevised"""
    return val

def SFM(val):
    """SpaceFlightMission"""
    return val

def EIN(val):
    """ErratumIn"""
    return val

def AID(val):
    """ArticleIdentifier
    The given values do not require any work"""
    return val

def PRIN(val):
    """PartialRetractionIn"""
    return val

def DEP(val):
    """DateElectronicPublication"""
    return val

def AUID(val):
    """AuthorIdentifier
    one line only just need to undo the parser's effects"""
    retDict = {}
    for v in val:
        split = v.split(' : ')
        retDict[split[0]] = ' : '.join(split[1:])
    return retDict

def SI(val):
    """SecondarySourceID"""
    return val

def ISBN(val):
    """ISBN"""
    return val

def RN(val):
    """RegistryNumber"""
    return val

def JID(val):
    """NLMID"""
    return val

def GR(val):
    """GrantNumber"""
    return [MedlineGrant(v) for v in val]

medlineTagToFunc = {
    "IR" : IR,
    "FIR" : FIR,
    "PROF" : PROF,
    "PUBM" : PUBM,
    "CN" : CN,
    "MHDA" : MHDA,
    "LID" : LID,
    "EDAT" : EDAT,
    "OCI" : OCI,
    "SB" : SB,
    "DA" : DA,
    "PMCR" : PMCR,
    "PG" : PG,
    "GS" : GS,
    "VI" : VI,
    "UOF" : UOF,
    "OWN" : OWN,
    "ORI" : ORI,
    "MID" : MID,
    "PMID" : PMID,
    "PMC" : PMC,
    "RIN" : RIN,
    "RPF" : RPF,
    "CIN" : CIN,
    "FPS" : FPS,
    "TT" : TT,
    "PHST" : PHST,
    "EFR" : EFR,
    "PST" : PST,
    "SPIN" : SPIN,
    "AU" : AU,
    "FED" : FED,
    "NM" : NM,
    "SO" : SO,
    "IP" : IP,
    "OABL" : OABL,
    "CRDT" : CRDT,
    "DDIN" : DDIN,
    "MH" : MH,
    "DP" : DP,
    "GN" : GN,
    "CRF" : CRF,
    "TI" : TI,
    "CRI" : CRI,
    "OT" : OT,
    "ROF" : ROF,
    "OTO" : OTO,
    "OID" : OID,
    "PT" : PT,
    "RPI" : RPI,
    "AB" : AB,
    "EN" : EN,
    "AD" : AD,
    "LA" : LA,
    "TA" : TA,
    "JT" : JT,
    "IRAD" : IRAD,
    "PS" : PS,
    "IS" : IS,
    "PL" : PL,
    "CTI" : CTI,
    "FAU" : FAU,
    "VTI" : VTI,
    "DCOM" : DCOM,
    "BTI" : BTI,
    "CI" : CI,
    "STAT" : STAT,
    "DRIN" : DRIN,
    "RF" : RF,
    "UIN" : UIN,
    "LR" : LR,
    "SFM" : SFM,
    "EIN" : EIN,
    "AID" : AID,
    "PRIN" : PRIN,
    "DEP" : DEP,
    "AUID" : AUID,
    "SI" : SI,
    "ISBN" : ISBN,
    "RN" : RN,
    "JID" : JID,
    "GR" : GR,
}
