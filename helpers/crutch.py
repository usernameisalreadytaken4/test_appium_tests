import time


def push_continue(driver):
    """
    Периодически багается вход, хотя на самом деле - он работает.
    """
    _id = 'com.mapswithme.maps.pro:id/btn__continue'
    timestart = time.time()
    while True or (time.time() - timestart) < 5:
        try:
            driver.find_element_by_id(_id).click()
            return
        except Exception:
            print('\n****** ANOTHER BUG WITH CONTINUE BUTTON ******')
            continue
    raise Exception(f'\n{_id} not work')
