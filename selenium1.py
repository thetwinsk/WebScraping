#import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

#os.environ['PATH'] += r"/Users/kaylanguyen/PycharmProjects/pythonProject/SeleniumDrivers"
driver = webdriver.Chrome("/Users/kaylanguyen/PycharmProjects/pythonProject/SeleniumDrivers/chromedriver")

# driver.get("https://jqueryui.com/resources/demos/progressbar/download.html")
# driver.implicitly_wait(8) #time.sleep(30)
# my_element = driver.find_element_by_id('downloadButton')
# my_element.click()

# progress_element = driver.find_element_by_class_name('progress-label')
# print(f"{progress_element.text == 'Completed!'}")

# WebDriverWait(driver, 30).until(
#     EC.text_to_be_present_in_element(
#         (By.CLASS_NAME, 'progress-label') , # Element filtration
#         'Completed!' # The expected text
#     )
# )

driver.get("https://syntaxprojects.com/basic-first-form-demo.php")
driver.implicitly_wait(5)

try: #for this case in direct Selenium Easy with pop-up appearing
    no_button = driver.find_element_by_class_name('at-cm-no-button')
    no_button.click()
except:
    print('No element with this class name. Skipping...')

sum1 = driver.find_element_by_id('sum1')
sum2 = driver.find_element_by_id('sum2')

sum1.send_keys(Keys.NUMPAD1, Keys.NUMPAD5)
sum2.send_keys(24)

btn = driver.find_element_by_css_selector('button[onclick="return total()"]')
btn.click()