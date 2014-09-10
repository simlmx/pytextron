# TODO : Organize those in more clever files

import sys
from base import Command, Environment, Container

# Some environments and commands where we only have ton 
# inherit and not subclass any fields/methods

# There aren't many right now but I feel there is going to be more of those
simple_environments = (
'document',
'center',
)

simple_commands = (
'documentclass', 'usepackage',
)

def _subclass(name, base_class):
    namecap = name.capitalize()
    module = sys.modules[__name__]
    setattr(module, namecap, type(namecap, (base_class,), {'name' : name}))

for name in simple_environments:
    _subclass(name, Environment)

for name in simple_commands:
    _subclass(name, Command)


# Section, subsection, subsubsection
class Section(Environment):

    _name = 'section'

    def __init__(self, title, content, numbering=True):
        r"""
            \begin{section*}{title}
                content
            \end{section*}

            The star is there only if `show_numbering` is False
        """
        super(Section, self).__init__(content, title)
        self.numbering = numbering

    @property
    def name(self):
        return self._name + ('' if self.numbering else '*')

class Subsection(Section):
    _name = 'subsection'

class Subsubsection(Section):
    _name = 'subsubsection'


class PageBreak(Command):
    template = r'\pagebreak'


# Equations
class Eq(Container):
    indent = False
    before = after = '$'

class DisplayEq(Container):
    indent = False
    before = after = '$$'

# Math

#class Sqrt(Command):
#    name = 'sqrt'
#
#class Frac(Command):
#    name = 'frac'

if 0 :
    endl = u'\n'
    class Tabular(Block):
        """
        Simple tabular
        TODO : It's a bit too simple :P
        """
        def __init__(self, matrix, col_type = 'c', borders=True):
            """ `matrix` : 2d iterable """
    
            print 'TODO : In tabular, change Block for Container'
    
            nbrow = len(matrix)
            nbcol = len(matrix[0])
    
            if borders:
                cols = '|' + '|'.join([col_type]*nbcol) + '|'
            else:
                cols = col_type*nbcol
                
    
            s = ur'\begin{tabular}{' + cols + ur'}' + endl
    
            middle = ''
            if borders:
                middle += r'\hline' + endl
            for row in matrix:
                middle += u' & '.join(map(unicode, row)) + ur'\\' + endl
                if borders:
                    middle += r'\hline' + endl
            middle = indent(middle)
    
            s += middle
            s += ur'\end{tabular}'
    
            self.latex_code = s
    
        def __unicode__(self):
            return self.latex_code

