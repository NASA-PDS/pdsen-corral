import unittest
from pdsen_corral.summary import get_changelog_signet


class MyTestCase(unittest.TestCase):
    def test_get_changelog_signet(self):
        changelog_url = "https://nasa-pds.github.io/validate/CHANGELOG.html"
        changelog_signet = get_changelog_signet(changelog_url)
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
