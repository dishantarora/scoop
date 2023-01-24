from core.util.setting import Setting


class AppSetting(Setting):

    def __init__(self):
        super().__init__('scoop\\amazon-scrapper\\app-settings.yml')
        self._application_settings = self._get_setting_data['application-setting']

    @property
    def application_url(self):
        return self._application_settings['application-url']
    
    @property
    def product_name(self):
        return self._application_settings['product-name']
