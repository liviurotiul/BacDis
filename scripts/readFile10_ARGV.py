import os
import sys
import numpy as np

#print ('Name', '\t', 'No.of_contigs', '\t', '1st_Contig', '\t', '1st_C_len', '\t', '1st_C_cov', '\t', 'Species', '\t', 'ST', '\t', 'STgene1', '\t', 'STgene2', '\t', 'STgene3', '\t', 'STgene4', '\t', 'STgene5', '\t', 'STgene6', '\t', 'STgene7', '\t', 'Sp.i.Ef.ANI', '\t', 'Sp.i.Ef.mapped', '\t', 'Sp.i.Ef.TotQueryFrag', '\t', 'Sp.i.Sa.ANI', '\t', 'Sp.i.Sa.mapped', '\t', 'Sp.i.Sa.TotQueryFrag', '\t', 'Sp.i.Kp.ANI', '\t', 'Sp.i.Kp.mapped', '\t', 'Sp.i.Kp.TotQueryFrag', '\t', 'Sp.i.Ab.ANI', '\t', 'Sp.i.Ab.mapped', '\t', 'Sp.i.Ab.TotQueryFrag', '\t', 'Sp.i.Pa.ANI', '\t', 'Sp.i.Pa.mapped', '\t', 'Sp.i.Pa.TotQueryFrag', '\t', 'Sp.i.Esp.ANI', '\t', 'Sp.i.Esp.mapped', '\t', 'Sp.i.Esp.TotQueryFrag', '\t', 'Sp.i.Ec.ANI', '\t', 'Sp.i.Ec.mapped', '\t', 'Sp.i.Ec.TotQueryFrag', '\t', 'PF_contigNo.', '\t', 'PF_start', '\t', 'PF_end', '\t', 'PF_gene', '\t', 'PF_%Cov', '\t', 'PF_%ID', '\t', 'PF_AccNo.', '\t', 'PF_Product', '\t', 'RES_contigNo.', '\t', 'RES_start', '\t', 'RES_end', '\t', 'RES_gene', '\t', 'RES_%Cov', '\t', 'RES_%ID', '\t', 'RES_AccNo.', '\t', 'RES_Product', '\t', 'ARB_gene', '\t', 'ARB_flag', '\t', 'ARB_reads', '\t', 'ARB_PcID', '\t', 'ARB_CtgLen', '\t', 'ARB_CtgCov', '\t', 'ARB_change', '\t', 'ARB_effect', '\t', 'ARB_CtgStart', '\t', 'ARB_CtgEnd', '\t', 'ARB_Product', '\t', 'VIR_contigNo', '\t', 'VIR_start', '\t', 'VIR_end', '\t', 'VIR_gene', '\t', 'VIR_%Cov', '\t', 'VIR_%ID', '\t', 'VIR_AccNo.', '\t', 'VIR_Product')

"""
************************************************************************************************************
*** Search for the given string in file and return lines containing that string, along with line numbers ***
************************************************************************************************************
"""
def search_string_in_file(file_name, string_to_search):
    line_number = 0
    list_of_results = []
    # Open the file in read only mode
    with open(file_name, 'r') as read_obj:
        # Read all lines in the file one by one
        for line in read_obj:
            # For each line, check if line contains the string
            line_number += 1
            if string_to_search in line:
                # If yes, then add the line number & line as a tuple in the list
                list_of_results.append((line_number, line.rstrip()))
    # Return list of tuples containing line numbers and lines where string is found
    return list_of_results

with open(sys.argv[2], 'r') as fisierB:
    for line in open(sys.argv[2]):
        column1split = line.split('/')
        if len(column1split) > 0:
            print (column1split[0], end="\t")


"""
###################################
#### READING "contigs.fa" FILE ####
###################################
"""
matched_lines = search_string_in_file(sys.argv[1], '>')
#print('Total no. of contigs: ', len(matched_lines), end="\t")
print(len(matched_lines), end="\t")

#for element in matched_lines:
#    print('Line Number = ', element[0], ' :: Line = ', element[1])  # prints each contig header line


