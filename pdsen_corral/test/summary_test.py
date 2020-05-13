import unittest
import logging
from pdsen_corral.summary import gather_the_herd

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class MyTestCase(unittest.TestCase):

    def test_gather_the_herd(self):
        gather_the_herd()


if __name__ == '__main__':
    unittest.main()
