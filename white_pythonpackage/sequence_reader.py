import dendropy
import os

''' 
Reads in a DNA matrix in phylip format
    Check to make sure the path actually exists
    
    Parameters:
    Arg1 = filepath
    
    Return the sequence as a phylip file
    '''
     
def sequence_reader(filepath):
    assert os.path.exists(filepath) 
    sequence_set = dendropy.DnaCharacterMatrix.get(
    path=filepath,
    schema="phylip"
)
    assert type(sequence_set) == dendropy.datamodel.charmatrixmodel.DnaCharacterMatrix
    return(sequence_set)
