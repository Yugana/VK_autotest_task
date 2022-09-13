import pytest


# Первый тест
@pytest.mark.parametrize("pre_list, a, af_list", [
    ([123, 333, 4], 4, [123, 333, 4, 4]),
    ([123, 4], 7, [123, 4, 7]),
    ([333, 4], 2, [333, 4, 2]),
    ([7774], 0, [7774, 0])
])
def test_list_append_positive(pre_list, a, af_list):
    li = pre_list
    li.append(a)
    assert li == af_list


# Второй тест
def test_list_count():
    li = [1, 5, 6, 6, 7, 8, 6]
    assert li.count(6) == 3
    li = [123, 44, 2, 2, 2, 2]
    assert li.count(2) == 4
    li = [1, 5, 6, 6, 7, 8, 6]
    assert li.count(61) == 0


# Третий тест
def test_list_pop_negative():
    try:
        assert [].pop(3)
    except IndexError:
        pass
