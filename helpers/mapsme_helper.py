class MapsMeConnector:

    PACKAGE_NAME = 'com.mapswithme.maps'

    def __init__(self):

        self.app_package = f'{self.PACKAGE_NAME}.pro'
        self.app_activity = f'{self.PACKAGE_NAME}.SplashActivity'
        self.id_mask = f'{self.app_package}:id/'

    def open_app(self, driver):
        from helpers import push_continue
        push_continue(driver)
        driver.find_element_by_id('com.android.packageinstaller:id/permission_allow_button').click()
        driver.find_element_by_id('com.android.packageinstaller:id/permission_allow_button').click()
        push_continue(driver)

    @property
    def search(self):
        return f'{self.id_mask}search'

    @property
    def title(self):
        return f'{self.id_mask}title'

    @property
    def recycler(self):
        return f'{self.id_mask}recycler'

    @property
    def map_surfaceview(self):
        return f'{self.id_mask}map_surfaceview'

    @property
    def av__direction(self):
        return f'{self.id_mask}av__direction'

    @property
    def pp__preview(self):
        return f'{self.id_mask}pp__preview'

    @property
    def tv__title(self):
        return f'{self.id_mask}tv__title'

    @property
    def tv__subtitle(self):
        return f'{self.id_mask}tv__subtitle'

    @property
    def tv__address(self):
        return f'{self.id_mask}tv__address'

    @property
    def tv__straight_distance(self):
        return f'{self.id_mask}tv__straight_distance'

    @property
    def today_opening_hours(self):
        return f'{self.id_mask}today_opening_hours'

    @property
    def tv__place_phone(self):
        return f'{self.id_mask}tv__place_phone'

    @property
    def tv__place_website(self):
        return f'{self.id_mask}tv__place_website'

    @property
    def tv__place_cuisine(self):
        return f'{self.id_mask}tv__place_cuisine'

    @property
    def tv__place_latlon(self):
        return f'{self.id_mask}tv__place_latlon'


MAPS_ME = MapsMeConnector()

