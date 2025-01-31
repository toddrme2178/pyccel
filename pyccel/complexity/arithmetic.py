# coding: utf-8


from sympy import count_ops as sympy_count_ops
from sympy import Tuple
from sympy.core.expr import Expr
from sympy.utilities.iterables import iterable

from pyccel.ast import (For, Assign, While,NewLine,
                        FunctionDef, Import, Print,
                        Comment, AnnotatedComment,
                        If, Zeros, Ones, Array, 
                        Len, Dot, IndexedElement)

from pyccel.complexity.basic import Complexity

__all__ = ["count_ops", "OpComplexity"]

class OpComplexity(Complexity):
    """class for Operation complexity computation."""

    def cost(self):
        """
        Computes the complexity of the given code.

        verbose: bool
            talk more
        """
        return count_ops(self.ast, visual=True)


def count_ops(expr, visual=None):
    
    if isinstance(expr, Assign):
        return sympy_count_ops(expr.rhs, visual)
    elif isinstance(expr, For):
        a = expr.iterable.size
        ops = sum(count_ops(i, visual) for i in expr.body)
        return a*ops
    elif isinstance(expr, Tuple):
        return sum(count_ops(i, visual) for i in expr)
    elif isinstance(expr, (Zeros, Ones,NewLine)):
        return 0
    else:
        raise NotImplementedError('TODO count_ops for {}'.format(type(expr)))


##############################################
if __name__ == "__main__":
    code = '''
n = 10

for i in range(0,n):
    for j in range(0,n):
        x = pow(i,2) + pow(i,3) + 3*i
        y = x / 3 + 2* x
    '''

    complexity = OpComplexity(code)
    print((complexity.cost()))
