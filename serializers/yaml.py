__author__ = 'Meggapixxel'

from yaml import load, dump

try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper


class YamlSerializer:
    @staticmethod
    def load_matches(filename='matches.yaml'):
        """
        Load objects from file
        :param filename:
        :return:
        """
        with open(filename, 'rt') as f:
            matches = load(f, Loader=Loader)
            return matches

    @staticmethod
    def save_matches(matches,  filename='matches.yaml'):
        """
        Save objects to file
        :param matches:
        :param filename:
        :return:
        """
        with open(filename, 'wt') as f:
            dump(matches, f, Dumper=Dumper)
