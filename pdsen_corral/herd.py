import os
from configparser import ConfigParser
import logging
from pdsen_corral.cattle_head import CattleHead

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class Herd:
    def __init__(self, dev=False, token=False):
        self._dev =dev
        self._token = token
        self._config = ConfigParser()
        self._config.read(os.path.join(os.getcwd(), ".gitmodules"))

        self._gather_the_herd()

    def number_of_heads(self):
        return len(self._herd)

    def get_cattle_heads(self):
        return self._herd

    def _gather_the_herd(self):
        logger.info('gather the herd of submodules listed in .gitmodule')

        self._herd = {}
        self._shepard_version = None
        for section in self._config.sections():
            if 'submodule "."' not in section:
                module_name = section.split(" ")[1].strip('"')
                optional_module_options = {k:self._config.get(section, k).strip("/") for k in ['version'] if self._config.has_option(section, k)}
                self._herd[module_name] = CattleHead(module_name,
                                                     self._config.get(section, "url").strip("/"),
                                                     self._config.get(section, "description").strip("/"),
                                                     dev=self._dev,
                                                     token=self._token,
                                                     **optional_module_options)
            else:
                self._shepard_version = self._config.has_option(section, 'version')

        return 0

    def get_shepard_version(self):
        return self._config.get('submodule "."', 'version').strip(" ")