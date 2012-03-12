from pytextron import *
from pytextron.blocks import *

LatexDocument(
    preambule = concatenate(
        Documentclass('article', def_args='french'),
    ),
    content = Document(
        concatenate(
            Center('Here is a nice equation'),
            DisplayEq(r'\frac{x}{2}= 200'),
        )
    ),
).make('.', 'example')
