"""
This module contains the ListComparator class, which compares two lists of numbers
and calculates their average values.
"""
class ListComparator:
    """
    This class compares two lists of numbers and calculates their average values.
    """

    def __init__(self, list1, list2):
        """
        Initialize the class with two lists of numbers.
        """
        self.list1 = list1
        self.list2 = list2

    def calculate_average(self, lst):
        """
        Calculate the average value of a list.

        Args:
            lst (list): The list of numbers.

        Returns:
            float: The average value of the list.
        """
        if not lst:
            return 0
        return sum(lst) / len(lst)

    def compare_lists(self):
        """
        Compare the average values of two lists and return a message.

        Returns:
            str: A message indicating which list has a greater average value.
        """
        avg1 = self.calculate_average(self.list1)
        avg2 = self.calculate_average(self.list2)

        if avg1 > avg2:
            return "Первый список имеет большее среднее значение"
        if avg1 < avg2:
            return "Второй список имеет большее среднее значение"
        return "Средние значения равны"
