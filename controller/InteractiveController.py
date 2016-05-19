import functools
import getch
import os

import util.notify as notify
from controller.Controller import Controller
from model.Model import Model


class InteractiveController(Controller):
    def __init__(self, data):
        super().__init__(data)
        self.render_all = notify.after(self.view.render_menu)(self.render_all)
        self.data.add = notify.after(self.render_all)(self.data.add)
        self._action_dict = {
            'a': self.add_result,
            's': self.get_by_team,
            'e': functools.partial(exit),
            ' ': self.render_all
        }

    def render_all(self):
        os.system("clear")
        super().render_all()

    def add_result(self):
        self.data.add(Model(input("First team name: "),
                            input("Second team name: "),
                            int(input("First team goals count: ")),
                            int(input("Second team goals count: ")),
                            input("Date in format mm.dd.yy: ")))

    def get_by_team(self):
        self.view.output(self.data.get_by_team(input("Input team name: ")))

    def run(self):
        self.render_all()
        while True:
            key = getch.getch()
            if key in self._action_dict:
                self._action_dict[key]()
