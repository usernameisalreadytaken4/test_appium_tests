import time
import logging
from datetime import datetime

logging.basicConfig(
    filename=f'case_{datetime.now().strftime("%H%M_%d%m")}',
    filemode='a',
    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
    datefmt='%H:%M:%S',
    level=logging.INFO
)


def check_simple_sequence(client, id_list):
    """
    простая последовательная проверка элементов на само наличие
    :param client: client
    :param id_list: список элементов
    :return:
    """
    logging.info(f'\n{client.device_name} RUNNING... {check_simple_sequence.__name__}')
    for _id in id_list:
        logging.info(f'{client.device_name} CHECKING ELEMENT ID: {_id}...')
        assert client.driver.find_element_by_id(_id)
        logging.info(f'{client.device_name} ...{_id} EXIST\n')


def check_additional_property(client, element_id, property_list=None):
    """
    чекаем элемент на вторичные признаки
    :param client: client
    :param element: айди элемента или сам элемент
    :param property_list: list or dict
     либо просто список, тогда проверяем на наличие,
     либо словарь, проверяем у атрибута-ключа, значение ключа
    :return:
    """
    logging.info(f'{client.device_name} RUNNING... {check_additional_property.__name__}')
    logging.info(f'{client.device_name} CHECKING ELEMENT ID {element_id}')
    element = client.driver.find_element_by_id(element_id)
    assert element
    logging.info(f'{client.device_name} ...{element_id} EXIST\n')
    if isinstance(property_list, list):
        for _property in property_list:
            assert getattr(element, _property)
            logging.info(f'{client.device_name} {element_id} HAS {_property}\n')
    if isinstance(property_list, dict):
        for _property, value in property_list.items():
            assert getattr(element, _property) == value
            logging.info(f'{client.device_name} {element_id} HAS {_property} WITH {value}\n')


def wait_element(client, element_id, active_element, condition, wait_time=5):
    """
    ждем, пока элемент соизволит измениться по клику, и когда сможем его адекватно прочитать
    :param client: client
    :param element_id:  id изменяевого Элемента
    :param active_element: активный изменяемый элемент, который должен изменить свое состояние
    :param condition:
    :param wait_time:
    :return:
    """
    logging.info(f'{client.device_name} RUNNING... {wait_element.__name__}')
    logging.info(f'{client.device_name} WAITING ELEMENT {element_id}...')
    timestart = time.time()
    while not condition() or (time.time() - timestart) < wait_time:
        active_element.click()
        active_element = client.driver.find_element_by_id(element_id)
    assert active_element
    logging.info(f'{client.device_name} ... ELEMENT {element_id} EXIST\n')
    return active_element


def wait_elements(client, element_id, wait_time=5):
    """
    пытаемся выцепить элементы, которые нам нужны
    :param client: client
    :param element_id: id элементов, которых ждем
    :param wait_time:
    :return:
    """
    logging.info(f'{client.device_name} RUNNING... {wait_elements.__name__}')
    logging.info(f'{client.device_name} WAITING ELEMENTS {element_id}...')
    elements = None
    timestart = time.time()
    while not elements or (time.time() - timestart) < wait_time:
        elements = client.driver.find_elements_by_id(element_id)
    assert len(elements) > 0
    logging.info(f'{client.device_name} FINDING {len(elements)} ELEMENTS\n')
    return elements


def swipe_until_element_and_click(client, element_id, element_text, wait_time=30):
    """
    свайпаем, пока не найдем нужный элемент
    :param client: client
    :param element_id: айди искомого элемента
    :param element_text: текст искомого элемента
    :param wait_time: сколько ждем
    :return:
    """
    logging.info(f'{client.device_name} RUNNING... {swipe_until_element_and_click.__name__}')
    logging.info(f'{client.device_name} LOOKING ELEMENT {element_id} WITH TEXT {element_text}')
    element = None
    timestart = time.time()
    while not element or (time.time() - timestart) < wait_time:
        client.driver.swipe(100, 700, 100, 200)
        possible_elements = client.driver.find_elements_by_id(element_id)
        check = list(filter(lambda x: x.text == element_text, possible_elements))
        if len(check):
            element = check[0]
            break
    assert element
    logging.info(f'{client.device_name} ... ELEMENT {element_id} EXIST\n')
    element.click()


