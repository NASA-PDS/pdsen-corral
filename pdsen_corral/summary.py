import os
import logging
from configparser import ConfigParser
from mdutils import MdUtils
from pdsen_corral.cattle_head import cattleHead

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def gather_the_herd(dev, token):
    logger.info('gather the herd of submodules listed in .gitmodule')
    config = ConfigParser()
    config.read(os.path.join(os.getcwd(), ".gitmodules"))

    herd = {}
    for section in config.sections():
        module_name = section.split(" ")[1].strip('"')
        herd[module_name] = cattleHead(module_name,
                                       config.get(section, "url").strip("/"),
                                       config.get(section, "description").strip("/"),
                                       dev=dev,
                                       token=token)
    return herd


def write_build_summary(output_file_name, token=None, dev=False):

    software_summary_md = MdUtils(file_name=output_file_name, title="Software Summary")

    herd = gather_the_herd(dev, token)

    table = ["tool", "version", "description", "download", "manual",
             "changelog", "requirements", "license", "feedback"]
    n_columns = len(table)
    for k, v in herd.items():
        table.extend(v.get_table_row())
    software_summary_md.new_table(columns=n_columns,
                                  rows=len(herd)+1,
                                  text=table,
                                  text_align='center')

    software_summary_md.create_md_file()
