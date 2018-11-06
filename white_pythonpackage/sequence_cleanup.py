import dendropy

def sequence_cleanup(sequence_set, out_file):
'''pick out a specific sequence and write it as a fasta file'''
# check that we have a file and that it's in the right format
# make sure the taxon is present; Let's do this one
# make sure the gene is present
    assert sequence_set(taxon)
    my_taxon_sequence = sequence_set[taxon].symbols_as_strings()
    my_taxon_sequence[int(gene[0]) : int(gene[1])]
    my_taxon_sequence.to_path (out_file, 'fasta')
    ofile = open(outfile, "w")
    ofile.write(">" + taxon + "\n" + my_taxon_sequence + "\n")
    ofile.close()
#Verify that the output is not size zero
    assert os.stat(out_file).st_size != 0