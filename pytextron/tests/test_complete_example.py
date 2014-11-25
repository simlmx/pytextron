import os
from pytextron import LatexDocument
from pytextron.blocks import (Command, Documentclass, Usepackage, Document, Center,
    DisplayEq)

doc = LatexDocument(
    content = [
        Documentclass('article', def_args='french'),
        Usepackage('geometry', 'letterpaper'),
        Command('geometry', args='tmargin=1cm,lmargin=5cm,rmargin=5cm'),
        Document([
            Center(
                "I can also add all sorts of text since I've got a keyboard. "
                "It's quite nice as you can see : I type and type and type. "
                "I just want to add enough text so I can see if my margins "
                "worked as expected. Here, that should do it." r'\\'),
            'Here is a nice equation',
            DisplayEq(r'\frac{x}{2}= 200')
        ])
    ]
)

keep_files = False
if not os.path.exists('tmp'):
    os.mkdir('tmp')
filename = 'tmp/test_example'
try:
    doc.make(filename)
finally:
    if not keep_files:
        os.remove(filename + '.tex')
        os.remove(filename + '.pdf')
