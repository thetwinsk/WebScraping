# This file will include a class with instance methods
# That will be responsible to interact with our website
# After we have some results, to apply filtration
from typing import List
from selenium.webdriver.remote.webdriver import WebDriver


class BookingFiltration:
    def __init__(self, driver:WebDriver):
        #pass # ignore the error
        self.driver = driver


    def apply_star_rating(self, *star_values):
        star_filtration_box = self.driver.find_element_by_xpath(
            '//*[@id="searchboxInc"]/div[1]/div/div/div[1]/div[5]')
        star_child_elements = star_filtration_box.find_elements_by_css_selector("*")
        #print(len(star_child_elements))

        for star_value in star_values:
            for star_element in star_child_elements:
                if str(star_element.get_attribute('innerHTML')).strip() == f'{star_value} stars':
                    star_element.click()

    def sort_price_lowest_first(self):
        element = self.driver.find_element_by_css_selector(
            'li[data-id="price"]'
        )
        element.click()
