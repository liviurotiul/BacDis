var="Name	No.of_contigs	1st_Contig	1st_C_len	1st_C_cov	Species	ST	STgene1	STgene2	STgene3	STgene4	STgene5	STgene6	STgene7	Sp.i.Ef.ANI	Sp.i.Ef.mapped	Sp.i.Ef.TotQueryFrag	Sp.i.Sa.ANI	Sp.i.Sa.mapped	Sp.i.Sa.TotQueryFrag	Sp.i.Kp.ANI	Sp.i.Kp.mapped	Sp.i.Kp.TotQueryFrag	Sp.i.Ab.ANI	Sp.i.Ab.mapped	Sp.i.Ab.TotQueryFrag	Sp.i.Pa.ANI	Sp.i.Pa.mapped	Sp.i.Pa.TotQueryFrag	Sp.i.Esp.ANI	Sp.i.Esp.mapped	Sp.i.Esp.TotQueryFrag	Sp.i.Ec.ANI	Sp.i.Ec.mapped	Sp.i.Ec.TotQueryFrag	PF_contigNo.	PF_start	PF_end	PF_gene	PF_%Cov	PF_%ID	PF_AccNo.	PF_Product	RES_contigNo.	RES_start	RES_end	RES_gene	RES_%Cov	RES_%ID	RES_AccNo.	RES_Product	ARB_gene	ARB_flag	ARB_reads	ARB_PcID	ARB_CtgLen	ARB_CtgCov	ARB_change	ARB_effect	ARB_CtgStart	ARB_CtgEnd	ARB_Product	VIR_contigNo	VIR_start	VIR_end	VIR_gene	VIR_%Cov	VIR_%ID	VIR_AccNo.	VIR_Product"

printf "%s\n" "$var" >> filtered_data.tsv

for file in /home/marius/0WORK/WORK/00_SEQUENCING/RAW_data/RADAR/all_raws/TR_ASMBL_*/*_contigs_species_Ef.tsv; do

base=${file%Ef.tsv}; # ptr cele care au "contig_species"
secondbase=${file%contigs_species_Ef.tsv};
folder=$(dirname "${file}"); # echivalent cu ${file%/*}

python3 readFile10_ARGV.py ${folder}/contigs.fa ${secondbase}MLST.tsv ${file} ${base}Sa.tsv ${base}Kp.tsv ${base}Ab.tsv ${base}Pa.tsv ${base}Esp.tsv ${base}Ec.tsv ${secondbase}ABRICATE_PlasmidFinder.tsv ${secondbase}ABRICATE_rezist.tsv ${folder}/ARIBA_output/report.tsv ${secondbase}ABRICATE_VirulenceFactors.tsv >> filtered_data.tsv;
done
