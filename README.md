# tools
General-purpose bioinformatics tools

1. runoverchr.py
Tool to iterate a command over chromosomes 1 to 22.
To run: 
-Download Python script, and place it in a directory that's in your path. Make it executable (chmod u+x runoverchr.py)
$ runoverchr.py --command "vcftools --vcf allchr.vcf --chr chrXXX --recode --out chrXXX"

The program will replace XXX with 1 to 22 and iterate.

To run the command for each chromosome in parallel, add the parameter --parallel:
$ runoverchr.py -c "vcftools --vcf allchr.vcf --chr chrXXX --recode --out chrXXX" --parallel

To run the command for a range of chromosomes:
$ runoverchr.py -c "vcftools --vcf allchr.vcf --chr chrXXX --recode --out chrXXX" --parallel --chr_start 3 --chr_end 20
