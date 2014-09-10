# TODO : loose the `indent` keyword for containers and always indent?
# or just keep it as a class field

class Block(object):

    """ Latex base block. """

    template = u'{self.formated_content}'

    #def __init__(self, content=''):
    #    self.content = content
    def __init__(self, content=None):
        self.assign_to_self(content=content)
        
    def assign_to_self(self, **kwargs):
        for k,v in kwargs.iteritems():
            # If it's not None or if we don't already have it anyway
            if v is not None or not hasattr(self, k):
                setattr(self, k, v)
    
    @property
    def formated_content(self):
        return self.content

    def __unicode__(self):
        return self.template.format(self=self)#dict(self.__dict__, **self.__class__.__dict__)

    def __add__(self, other):
        return u'{0}{1}'.format(self, other)

    def __radd__(self, other):
        return u'{0}{1}'.format(other, self)


class Container(Block):

    """ Latex block with the indentation option. """

    template = '{self.before}' '{self.indented_content}' '{self.after}'

    # Change those when subclassing
    before = ''
    after = ''
    indent = True

    def _block_indent(self, content, tab='\t'):
        """ Adds `tab` in front of each line of content. """
        lines = content.split('\n')
        lines = [ tab + l + '\n' for l in lines ]
        return u''.join(lines)[:-1]

    @property
    def indented_content(self):
        if self.indent:
            before = '\n' if self.before != '' else ''
            after = '\n' if self.after != '' else ''
            return before + self._block_indent(unicode(self.content)) + after
        else:
            return u' %s ' % self.content
      
    def __init__(self, content=None):#, indent=True):#content=None, indent=True):
        """ Constructor for Container object.
            
            Arguments
                - content
                    The content.
                - indent (deprecated as a constructor argument) 
                    Tells if we have to indent the `content`, like
                            "before
                                inside
                            after"
                            or not :
                            "before inside after"
                            
        """
        self.assign_to_self(content=content)
        super(Container, self).__init__()

    def __add__(self, other):
        return u'{0}\n{1}'.format(self, other)

    def __radd__(self, other):
        return u'{1}\n{0}'.format(self, other)

class ArgumentError(ValueError):
    pass

class ParseArgsMixin(object):

    """ Argument parsing for Command and Environment. """

    def _format_any_args(self, args, join_char = '}{', container='{%s}'):
        if not args:
            return ''
        elif isinstance(args, (basestring, Block)):
            args = [args]
        args = map(unicode, args)
        args = join_char.join(args)
        return container % args

    @property
    def formated_def_args(self):
        return self._format_any_args(self.def_args, ', ', '[%s]')
        
    @property
    def formated_args(self):
        return self._format_any_args(self.args)

    # work in progress...
    #@property
    #def formated_kwargs(self):
    #    kwargs = self.kwargs
    #    if not isinstance(kwargs, dict):
    #        raise TypeError(
    #            'The kwargs argument of the `formated_kwargs` property must be '
    #            'a dictionary')
        

class Environment(Container, ParseArgsMixin):

    """ Subclass this for latex environments. """
    
    # Set this when subclassing
    name = ''

    @property
    def before(self):
        return ur'\begin{{{self.name}}}' '{self.formated_def_args}' '{self.formated_args}'.format(self=self)

    @property
    def after(self):
        return ur'\end{{{self.name}}}'.format(self=self)


    def __init__(self, content=None, args=None, def_args=None):
        """
            Note : giving a `content` is the same as appending it to `args`
            except that we are going to indent it if `indent`=True
            Arguments:
                content --  The main content. Same as last argument but indented.
                args    --  Arguments, e.g. \begin{env}{arg1}{arg2}
                def_args--  Default arguments for the latex environment, ends up
                            in something like \begin{env}[defarg1, defarg2]...
        """
        #self.args = self.parse_args(args)
        #self.def_args = self.parse_def_args(def_args)
        self.assign_to_self(
                def_args=def_args,
                args=args,
                )
        super(Environment, self).__init__(content)#, indent)


class Command(Block, ParseArgsMixin):

    r""" Subclass this for latex commands. """
    
    # Set this when subclassing
    name = ''

    template = ur'\{self.name}' '{self.formated_def_args}' '{self.formated_args}'

    def __init__(self, args=None, def_args=None):
        self.assign_to_self(args=args, def_args=def_args)
