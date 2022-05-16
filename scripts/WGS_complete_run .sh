conda activate WgsPipelineBac
ls -l | awk '{print $9}' | awk '{if ($0 ~ /R1/) {printf("shovill --keepfiles --trim --outdir TR_ASMBL_%s --R1 %s",substr($0,1,3),$0)} else if ($0 ~ /R2/) {printf(" --R2 %s\n",$0)}}' > shovill_run.sh
chmod +x shovill_run.sh
./shovill_run.sh
ls -l | awk '{print $9}' | awk '{if ($0 ~ /TR_ASMBL/) {printf("fastqc TR_ASMBL_%s/R1.fq.gz TR_ASMBL_%s/R2.fq.gz\n",substr($0,10,3),substr($0,10,3))}}' > fastqc_run.sh
chmod +x fastqc_run.sh
./fastqc_run.sh 
ls -l | awk '{print $9}' | awk '{if ($0 ~ /TR_ASMBL/) {printf("fastqc TR_ASMBL_%s/shovill.bam\n",substr($0,10,3))}}' > fastqc_run_bams.sh
chmod +x fastqc_run_bams.sh
./fastqc_run_bams.sh 
ls -l | awk '{print $9}' | awk '{if ($0 ~ /TR_ASMBL/) {printf("fastANI -q TR_ASMBL_%s/contigs.fa -r /home/marius/0WORK/WORK/00_SEQUENCING/REFERENCE_GENOMES/Klebsiella_pneumoniae.fasta -o TR_ASMBL_%s/%s_contigs_species_Kp.tsv\n",substr($0,10,3),substr($0,10,3),substr($0,10,3))}}' > fastANI_species_Kp.sh
ls -l | awk '{print $9}' | awk '{if ($0 ~ /TR_ASMBL/) {printf("fastANI -q TR_ASMBL_%s/contigs.fa -r /home/marius/0WORK/WORK/00_SEQUENCING/REFERENCE_GENOMES/Acinetobacter_baumannii.fasta -o TR_ASMBL_%s/%s_contigs_species_Ab.tsv\n",substr($0,10,3),substr($0,10,3),substr($0,10,3))}}' > fastANI_species_Ab.sh
ls -l | awk '{print $9}' | awk '{if ($0 ~ /TR_ASMBL/) {printf("fastANI -q TR_ASMBL_%s/contigs.fa -r /home/marius/0WORK/WORK/00_SEQUENCING/REFERENCE_GENOMES/Enterobacter_spp.fasta -o TR_ASMBL_%s/%s_contigs_species_Esp.tsv\n",substr($0,10,3),substr($0,10,3),substr($0,10,3))}}' > fastANI_species_Esp.sh
ls -l | awk '{print $9}' | awk '{if ($0 ~ /TR_ASMBL/) {printf("fastANI -q TR_ASMBL_%s/contigs.fa -r /home/marius/0WORK/WORK/00_SEQUENCING/REFERENCE_GENOMES/Enterococcus_faecium.fasta -o TR_ASMBL_%s/%s_contigs_species_Ef.tsv\n",substr($0,10,3),substr($0,10,3),substr($0,10,3))}}' > fastANI_species_Ef.sh
ls -l | awk '{print $9}' | awk '{if ($0 ~ /TR_ASMBL/) {printf("fastANI -q TR_ASMBL_%s/contigs.fa -r /home/marius/0WORK/WORK/00_SEQUENCING/REFERENCE_GENOMES/Escherichia_coli.fasta -o TR_ASMBL_%s/%s_contigs_species_Ec.tsv\n",substr($0,10,3),substr($0,10,3),substr($0,10,3))}}' > fastANI_species_Ec.sh
ls -l | awk '{print $9}' | awk '{if ($0 ~ /TR_ASMBL/) {printf("fastANI -q TR_ASMBL_%s/contigs.fa -r /home/marius/0WORK/WORK/00_SEQUENCING/REFERENCE_GENOMES/Pseudomonas_aeruginosa.fasta -o TR_ASMBL_%s/%s_contigs_species_Pa.tsv\n",substr($0,10,3),substr($0,10,3),substr($0,10,3))}}' > fastANI_species_Pa.sh
ls -l | awk '{print $9}' | awk '{if ($0 ~ /TR_ASMBL/) {printf("fastANI -q TR_ASMBL_%s/contigs.fa -r /home/marius/0WORK/WORK/00_SEQUENCING/REFERENCE_GENOMES/Staphylococcus_aureus.fasta -o TR_ASMBL_%s/%s_contigs_species_Sa.tsv\n",substr($0,10,3),substr($0,10,3),substr($0,10,3))}}' > fastANI_species_Sa.sh
chmod +x fastANI_species_Kp.sh fastANI_species_Ab.sh fastANI_species_Esp.sh fastANI_species_Ef.sh fastANI_species_Ec.sh fastANI_species_Pa.sh fastANI_species_Sa.sh
./fastANI_species_Kp.sh 
./fastANI_species_Ab.sh 
./fastANI_species_Esp.sh 
./fastANI_species_Ef.sh 
./fastANI_species_Ec.sh 
./fastANI_species_Pa.sh 
./fastANI_species_Sa.sh 
ls -l | awk '{print $9}' | awk '{if ($0 ~ /TR_ASMBL/) {printf("mlst TR_ASMBL_%s/contigs.fa > TR_ASMBL_%s/%s_MLST.tsv\n",substr($0,10,3),substr($0,10,3),substr($0,10,3),substr($0,10,3))}}' > MLST.sh
chmod +x MLST.sh
./MLST.sh 
ls -l | awk '{print $9}' | awk '{if ($0 ~ /TR_ASMBL/) {printf("abricate --db ncbi TR_ASMBL_%s/contigs.fa > TR_ASMBL_%s/%s_ABRICATE_rezist.tsv\n",substr($0,10,3),substr($0,10,3),substr($0,10,3))}}' > ABRICATE_resistance.sh
chmod +x ABRICATE_resistance.sh
./ABRICATE_resistance.sh 
ls -l | awk '{print $9}' | awk '{if ($0 ~ /TR_ASMBL/) {printf("abricate --db plasmidfinder TR_ASMBL_%s/contigs.fa > TR_ASMBL_%s/%s_ABRICATE_PlasmidFinder.tsv\n",substr($0,10,3),substr($0,10,3),substr($0,10,3))}}' > ABRICATE_PlasmidFinder.sh
chmod +x ABRICATE_PlasmidFinder.sh
./ABRICATE_PlasmidFinder.sh 
ls -l | awk '{print $9}' | awk '{if ($0 ~ /TR_ASMBL/) {printf("abricate --db vfdb TR_ASMBL_%s/contigs.fa > TR_ASMBL_%s/%s_ABRICATE_VirulenceFactors.tsv\n",substr($0,10,3),substr($0,10,3),substr($0,10,3))}}' > ABRICATE_VirulenceFactors.sh
chmod +x ABRICATE_VirulenceFactors.sh
./ABRICATE_VirulenceFactors.sh 
conda activate prokka
prokka --listdb
ls -l | awk '{print $9}' | awk '{if ($0 ~ /TR_ASMBL/) {printf("prokka --cpus 8 --gcode 11 --rnammer --compliant --centre XXX TR_ASMBL_%s/contigs.fa --outdir TR_ASMBL_%s/PROKKA_output --prefix %s_ANNOTATIONS\n",substr($0,10,3),substr($0,10,3),substr($0,10,3))}}' > PROKKA_run.sh
chmod +x PROKKA_run.sh
./PROKKA_run.sh 
mkdir prokka_all_GFFs_for_Roary
ls -l | awk '{print $9}' | awk '{if ($0 ~ /TR_ASMBL/) {printf("cp TR_ASMBL_%s/PROKKA_output/%s_ANNOTATIONS.gff prokka_all_GFFs_for_Roary/\n",substr($0,10,3),substr($0,10,3))}}' > cp_prokka_GFFs.sh
chmod +x cp_prokka_GFFs.sh
./cp_prokka_GFFs.sh 
conda activate multiqc
ariba prepareref -f /home/marius/0WORK/WORK/00_SEQUENCING/RAW_data/RADAR/all_raws/out.ncbi.fa -m /home/marius/0WORK/WORK/00_SEQUENCING/RAW_data/RADAR/all_raws/out.ncbi.tsv out.ncbi.prepareref &
ls -l | awk '{print $9}' | awk '{if ($0 ~ /TR_ASMBL/) {printf("ariba run out.ncbi.prepareref TR_ASMBL_%s/R1.fq.gz TR_ASMBL_%s/R2.fq.gz TR_ASMBL_%s/ARIBA_output --threads 8 --noclean\n",substr($0,10,3),substr($0,10,3),substr($0,10,3))}}' > ARIBA_run.sh
chmod +x ARIBA_run.sh
./ARIBA_run.sh 
###Urmatoarele predictii:snippy, ParSNP si Roary le voi face in directorul fiecarei specii, dupa ce am copiat acolo folderele TR_ASMBL###
conda deactivate
conda deactivate
conda deactivate
