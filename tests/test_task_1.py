from unittest import TestCase

from task_1 import MENTORS, COURSES, DURATIONS, get_top3_popular_names, get_longest_and_shortest_course, sort_duration_courses


class TestTask1(TestCase):
    def test_get_top3_popular_names(self):
        expected = 'Александр: 10 раз(а), Евгений: 5 раз(а), Максим: 4 раз(а)'
        result = get_top3_popular_names(MENTORS)
        self.assertEqual(expected, result)

    def test_get_longest_and_shortest_course(self):
        expected = \
'''Самый короткий курс(ы): Python-разработчик с нуля - 12 месяца(ев)
Самый длинный курс(ы): Fullstack-разработчик на Python, Frontend-разработчик с нуля - 20 месяца(ев)'''
        result = get_longest_and_shortest_course(COURSES, MENTORS, DURATIONS)
        self.assertEqual(expected, result)

    def test_sort_duration_courses(self):
        expected = \
'''Python-разработчик с нуля - 12 месяцев
Java-разработчик с нуля - 14 месяцев
Fullstack-разработчик на Python - 20 месяцев
Frontend-разработчик с нуля - 20 месяцев'''
        result = sort_duration_courses(COURSES, MENTORS, DURATIONS)
        self.assertEqual(expected, result)