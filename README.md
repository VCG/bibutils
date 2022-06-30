# bibutils
Biblography utility functions for the VCG

### Setup
1. If you want to makes changes to bibutils functionality, request access to the Google Cloud Project from [Jakob Troidl](jakobtroidl.github.io).

2. Setup and activate the conda environment:
```shell
$ conda env create -f environment.yml
$ conda activate bibutils
```

### Pretty Printing 
Download references as bibtex file from the VCG Website. This command returns a pretty print of the [downloaded bib file](https://vcg.seas.harvard.edu/publications.bib). 

```shell
pybtex-format --style plain --abbreviate-names <mybibfile.bib> <mytextfile.txt>
```

### Conflicts of Interests
Here is a simple example of how to compile conflicts of interest for Hanspeter. The `conflict` folder is synced with a [Google Cloud Function](https://console.cloud.google.com/functions/details/us-east1/conflict_of_interest?env=gen1&project=jakob-troidl). [`conflict/main.py`](https://github.com/VCG/bibutils/blob/main/conflict/main.py) automatically downloads content of the [VCG Website](https://vcg.seas.harvard.edu/publications.bib) and returns a list of conflicting authors. The function can be triggered using this link:

```
https://us-east1-jakob-troidl.cloudfunctions.net/conflict_of_interest?first=Hanspeter&last=Pfister&from=2018&to=2022
```

For making changes to the script, edit [`conflict/main.py`](https://github.com/VCG/bibutils/blob/main/conflict/main.py) and push to the `main` branch to make the changes publicly accessible through the above link. 
