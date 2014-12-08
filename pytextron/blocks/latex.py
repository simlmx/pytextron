# TODO : Organize those in more clever files

import sys
from base import CommandBase, Environment, Container

# Some environments and commands where we only have to
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
    _subclass(name, CommandBase)


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


class PageBreak(CommandBase):
    template = r'\pagebreak'


# Equations
class Eq(Container):
    indent = False
    before = after = '$'

class DisplayEq(Container):
    indent = False
    before = after = '$$'


class TableBase(Environment):
    name = ''

    def __init__(self, content):
        """ `content` : list of list of strings
            example : [[1,2,3],[3,4,5]] will become
            \begin{align*}
                1 & 2 & 3 \\
                3 & 4 & 5 \\
            \end{align*}
        """
        self.data = content

    @property
    def content(self):
        return (r' \\' '\n').join(
            [u' & '.join(map(unicode, row)) for row in self.data])


class Align(TableBase):
    # TODO test
    name = 'align*'


class Matrix(TableBase):
    # TODO test
    name = 'matrix'

class Cases(TableBase):
    # TODO
    name = 'cases'


class Tabular(Environment):
    """
    Simple tabular
    TODO : It's a bit too simple :P
    """
    name = 'tabular'

    def __init__(self, content, col_def = '', hlines='all'):
        """ `content` : 2d iterable with the content of each cell
            `col_def` : e.g. 'c|c|c|c'
            `hlines` : 'all' : hlines everywhere
                        TODO : only first, etc.
        """
        nbcol = 0
        for c in col_def:
            if c in 'lcrpmb':
                nbcol += 1
        if nbcol != len(content[0]):
            raise ValueError('{} implies {} columns but our content has {}'.
                    format(col_def, nbcol, len(content[0])))

        self.col_def = col_def
        self.data = content
        if hlines not in ['all']:
            raise ValueError('{} is not supported (yet?) for `hlines`')
        self.hlines = hlines

    @property
    def args(self):
        return self.col_def

    @property
    def content(self):
        s = ''
        endl = u'\n'
        hline = r'\hline'
        nbrows = len(self.data)
        if self.hlines == 'all':
            hlines = [True for x in xrange(nbrows + 1)]
        # TODO support more hlines possibilities
        if hlines[0]:
            s += hline + endl
        for row,hl in zip(self.data, hlines[1:]):
            s += u' & '.join(map(unicode, row)) + ur' \\' + endl
            if hl:
                s += r'\hline' + endl
        return s[:-1]  # remove last \n

class Itemize(Environment):
    name = 'itemize'

    def __init__(self, content):
        """ content = a list of strings/blocks """
        self.content = map(lambda x : r'\item ' + x, content)


class Bold(CommandBase):
    # TODO test
    name = 'textbf'

    def __init__(self, content):
        self.args = content
