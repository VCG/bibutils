# bibutils
Utility functions &amp; instructions for working with VCG Zotero

Setup and activate the conda environment:
```shell
$ conda env create -f environment.yml
$ conda activate bibutils
```

Download references as bibtex file from the [VCG Zotero](https://www.zotero.org/groups/4672801/vcg-papers/library).
Convert to lib style of your choice.

```shell
pybtex-format --style plain <mybibfile.bib> <mytextfile.txt>
```

### Compiling conflict of interests
Here is a simple example of how to compile conflicts of interest for Hanspeter from 2010 to 2022.

``` shell
python coi.py
    --first Hanspeter // first name of author
    --last Pfister // last name of author
    --i papers.bib // input bib file with references to consider
    --sy 2010 // start year of conflict of interests
    --ey 2022 // end year of conflict of interests
```
