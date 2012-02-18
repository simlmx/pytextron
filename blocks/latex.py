# TODO : Organize those in more clever files

from base import Command, Environment, Container

class Document(Environment):
    name = 'document'

class PageBreak(Command):
    template = r'\pagebreak'

class Usepackage(Command):
    name = 'usepackage'

class Center(Environment):
    name = 'center'

class Eq(Container):
    indent = False
    before = after = '$'

class DisplayEq(Container):
    indent = False
    before = after = '$$'

# Math
# 
# class Sqrt(Command):
#     name = 'sqrt'
#     min_args = 1
# 
# class Frac(Command):
#     name = 'frac'
#     min_args = 2

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

