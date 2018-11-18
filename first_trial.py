import os
import time
from datetime import datetime

from appium import webdriver
import pytest

from crutch import push_continue

PACKAGE_NAME = 'com.mapswithme.maps'
MOSCOW_CENTER = (55.75370903771494, 37.61981338262558, 200)
RUKKOLA_NAME = 'Руккола'


@pytest.fixture
def client():
    desired_caps = {
        'platformName': 'Android',
        'platformVersion': '6.0.1',
        'deviceName': 'device',
        'appPackage': f'{PACKAGE_NAME}.pro',
        'country': 'Russia',
        'appActivity': f'{PACKAGE_NAME}.SplashActivity',
    }
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    push_continue(driver)
    driver.find_element_by_id('com.android.packageinstaller:id/permission_allow_button').click()
    driver.find_element_by_id('com.android.packageinstaller:id/permission_allow_button').click()
    push_continue(driver)

    # driver.scroll('origin', 'destination')
    # driver.find_element_by_class_name()
    yield driver
    driver.quit()


def test_find_restoraint(client):
    client.set_location(*MOSCOW_CENTER)
    client.find_element_by_id(f'{PACKAGE_NAME}.pro:id/search').click()
    frame = client.find_element_by_id(f'{PACKAGE_NAME}.pro:id/recycler')
    menu = frame.find_elements_by_class_name('android.widget.TextView')
    list(filter(lambda x: x.text == 'Еда', menu))[0].click()
    restoraints = None
    timestart = time.time()
    while not restoraints or (time.time() - timestart) < 5:
        restoraints = client.find_elements_by_id('com.mapswithme.maps.pro:id/title')

    assert len(restoraints) > 0

    timestart = time.time()
    rukkola = None
    while not rukkola or (time.time() - timestart) < 30:
        client.swipe(100, 700, 100, 200)
        current_rests = client.find_elements_by_id('com.mapswithme.maps.pro:id/title')
        check = list(filter(lambda x: x.text == RUKKOLA_NAME, current_rests))
        if len(check):
            rukkola = check[0]
            break

    assert rukkola

    rukkola.click()
    ###########
    _map = client.find_element_by_id('com.mapswithme.maps.pro:id/map_surfaceview')
    assert _map
    direction = client.find_element_by_id('com.mapswithme.maps.pro:id/av__direction')
    assert direction
    preview = client.find_element_by_id('com.mapswithme.maps.pro:id/pp__preview')
    assert preview
    title = client.find_element_by_id('com.mapswithme.maps.pro:id/tv__title')
    assert title
    subtitle = client.find_element_by_id('com.mapswithme.maps.pro:id/tv__subtitle')
    assert subtitle
    address = client.find_element_by_id('com.mapswithme.maps.pro:id/tv__address')
    assert address
    distance = client.find_element_by_id('com.mapswithme.maps.pro:id/tv__straight_distance')
    assert distance
    #########
    timestart = time.time()
    while preview.location['y'] != 960 or (time.time() - timestart) < 5:
        preview.click()
        preview = client.find_element_by_id('com.mapswithme.maps.pro:id/pp__preview')

    client.swipe(500, 1200, 500, 0)
    client.swipe(500, 1200, 500, 0)
    worktime = client.find_element_by_id('com.mapswithme.maps.pro:id/today_opening_hours')
    assert worktime
    phone = client.find_element_by_id('com.mapswithme.maps.pro:id/tv__place_phone')
    assert phone
    assert phone.text
    site = client.find_element_by_id('com.mapswithme.maps.pro:id/tv__place_website')
    assert site
    kitchen = client.find_element_by_id('com.mapswithme.maps.pro:id/tv__place_cuisine')
    assert kitchen
    koord = client.find_element_by_id('com.mapswithme.maps.pro:id/tv__place_latlon')
    assert 'N' not in koord.text
    timestart = time.time()
    while 'N' not in koord.text or (time.time() - timestart) < 5:
        koord.click()
        koord = client.find_element_by_id('com.mapswithme.maps.pro:id/tv__place_latlon')
    assert 'N' in koord.text




