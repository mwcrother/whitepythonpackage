import dendropy
import os.path

def sequence_reader(filepath):
    #check that file exists or that file path is correct
    assert os.path.exists(filepath)
    sequence_set = dendropy.DnaCharacterMatrix.get(
        path=filepath,
        schema='phylip'
     
    #check the return type. should be dendropy character matrix
    assert type(sequence_set) == dendropy.datamodel.charmatrixmodel.DnaCharacterMatrix
    return(sequence_set)
    