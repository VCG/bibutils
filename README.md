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
