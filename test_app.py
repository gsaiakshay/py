
import unittest
from app import add

class Test(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(10, 20), 30)
