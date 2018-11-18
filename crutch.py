def push_continue(driver):
    while True:
        try:
            # как же эта ска затрахала
            driver.find_element_by_id('com.mapswithme.maps.pro:id/btn__continue').click()
            break
        except Exception as e:
            continue