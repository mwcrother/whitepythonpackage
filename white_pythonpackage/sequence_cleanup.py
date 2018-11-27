import dendropy
import os
''' 
Takes a phylip file and subsets a specific taxon and gene (as desired)
    Converts it to a string so it can be saved as a fast file
    
    Parameters
    ----------
    
    Arg1 name of the file
    Arg2 path to the file
    Arg3 taxon to be subset
    Arg4 start of gene sequence in string
    Arg5 end of gene sequence in string
    
    Returns
    -------
    fasta file
'''
def sequence_cleanup(sequence_set, out_file, taxon, gene_start, gene_end):
    '''pick out a specific sequence and write it as a fasta file'''
# check that we have a file and that it's in the right format
# make sure the taxon is present; Let's do this one
# make sure the gene is present
    #assert sequence_set(taxon)
    my_taxon_sequence = sequence_set[taxon].symbols_as_string()
    my_taxon_gene = my_taxon_sequence[gene_start : gene_end]
    #my_taxon_sequence.to_path(out_file, 'fasta')
    ofile = open(out_file, "w")
    ofile.write(">" + taxon + "\n" + my_taxon_gene + "\n")
    ofile.close()
#Verify that the output is not size zero
    assert os.stat(out_file).st_size != 0