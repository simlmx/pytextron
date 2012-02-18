# TODO : test for this
def concatenate(*block_list):
    """ Concatenate a list of Blocks. """
    return reduce(lambda x,y : x+y, block_list)

from document import *
