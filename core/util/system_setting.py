from core.util.setting import Setting
from core.util.singleton import Singleton


class SystemSetting(Setting):

    __metaclass__ = SettingsMeta

    @property
    def target_browser(self):
        return self._some['target_browser']

    @property
    def chrome_driver_path(self):
        return self._some['chrome_driver_path']

    @property
    def chrome_binary_location(self):
        return self._some['chrome_binary_location']

    @property
    def firefox_driver_path(self):
        return self._some['firefox_driver_path']

    @property
    def firefox_binary_location(self):
        return self._some['firefox_binary_location']

    @property
    def application_url(self):
        return self._some['application_url']
