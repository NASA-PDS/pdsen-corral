import requests
from bs4 import BeautifulSoup
from mdutils import MdUtils

from pdsen_corral.versions import grab_latest_versions


def get_changelog_signet(changelog_url):
    headers = requests.utils.default_headers()
    changelog = requests.get(changelog_url, headers)
    soup = BeautifulSoup(changelog.content, 'html.parser')
    changelog_signets = {}
    for h2 in soup.find_all('h2'):
        changelog_signets[h2.find("a").text] = "#".join([changelog_url, h2.get('id')])

    return changelog_signets


def write_build_summary(token, output_file_name, dev=False):

    repo_latest_versions = grab_latest_versions(token, dev=dev)
    software_summary_md = MdUtils(file_name=output_file_name, title="Software Summary")

    table = ["tool", "version", "changelog"]
    nrow = 1
    for repo,vers in repo_latest_versions.items():
        changelog_signets = get_changelog_signet(f"http://nasa-pds.github.io/{repo}/CHANGELOG.html")
        changelog_link = f"[:footprints:]({changelog_signets[vers]})"
        table.extend([repo, vers, changelog_link])
        nrow += 1

    software_summary_md.new_line()
    software_summary_md.new_table(columns=3, rows=nrow, text=table, text_align='center')

    software_summary_md.create_md_file()