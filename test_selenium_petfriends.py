import time

def test_petfriends(selenium):
    selenium.get("https://petfriends.skillfactory.ru/")

    time.sleep(5)

    btn_newuser = selenium.find_element_by_xpath("//button[@onclick=\"document.location='/new_user';\"]")

    btn_newuser.click()

    btn_exist_acc = selenium.find_element_by_link_text(u"У меня уже есть аккаунт")
    btn_exist_acc.click()

    field_email = selenium.find_element_by_id("email")
    field_email.clear()
    field_email.send_keys("cerber19912@gmail.com")

    field_pass = selenium.find_element_by_id("pass")
    field_pass.clear()
    field_pass.send_keys("Cnhjbntkm4556")

    btn_submit = selenium.find_element_by_xpath("//button[@type='submit']")
    btn_submit.click()

    time.sleep(10)

    if selenium.current_url == 'https://petfriends.skillfactory.ru/all_pets':
        selenium.save_screenshot('result_petfriends.png')
    else:
        raise Exception("login error")