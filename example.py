from pytextron import *
from pytextron.blocks import *

LatexDocument(
    preambule = concatenate(
        Documentclass('article', def_args='french'),
    ),
    content = Document(
        concatenate(
            'Here is a nice equation',
            DisplayEq(Frac([Sqrt('x'), 'x+y']) + '= 200'),
        )
    ),
).make('.', 'example')
