# Модуль одномерных оптимизаций

import random
import math


def golden_ratio(func, a=0, b=1, eps=1e-3):
    ratio = (1 + math.sqrt(5)) / 2

    x1 = b - (b - a) / ratio
    x2 = a + (b - a) / ratio
    iters = 0
    calls = 0
    y1 = func(x1)
    y2 = func(x2)
    calls += 2
    while abs(b - a) >= eps:
        if y1 < y2:
            b = x2
            x2 = x1
            y2 = y1
            x1 = b - (b - a) / ratio
            y1 = func(x1)
            calls += 1
        elif y1 > y2:
            a = x1
            x1 = x2
            y1 = y2
            x2 = a + (b - a) / ratio
            y2 = func(x2)
            calls += 1
        iters += 1
    return (a + b) / 2


def fibonacci(n):
    a = 0
    b = 1
    for __ in range(n):
        a, b = b, a + b
    return a


def fibonachi(func, a=0, b=1, eps=1e-8):
    iters = 0
    calls = 0
    n = 0
    while fibonacci(n) < (b - a) / eps:
        n += 1
    x1 = a + fibonacci(n - 2) / fibonacci(n) * (b - a)
    x2 = a + fibonacci(n - 1) / fibonacci(n) * (b - a)
    y1 = func(x1)
    y2 = func(x2)
    ai = a
    bi = b
    arr = []
    calls += 2
    for k in range(2, n + 1):
        if y1 < y2:
            b = x2
            x2 = x1
            y2 = y1
            x1 = a + fibonacci(n - k - 1) / fibonacci(n - k + 1) * (b - a)
            y1 = func(x1)
            calls += 1
        else:
            a = x1
            x1 = x2
            y1 = y2
            x2 = a + fibonacci(n - k) / fibonacci(n - k + 1) * (b - a)
            y2 = func(x2)
            calls += 1
        k += 1
        arr.append([iters, a, b, abs(b - a), (b + a) / 2, abs(ai - bi) / abs(b - a)])
        bi = b
        ai = a
        iters += 1

    return (b + a) / 2


def search_min(func, a=0, b=1, eps=1e-8):
    while abs(b - a) >= eps:
        x1 = random.uniform(a, b)
        x2 = random.uniform(x1, b)
        y1 = func(x1)
        y2 = func(x2)
        if y1 < y2:
            b = x2
        elif y1 > y2:
            a = x1

        else:
            a = x1
            b = x2
    return (a + b) / 2
