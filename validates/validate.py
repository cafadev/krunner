import sublime


class Validate:

    _INVALID_TYPE = "Invalid type for '%s' key in krunner settings"
    _MISSING_REQUIRED_KEY = "Missing required '%s' key in krunner settings"

    TYPES = {
        'main': (str, True, ),
        'shell': (str, True, ),
        'lang': (str, True, )
    }

    window = None
    krunner_settings = None

    def __init__(self, krunner_settings):
        self.krunner_settings = krunner_settings

    def is_type_valid(self, item):
        if type(self.krunner_settings[item]) is not self.TYPES[item][0]:
            sublime.error_message(self._INVALID_TYPE % item)
            return False
        return True

    def is_valid(self):
        for item in list(self.TYPES):
            if self.TYPES[item][1] is True:
                if item not in self.krunner_settings:
                    sublime.error_message(self._MISSING_REQUIRED_KEY % item)
                    return False

            if item in self.krunner_settings:
                if all([self.is_type_valid(item), ]) is False:
                    return False
        return True
