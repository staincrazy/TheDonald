import time

from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ChromeOptions, ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import test_data

opts = ChromeOptions()
opts.add_experimental_option("detach", True)


def russia_test():
    driver = webdriver.Chrome(test_data.driver_path, chrome_options=opts)
    driver.get(test_data.archive_url)
    driver.maximize_window()
    driver.find_element_by_xpath(test_data.archive_searchbox).send_keys(test_data.russia)
    time.sleep(10)
    results = driver.find_element_by_xpath(".//span[@class='results___1pfEc']")
    n_max = int(results.text)
    n = 1

    while n < n_max:
        tweet = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, ".//div[@class='tweet___2xXtA ttaTweet']" + "[" + str(n) + "]")))
        if "Obama" in tweet.text:
            driver.save_screenshot(str(n)+".png")

        n += 1
        driver.find_element_by_xpath(".//body").send_keys(Keys.PAGE_DOWN)
    driver.close()


if __name__ == "__main__":
    russia_test()
