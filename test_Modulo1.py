import unittest
import Modulo1
def test_modulo1():
    modulo1 = Modulo1.Modulo1(19)
    modulo1.setValor(10)
    assert modulo1.getValor() == 10
