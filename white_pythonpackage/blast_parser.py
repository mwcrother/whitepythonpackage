from Bio.Blast import NCBIXML
'''
This function parses the results from a blast search. 
    It prints only results with <0.04 E value.
    It prints the e value and the length of the returned sequence for each hit 
    It shows each sequence aligned with the query sequence
    
    Parameter
    ---------
    arg1 results path path to results file (xml default)
    '''

def blast_parser(results_path):
    path=results_path
    result_handle = open(results_path)
    blast_record = NCBIXML.read(result_handle)
    
    E_VALUE_THRESH = 0.04
    
    for alignment in blast_record.alignments:
         for hsp in alignment.hsps:
            if hsp.expect < E_VALUE_THRESH:
                print("****Alignment****")
                print("sequence:", alignment.title)
                print("length:", alignment.length)
                print("e value:", hsp.expect)
                print(hsp.query[0:75] + "...")
                print(hsp.match[0:75] + "...")
                print(hsp.sbjct[0:75] + "...")