# ADDI Synthetic Data

First, export the CPAD (Alzheimer's) data from CODR.
My file was called "fullExportDb-744-C-PathOnly-CSV.zip".
Unzip this, and find the file "cm.csv" which has this structure:

```
$ csvchk cm.csv
// ****** Record 1 ****** //
STUDYID  : 1142
DOMAIN   : CM
USUBJID  : XXXXX
CMSEQ    : 8
CMGRPID  :
CMSPID   : .
CMLNKID  :
CMTRT    : CELEXA
CMMODIFY :
CMDECOD  :
CMCAT    : GENERAL
CMSCAT   :
CMPRESP  :
CMOCCUR  :
CMSTAT   :
CMREASND :
CMINDC   : agitation
CMCLAS   :
CMCLASCD :
CMDOSE   :
CMDOSU   :
CMDOSFRM :
CMDOSFRQ : qd
CMDOSTOT :
CMDOSRGM :
CMROUTE  : po
CMPSTRG  :
CMPSTRGU :
VISITNUM :
VISIT    :
EPOCH    :
CMDTC    :
CMSTDTC  :
CMENDTC  :
CMDY     :
CMSTDY   : 285
CMENDY   :
CMDUR    :
CMSTRF   : DURING
CMENRF   :
CMEVLINT :
CMEVINTX :
CMSTRTPT :
CMSTTPT  :
CMENRTPT : AFTER
CMENTPT  : 18 Month or Trial Discontinuation
CMDOSTXT : 10mg
```

NOTE: SDTMIG_CM_Domain.pdf is the data dictionary.

So far I've written a simple program in Python that will 

* Read input file,
* Remove the CMGRPID, CMSPID, and CMLNKID variables
* Remove the variables with no data (they were added by CODR – one of CODR’s annoying attributes)
* Modify the "USUBJID" to a generated UUID
* Randomly select some number of records or all

```
$ ./synth.py -h
usage: synth.py [-h] -f FILE [-o OUTFILE] [-m MAX] [-x EXCLUDE [EXCLUDE ...]]

ADDI synthetic data

optional arguments:
  -h, --help            show this help message and exit
  -f FILE, --file FILE  Input file (default: None)
  -o OUTFILE, --outfile OUTFILE
                        Output file (default: out.csv)
  -m MAX, --max MAX     Maximum number of records (default: 0)
  -x EXCLUDE [EXCLUDE ...], --exclude EXCLUDE [EXCLUDE ...]
                        Exclude fields (default: ['CMGRPID', 'CMSPID',
                        'CMLNKID'])
```

Some additional suggestions:

* Add some noise to the start and end timing variables (CMSTDY and CMENDY) – also, Amanda had mentioned that they may want actual dates instead of the relative timing variables

To run, use `make sample`:

```
$ make
./scripts/synth.py -f data/cm.csv -m 10000 -o addi_cm.csv
Done, wrote 10,000 to "addi_cm.csv".
```

This will generate data like this:

```
$ csvchk addi_cm.csv
// ****** Record 1 ****** //
STUDYID  : 1013
DOMAIN   : CM
USUBJID  : E9cTf9Cjg8JxjbqSBsTDxN
CMSEQ    : 24
CMTRT    : NEXIUM
CMMODIFY :
CMDECOD  : ESOMEPRAZOLE
CMCAT    :
CMSCAT   :
CMPRESP  :
CMINDC   : GORD
CMCLAS   :
CMDOSE   :
CMDOSU   :
CMDOSFRQ :
CMDOSTOT :
CMROUTE  :
VISITNUM :
VISIT    :
CMSTDY   : -1024.0
CMENDY   :
CMSTRF   : BEFORE
CMENRF   : AFTER
CMENRTPT :
CMENTPT  :
CMDOSTXT : 40 MG DAILY
```

## Author

Ken Youens-Clark <kyclark@c-path.org>
