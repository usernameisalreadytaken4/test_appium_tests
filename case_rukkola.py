import logging

import pytest

from devices import devices
from helpers import (
    MAPS_ME,
    check_simple_sequence,
    wait_element,
    wait_elements,
    check_additional_property,
    swipe_until_element_and_click,
)

MOSCOW_CENTER = (55.75370903771494, 37.61981338262558, 200)
RUKKOLA_NAME = 'Руккола'

logging.info('DEVICES IN WORK: ' + ', '.join(map(lambda x: x.device_name, devices)))


@pytest.mark.parametrize('client', devices)
def test_find_restoraint(client):
    client.connect()
    MAPS_ME.open_app(client.driver)
    client.driver.set_location(*MOSCOW_CENTER)
    client.driver.find_element_by_id(MAPS_ME.search).click()

    frame = client.driver.find_element_by_id(MAPS_ME.recycler)

    menu = frame.find_elements_by_class_name('android.widget.TextView')

    list(filter(lambda x: x.text == 'Еда', menu))[0].click()

    wait_elements(client, MAPS_ME.title)
    swipe_until_element_and_click(client, element_id=MAPS_ME.title, element_text=RUKKOLA_NAME)

    check_simple_sequence(client, [
        MAPS_ME.map_surfaceview, MAPS_ME.av__direction, MAPS_ME.pp__preview, MAPS_ME.tv__title,
        MAPS_ME.tv__subtitle, MAPS_ME.tv__address, MAPS_ME.tv__straight_distance
    ])

    preview = client.driver.find_element_by_id(MAPS_ME.pp__preview)
    wait_element(client, MAPS_ME.pp__preview,
                 active_element=preview, condition=lambda: preview.location['y'] != 960)

    client.driver.swipe(500, 1200, 500, 0)
    client.driver.swipe(500, 1200, 500, 0)

    check_simple_sequence(client, [
        MAPS_ME.today_opening_hours, MAPS_ME.tv__place_website, MAPS_ME.tv__place_cuisine
    ])

    check_additional_property(client, MAPS_ME.tv__place_phone, property_list=['text'])
    check_additional_property(client, MAPS_ME.tv__place_latlon, property_list={'text': '55.756881, 37.622613'})

    koord = client.driver.find_element_by_id(MAPS_ME.tv__place_latlon)
    wait_element(client, MAPS_ME.tv__place_latlon, active_element=koord, condition=lambda: 'N' in koord.text)
    check_additional_property(client, MAPS_ME.tv__place_latlon, property_list={'text': '55°45′24.77″N, 37°37′21.41″E'})

    client.driver.quit()
