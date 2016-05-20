from controller.Controller import Controller
from model.Model import Model
from getopt import getopt
import sys


class PromptController(Controller):
    def __init__(self, data):
        super().__init__(data)

    def run(self):
        opts, args = getopt(sys.argv[1:], 'aht:', ['add', 'help', 'team='])
        if opts.__len__() == 0:
            self.render_all()
        elif opts.__len__() > 1 or (opts[0][0] in ('-a', '--add') and args.__len__() != 5) \
                or opts[0][0] in ('-h', '--help'):
            self.view.console_help()
        elif opts[0][0] in ('-a', '--add'):
            self.data.add(Model(args[0], args[1], args[2], args[3], args[4]))
        elif opts[0][0] in ('-t', '--team'):
            self.view.output(self.data.get_by_team(opts[0][1]))


