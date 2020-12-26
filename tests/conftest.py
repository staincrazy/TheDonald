import pytest

import test_data


@pytest.fixture(scope="class")
def setup_Chrome(request):
    print("initiating chrome driver")
    driver = webdriver.Chrome("/Users/reonoldpetrenko/PycharmProjects/TheDonald/chromedriver")
    driver.get(test_data.archive_url)
    driver.maximize_window()
    request.cls.driver = driver

    yield driver
    driver.close()
