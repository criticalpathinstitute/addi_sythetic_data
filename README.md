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

TODO: I need to get a data dictionary to define all these fields.

So far I've written a simple synthesizer program in Python that will process this input file, modify the "USUBJID" to a generated UUID, and will randomly select values for each field from all the other values in the file.
This is just a start and is probably a long way from what the final will do:

```
$ ./synth.py -h
usage: synth.py [-h] -f FILE [-o OUTFILE] [-m MAX]

ADDI synthetic data

optional arguments:
  -h, --help            show this help message and exit
  -f FILE, --file FILE  Input file (default: None)
  -o OUTFILE, --outfile OUTFILE
                        Output file (default: out.csv)
  -m MAX, --max MAX     Maximum number of records (default: 0)
```

## Author

Ken Youens-Clark <kyclark@c-path.org>
