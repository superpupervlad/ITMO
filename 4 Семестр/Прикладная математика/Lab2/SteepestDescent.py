from Lab2.DescentFunction import DescentFunction
from sympy import *

x, y, z = symbols('x y z')
init_printing(use_unicode=True)


class SteepestDescent(DescentFunction):
    name = "Steepest Descent Method"

    def __init__(self, max_iter=100, step=0.1):
        super().__init__()
        self.max_iter = max_iter
        self.alpha = step

    @DescentFunction._increment_calls
    def run_once(self, xx, df):
        return xx - self.alpha*df

    def run(self, func, xx=0):
        cur_iter = 0
        df = diff(func)
        while cur_iter < self.max_iter:
            xx = self.run_once(xx, df)
