def join(*block_list):
    """ Concatenate a list of Blocks. """
    return u''.join(map(unicode,block_list))

def stack(*block_list):
    r""" Concatenate a list of Blocks with '\n' """
    return '\n'.join(map(unicode,block_list))
