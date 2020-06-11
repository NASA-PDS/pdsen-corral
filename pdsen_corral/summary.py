import os
import logging
from mdutils import MdUtils
from pdsen_corral.herd import Herd

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def write_build_summary(output_file_name=None, token=None, dev=False, version=None):

    herd = Herd(dev=dev, token=token)

    if version is None:
        version = herd.get_shepard_version()
    else:
        # for unit test
        herd.set_shepard_version(version)

    if dev and not ('dev' in version or 'SNAPSHOT' in version):
        logger.error("version of build does not contain dev or SNAPSHOT, dev build summary is not generated")
        exit(1)
    elif not dev and ('dev' in version or 'SNAPSHOT' in version):
        logger.error("version of build contains dev or SNAPSHOT, release build summary is not generated")
        exit(1)

    if not output_file_name:
        output_file_name = os.path.join('output', version, 'index')
        os.makedirs(os.path.dirname(output_file_name), exist_ok=True)

    software_summary_md = MdUtils(file_name=output_file_name, title="Software Summary")

    table = ["tool", "version", "description", "", "",
             "", "", "", ""]
    n_columns = len(table)
    for k, ch in herd.get_cattle_heads().items():
        table.extend(ch.get_table_row())
    software_summary_md.new_table(columns=n_columns,
                                  rows=herd.number_of_heads()+1,
                                  text=table,
                                  text_align='center')

    software_summary_md.create_md_file()

    return os.path.dirname(output_file_name)