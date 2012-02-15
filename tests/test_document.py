import unittest
from os.path import dirname, join
from pytextron.blocks.base import *
from pytextron.blocks.basic import *
from pytextron.document import *

class TestLatexDocument(unittest.TestCase):

    def test_latex_document_tex(self):
        preambule = ur'\documentclass{article}'
        d = Document('patate')

        doc = LatexDocument(preambule, d)
        tex_file = join(dirname(__file__), 'test.tex') 
        doc.make_tex(tex_file, ask_overwrite=False)
        
        self.assertEqual(open(tex_file).read(), 
            ur'\documentclass{article}' '\n\n'
            ur'\begin{document}' '\n\tpatate\n'
            ur'\end{document}')
        
if __name__ == '__main__':
    unittest.main()

