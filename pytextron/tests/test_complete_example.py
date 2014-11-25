from pytextron import LatexDocument, stack
from pytextron.blocks import (Command, Documentclass, Usepackage, Document, Center,
    DisplayEq)

class Geometry(Command):
    name = 'geometry'

LatexDocument(
    preambule = stack(
        Documentclass('article', def_args='french'),
        Usepackage('geometry', 'letterpaper'),
        Geometry(args='tmargin=1cm,lmargin=5cm,rmargin=5cm'),
    ),
    content = Document(
        stack(
            Center(
                "I can also add all sorts of text since I've got a keyboard. "
                "It's quite nice as you can see : I type and type and type. "
                "I just want to add enough text so I can see if my margins "
                "worked as expected. Here, that should do it." r'\\'
            ),
            'Here is a nice equation',
            DisplayEq(r'\frac{x}{2}= 200'),
        )
    ),
).make('.', 'example')
