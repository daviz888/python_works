import unittest
from name_function import get_formatted_name

import screen
screen.clear()

class NamesTestCase(unittest.TestCase):
    # Test for 'name_function.py'

    def test_first_last_name(self):
        # Do name like 'Janis Joplin' work?
        formatted_name = get_formatted_name('dovvy','pacamalan', 'aban')
        self.assertEqual(formatted_name, 'Dovvy Aban Pacamalan')

unittest.main()