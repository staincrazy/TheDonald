import time
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ChromeOptions, ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

import test_data

opts = ChromeOptions()
opts.add_experimental_option("detach", True)


class TestClass:

    def __init__(self):
        print("initiating chrome driver")
        self.driver = webdriver.Chrome("/Users/reonoldpetrenko/PycharmProjects/TheDonald/chromedriver")
        self.driver.get(test_data.archive_url)
        self.driver.maximize_window()

    def test_navigation(self):
        print("performing login")
        assert self.driver.find_element_by_xpath(".//*[text()='Trump Twitter Archive ']").is_displayed()

    def test_enemy(self, keyword):
        print("performing test for the keyword " + keyword)
        actions = ActionChains(self.driver)
        self.driver.find_element_by_xpath(test_data.archive_searchbox).clear()
        self.driver.find_element_by_xpath(test_data.archive_searchbox).send_keys(keyword)
        time.sleep(10)
        results = self.driver.find_element_by_xpath(".//span[@class='results___1pfEc']")
        n_max = int(results.text)
        # driver.find_element_by_xpath(".//body").send_keys(Keys.END)

        n = 1

        while n < n_max:
            try:
                tweet = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located(
                        (By.XPATH, ".//div[@class='tweet___2xXtA ttaTweet']" + "[" + str(n) + "]")))

                actions.move_to_element(tweet)

            except TimeoutException as e:
                print("Timeout exception on the element: " + str(n))
                self.driver.find_element_by_xpath(".//body").send_keys(Keys.PAGE_DOWN)

            if test_data.enemy in tweet.text:
                actions.move_to_element(tweet)
                try:
                    show = self.driver.find_element_by_xpath \
                        ("//div[@class='tweet___2xXtA ttaTweet']" + "[" + str(n) + "]//span[text()='Show']/div/*")
                    try:
                        show.click()
                        self.driver.save_screenshot(keyword + str(n) + ".png")

                    except ElementClickInterceptedException as e:
                        print("This element is not clickable " + str(n))
                except NoSuchElementException as e:
                    print("This element cannot be located: " + str(n))

            n += 1

    def tear_down(self):
        self.driver.close()


if __name__ == "__main__":
    test = TestClass()
    test.test_navigation()
    test.test_enemy()
    test.test_enemy(test_data.russia)
    test.test_enemy(test_data.collusion)
    test.tear_down()
