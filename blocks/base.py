class Block(object):

    """ Latex base block. 
        
    """

    template = u'%(content)s'

    def __init__(self, content=''):
        self.content = content

    def __unicode__(self):
        return self.template % self.__dict__

    def __add__(self, other):
        return u'%s %s' % (self, other)

def block_indent(content, tab = '    '):
    """ Adds `tab` in front of each line of content. """
    lines = content.split(endl)
    lines = [ tab + l + endl for l in lines[:-1] ] + lines[-1:]
    return u''.join(lines)

class Container(Block):

    """ Latex block with the indentation option. """

    # Subclass and change for something like ur'\begin{foo}%(content)s%(smthng)s\end{foo}'
    # If content = 'bar', __unicode__ will return
    # \begin{foo} bar \end{foo} or 
    # \begin{foo}
    #     bar
    # \end{foo}
    # depending whether indent is False or True
    template = u'%(content)s'

    def __init__(self, content='', indent=True):
        """ Constructor for Container object.
            
            Arguments
            indent -- If we indent the inside, like
                "before
                    inside
                after"
                or not :
                "before inside after"
        """

        #self.content = content
        if indent:
            content = '\n%s\n' % block_indent(content)
        
        self.content = content

class ParseArgsMixin(object):

    """ Argument parsing for Command and Environment. """

    def _parse(args, template = '[%s]'):
        if args is None:
            args = ''
        elif isinstance(args, basestring):
            args = [args]
        args = ', '.join(args)
        return template % options if options else ''

    def parse_def_args(self, args):
        return _parse(args)

    def parse_args(self, args):
        return _parse(args, '{%s}')

        

class Environment(Container, ParseArgsMixin):

    """ Subclass this for latex environments. """
    
    # Set this when subclassing
    name = ''
    template = ur'\begin{%(name)s}' '%(def_args)s' '%(args)s' '%(content)s' ur'\end{%(name)s}'

    def __init__(self, content='', indent=True, def_args=None, args=None):
        super(Environment, self).__init__(content, indent)
        self.args = parse_args(args)
        self.def_args = parse_def_args(def_args)

class Command(Block, ParseArgsMixin):

    r""" Subclass this for latex commands. """
    
    # Set this when subclassing
    name = ''
    template = ur'\%(name)s' '%(def_args)s' '%(args)s' '{%(content)s}'

    def __init__(self, content='', def_args=None, args=None):
        super(Command, self).__init__(content)
        self.args = self.parse_args(args)
        self.def_args = self.parse_def_args(def_args)