with open(sys.argv[1], 'r') as fisierA:
#    for line in filecontent: pass
#    print (first_line)        # prints first line
#    print (line)              # prints last line
    
    for line in open(sys.argv[1]):
        columns = line.split() # split line into parts. Other (than "space") separators can be specified
        if len(columns) > 1:   # if there are at least 2 columns
            if columns[0]=='>contig00001':
                print (columns[0], '\t', columns[1], '\t', columns[2], end="\t") # print column 2 of each line


"""
#################################
#### READING "MLST.tsv" FILE ####
#################################
"""
with open(sys.argv[2], 'r') as fisierB:
    for line in open(sys.argv[2]):
        columns = line.split()
        if len(columns) < 4:
            print ("No_MLST_found", '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#')
        elif len(columns) > 4:
            print (columns[1], '\t', columns[2], '\t', columns[3], '\t', columns[4], '\t', columns[5], '\t', columns[6], '\t', columns[7], '\t', columns[8], '\t', columns[9], '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#')


"""
#################################
#### READING "Species" FILES ####
#################################
"""
with open(sys.argv[2], 'r') as fisierB:
    for line in open(sys.argv[2]):
        column1split = line.split('/')
        if len(column1split) > 0:
            print (column1split[0], end="\t")

if os.stat(sys.argv[3]).st_size == 0:     # check if the file is empty
    print('#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '0', '\t', '0', '\t', '0', end="\t")
else:                                   # if not, do this
    with open(sys.argv[3], 'r') as fisierC, open(sys.argv[2], 'r') as fisierB:
        for line in open(sys.argv[3]):
            columns = line.split()
            for line in open(sys.argv[2]):
                columnSpeciesST = line.split()
            if len(columns) > 1 and len(columnSpeciesST) < 4:
                print ('#', '\t', '#', '\t', '#', '\t', '#', '\t', "No_MLST_found", '\t', "No_ST_found", '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', columns[2], '\t', columns[3], '\t', columns[4], end="\t")
            elif len(columns) > 1 and len(columnSpeciesST) > 4:
                print ('#', '\t', '#', '\t', '#', '\t', '#', '\t', columnSpeciesST[1], '\t', columnSpeciesST[2], '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', columns[2], '\t', columns[3], '\t', columns[4], end="\t")

if os.stat(sys.argv[4]).st_size == 0:
    print('0', '\t', '0', '\t', '0', end="\t")
else:                                   
    with open(sys.argv[4], 'r') as fisierD:
        for line in open(sys.argv[4]):
            columns = line.split()
            if len(columns) > 1:
                print (columns[2], '\t', columns[3], '\t', columns[4], end="\t")

if os.stat(sys.argv[5]).st_size == 0:
    print('0', '\t', '0', '\t', '0', end="\t")
else:                                   
    with open(sys.argv[5], 'r') as fisierE:
        for line in open(sys.argv[5]):
            columns = line.split()
            if len(columns) > 1:
                print (columns[2], '\t', columns[3], '\t', columns[4], end="\t")

if os.stat(sys.argv[6]).st_size == 0:
    print('0', '\t', '0', '\t', '0', end="\t")
else:                                   
    with open(sys.argv[6], 'r') as fisierF:
        for line in open(sys.argv[6]):
            columns = line.split()
            if len(columns) > 1:
                print (columns[2], '\t', columns[3], '\t', columns[4], end="\t")

if os.stat(sys.argv[7]).st_size == 0:
    print('0', '\t', '0', '\t', '0', end="\t")
else:                                   
    with open(sys.argv[7], 'r') as fisierG:
        for line in open(sys.argv[7]):
            columns = line.split()
            if len(columns) > 1:
                print (columns[2], '\t', columns[3], '\t', columns[4], end="\t")

if os.stat(sys.argv[8]).st_size == 0:
    print('0', '\t', '0', '\t', '0', end="\t")
else:                                   
    with open(sys.argv[8], 'r') as fisierH:
        for line in open(sys.argv[8]):
            columns = line.split()
            if len(columns) > 1:
                print (columns[2], '\t', columns[3], '\t', columns[4], end="\t")

if os.stat(sys.argv[9]).st_size == 0:
    print('0', '\t', '0', '\t', '0', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#')
else:                                   
    with open(sys.argv[9], 'r') as fisierI:
        for line in open(sys.argv[9]):
            columns = line.split()
            if len(columns) > 1:
                print (columns[2], '\t', columns[3], '\t', columns[4], '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#')


"""
#################################
##### READING PLASMIDg FILE #####
#################################
"""
with open(sys.argv[10], 'r') as fisierJ, open(sys.argv[2], 'r') as fisierB:
    count = len(open(sys.argv[10]).readlines(  ))
    for line in open(sys.argv[10]):
        columns = line.split('\t') # split line into parts. Other (than "space") separators can be specified
        for line in open(sys.argv[2]):
            column1split = line.split('/')
        for line in open(sys.argv[2]):
            columnSpeciesST = line.split()
#        gene_length = np.substract(columns[3],columns[2])
#        print (gene_length)
        if len(columns) > 1 and len(columnSpeciesST) < 4:   # if there are at least 2 columns
            if columns[0]!='#FILE':
                print (column1split[0], '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t' "No_MLST_found", '\t', "No_ST_found", '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', columns[1], '\t', columns[2], '\t', columns[3], '\t', columns[4], '\t', columns[8], '\t', columns[9], '\t', columns[11], '\t', columns[12][:-1], '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#') # print columns of interest
            elif count == 1:
                print(column1split[0], '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', "No_MLST_found", '\t', "No_ST_found", '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '0', '\t', '0', '\t', '0', '\t', '0', '\t', '0', '\t', '0', '\t', '0', '\t', '0', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#')
        elif len(columns) > 1 and len(columnSpeciesST) > 4:   # if there are at least 2 columns
            if columns[0]!='#FILE':
                print (column1split[0], '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', columnSpeciesST[1], '\t', columnSpeciesST[2], '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', columns[1], '\t', columns[2], '\t', columns[3], '\t', columns[4], '\t', columns[8], '\t', columns[9], '\t', columns[11], '\t', columns[12][:-1], '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#') # print columns of interest
            elif count == 1:
                print(column1split[0], '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', columnSpeciesST[1], '\t', columnSpeciesST[2], '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '0', '\t', '0', '\t', '0', '\t', '0', '\t', '0', '\t', '0', '\t', '0', '\t', '0', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#')


"""
#################################
#### READING REZISTANCE FILE ####
#################################
"""
with open(sys.argv[11], 'r') as fisierK, open(sys.argv[2], 'r') as fisierB:
    count = len(open(sys.argv[11]).readlines(  ))
    for line in open(sys.argv[11]):
        columns = line.split('\t') # split line into parts. Other (than "space") separators can be specified
        for line in open(sys.argv[2]):
            column1split = line.split('/')
        for line in open(sys.argv[2]):
            columnSpeciesST = line.split()
        if len(columns) > 1 and len(columnSpeciesST) < 4:   # if there are at least 2 columns
            if columns[0]!='#FILE':
                print (column1split[0], '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', "No_MLST_found", '\t', "No_ST_found", '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', columns[1], '\t', columns[2], '\t', columns[3], '\t', columns[4], '\t', columns[8], '\t', columns[9], '\t', columns[11], '\t', columns[12][:-1], '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#') # print columns of interest
            elif count == 1:
                print(column1split[0], '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', "No_MLST_found", '\t', "No_ST_found", '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '0', '\t', '0', '\t', '0', '\t', '0', '\t', '0', '\t', '0', '\t', '0', '\t', '0', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#')
        elif len(columns) > 1 and len(columnSpeciesST) > 4:   # if there are at least 2 columns
            if columns[0]!='#FILE':
                print (column1split[0], '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', columnSpeciesST[1], '\t', columnSpeciesST[2], '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', columns[1], '\t', columns[2], '\t', columns[3], '\t', columns[4], '\t', columns[8], '\t', columns[9], '\t', columns[11], '\t', columns[12][:-1], '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#') # print columns of interest
            elif count == 1:
                print(column1split[0], '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', columnSpeciesST[1], '\t', columnSpeciesST[2], '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '0', '\t', '0', '\t', '0', '\t', '0', '\t', '0', '\t', '0', '\t', '0', '\t', '0', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#')


"""
#################################
####### READING ARIBA FILE ######
#################################
"""
with open(sys.argv[12], 'r') as fisierL, open(sys.argv[2], 'r') as fisierB:
    count = len(open(sys.argv[12]).readlines(  ))
    for line in open(sys.argv[12]):
        columns = line.split('\t') # split line into parts. Other (than "space") separators can be specified
        for line in open(sys.argv[2]):
            column1split = line.split('/')
        for line in open(sys.argv[2]):
            columnSpeciesST = line.split()
        if len(columns) > 1 and len(columnSpeciesST) < 4:   # if there are at least 2 columns
            if columns[0]!='#ariba_ref_name':
                print (column1split[0], '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', "No_MLST_found", '\t', "No_ST_found", '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', columns[1], '\t', columns[4], '\t', columns[5], '\t', columns[9], '\t', columns[11], '\t', columns[12], '\t', columns[18], '\t', columns[19], '\t', columns[23], '\t', columns[24], '\t', columns[30][:-1], '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#') # print columns of interest
            elif count == 1:
                print(column1split[0], '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', "No_MLST_found", '\t', "No_ST_found", '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '0', '\t', '0', '\t', '0', '\t', '0', '\t', '0', '\t', '0', '\t', '0', '\t', '0', '\t', '0', '\t', '0', '\t', '0', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#')
        elif len(columns) > 1 and len(columnSpeciesST) > 4:   # if there are at least 2 columns
            if columns[0]!='#ariba_ref_name':
                print (column1split[0], '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', columnSpeciesST[1], '\t', columnSpeciesST[2], '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', columns[1], '\t', columns[4], '\t', columns[5], '\t', columns[9], '\t', columns[11], '\t', columns[12], '\t', columns[18], '\t', columns[19], '\t', columns[23], '\t', columns[24], '\t', columns[30][:-1], '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#') # print columns of interest
            elif count == 1:
                print(column1split[0], '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', columnSpeciesST[1], '\t', columnSpeciesST[2], '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '0', '\t', '0', '\t', '0', '\t', '0', '\t', '0', '\t', '0', '\t', '0', '\t', '0', '\t', '0', '\t', '0', '\t', '0', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#')


"""
##################################
##### READING VIRULENCE FILE #####
##################################
"""
with open(sys.argv[13], 'r') as fisierM, open(sys.argv[2], 'r') as fisierB:
    count = len(open(sys.argv[13]).readlines(  ))
    for line in open(sys.argv[13]):
        columns = line.split('\t') # split line into parts. Other (than "space") separators can be specified
        for line in open(sys.argv[2]):
            column1split = line.split('/')
        for line in open(sys.argv[2]):
            columnSpeciesST = line.split()
        if len(columns) > 1  and len(columnSpeciesST) < 4:   # if there are at least 2 columns
            if columns[0]!='#FILE':
                print (column1split[0], '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', "No_MLST_found", '\t', "No_ST_found", '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', columns[1], '\t', columns[2], '\t', columns[3], '\t', columns[4], '\t', columns[8], '\t', columns[9], '\t', columns[11], '\t', columns[12][:-1]) # print columns of interest
            elif count == 1:
                print(column1split[0], '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', "No_MLST_found", '\t', "No_ST_found", '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '0', '\t', '0', '\t', '0', '\t', '0', '\t', '0', '\t', '0', '\t', '0', '\t', '0')
        elif len(columns) > 1  and len(columnSpeciesST) > 4:   # if there are at least 2 columns
            if columns[0]!='#FILE':
                print (column1split[0], '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', columnSpeciesST[1], '\t', columnSpeciesST[2], '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', columns[1], '\t', columns[2], '\t', columns[3], '\t', columns[4], '\t', columns[8], '\t', columns[9], '\t', columns[11], '\t', columns[12][:-1]) # print columns of interest
            elif count == 1:
                print(column1split[0], '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', columnSpeciesST[1], '\t', columnSpeciesST[2], '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '#', '\t', '0', '\t', '0', '\t', '0', '\t', '0', '\t', '0', '\t', '0', '\t', '0', '\t', '0')


