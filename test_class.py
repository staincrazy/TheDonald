import time
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ChromeOptions, ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import test_data

opts = ChromeOptions()
opts.add_experimental_option("detach", True)


class TheDonald:

    def __init__(self):
        self.driver = webdriver.Chrome(test_data.driver_path, chrome_options=opts)

    def take_screenshot(self, tweet):
        driver = self.driver
        driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 't')
        driver.get(test_data.url)
        time.sleep(3)
        driver.find_element_by_xpath(".//input").send_keys(tweet, Keys.RETURN)
        time.sleep(3)
        driver.find_element_by_xpath(".//*[text()='" + tweet + "]").click()
        driver.get_screenshot_as_png()
        driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 'w')

    def collusion_test(self):
        driver = self.driver
        driver.get(test_data.archive_url)
        driver.maximize_window()
        driver.find_element_by_xpath(test_data.archive_searchbox).send_keys(test_data.collusion)
        time.sleep(10)
        results = driver.find_element_by_xpath(".//span[@class='results___1pfEc']")
        n_max = int(results.text)
        n = 1

        while n < n_max:
            tweet = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, ".//div[@class='tweet___2xXtA ttaTweet']" + "[" + str(n) + "]")))

            if test_data.enemy in tweet.text:
                show = tweet.find_element_by_xpath(".//span[text()='Show']/div/..")
                show.click()
                driver.get_screenshot_as_png()
                time.sleep(1)

            n += 1
            driver.find_element_by_xpath(".//body").send_keys(Keys.PAGE_DOWN)
        driver.close()

    def russia_test(self):
        actions = ActionChains(self.driver)
        driver = self.driver
        driver.get(test_data.archive_url)
        driver.maximize_window()
        driver.find_element_by_xpath(test_data.archive_searchbox).send_keys(test_data.russia)
        time.sleep(10)
        results = driver.find_element_by_xpath(".//span[@class='results___1pfEc']")
        n_max = int(results.text)
        n = 1

        while n < n_max:
            tweet = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, ".//div[@class='tweet___2xXtA ttaTweet']" + "[" + str(n) + "]")))
            actions.move_to_element(tweet)
            if test_data.enemy in tweet.text:
                show = tweet.find_element_by_xpath("//span[text()='Show']/div/*")
                print(show)
                driver.save_screenshot(str(n)+".png")
            n += 1
            driver.find_element_by_xpath(".//body").send_keys(Keys.PAGE_DOWN)
        driver.close()


if __name__ == "__main__":
    a = TheDonald()
    a.russia_test()
