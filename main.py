
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

def go_look_for_book(name):

    driver = webdriver.Chrome()
    driver.get("https://books.google.com/")
    assert "Google" in driver.title
    elem = driver.find_element(By.ID, "oc-search-input")  # We select the schearch bar
    elem.clear()
    elem.send_keys(name)
    elem.send_keys(Keys.RETURN)

    assert "No results found." not in driver.page_source

    driver.close()

if __name__ == '__main__':
    go_look_for_book("Le parfum")
    # If there is some results so we store it in variable and will display it on the cli below



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
