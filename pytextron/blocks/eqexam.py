from pytextron.blocks import Environment, Container
from pytextron.utils import stack

class Solution(Environment):
    name = 'solution'

class Parts(Environment):
    name = 'parts'

# Note we need the {} after {exam} hence this is why we
# subclass Container and not Environment
class Exam(Container):
    before = ur'\begin{exam}{}'
    after = ur'\end{exam}'

    def __init__(self, problem_list, **kwargs):
        if isinstance(problem_list, Problem):
            problem_list = [problem_list]
        super(Exam, self).__init__(stack(problem_list))


class SolutionMixin(object):

    """ Common solution stuff for Item and Problem. """
    @property
    def content(self):
        if self.solution:
            sol = self.solution
            if not isinstance(sol, Solution):
                sol = Solution(sol)
            return self.question + sol
        else:
            return self.question

class Item(Container, SolutionMixin):

    """ Item of a problem. """
    @property
    def before(self):
        return r'\item' '{self.formated_points}'.format(self=self)

    @property
    def formated_points(self):
        if self.points is None:
            return ''
        else:
            return r'\PTs{%i}' % self.points

    def __init__(self, question=None, solution=None, points=None):
        self.assign_to_self(
            question=question,
            solution=solution,
            points=points)
        super(Item, self).__init__()

class Problem(Environment, SolutionMixin):

    name = 'problem*'

    def __init__(self, content='', points=r'\auto', solution=None):
        """
            Arguments :
                content -- Can also be a list of `Item`s
        """
        # If content is a list of Items
        if isinstance(content, (list,tuple)):
            content = Parts(reduce(lambda x,y : x+y, content))
        self.assign_to_self(
            question = content,
            solution = solution)
        super(Problem, self).__init__(def_args=str(points))
