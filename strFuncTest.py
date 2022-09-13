import pytest


# Первый тест
def test_str_len_positive():
    s1 = 'jjj'
    assert len(s1) == 3
    s1 = 't'
    assert len(s1) == 1
    s1 = ''
    assert len(s1) == 0
    s1 = 'oqpwo'
    assert len(s1) == 5


# Второй тест
@pytest.mark.parametrize("stroka,flag",
                         [("Hello", 1),
                          ("privet", 0),
                          ("tevirP", 0),
                          ("Uw", 1),
                          ("123", 0)
                          ])
def test_str_istitle(stroka, flag):
    assert stroka.istitle() == flag


# Третий тест
def test_str_min_div_negative():
    try:
        assert 'asd' - 'vvv'
    except TypeError:
        pass
