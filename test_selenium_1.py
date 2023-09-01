import time


def test_search_example(selenium):
    selenium.get('https://google.com')

    time.sleep(5)

    search_input = selenium.find_element_by_id('APjFqb')
    search_input.clear()
    search_input.send_keys('first test')

    time.sleep(5)

    search_button = selenium.find_element_by_name('btnK')
    search_button.submit()

    time.sleep(10)

    selenium.save_screenshot('result.png')