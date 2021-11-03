import pytest
from main import comprobar_edad, comprobar_mes, comprobar_numero_multiplicar, rango_edad, par_o_impar


@pytest.mark.parametrize("ec,re", [
    (6, True), (7, True), (8, True), (9, True), (10, True), (11, True), (12, True), (4, False), (15, False)
])
def test_comprobar_edad(ec, re):
    assert comprobar_edad(ec) == re


@pytest.mark.parametrize("mc, rm", [
    (1, True), (2, True), (3, True), (4, True), (5, True), (6, True), (7, True), (8, True), (9, True), (10, True),
    (11, True), (12, True), (15, False), (0, False),
])
def test_comprobar_mes(mc, rm):
    assert comprobar_mes(mc) == rm


@pytest.mark.parametrize("et,mt,rt", [
    (11, 4, [11, 12, 13]), (9, 4, [6, 8, 10]), (9, 3, [7, 9]), (7, 8, [2, 4]), (7, 5, [1, 3, 5])
])
def test_comprobar_numero_multiplicar(et, mt, rt):
    assert comprobar_numero_multiplicar(et, mt) == rt


@pytest.mark.parametrize("er, rangoe", [
    (6, "[6-8]"), (7, "[6-8]"), (8, "[6-8]"), (9, "[9-10]"), (10, "[9-10]"), (11, "[11-12]"), (12, "[11-12]")
])
def test_rango_edad(er, rangoe):
    assert rango_edad(er) == rangoe


@pytest.mark.parametrize("mes, rmes", [
    (4, "par"), (8, "par"), (3, "impar"), (9, "impar")
])
def test_par_impar(mes, rmes):
    assert par_o_impar(mes) == rmes
