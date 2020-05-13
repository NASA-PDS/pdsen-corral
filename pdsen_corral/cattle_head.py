import logging
import requests
from bs4 import BeautifulSoup
import github3
from pdsen_corral.versions import is_dev_version, get_max_tag

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class cattleHead():
    def __init__(self, name, github_path, description, dev=False, token=None):
        logger.info(f'create cattleHead {name}, {github_path}, {description}')
        self._name = name
        self._github_path = github_path
        self._org = self._github_path.split("/")[-2]
        self._repo_name = self._github_path.split("/")[-1]
        self._description = description
        self._changelog_url = f"http://nasa-pds.github.io/{self._repo_name}/CHANGELOG.html"
        self._changelog_signets = self._get_changelog_signet()
        self._dev = dev
        self._token = token
        self._version = self._get_version()

    def _get_version(self):
        gh = github3.login(token=self._token)
        repo = gh.repository(self._org, self._repo_name)
        latest_tag = None
        for tag in repo.tags():
            if is_dev_version(tag.name) and self._dev:  # if we have a dev version and we look for dev version
                latest_tag = get_max_tag(tag.name, latest_tag) if latest_tag else tag.name
            elif not (is_dev_version(tag.name) or self._dev):  # if we don't have a dev version and we look for stable version
                latest_tag = get_max_tag(tag.name, latest_tag) if latest_tag else tag.name

        return latest_tag.__str__() if latest_tag else None

    def write(self, mdutil_file):
        mdutil_file.new_header(level=1, title=f'{self._name} ({self._version})')
        mdutil_file.new_paragraph(self._description)
        mdutil_file.new_line()
        mdutil_file.write("&nbsp;&nbsp;&nbsp;")
        mdutil_file.write(f'[:floppy_disk:](http://www.google.com "DOWNLOAD")')
        mdutil_file.write("&nbsp;&nbsp;&nbsp;")
        mdutil_file.write(f'[:mag:](http://www.google.com "USER\'S MANUAL")')

        mdutil_file.write("&nbsp;&nbsp;&nbsp;")
        if self._version:
            mdutil_file.write(f'[:footprints:]({self._changelog_signets[self._version]} "CHANGELOG")')
        else:
            mdutil_file.write(f'[:footprints:](https://www.gnupg.org/gph/en/manual/r1943.html "CHANGELOG")')

        mdutil_file.write(f'[:unicor:](http://www.google.com "REQUIREMENTS")')
        mdutil_file.write("&nbsp;&nbsp;&nbsp;")
        mdutil_file.write(f'[:scroll:](http://www.google.com "LICENSE")')
        mdutil_file.write("&nbsp;&nbsp;&nbsp;")
        mdutil_file.write(f'[:pencil:](http://www.google.com "FEEDBACK")')


    def _get_changelog_signet(self):
        headers = requests.utils.default_headers()
        changelog = requests.get(self._changelog_url, headers)
        soup = BeautifulSoup(changelog.content, 'html.parser')
        changelog_signets = {}
        for h2 in soup.find_all('h2'):
            changelog_signets[h2.find("a").text] = "#".join([self._changelog_url, h2.get('id')])

        return changelog_signets

