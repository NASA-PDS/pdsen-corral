import unittest
from pdsen_corral.output.root_index import update_root_index


class MyTestCase(unittest.TestCase):
    def test_root_index(self):
        update_root_index('output')

if __name__ == '__main__':
    unittest.main()
