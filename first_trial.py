import time

from appium import webdriver
import pytest

from helpers import MAPS_ME, push_continue, check_simple_sequence, wait_element, wait_elements, \
    check_additional_property

PACKAGE_NAME = 'com.mapswithme.maps'
MOSCOW_CENTER = (55.75370903771494, 37.61981338262558, 200)
RUKKOLA_NAME = 'Руккола'


@pytest.fixture
def driver():
    desired_caps = {
        'platformName': 'Android',
        'platformVersion': '6.0.1',
        'deviceName': 'device',
        'appPackage': MAPS_ME.app_package,
        'country': 'Russia',
        'appActivity': MAPS_ME.app_activity,
    }
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    MAPS_ME.open_app(driver)
    yield driver
    driver.quit()


def test_find_restoraint(driver):
    driver.set_location(*MOSCOW_CENTER)
    driver.find_element_by_id(MAPS_ME.search).click()
    frame = driver.find_element_by_id(MAPS_ME.recycler)
    menu = frame.find_elements_by_class_name('android.widget.TextView')
    list(filter(lambda x: x.text == 'Еда', menu))[0].click()
    restoraints = None
    timestart = time.time()
    while not restoraints or (time.time() - timestart) < 5:
        restoraints = driver.find_elements_by_id(MAPS_ME.title)
    wait_elements(driver, MAPS_ME.title, restoraints, )
    assert len(restoraints) > 0

    timestart = time.time()
    rukkola = None
    while not rukkola or (time.time() - timestart) < 30:
        driver.swipe(100, 700, 100, 200)
        current_rests = driver.find_elements_by_id(MAPS_ME.title)
        check = list(filter(lambda x: x.text == RUKKOLA_NAME, current_rests))
        if len(check):
            rukkola = check[0]
            break

    assert rukkola

    rukkola.click()

    check_simple_sequence(driver, [
        MAPS_ME.map_surfaceview, MAPS_ME.av__direction, MAPS_ME.pp__preview, MAPS_ME.tv__title,
        MAPS_ME.tv__subtitle, MAPS_ME.tv__address, MAPS_ME.tv__straight_distance
         ])


    timestart = time.time()
    while preview.location['y'] != 960 or (time.time() - timestart) < 5:
        preview.click()
        preview = driver.find_element_by_id(MAPS_ME.pp__preview)

    driver.swipe(500, 1200, 500, 0)
    driver.swipe(500, 1200, 500, 0)
    check_simple_sequence(driver, [
        MAPS_ME.today_opening_hours, MAPS_ME.tv__place_website, MAPS_ME.tv__place_cuisine
    ])
    check_additional_property(driver, MAPS_ME.tv__place_phone, property_list=['text'])

    koord = driver.find_element_by_id(MAPS_ME.tv__place_latlon)
    assert 'N' not in koord.text

    koord = wait_element(
        driver, MAPS_ME.tv__place_latlon, active_element=koord, condition='N' not in koord.text
     )
    assert 'N' in koord.text




