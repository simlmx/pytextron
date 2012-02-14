# TODO : Organize those in more clever files

from pytextron.base import Command, Environment

class Document(Environment):
    name = 'document'

class PageBreak(Command):
    template = r'\pagebreak'

class Usepackage(Environment):
    name = 'usepackage'

class Center(Environment):
    name = 'center'


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

