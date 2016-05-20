from configparser import ConfigParser
import os
from controller.PromptController import PromptController
from controller.InteractiveController import InteractiveController
from serializers.json import JsonSerializer
from serializers.pickle import PickleSerializer
from serializers.yaml import YamlSerializer
from model.Services import Service
import util.notify as notify
from functools import partial


class Configurator:
    def __init__(self):
        self._config_file_path = './tables.ini'
        if not os.path.isfile(self._config_file_path):
            self.config = self._first_launch()
        else:
            self.config = ConfigParser().read(self._config_file_path)
        print(self.config)

    def _first_launch(self):
        cp = ConfigParser()
        cp['BackUp'] = {
            'json': 'True',
            'pickle': 'True',
            'yaml': 'True'
        }
        cp['Restore'] = {'from': 'json'}
        cp['Controller'] = {'type': 'prompt'}
        with open(self._config_file_path, 'w') as config:
            cp.write(config)
        return cp

    def _restore_data(self):
        from_ = self.config['Restore']['from']
        return JsonSerializer.load_matches() if from_ == 'json' else PickleSerializer.load_matches() \
            if from_ == 'pickle' else YamlSerializer.load_matches() if from_ == 'yaml' else []

    def _get_data(self):
        data = Service(self._restore_data())

        def backup(json, pickle, yaml):
            save = data.get_all_games()
            if json:
                JsonSerializer.save_matches(save)
            if pickle:
                PickleSerializer.save_matches(save)
            if yaml:
                YamlSerializer.save_matches(save)

        bs = self.config['BackUp']
        data.add = notify.after(partial(backup, json=bs['json'], pickle=bs['pickle'], yaml=bs['yaml']))(data.add)
        return data

    def get_controller(self):
        type_ = 'prompt'#self.config['Controller']['type']
        data = self._get_data()
        return PromptController(data) if type_ == 'prompt' else InteractiveController(data)
