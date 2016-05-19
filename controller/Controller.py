from model.Services import Service
from view.View import View
import functools
import util.notify as notify


class Controller:
    def __init__(self, data):
        if not isinstance(data, Service):
            raise AttributeError
        self.data = data
        self.data.add = notify.after(self.render_all)(self.data.add)
        self.view = View()

    def render_all(self):
        self.view.output(self.data.get_all_games())

    def run(self):
        pass
