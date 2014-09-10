import unittest, os
import os.path
from pytextron.blocks.base import Block
from pytextron.blocks.latex import Document, Documentclass
from pytextron import *
from pytextron import join, stack

class TestLatexDocument(unittest.TestCase):

    def test_latex_document_tex(self):
        preambule = Documentclass('article')# ur'\documentclass{article}'
        d = Document('patate')

        doc = LatexDocument(preambule, d)
        cur_dir = os.path.dirname(__file__)
        tex_file = os.path.join(cur_dir, 'test.tex')
        pdf_file = tex_file[:-3] + 'pdf'
        if os.path.exists(tex_file):
            os.remove(tex_file)
        doc.make_tex(tex_file)

        def test_tex_file():
            self.assertEqual(open(tex_file).read(), 
                ur'\documentclass{article}' '\n\n'
                ur'\begin{document}' '\n\tpatate\n'
                ur'\end{document}')
        test_tex_file()

        doc.make_pdf(tex_file)
        self.assertTrue(os.path.exists(pdf_file))
        os.remove(tex_file)
        os.remove(pdf_file)

        doc.make(cur_dir, 'test')
        test_tex_file()
        self.assertTrue(os.path.exists(pdf_file))
        os.remove(tex_file)
        os.remove(pdf_file)

    def test_join_stack(self):
        b1 = Block('patate')
        b2 = Block('poil')
        self.assertEqual(join(b1,b2), 'patatepoil')
        self.assertEqual(stack(b1,b2), 'patate\npoil')
        
if __name__ == '__main__':
    unittest.main()

