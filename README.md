# bibutils
Utility functions &amp; instructions for working with VCG Zotero

### Setup
Setup and activate the conda environment:
```shell
$ conda env create -f environment.yml
$ conda activate bibutils
```

### Pretty Printing 
Download references as bibtex file from the [VCG Zotero](https://www.zotero.org/groups/4672801/vcg-papers/library). Contact [Jakob](https://jakobtroidl.github.io/) for access. This command writes a pretty print of  `<mybibfile.bib>` into `<mytextfile.txt>`

```shell
pybtex-format --style plain --abbreviate-names <mybibfile.bib> <mytextfile.txt>
```

### Conflicts of Interests
Here is a simple example of how to compile conflicts of interest for Hanspeter from 2010 to 2022. This script writes the list of conflicting authors to `conflicting_authors.txt` in the same directory. 

``` shell
python coi.py
    --first Hanspeter // first name of author
    --last Pfister // last name of author
    --i papers.bib // input bib file with references to consider
    --sy 2010 // start year of conflict of interests
    --ey 2022 // end year of conflict of interests
```
