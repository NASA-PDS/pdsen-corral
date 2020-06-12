import unittest
import os
import logging
from pdsen_corral.herd import Herd
from pdsen_corral.summary import write_build_summary

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

TOKEN = os.environ.get('GITHUB_TOKEN')

class MyTestCase(unittest.TestCase):

    def test_gather_the_herd(self):
        herd = Herd(token=TOKEN)
        cattle_heads = herd.get_cattle_heads()
        version = herd.get_shepard_version()

    def test_summary_dev(self):
        write_build_summary(output_file_name='output/dev_summary.md', token=TOKEN, dev=True, version='10.0-SNAPSHOT')

    def test_summary_release(self):
        write_build_summary(output_file_name='output/rel_summary.md', token=TOKEN, dev=False, version='10.0')


if __name__ == '__main__':
    unittest.main()