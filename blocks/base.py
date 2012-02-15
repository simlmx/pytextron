class Block(object):

    """ Latex base block. """

    template = u'%(content)s'

    def __init__(self, content=''):
        self.content = content

    def __unicode__(self):
        return self.template % dict(self.__dict__, **self.__class__.__dict__)

    def __add__(self, other):
        return u'%s %s' % (self, other)

    def __radd__(self, other):
        return u'%s %s' % (other, self)


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
    tab = '\t'

    def _block_indent(self, content, tab=None):
        """ Adds `tab` in front of each line of content. """
        if tab is None:
            tab = self.tab
        endl = '\n'
        lines = content.split(endl)
        lines = [ tab + l + endl for l in lines ]
        return u''.join(lines)[:-1]
      
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
        if indent:
            content = '\n%s\n' % self._block_indent(unicode(content))
        else:
            content = u' %s ' % content
        self.content = content

class ParseArgsMixin(object):

    """ Argument parsing for Command and Environment. """

    def parse_def_args(self, args):
        if args is None:
            args = ''
        elif isinstance(args, basestring):
            args = [args]
        args = ', '.join(args)
        return '[%s]' % args if args else ''

    def parse_args(self, args):
        if args is None:
            args = ''
        elif isinstance(args, basestring):
            args = [args]
        args = '}{'.join(args)
        if args:
            args = '{%s}' % args
        return args

        

class Environment(Container, ParseArgsMixin):

    """ Subclass this for latex environments. """
    
    # Set this when subclassing
    name = ''
    template = ur'\begin{%(name)s}' '%(def_args)s' '%(args)s' '%(content)s' ur'\end{%(name)s}'

    def __init__(self, content='', indent=True, def_args=None, args=None):
        """
            Note : giving a `content` is the same as appending it to `args`
            except that we are going to indent it if `indent`=True
        """
        super(Environment, self).__init__(content, indent)
        self.args = self.parse_args(args)
        self.def_args = self.parse_def_args(def_args)

class Command(Block, ParseArgsMixin):

    r""" Subclass this for latex commands. """
    
    # Set this when subclassing
    name = ''
    template = ur'\%(name)s' '%(def_args)s' '%(args)s'

    def __init__(self, args=None, def_args=None):
        self.args = self.parse_args(args)
        self.def_args = self.parse_def_args(def_args)
