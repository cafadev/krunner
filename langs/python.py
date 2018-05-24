import os

from krunner.utils.shell import Shell
from krunner.validates.validate import Validate
from .lang_loader import StandardClass


class Python(StandardClass):

    virtualenv = None

    def __init__(self, window, krunner_settings):
        self.validation = Validate(krunner_settings)

        self.validation.TYPES.update({
            'virtualenv': (str, False, )
        })

        if not self.validation.is_valid():
            return

        super(Python, self).__init__(window, krunner_settings)
        self.virtualenv = krunner_settings.get('virtualenv', None)
        self.menu_items = [''] + krunner_settings.get('menu_items', [])
        self.menu_items += ["<args>"]

    def input_args(self, args=None):
        if args is None:
            self.window.show_input_panel(
                "args", str(), self.input_args, None, None
            )
            return
        else:
            self.command += args.split()
            Shell(self.window, self.shell, self.command, self.main_file).run()

    def show_menu(self, item_selected=None):
        """ Recursive function """
        if item_selected is None:
            self.window.show_quick_panel(
                [' '.join([self.main_file, item]) for item in self.menu_items],
                self.show_menu
            )
            return
        elif item_selected > -1:
            python = 'python'
            if self.virtualenv is not None:
                python = os.path.join(self.virtualenv, python)

            self.command = [python, os.path.join(self.folder, self.main_file)]

            if item_selected > 0 and item_selected != len(self.menu_items) - 1:
                self.command += [self.menu_items[item_selected]]
            else:
                self.input_args()
                return
            Shell(self.window, self.shell, self.command, self.main_file).run()

    def run(self):
        self.show_menu()
