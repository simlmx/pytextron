import unittest
from pytextron.blocks import Item, Problem, Solution, Exam

class TestEqexam(unittest.TestCase):

    def test_item(self):
        self.assertEqual(
            unicode(Item('patate')),
            ur'\item' '\n\tpatate')
        self.assertEqual(
            unicode(Item(
                'patate',
                solution=Solution('solution', def_args='8cm'))),
            ur'\item' '\n'
            '\t' 'patate' '\n'
            '\t' ur'\begin{solution}[8cm]' '\n'
            '\t\t' 'solution' '\n'
            '\t' ur'\end{solution}'
        )

    def test_problem(self):
        self.assertEqual(
            unicode(Problem('patate', points='auto')),
            ur'\begin{problem*}[\auto]' '\n\tpatate\n' ur'\end{problem*}'
        )
        self.assertEqual(
            unicode(Problem('patate', solution='poil')),
            r'\begin{problem*}' '\n'
            '\t' 'patate' '\n'
            '\t' r'\begin{solution}' '\n'
            '\t\t' 'poil' '\n'
            '\t' r'\end{solution}' '\n'
            '' r'\end{problem*}')

        self.assertEqual(
            unicode(Problem(points = 'auto',
                content = [Item('patate', points=4, solution = Solution('sol patate', def_args='4cm')),
                    Item('poil', points=3)])),
            ur'\begin{problem*}[\auto]' '\n'
            '\t' r'\begin{parts}' '\n'
            '\t\t' r'\item\PTs{4}' '\n'
            '\t\t\t' 'patate' '\n'
            '\t\t\t' r'\begin{solution}[4cm]' '\n'
            '\t\t\t\t' 'sol patate' '\n'
            '\t\t\t' r'\end{solution}' '\n'
            '\t\t' r'\item\PTs{3}' '\n'
            '\t\t\t' 'poil' '\n'
            '\t' r'\end{parts}' '\n'
            r'\end{problem*}')

    def test_exam(self):
        p1 = Problem('patate')
        p2 = Problem('poil')
        self.assertEqual(unicode(Exam([p1,p2])),
            ur'\begin{exam}{}' '\n'
            '\t' r'\begin{problem*}' '\n'
            '\t\t' 'patate' '\n'
            '\t' r'\end{problem*}' '\n'
            '\t' r'\begin{problem*}' '\n'
            '\t\t' 'poil' '\n'
            '\t' r'\end{problem*}' '\n'
            ur'\end{exam}')


if __name__ == '__main__':
    unittest.main()
