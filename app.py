from multiprocessing import Value
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import pyautogui
from selenium.common.exceptions import NoSuchElementException

contact = "Test"
waiter_contact = "Waiter"
text = "Hey, this message was sent using Selenium"
driver = webdriver.Chrome()
driver.get("https://web.whatsapp.com")
print("Scan QR Code, And then Enter")
input()
print("Logged In")
# inp_xpath_search = "/html/body/div[1]/div/div/div[4]/div/div[1]/div/div/div[2]/div/div[1]"
# input_box_search = WebDriverWait(driver,50).until(lambda driver: driver.find_element(by=By.XPATH, value=inp_xpath_search))
# input_box_search.click()
# time.sleep(2)
# input_box_search.send_keys(contact)
# time.sleep(2)
# selected_contact = driver.find_element(by=By.XPATH, value="//span[@title='"+contact+"']")
# selected_contact.click()
# inp_xpath = '/html/body/div[1]/div/div/div[5]/div/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]'
# input_box = driver.find_element(by=By.XPATH, value=inp_xpath)
# time.sleep(2)
# input_box.send_keys(text + Keys.ENTER)
# time.sleep(2)

while True:

    try:
        time.sleep(3)
        # circle_xpath = '//*[@id="pane-side"]/div[2]/div/div/div[1]/div/div/div/div[2]/div[2]/div[2]/span[1]/div/span'
        # circle = driver.find_element(by=By.XPATH, value=circle_xpath)
        print("New message")
        res = pyautogui.locateOnScreen("message.png", confidence=0.8)
        if res != None:
            res_center = pyautogui.center(res)
            x, y = res_center
            pointer = x-20, y
            print(res_center)
            print(pointer)
            pyautogui.moveTo(pointer)
            pyautogui.click()
            time.sleep(1)
            elements = WebDriverWait(driver, 20).until(EC.visibility_of_all_elements_located((By.CLASS_NAME, "_21Ahp")))
            # for element in elements:
            #     print(element.text)
            latest_message = elements[len(elements)-1].text
            incident_id_index = str(latest_message).find("Incident Id")
            incident_id = latest_message[ incident_id_index + 13 : incident_id_index + 8+13]
            circuit_id_index = str(latest_message).find("Circuit Id")
            circuit_id = latest_message[circuit_id_index + 12 : circuit_id_index + 33+12]
            incident_time_index = str(latest_message).find("Incident Time")
            incident_time = latest_message[incident_time_index + 15 : incident_time_index + 20+15]
            summary_index = str(latest_message).find("Summary")
            summary = latest_message[summary_index + 9 : len(latest_message)-1]
    
            payload = {
                "Body": latest_message,
                "Incident Id": incident_id,
                "Circuit Id": circuit_id,
                "Incident Time": incident_time,
                "Summary": summary
            }

            print(payload)
        
        inp_xpath_search = "/html/body/div[1]/div/div/div[4]/div/div[1]/div/div/div[2]/div/div[1]"
        input_box_search = WebDriverWait(driver,50).until(lambda driver: driver.find_element(by=By.XPATH, value=inp_xpath_search))
        input_box_search.click()
        time.sleep(2)
        input_box_search.send_keys(waiter_contact)
        time.sleep(2)
        selected_contact = driver.find_element(by=By.XPATH, value="//span[@title='"+waiter_contact+"']")
        selected_contact.click()
        waiter_back_button_xpath = "/html/body/div[1]/div/div/div[4]/div/div[1]/div/div/button"
        waiter_back_button = driver.find_element(by=By.XPATH, value=waiter_back_button_xpath)
        waiter_back_button.click()
        # waiter_back_xpath = '//*[@id="pane-side"]/div[2]/div/div/div[1]/div/div/div/div[2]/div[2]/div[2]/span[1]/div/span'
        # waiter_back = driver.find_element(by=By.XPATH, value=waiter_back_xpath)
        # res = pyautogui.locateOnScreen("message.png", confidence=0.8)
        time.sleep(3)
    except NoSuchElementException:
        print("No new messages")

    
    

    # time.sleep(2)

    # elements = WebDriverWait(driver, 20).until(EC.visibility_of_all_elements_located((By.CLASS_NAME, "_21Ahp")))

    # for element in elements:
    #     print(element.text)

driver.quit()