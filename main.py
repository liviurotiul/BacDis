'''
This is the entry point for the app
'''

import os
import tempfile
from app.stage1 import *


# Provide paths
DATABASE_PATH = "./database"
QUERRY_DATA_PATH = "./querry_data_temp"
REFERENCE_GENOMES = "./reference_genomes"
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

    data_path = os.path.join(QUERRY_DATA_PATH, data)

    # if len(os.listdir(data_path)) != 2:
    #     raise RuntimeError("Each sample folder must have exactly 2 files for paired reads")

    tempdirname = "./querry_data_temp/547_S1_ME_L001"

    # WARNING: the names of the fastq files sould be identical except for the R1/R2
    # R1_path = os.path.join(tempdirname, os.listdir(tempdirname)[0])
    # R2_path = os.path.join(tempdirname, os.listdir(tempdirname)[1])

    # Perform quality control b4 assembly
    # fastqc_run_fastq(tempdirname, R1_path, R2_path)

    # # Run assembly
    # shovil_run(tempdirname, R1_path, R2_path)

    reference_genomes_paths = find_extension(REFERENCE_GENOMES, ".fasta")
    import pdb;pdb.set_trace()
    # Run FastANI
    for reference_genome in reference_genomes_paths:
        FastANI(tempdirname, reference_genome, os.path.join(tempdirname, "shovil", "contigs.fasta"))

    import pdb;pdb.set_trace()

    # # Work in a temporary folder
    # with tempfile.TemporaryDirectory() as tempdirname:

    #     # Copy the files to the temp folder
    #     os.system("cp " + data_path+"/* " + tempdirname)

    #     # WARNING: the names of the fastq files sould be identical except for the R1/R2
    #     R1_path = os.path.join(tempdirname, os.listdir(tempdirname)[0])
    #     R2_path = os.path.join(tempdirname, os.listdir(tempdirname)[1])

    #     # Perform quality control b4 assembly
    #     fastqc(tempdirname, R1_path, R2_path)

    #     # Run assembly
    #     shovil(tempdirname, R1_path, R2_path)

    #     import pdb;pdb.set_trace()


        