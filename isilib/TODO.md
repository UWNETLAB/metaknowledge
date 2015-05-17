#TODO

## Implementation
### Add more documentation
###remove general exceptions
### Record class
* add methods for every important tag
* maybe do geocoding

### RecordCollection class
* extract subset from more ranges
* add more methods to create networks
* look a error handling
   - addition needs work
* Consider making network checks more in depth

## Cleaning and Preprocessing WOS data

* [reconcile journal names](http://cishell.wiki.cns.iu.edu/Reconcile+Journal+Names). link includes a link to the source code, and a download to an Excel file with journal names.

### citation, co-citation, co-author, bibliographic coupling, etc.  

* extract citation networks
    - for within record set only *or* "core and references" / unrestricted
        + paper citation networks
        + author citation networks
        + source citation networks

* extract co-citation networks
    - the co-citeMaker.py script works *great,* but would be more useful if it could take data within a given time frame from a large collection of WOS files that are not organized around dates (see split records task in "cleaning and preprocessing WOS data")
    - add ability / new scripts for:
        + author co-citation
        + source co-citation

* extract co-author networks
    - again, this is *great,* but would be even better if it could be based on a specific time frame specified by the researcher

* bibliographic coupling
    - to get institutional collaboration networks
    - to group records based on similar bibliographies (this is less important to me than getting institutional networks)

* two-mode networks
    - paper and: SO, WC, SC, or keywords
    - author and: SO, WC, SC, or keywords
    - looks like there is a link to Sci^2 source code for 2 mode networks [here](http://cishell.wiki.cns.iu.edu/Bipartite+Network+Graph)

* community detection for all ^ networks
    - the Blondel / Louvain community detection algorithm is not available in iGraph, but Sci^2 has the Blondel version, and NetworkX has the Louvain version. can you include it in the scripts above so community membership attributes are included in the graphml file? however it would be good if this was easy to quickly turn off if I want to speed things up. I prefer Blondel (2008), but Louvain is fine. **Note that this should only work for 1 mode networks. There are different methods for community detection in 2 mode networks. Perhaps you can look into them.**

* writing network files
    - write to graphml for easy analysis in iGraph or NetworkX
    - export for D3 (e.g. in Neal Caren's script, which requires Drew Conway's fork of NetworkX)

* whenever a new network is created (e.g. by co-citeMaker.py), print:
    - whether directed or undirected
    - number of nodes and edges
    - number of nodes in the giant component
    - number of isolates

## Content: Burst Detection, Topics, etc.

### Burst Detection

Sci^2 is capable of burst detection, which was originally implemented in C, and then rewritten by the Sci^2 team in Java. You can read about it [here](http://cishell.wiki.cns.iu.edu/Burst+Detection). There is a link to their source code (which fails on my machine), and to the original C implementation. Burst detection is *really* useful for identifying changes over time.

* burst detection for keywords
* burst detection for authors
* burst detection for documents
* burst detection for references


### Bad Records

FN Thomson Reuters Web of Science™
VR 1.0
P J
AU BREVIK, I
AF BREVIK, I
TI EXPERIMENTS IN PHENOMENOLOGICAL ELECTRODYNAMICS AND THE ELECTROMAGNETIC
   ENERGY-MOMENTUM TENSOR
SO PHYSICS REPORTS-REVIEW SECTION OF PHYSICS LETTERS
LA English
DT Review
C1 UNIV TRONDHEIM,INST THEORET PHYS,N-7034 TRONDHEIM,NORWAY.
   LUFTKRIGSSKOLEN,TRONDHEIM MIL 7000,NORWAY.
CR Abraham M., 1909, RC CIRC MAT PALERMO, V28, P1
   Abraham M., 1910, REND CIRC MATEM PALE, V30, P5
   ALLEN PJ, 1966, AM J PHYS, V34, P1185, DOI 10.1119/1.1972585
   Arnaud J. A., 1973, Optics Communications, V7, DOI 10.1016/0030-4018(73)90041-2
   ARNAUD JA, 1972, ELECTRON LETT, V8, P541, DOI 10.1049/el:19720394
   ARNAUD JA, 1975, J OPT SOC AM, V65, P174, DOI 10.1364/JOSA.65.000174
   ARNAUD JA, 1974, AM J PHYS, V42, P71, DOI 10.1119/1.1987607
   ASHKIN A, 1973, PHYS REV LETT, V30, P139, DOI 10.1103/PhysRevLett.30.139
   ASHKIN A, 1971, APPL PHYS LETT, V19, P283, DOI 10.1063/1.1653919
   ASHKIN A, 1974, APPL PHYS LETT, V24, P586, DOI 10.1063/1.1655064
   ASHKIN A, 1970, PHYS REV LETT, V24, P156, DOI 10.1103/PhysRevLett.24.156
   ASHKIN A, 1975, SCIENCE, V187, P1073, DOI 10.1126/science.187.4181.1073
   ASHKIN A, 1976, APPL PHYS LETT, V28, P333, DOI 10.1063/1.88748
   Barlow G, 1912, P R SOC LOND A-CONTA, V87, P1, DOI 10.1098/rspa.1912.0054
   Beth RA, 1936, PHYS REV, V50, P115, DOI 10.1103/PhysRev.50.115
   BILGER HR, 1972, PHYS REV A, V5, P591, DOI 10.1103/PhysRevA.5.591
   BOTTCHER CJF, 1973, THEORY ELECTRIC POLA, V1
   BREVIK I, 1970, MAT FYS MEDD DAN VID, V37
   BREVIK I, 1970, MAT FYS MEDD DAN VID, V38
   BREVIK I, 1973, LETT NUOVO CIMENTO, V7, P518, DOI 10.1007/BF02727866
   BULLOUGH RK, 1970, PHYSICS QUANTUM ELEC
   CARRARA N, 1949, NATURE, V164, P882, DOI 10.1038/164882c0
   CAVALLERI G, 1974, LETT NUOVO CIMENTO, V12, P626
   CAVALLER.G, 1973, LETT NUOVO CIMENTO, V6, P305, DOI 10.1007/BF02743635
   COSTADEB.O, 1971, CR ACAD SCI B PHYS, V272, P1340
   Costa de Beauregard O., 1974, Comptes Rendus Hebdomadaires des Seances de l'Academie des Sciences, Serie B (Sciences Physiques), V278
   COSTADEB.O, 1972, CR ACAD SCI B PHYS, V274, P1299
   COSTADEB.O, 1972, CR ACAD SCI B PHYS, V274, P164
   COSTADEBEAUREGARD O, 1975, CAN J PHYS, V53, P2355
   Debye P, 1909, ANN PHYS-BERLIN, V30, P57
   Durand E., 1953, ELECTROSTATIQUE MAGN
   Einstein A, 1908, ANN PHYS-BERLIN, V26, P541
   Ginzburg V. L., 1960, SOV PHYS USP, V2, P874, DOI 10.1070/PU1960v002n06ABEH003185
   Ginzburg V. L., 1976, Soviet Physics - Uspekhi, V19, DOI 10.1070/PU1976v019n01ABEH005127
   GINZBURG VL, 1974, SOV PHYS USP, V16, P434
   Ginzburg VL, 1940, J PHYS-USSR, V2, P441
   GOETZ H, 1955, Z PHYS, V141, P277, DOI 10.1007/BF01325743
   GOETZ H, 1958, Z PHYS, V151, P202, DOI 10.1007/BF01344215
   GORDON JP, 1973, PHYS REV A, V8, P14, DOI 10.1103/PhysRevA.8.14
   GRODZINS L, 1961, PHYS REV, V124, P774, DOI 10.1103/PhysRev.124.774
   GROOT SRD, 1972, F ELECTRODYNAMICS
   Gyorgyi G., 1960, American Journal of Physics, V28
   Hakim S.S., 1962, Proceedings of the Institution of Electrical Engineers. C. Institution Monographs, V109
   HAKIM SS, 1962, P PHYS SOC LOND, V80, P190, DOI 10.1088/0370-1328/80/1/322
   HAUS HA, 1969, PHYSICA, V43, P77, DOI 10.1016/0031-8914(69)90283-3
   IRVINE WM, 1965, J OPT SOC AM, V55, P16, DOI 10.1364/JOSA.55.000016
   JAMES RP, 1968, THESIS STANFORD U
   JAMES RP, 1968, P NATL ACAD SCI USA, V61, P1149
   Jauch J M, 1955, THEORY PHOTONS ELECT
   JAUCH JM, 1948, PHYS REV, V74, P950, DOI 10.1103/PhysRev.74.950
   JAUCH JM, 1948, PHYS REV, V74, P1485, DOI 10.1103/PhysRev.74.1485
   JAUCH JM, 1949, PHYS REV, V75, P1249
   JONES RV, 1975, P ROY SOC LOND A MAT, V345, P351, DOI 10.1098/rspa.1975.0141
   JONES RV, 1972, PROC R SOC LON SER-A, V328, P337, DOI 10.1098/rspa.1972.0081
   JONES RV, 1978, P ROY SOC LOND A MAT, V360, P365, DOI 10.1098/rspa.1978.0073
   JONES RV, 1978, P ROY SOC LOND A MAT, V360, P347, DOI 10.1098/rspa.1978.0072
   JONES RV, 1954, PROC R SOC LON SER-A, V221, P480, DOI 10.1098/rspa.1954.0043
   JONES RV, 1973, RAD PRESSURE OPTICAL
   KASTLER A, 1974, CR ACAD SCI B PHYS, V278, P1013
   LAHOZ DG, 1974, ELECTROMAGNETIC FORC
   LAI HM, 1976, PHYS REV A, V14, P2329, DOI 10.1103/PhysRevA.14.2329
   Landau L.D., 1959, FLUID MECHANICS
   LANDOLTBORNSTEI, 1962, ZAHLENWERTE FUNKTION
   LAUE MV, 1950, Z PHYSIK, V128, P387, DOI 10.1007/BF01339439
   LOSURDO C, 1973, NUOVO CIMENTO B, VB 13, P217
   LUCAS R, 1974, CR ACAD SCI B PHYS, V278, P693
   M.Abramowitz, 1970, HDB MATH FUNCTIONS
   Marx G., 1955, Annalen der Physik, V16
   MIKURA Z, 1976, PHYS REV A, V13, P2265, DOI 10.1103/PhysRevA.13.2265
   Minkowski H, 1910, MATH ANN, V68, P472, DOI 10.1007/BF01455871
   Minkowski H., 1908, Nachrichten von der Koniglicher Gesellschaft der Wissenschaften zu Gottingen, Mathematisch-Physikalische Klasse
   Moller C, 1972, THEORY RELATIVITY
   Nagy K., 1955, Acta Physica Hungarica, V5
   PANOFSKY WKH, 1955, CLASSICAL ELECTRICIT
   PAO YH, 1975, 2508 CORN U MAT SCI
   PAO YH, 1977, MECHANICS TODAY, V4
   PEIERLS R, 1977, P ROY SOC LOND A MAT, V355, P141, DOI 10.1098/rspa.1977.0091
   PEIERLS R, 1976, P ROY SOC LOND A MAT, V347, P475, DOI 10.1098/rspa.1976.0012
   Penfield P., 1967, ELECTRODYNAMICS MOVI
   RATCLIFF KF, 1972, AM J PHYS, V40, P1044, DOI 10.1119/1.1986744
   Robinson F. N. H., 1975, Physics Reports. Physics Letters Section C, V16C, DOI 10.1016/0370-1573(75)90057-5
   ROOSEN G, 1977, J OPT, V8, P181, DOI 10.1088/0150-536X/8/3/005
   ROOSEN G, 1973, CR ACAD SCI B PHYS, V277, P147
   ROOSEN G, 1974, CAN J PHYS, V52, P1903
   ROOSEN G, 1973, CR ACAD SCI B PHYS, V277, P135
   ROOSEN G, 1976, PHYS LETT A, V59, P6, DOI 10.1016/0375-9601(76)90333-9
   Ryazanov M. I., 1958, SOV PHYS JETP, V7, P869
   Ryazanov M. I., 1957, SOV PHYS JETP, V5, P1013
   Schiff L. I., 1968, QUANTUM MECHANICS
   SHOCKLEY W, 1968, P NATL ACAD SCI USA, V60, P807, DOI 10.1073/pnas.60.3.807
   Skobel'tsyn D. V., 1973, Soviet Physics - Uspekhi, V16, DOI 10.1070/PU1973v016n03ABEH005188
   SKOBELTSYN DV, 1978, SOV PHYS USPEKHI, V20, P528
   SKOBELTZYNE DV, 1975, CR ACAD SCI B PHYS, V280, P251
   SKOBELTZYNE DV, 1975, CR ACAD SCI B PHYS, V280, P287
   Stratton J. S., 1941, ELECTROMAGNETIC THEO
   THORNBER KK, 1973, PHYS LETT A, VA 43, P501, DOI 10.1016/0375-9601(73)90012-1
   WALKER GB, 1976, NATURE, V263, P401, DOI 10.1038/263401a0
   WALKER GB, 1975, CAN J PHYS, V53, P2577
   WALKER GB, 1975, NATURE, V253, P339, DOI 10.1038/253339a0
   WALKER GB, 1977, NATURE, V265, P324, DOI 10.1038/265324a0
   WALKER GB, 1977, CAN J PHYS, V55, P2121
   WONG HK, 1977, AM J PHYS, V45, P195, DOI 10.1119/1.10655
   Yariv A., 1971, INTRO OPTICAL ELECTR
   ZAHN W, 1962, Z PHYS, V166, P275, DOI 10.1007/BF01380775
NR 104
TC 244
Z9 245
PU ELSEVIER SCIENCE BV
PI AMSTERDAM
PA PO BOX 211, 1000 AE AMSTERDAM, NETHERLANDS
SN 0370-1573
J9 PHYS REP
JI Phys. Rep.-Rev. Sec. Phys. Lett.
PY 1979
VL 52
IS 3
BP 133
EP 201
DI 10.1016/0370-1573(79)90074-7
PG 69
WC Physics, Multidisciplinary
SC Physics
GA GV556
UT WOS:A1979GV55600001
ER
