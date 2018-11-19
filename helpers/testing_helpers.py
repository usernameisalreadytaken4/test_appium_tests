import time


def check_simple_sequence(device, id_list):
    for _id in id_list:
        assert device.find_element_by_id(_id)


def check_additional_property(device, element_name, property_list=None):
    """
    :param element_name:
    :param property_list: list or dict
     либо просто список, тогда проверяем на наличие,
     либо словарь, проверяем у атрибута-ключа, значение ключа
    :return:
    """
    el = device.find_element_by_id(element_name)
    assert el
    if isinstance(property_list, list):
        for _property in property_list:
            assert getattr(el, _property)
    if isinstance(property_list, dict):
        for _property, value in property_list.items():
            assert getattr(el, _property) == value


def wait_element(device, element_name, active_element, condition=None, wait_time=5):
    timestart = time.time()
    while not condition or (time.time() - timestart) < wait_time:
        active_element.click()
        active_element = device.find_element_by_id(element_name)
    return active_element


def wait_elements(device, element_name, active_element, condition=None, wait_time=5):
    timestart = time.time()
    while not el or (time.time() - timestart) < wait_time:
        pass
