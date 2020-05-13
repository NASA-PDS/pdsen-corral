import unittest
from pdsen_corral.cattle_head import get_changelog_signet


class MyTestCase(unittest.TestCase):
    def test_get_changelog_signet(self):
        changelog_url = "https://nasa-pds.github.io/validate/CHANGELOG.html"
        changelog_signet = get_changelog_signet(changelog_url)



if __name__ == '__main__':
    unittest.main()
