import argparse
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


def print_hi(name):

if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get("http://www.amazon.fr")
    assert "Amazon" in driver.title
    elem = driver.find_element(By.NAME, "field-keywords")  # We select the schearch bar
    elem.clear()
    elem.send_keys("vélo")
    elem.send_keys(Keys.RETURN)
    assert "No results found." not in driver.page_source
    #If there is some results so we
    driver.close()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
