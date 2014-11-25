import unittest, os
import os.path
from pytextron.blocks import Document, Documentclass
from pytextron import LatexDocument

class TestLatexDocument(unittest.TestCase):

    def test_latex_document_tex(self):
        content = [
            Documentclass('article'),  # ur'\documentclass{article}'
            Document('patate')
        ]

        doc = LatexDocument(content)
        tex_file = 'tmp/test.tex'
        pdf_file = tex_file[:-3] + 'pdf'
        if os.path.exists(tex_file):
            os.remove(tex_file)
        doc.make_tex(tex_file)

        def test_tex_file():
            self.assertEqual(open(tex_file).read(),
                doc.header +
                ur'\documentclass{article}' '\n'
                ur'\begin{document}' '\n\tpatate\n'
                ur'\end{document}')
        test_tex_file()

        doc.make_pdf(tex_file)
        self.assertTrue(os.path.exists(pdf_file))
        os.remove(tex_file)
        os.remove(pdf_file)

        doc.make('tmp/test')
        test_tex_file()
        self.assertTrue(os.path.exists(pdf_file))
        os.remove(tex_file)
        os.remove(pdf_file)

if __name__ == '__main__':
    unittest.main()
