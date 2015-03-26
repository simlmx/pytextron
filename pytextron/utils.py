import os

def join(block_list):
    """ Concatenate a list of Blocks. """
    return u''.join(map(unicode,block_list))

def stack(block_list):
    r""" Concatenate a list of Blocks with '\n' """
    return u'\n'.join(map(unicode,block_list))

def ask_before_overwrite(filename):
    """ if `filename` already exists, will prompt before overwriting """
    if os.path.exists(filename):
        while True:
            choice = raw_input(u"The file {} already exists. Overwrite? (Y/N)".format(filename))
            if choice == 'Y':
                return True
            elif choice == 'N':
                return False
    else:
        return True
