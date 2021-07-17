import math
import function
import random

ratio = (1 + math.sqrt(5)) / 2


def search_min(a, b, eps):
    while abs(b - a) >= eps:
        x1 = random.uniform(a, b)
        x2 = random.uniform(x1, b)
        y1 = function.f(x1)
        y2 = function.f(x2)
        if y1 < y2:
            b = x2
        elif y1 > y2:
            a = x1
        else:
            a = x1
            b = x2
    return (a + b) / 2


def golden_ratio(a, b, eps):
    data = []
    x1 = b - (b - a) / ratio
    x2 = a + (b - a) / ratio
    iters = 0
    calls = 0
    y1 = function.f(x1)
    y2 = function.f(x2)
    calls += 2
    while abs(b - a) >= eps:
        # eps, итерации, а, b, разность a и b, вызовы функции
        data.append([eps, iters, a, b, abs(b - a), calls])
        if y1 < y2:
            b = x2
            x2 = x1
            y2 = y1
            x1 = b - (b - a) / ratio
            y1 = function.f(x1)
            calls += 1
        elif y1 > y2:
            a = x1
            x1 = x2
            y1 = y2
            x2 = a + (b - a) / ratio
            y2 = function.f(x2)
            calls += 1
        iters += 1

    return (a + b) / 2


def dichotomy(a, b, delta, eps):
    iters = 0
    calls = 0
    while abs(b - a) >= eps:
        c = (a + b) / 2
        x1 = c - delta
        x2 = c + delta
        y1 = function.f(x1)
        y2 = function.f(x2)
        calls += 2
        if y1 < y2:
            b = x2
        elif y1 > y2:
            a = x1
        else:
            a = x1
            b = x2
        iters += 1
    return (a + b) / 2, calls, iter


def parabola(x1, x3, eps):
    x2 = random.uniform(x1, x3)
    y1 = function.f(x1)
    y2 = function.f(x2)
    y3 = function.f(x3)
    iters = 0
    calls = 3
    while abs(x3 - x1) >= eps:
        x2 = random.uniform(x1, x3)
        y2 = function.f(x2)
        calls += 1
        u = x2 - (((x2 - x1) ** 2) * (y2 - y3) - ((x2 - x3) ** 2) * (y2 - y1)) / \
            (2 * ((x2 - x1) * (y2 - y3) - (x2 - x3) * (y2 - y1)))
        y4 = function.f(u)
        calls += 1
        if x2 < u:
            if y2 < y4:
                x3 = u
            else:
                x1 = x2
        else:
            if y2 < y4:
                x1 = u
            else:
                x3 = x2

<<<<<<< HEAD
    return (x1 + x3) / 2
=======

def fibonachi(a, b, eps):
    iters = 0
    calls = 0
    n = int(abs(b - a) // eps)

    k = 1
    x1 = a + F[n - 2] / F[n] * (b - a)
    x2 = a + F[n - 1] / F[n] * (b - a)
    y1 = function.f(x1)
    y2 = function.f(x2)
    calls += 2
    while k < n - 2:
        if y1 < y2:
            b = x2
            x2 = x1
            y2 = y1
            x1 = a + F[n - k - 2] / F[n - k] * (b - a)
            y1 = function.f(x1)
            calls += 1
        else:
            a = x1
            x1 = x2
            y1 = y2
            x2 = a + F[n - k - 1] / F[n - k] * (b - a)
            y2 = function.f(x2)
            calls += 1
        k += 1
    iters += 1
    return (x1 + x2) / 2, calls, iters
>>>>>>> 92cb47005c2f9f210eb74a2d874224810ab67b08


def brent(a, c, eps):
    golden_k = (math.sqrt(5) - 1) / 2
    a, c = a, c
    x = w = v = (a + c) / 2
    yx = yw = yv = function.f(x)
    d = e = c - a
    delta = c - a

    iters = 0
    calls = 1
    u = 0
    while delta > eps:
        g = e
        e = d
        if x != w and x != v and w != v and yx != yw and yx != yv and yw != yv:
            u = w - ((w - x) ** 2 * (yw - yv) - (w - v) ** 2 * (yw - yx)
                     ) / (2 * ((w - x) * (yw - yv) - (w - v) * (yw - yx)))
            if a + eps <= u < c - eps and abs(u - x) < g / 2:
                d = abs(u - x)
        else:
            if x < a + delta / 2:
                u = x + golden_k * (c - x)
                d = c - x
            else:
                u = x - golden_k * (x - a)
                d = x - a

        yu = function.f(u)
        calls += 1
        if yu <= yx:
            if u >= x:
                a = x
            else:
                c = x
            v = w
            w = x
            x = u
            yv = yw
            yw = yx
            yx = yu
        else:
            if u >= x:
                c = u
            else:
                a = u
            if yu <= yw or w == x:
                v = w
                w = u
                yv = yw
                yw = yu
            elif yu <= yv or v == x or v == w:
                v = u
                yv = yu

        delta = c - a
        iters += 1

    return x


def find_fibonacci_number(n):
    a = 0
    b = 1
    for _ in range(n):
        a, b = b, a + b
    return a


def fib_calc(a, b, n, k, is_first) -> float:
    if is_first:
        return a + (find_fibonacci_number(n - k - 1) * (b - a)) / find_fibonacci_number(n - k + 1)
    else:
        return a + (find_fibonacci_number(n - k) * (b - a)) / find_fibonacci_number(n - k + 1)


def fibonacci(a, b, eps):
    n = 0
    while find_fibonacci_number(n) < (b - a) / eps:
        n += 1

    x1 = fib_calc(a, b, n, 1, True)
    y1 = function.f(x1)

    x2 = fib_calc(a, b, n, 1, False)
    y2 = function.f(x2)

    for i in range(2, n + 1):
        if y1 <= y2:
            b = x2
            x2 = x1
            y2 = y1
            x1 = fib_calc(a, b, n, i, True)
            y1 = function.f(x1)
        else:
            a = x1
            x1 = x2
            y1 = y2
            x2 = fib_calc(a, b, n, i, False)
            y2 = function.f(x2)

    x2 = x1 + eps
    y2 = function.f(x2)

    if y1 <= y2:
        b = x1
    else:
        a = x1

    return (x1 + x2) / 2
