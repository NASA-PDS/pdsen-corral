import os
import logging
from mdutils import MdUtils
from pdsen_corral.herd import Herd

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def write_build_summary(output_file_name=None, token=None, dev=False):

    herd = Herd(dev=dev, token=token)

    if not output_file_name:
        output_file_name = os.path.join('output', herd.get_shepard_version(), 'index')
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

    return herd.get_shepard_version()
