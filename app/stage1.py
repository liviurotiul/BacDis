'''
This file describes the the tools used to build the database
ASSEMBLING READS
MLST
PHILOGENY
'''

import os

def shovil_run(work_path_dir: str, R1_path: str, R2_path: str) -> None:

    os.system("shovill  --keepfiles --trim --outdir {outdir} --R1 {R1} --R2 {R2}".format(outdir=os.path.join(work_path_dir, "shovill"), 
                                                                                        R1=R1_path,
                                                                                        R2=R2_path))

def fastqc_run_fastq(work_path_dir: str, R1_path: str, R2_path: str) -> None:

    os.system("mkdir {work_path}/fastqc_b4".format(work_path=work_path_dir))
    os.system("fastqc --outdir {outdir} {R1} {R2}".format(outdir=os.path.join(work_path_dir, "fastqc_b4"),
                                                                                R1=R1_path,
                                                                                R2=R2_path))

def fastqc_run_bam(work_path_dir: str, bam_path: str) -> None:

    os.system("mkdir {work_path}/fastqc_after".format(work_path=work_path_dir))
    os.system("fastqc --outdir {outdir} {bam}".format(outdir=os.path.join(work_path_dir, "fastqc_after"),
                                                        bam=bam_path))

def FastANI(work_path_dir: str, reference_path: str, contigs_path: str) -> None:
    
    os.system("mkdir {work_path}/fastANI".format(work_path=work_path_dir))
    os.system("fastANI -q {contigs_path} -r {reference_path} -o {outdir}".format(contigs_path=contigs_path,
                                                                                reference_path=reference_path,
                                                                                outdir=os.path.join(work_path_dir, "fastANI")))

def find_extension(search_path: str, extention: str) -> list:

    list_of_files = []

    for path, currentDirectory, files in os.walk(search_path):
        for file in files:
            print(file)
            if file.endswith(extention):
                list_of_files.append(file)
    
    return list_of_files


