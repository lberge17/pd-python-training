# Unittest

- [Slides](https://docs.google.com/presentation/d/12MMdWg8cd0V2Kwso0fe_bXXOw_wqjvew_0oiyY-ca40/edit?usp=sharing)
- [Docs](https://docs.python.org/3/library/unittest.html)
- [Real Python Blog on Testing in Python](https://realpython.com/python-testing/)

```python
# from unittest documentation
import unittest

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()

```