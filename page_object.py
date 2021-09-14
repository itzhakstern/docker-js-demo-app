from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class PageObject:

    def __init__(self):
        self.driver = self.init_driver()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get("http://localhost:3000/")

    def init_driver(self):
        driver = webdriver.Chrome()
        return driver

    def edit_button(self):
        self.driver.find_element_by_xpath('//*[@id="container"]/button').click()

    def edit_name(self):
        name_button = self.driver.find_element_by_id("input-name")
        name_button.clear()
        name_button.send_keys("Itzhak Stern")
        return name_button

    def edit_email(self):
        email_button = self.driver.find_element_by_id("input-email")
        email_button.clear()
        email_button.send_keys("sss@example.com")
        return email_button

    def edit_interests(self):
        interests_button = self.driver.find_element_by_id("input-interests")
        interests_button.clear()
        interests_button.send_keys("AI")
        return interests_button

    def update_button(self):
        self.driver.find_element_by_xpath('//*[@id="container-edit"]/button').click()

    def open_mongo_express(self):
        self.driver.get('http://localhost:8080/')
        self.driver.find_element_by_xpath("/html/body/div/div[2]/div/div[1]/div[2]/table/tbody/tr[4]/td[2]/h3/a").click()
        self.driver.find_element_by_xpath("/html/body/div/div[2]/div/div[1]/div[2]/table/tbody/tr/td[5]/h3/a").click()

    def mongo_express_data(self):
        return self.driver.find_elements_by_class_name("tableContent")

    def mongo_express_name(self):
        return self.mongo_express_data()[4].text

    def mongo_express_email(self):
        return self.mongo_express_data()[2].text

    def mongo_express_interests(self):
        return self.mongo_express_data()[3].text
