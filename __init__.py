def concatenate(block_list):
    """ Concatenate a list of Blocks. """
    return reduce(lambda x,y : x+y, block_list)
