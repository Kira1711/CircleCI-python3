import unittest
from main import to_upper


class MytestCase(unittest.TestCase):
    def test_to_upper(self):
        name = "sau"
        upper_name = to_upper(name)
        self.assertEqual(upper_name, 'SAU')
        
if __name__ == "__main__":
    unittest.main()
