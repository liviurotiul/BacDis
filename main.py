'''
This is the entry point for the app
'''

import os
import tempfile
from app.stage1 import *


# Provide paths
DATABASE_PATH = "./database"
# QUERRY_DATA_PATH = "./querry_data_temp" # For testing
QUERRY_DATA_PATH = "./querry_data"
REFERENCE_GENOMES_PATH = "./reference_genomes"
STORE_DATA = True


# Check for errors
if not os.path.exists(QUERRY_DATA_PATH):
    raise RuntimeError("The folder that contains the querry sequence does not exist")

if len(os.listdir(QUERRY_DATA_PATH)) == 0:
    raise RuntimeError("No querry sequences found")

# if len(os.listdir(DATABASE_PATH)) == 0:
#     raise RuntimeError("No database found")

#==============================================================================================
# Begin the pipline
#==============================================================================================

querry_data = os.listdir(QUERRY_DATA_PATH)

for data in querry_data:

    # Work in a temporary folder
    with tempfile.TemporaryDirectory() as tempdirname:

        # Copy the files to the temp folder
        data_path = os.path.join(QUERRY_DATA_PATH, data)

        os.system("cp " + data_path+"/* " + tempdirname)

        reference_genomes = os.listdir(os.path.join(REFERENCE_GENOMES_PATH, "fastas"))

        # WARNING: the names of the fastq files sould be identical except for the R1/R2
        R1_path = os.path.join(tempdirname, os.listdir(tempdirname)[0])
        R2_path = os.path.join(tempdirname, os.listdir(tempdirname)[1])

        # Perform quality control b4 assembly
        fastqc_run_fastq(tempdirname, R1_path, R2_path)

        # Run assembly
        shovill_run(tempdirname, R1_path, R2_path)

        contigs_path = os.path.join(tempdirname, "shovill", "contigs.fasta")

        # Run FastANI
        for reference_genome in reference_genomes:
            FastANI(
                tempdirname,
                os.path.join(REFERENCE_GENOMES_PATH, "fastas", reference_genome),
                contigs_path
            )

        # Run MLST
        mlst_run(tempdirname, contigs_path)

        




        