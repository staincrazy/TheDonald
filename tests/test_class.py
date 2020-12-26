import time
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ChromeOptions, ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import test_data

# This setting helps not to close Chrome before the test executes

opts = ChromeOptions()
opts.add_experimental_option("detach", True)


class TestClass:

    # Initiates chrome driver

    def __init__(self):
        print("initiating chrome driver")
        self.driver = webdriver.Chrome(test_data.driver_path)
        self.driver.get(test_data.archive_url)
        self.driver.maximize_window()

    # Navigate to url and verifies if the navigation is successful

    def test_navigation(self):
        print("performing login")
        assert self.driver.find_element_by_xpath(test_data.twetter_name).is_displayed()

    # Takes the keyword that is passed when class and method is called, and performs search

    def test_enemy(self, keyword):

        print("performing test for the keyword " + keyword)

        self.driver.find_element_by_xpath(test_data.archive_searchbox).clear()
        self.driver.find_element_by_xpath(test_data.archive_searchbox).send_keys(keyword)

        time.sleep(5)

        # results variable is used to store search results and convert it to integer

        results = self.driver.find_element_by_xpath(test_data.results_on_the_page)
        n_max = int(results.text)

        # n variable is used for proper xpath. when several elements on the page have the same xpath they can be
        # parsed using special counter (e.g. [1], [2], [3]....)

        n = 1

        # now we parse through tweets on the page from 1 to results using while cycle

        while n < n_max:
            try:
                tweet = WebDriverWait(self.driver, 5).until(
                    EC.presence_of_element_located(
                        (By.XPATH, ".//div[@class='tweet___2xXtA ttaTweet']" + "[" + str(n) + "]")))

            except TimeoutException as e:
                print("Timeout exception on the element: " + str(n))
                self.driver.find_element_by_xpath(".//body").send_keys(Keys.PAGE_DOWN)

            # here we check if enemy's name is presented in each tweet
            # and if so we try to click "Show" button to open original tweet
            # and make a screenshot of it with the name of "keyword + n(tweet number)"

            if test_data.enemy in tweet.text:

                try:
                    show = self.driver.find_element_by_xpath \
                        ("//div[@class='tweet___2xXtA ttaTweet']" + "[" + str(n) + "]//span[text()='Show']/div/*")
                    try:
                        show.click()
                        self.driver.execute_script("arguments[0].scrollIntoView();", show)
                        time.sleep(5)
                        self.driver.save_screenshot(keyword + str(n) + ".png")

                    except ElementClickInterceptedException as e:
                        print("This element is not clickable " + str(n))
                except NoSuchElementException as e:
                    print("This element cannot be located: " + str(n))

            n += 1

    def tear_down(self):
        self.driver.close()


# here we call our test method and call particular functions

if __name__ == "__main__":
    test = TestClass()
    test.test_navigation()
    test.test_enemy(test_data.both_words)
    test.test_enemy(test_data.russia)
    test.test_enemy(test_data.collusion)
    test.tear_down()
