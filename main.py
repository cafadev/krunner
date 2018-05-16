import sublime
import sublime_plugin

from importlib import import_module
import os

from .langs import lang_loader
from .validates.validate import Validate


class Krunner(sublime_plugin.WindowCommand):

    def run(self):
        krunner_settings = self.window.project_data()['krunner']

        if not Validate(krunner_settings).is_valid():
            return

        lang = krunner_settings["lang"]
        # load the module, will raise ImportError
        # if module cannot be loaded
        module = import_module("krunner.langs.%s" % lang)

        # get the class, will raise AttributeError
        # if class cannot be found
        class_name = lang[0].upper() + lang[1:]
        _class = getattr(module, class_name)
        _class(self.window, krunner_settings).run()
