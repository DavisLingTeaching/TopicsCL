# Versions of data for Wilcox et al. (2022)

The following describes some attempts to gather data comparable to the data used
to evaluated models in [Wilcox et al. (2022)](https://direct.mit.edu/ling/article/doi/10.1162/ling_a_00491/113304/Using-Computational-Models-to-Test-Syntactic).

## Filler Gap Experiments 

All data conversions are done with convert\_fgd.py

### Subject Gaps

For this I drew on the data from [Hu et al.
(2020)](https://www.aclweb.org/anthology/2020.acl-main.158). Namely, the data
found on github
[here](https://github.com/cpllab/syntactic-generalization/tree/master/test_suites).

I downloaded the json file (fgd\_subject.json) which gives the region of interest and the txt file (fgd\_subject.txt) which gives the sentences. I converted the txt file to a simple tsv that will work with my code (fgd\_subject.tsv). 


