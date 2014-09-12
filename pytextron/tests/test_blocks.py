import unittest
from pytextron.blocks import (Block, Container, Environment, Command, Center, Eq,
    Section, Subsection, Usepackage, DisplayEq)

class TestBasic(unittest.TestCase):

    def test_block(self):
        a = Block('patate')
        b = Block('poil')

        self.assertEqual(unicode(a), 'patate')
        self.assertEqual(unicode(b), 'poil')

        self.assertEqual(unicode(a + b), 'patatepoil')
        self.assertEqual(unicode(a + 'poil'), 'patatepoil')
        self.assertEqual(unicode('patate' + b), 'patatepoil')

    def test_container(self):
        class ConTest(Container):
            before = 'patate'
            after = 'poil'

        result = 'patate\n\tmiddle\npoil'
        self.assertEqual(
            unicode(ConTest('middle')),
            result)
        # With a block inside instead of a string
        self.assertEqual(
            unicode(ConTest(Block('middle'))),
            result)

    def test_adding_something_to_container(self):
        class ConTest(Container):
            before = 'patate'
            after = 'poil'

        c = ConTest('middle')
        c.content += ' middle2'

        self.assertEqual(
            unicode(c), ur'patate' '\n\t' 'middle middle2' '\n' 'poil')

    def test_environment(self):
        class EnvTest(Environment):
            name = 'test'

        self.assertEqual(
            unicode(EnvTest('patate')),
            ur'\begin{test}' '\n\tpatate\n' ur'\end{test}'
        )
        #self.assertEqual(
        #    unicode(EnvTest('patate', indent=False)),
        #    ur'\begin{test} patate \end{test}'
        #)
        self.assertEqual(
            unicode(EnvTest('patate',
                args=['poil', 'un', 'deux'],
                def_args = ['defpoil', 'defun'])),
            ur'\begin{test}[defpoil, defun]{poil}{un}{deux}'
            '\n\tpatate\n'
            ur'\end{test}')

    def test_command(self):
        class ComTest(Command):
            name = 'test'

        self.assertEqual(
            unicode(ComTest('patate')),
            ur'\test{patate}'
        )
        self.assertEqual(
            unicode(ComTest(
                args=['patate','poil'],
                def_args=['def_patate','def_poil'])),
            ur'\test[def_patate, def_poil]{patate}{poil}'
        )
        self.assertEqual(
            unicode(ComTest(
                args = '',
                def_args ='2')),
            ur'\test[2]'
        )

class TestLatex(unittest.TestCase):

    def test_sections(self):
        self.assertEqual(
            unicode(Section('patate', Subsection(
                'poil', 'patatepoil', numbering=False))),
            ur'\begin{section}{patate}'
            '\n\t' ur'\begin{subsection*}{poil}'
            '\n\t\t' 'patatepoil'
            '\n\t' ur'\end{subsection*}'
            '\n' ur'\end{section}')

    def test_simple_command(self):
        self.assertEqual(
            unicode(Usepackage('patate')),
            r'\usepackage{patate}')

    def test_simple_env(self):
        self.assertEqual(
            unicode(Center('patate')),
            r'\begin{center}'
            '\n\t' 'patate'
            '\n' r'\end{center}')

    def test_eq(self):
        self.assertEqual(
            unicode(Eq('a+b')), '$ a+b $')
        self.assertEqual(
            unicode(DisplayEq('a+b')), '$$ a+b $$')

if __name__ == '__main__':
    unittest.main()
