import configparser

from appium import webdriver

from helpers import MAPS_ME

config = configparser.ConfigParser()
config.read('devices.ini')


class Device:

    def __init__(self, **kwargs):
        self.name = kwargs.get('name')
        self.version = kwargs.get('version')
        self.device_name = kwargs.get('device')
        self.connect_address = kwargs.get('connect_address')
        self.app_package = kwargs.get('app_package')
        self.app_activity = kwargs.get('app_activity')
        self.country = kwargs.get('country', 'Russia')
        self.port = kwargs.get('port', '4723')

        self.driver = None

    @property
    def desired_caps(self):
        return {
            'platformName': self.name,
            'platformVersion': self.version,
            'deviceName': self.device_name,
            'appPackage': self.app_package,
            'country': self.country,
            'appActivity': self.app_activity,
        }

    def connect(self):
        self.driver = webdriver.Remote(f'http://localhost:{self.port}/wd/hub', self.desired_caps)


devices = []
for device in config.sections():
    devices.append(Device(
        name=config[device]['name'],
        version=config[device]['version'],
        device=config[device]['device'],
        app_package=MAPS_ME.app_package,
        country=config[device]['country'],
        app_activity=MAPS_ME.app_activity,
        port=config[device]['port']
    ))

__all__ = ['devices']
