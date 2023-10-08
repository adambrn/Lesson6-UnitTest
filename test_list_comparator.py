import pytest
from list_comparator import ListComparator

# Тест для случая, когда средние значения различны второй больше
def test_compare_lists_different_averages_second_large():
    list1 = [1, 2, 3, 4, 5]
    list2 = [6, 7, 8, 9, 10]
    comparator = ListComparator(list1, list2)
    assert comparator.compare_lists() == "Второй список имеет большее среднее значение"

# Тест для случая, когда средние значения различны первый больше больше
def test_compare_lists_different_averages_first_large():
    list2 = [1, 2, 3, 4, 5]
    list1 = [6, 7, 8, 9, 10]
    comparator = ListComparator(list1, list2)
    assert comparator.compare_lists() == "Первый список имеет большее среднее значение"


# Тест для случая, когда первый список пуст
def test_compare_lists_empty_list1():
    list1 = []
    list2 = [1, 2, 3]
    comparator = ListComparator(list1, list2)
    assert comparator.compare_lists() == "Второй список имеет большее среднее значение"

# Тест для случая, когда второй список пуст
def test_compare_lists_empty_list2():
    list2 = []
    list1 = [1, 2, 3]
    comparator = ListComparator(list1, list2)
    assert comparator.compare_lists() == "Первый список имеет большее среднее значение"

# Тест для случая, когда оба списка пусты
def test_compare_lists_both_empty():
    list1 = []
    list2 = []
    comparator = ListComparator(list1, list2)
    assert comparator.compare_lists() == "Средние значения равны"

# Тест для случая, когда средние значения равны
def test_compare_lists_equal_averages():
    list1 = [4, 6, 5]
    list2 = [4, 5, 6]
    comparator = ListComparator(list1, list2)
    assert comparator.compare_lists() == "Средние значения равны"
