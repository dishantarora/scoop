from core.util.setting import Setting


class SystemSetting(Setting):

    def __init__(self):
        super().__init__('settings.yml')
        self._system_settings = self._get_setting_data['system-setting']

    @property
    def target_browser(self):
        return self._system_settings['target-browser']

    @property
    def chrome_driver_path(self):
        return self._system_settings['chrome-driver-path']
