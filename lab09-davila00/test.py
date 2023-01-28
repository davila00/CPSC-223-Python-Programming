import unittest
import io

from si import SimpleInteger

class Test01_add_valid_data(unittest.TestCase):
    """
    === Test01 === Function Call: x = SimpleInteger
    """
    def test_list_int(self):
        x = SimpleInteger()
        x.add(1, 2)
        self.assertEqual(3, x.add(1,2))
        print()

class Test02_add_invalid_data(unittest.TestCase):
    """docstring for Test02_add_invalid_data."""
    def test_list_int(self):
        x = SimpleInteger()
        x.add(1.5, 2)
        self.assertEqual(None, x.add(1.5, 2))
        print()

class Test03_subtract_valid_data(unittest.TestCase):
    """docstring for Test03_subtract_valid_d."""
    def test_list_int(self):
        x = SimpleInteger()
        x.subtract(3, 7)
        self.assertEqual(-4, x.subtract(3, 7))
        print()

class Test04_subtract_invalid_data(unittest.TestCase):
    """docstring for Test04_subtract_invalid_data."""
    def test_list_int(self):
        x = SimpleInteger()
        x.subtract(3.5, 7)
        self.assertEqual(None, x.subtract(3.5, 7))
        print()

class Test05_multiply_valid_data(unittest.TestCase):
    """docstring for Test05_multiply_valid_data."""
    def test_list_int(self):
        x = SimpleInteger()
        x.multiply(5, 3)
        self.assertEqual(15, x.multiply(5, 3))
        print()

class Test06_multiply_invalid_data(unittest.TestCase):
    """docstring for Test06_multiply_invalid_data."""
    def test_list_int(self):
        x = SimpleInteger()
        x.multiply(5.5, 3)
        self.assertEqual(None, x.multiply(5.5, 3))
        print()

class Test07_isequal_valid_true_data(unittest.TestCase):
    """docstring for Test07_isequal_valid_true_data."""
    def test_list_int(self):
        x = SimpleInteger()
        x.isequal(7, 7)
        self.assertEqual(True, x.isequal(7, 7))
        print()

class Test08_isequal_valid_false_data(unittest.TestCase):
    """docstring for Test08_isequal_valid_false_data."""
    def test_list_int(self):
        x = SimpleInteger()
        x.isequal(7, 8)
        self.assertEqual(False, x.isequal(7, 8))
        print()

class Test09_isequal_invalid_data(unittest.TestCase):
    """docstring for Test09_isequal_invalid_data."""
    def test_list_int(self):
        x = SimpleInteger()
        x.isequal(7.5, 7)
        self.assertEqual(None, x.isequal(7.5, 7))
        print()

class Test10_isgreaterthan_valid_true_data(unittest.TestCase):
    """docstring for Test10_isgreaterthan_valid_true_data."""
    def test_list_int(self):
        x = SimpleInteger()
        x.isgreaterthan(10, 6)
        self.assertEqual(True, x.isgreaterthan(10, 6))
        print()

class Test11_isgreaterthan_valid_false_data(unittest.TestCase):
    """docstring for Test11_isgreaterthan_valid_false_data."""
    def test_list_int(self):
        x = SimpleInteger()
        x.isgreaterthan(10, 10)
        self.assertEqual(False, x.isgreaterthan(10, 10))
        print()

class Test12_isgreaterthan_invalid_data(unittest.TestCase):
    """docstring for Test12_isgreaterthan_invalid_data."""
    def test_list_int(self):
        x = SimpleInteger()
        x.isgreaterthan(10.5, 6)
        self.assertEqual(None, x.isgreaterthan(10.5, 6))
        print()

if __name__ == '__main__':
    with open('test.txt', "w") as f:
        runner = unittest.TextTestRunner(f)
        unittest.main(testRunner=runner)
