# tools
General-purpose bioinformatics tools

1. runoverchr.py
Tool to iterate a command over chromosomes 1 to 22.
To run: 
-Download Python script, and place it in a directory that's on your path. Make it executable (chmod u+x runoverchr.py)
$ runoverchr.py "vcftools --vcf allchr.vcf --chr chrXXX --recode --out chrXXX"

The program will replace XXX with 1 to 22 and iterate.
