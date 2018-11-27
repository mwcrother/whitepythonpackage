from Bio.Blast import NCBIWWW
from Bio import SeqIO
import os

'''
Reads a fasta file and runs a Blast search at NCBI
   Writes a Blast search to specified file with xml being the default
    
    Parameters
    ----------
    
    arg1 fastapath   path to fasta file
    arg2 results path  path to where the results file should be written
    
    Output: Blast file in xml format
    '''
def sequence_blaster(fasta_path, results_path):
    #check file format-- you don't have to do this because SeqIO.read does this test as the first line of code
   
    record = SeqIO.read(fasta_path, format="fasta")
    result_handle = NCBIWWW.qblast("blastn", "nt", record.format("fasta"))

    save_file = open(results_path, 'w')
    save_file.write(result_handle.read())
    save_file.close()
 #check that the results file in not size zero
    #assert os.stat(results_path).st_size != 0