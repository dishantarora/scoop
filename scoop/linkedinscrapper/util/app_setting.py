from core.util.base_setting import BaseSetting
from core.util.setting_meta import SettingMeta


class AppSetting(BaseSetting):

    __metaclass__ = SettingMeta

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
