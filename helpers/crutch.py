import time


def push_continue(driver):
    """
    Периодически багается вход, хотя на самом деле - он работает.
    """
    timestart = time.time()
    while True or (time.time() - timestart) < 5:
        try:
            driver.find_element_by_id('com.mapswithme.maps.pro:id/btn__continue').click()
            return
        except Exception as e:
            continue
    raise Exception('btn__continue not work')


def waiting(element, _time=5):
    pass