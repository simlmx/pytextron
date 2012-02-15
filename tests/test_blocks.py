import unittest
from pytextron.blocks.base import *
from pytextron.blocks.basic import *

class TestBasic(unittest.TestCase):

    def test_block(self):
        a = Block('patate')
        b = Block('poil')

        self.assertEqual(unicode(a), 'patate')
        self.assertEqual(unicode(b), 'poil')
        
        self.assertEqual(unicode(a + b), 'patate poil')
        self.assertEqual(unicode(a + 'poil'), 'patate poil')
        self.assertEqual(unicode('patate' + b), 'patate poil')

    def test_environment(self):
        class EnvTest(Environment):
            name = 'test'

        self.assertEqual(
            unicode(EnvTest('patate')),
            ur'\begin{test}' '\n\tpatate\n' ur'\end{test}'
        )
        self.assertEqual(
            unicode(EnvTest('patate', indent=False)),
            ur'\begin{test} patate \end{test}'
        )
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

if __name__ == '__main__':
    unittest.main()
