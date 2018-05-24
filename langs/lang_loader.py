from abc import ABCMeta, abstractmethod


class StandardClass(metaclass=ABCMeta):

    window = None
    main_file = str()
    shell = str()

    def __init__(self, window, krunner_settings):
        self.window = window
        self.folder = self.window.extract_variables()['folder']
        self.main_file = krunner_settings['main']
        self.shell = krunner_settings['shell']

    @abstractmethod
    def run(self):
        pass
