import unittest
import using_debugger

class TestDebuggerProgram(unittest.TestCase):

    def test_greeting(self):
        self.assertEqual(using_debugger.greeting(), "Hello World", "Should return 'Hello World'")

    def test_greeting_arguments(self):
        self.assertEqual(using_debugger.greeting('Laura'), 'Hello Laura', 'Allows an optional argument')

    def test_shopping_list(self):
        self.assertEqual(using_debugger.shopping_list(['chips', 'fruit']), 'I need to get: chips and fruit', 'Takes a list a returns those items in a sentence')

    def test_shopping_list_commas(self):
        self.assertEqual(using_debugger.shopping_list(['chips', 'fruit', 'veggies']), 'I need to get: chips, fruit, and veggies', 'Adds commas if more than 2 items')

    def test_shopping_list_oxford_commas(self):
        self.assertEqual(using_debugger.shopping_list(['chips', 'fruit', 'veggies'], False), 'I need to get: chips, fruit and veggies', 'Allows optional 2nd boolean to skip oxford comma - True by default')

    def test_shopping_list_single_item(self):
        self.assertEqual(using_debugger.shopping_list(['chips']), 'I need to get: chips', 'Works if just one item is in the list')


if __name__ == '__main__':
    unittest.main()
