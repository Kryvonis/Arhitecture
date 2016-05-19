from configparser import ConfigParser
import os
from controller.PromptController import PromptController
from controller.InteractiveController import InteractiveController
from model.Services import Service
import util.notify as notify
from functools import partial


class Configurator:
    def __init__(self):
        self._config_file_path = '~/.tables.ini'
        if not os.path.isfile(self._config_file_path):
            self.config = self._first_launch()
        else:
            self.config = ConfigParser().read(self._config_file_path)

    def _first_launch(self):
        cp = ConfigParser()
        cp['BackUp'] = {'json': 'True',
                        'pickle': 'True',
                        'yaml': 'True'}
        cp['Restore'] = {'from': 'json'}
        cp['Controller'] = {'type': 'prompt'}
        with open(self._config_file_path, 'w') as config:
            cp.write(config)
        return cp

    def _get_data(self):
        def backup(json, pickle, yaml):
            if json:
                pass
            if pickle:
                pass
            if yaml:
                pass
        bs = self.config['BackUp']
        data = Service("""here must be readed data""")
        data.add = notify.after(partial(backup, json=bs['json'], pickle=bs['pickle'], yaml=bs['yaml']))(data.add)
        return data

    def get_controller(self):
        type_ = self.config['Controller']['type']
        data = self._get_data()
        return PromptController(data) if type_ == 'prompt' else InteractiveController(data)