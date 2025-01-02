# in file tests_mytest.py

import pytest

def add5(v):
    myval = v + 5
    return myval

def tests_add5():
    r = add5(1)
    assert r == 6
    r = add5(5)
    assert r == 10
    r = add5(10.102645)
    assert r == 15.102645
    r = add5(4)
    assert r < 15.4

    werte =  [0, 1, 2, 3, 4]
    ergebnisse = [1, 2, 3, 4, 5]

    for wert, ergebnis in zip(werte, ergebnisse):
        r = add5(wert)
        assert r == ergebnis
