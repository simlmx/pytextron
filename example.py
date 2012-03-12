from pytextron import *
from pytextron.blocks import *

LatexDocument(
    preambule = concatenate(
        Documentclass('article', def_args='french'),
        Usepackage(['geometry', 'lmargin=1cm,rmargin=1cm']),
    ),
    content = Document(
        concatenate(
            Center('Here is a nice equation'),
            DisplayEq(r'\frac{x}{2}= 200'),
        )
    ),
).make('.', 'example')
