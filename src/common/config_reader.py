"""
    TODO: Write module docstring.
"""
import toml

class ConfigReader():
    """
        TODO: Write class docstring.
    """
    def __init__(self) -> None:
        self.config = toml.load(r".\config.toml")

    def get_webdriver_value(self, key:str):
        """
            TODO: Write method docstring.
        """
        return self.config['WebDriver'][key]

    def get_browser_value(self, key:str):
        """
            TODO: Write method docstring.
        """
        return self.config['Browser'][key]

    def get_browser_resolution_value(self, key:str):
        """
            TODO: Write method docstring.
        """
        return self.config['Browser']['Resolution'][key]

    def get_application_value(self, key:str):
        """
            TODO: Write method docstring.
        """
        return self.config['Application'][key]

    def get_default_value(self, key:str):
        """
            TODO: Write method docstring.
        """
        return self.config['Default'][key]
