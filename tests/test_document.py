import unittest, os
from os.path import dirname, join, exists
from pytextron.blocks.base import *
from pytextron.blocks.basic import *
from pytextron.document import *

class TestLatexDocument(unittest.TestCase):

    def test_latex_document_tex(self):
        preambule = ur'\documentclass{article}'
        d = Document('patate')

        doc = LatexDocument(preambule, d)
        cur_dir = dirname(__file__)
        tex_file = join(cur_dir, 'test.tex')
        pdf_file = tex_file[:-3] + 'pdf'
        if exists(tex_file):
            os.remove(tex_file)
        doc.make_tex(tex_file)

        def test_tex_file():
            self.assertEqual(open(tex_file).read(), 
                ur'\documentclass{article}' '\n\n'
                ur'\begin{document}' '\n\tpatate\n'
                ur'\end{document}')
        test_tex_file()

        doc.make_pdf(tex_file)
        self.assertTrue(exists(pdf_file))
        os.remove(tex_file)
        os.remove(pdf_file)

        doc.make(cur_dir, 'test')
        test_tex_file()
        self.assertTrue(exists(pdf_file))
        os.remove(tex_file)
        os.remove(pdf_file)
        
if __name__ == '__main__':
    unittest.main()

