import pickle
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


def test_books(name):
    driver = webdriver.Chrome()
    driver.get("https://books.google.com/")
    elem = driver.find_element(By.ID, "oc-search-input")  # We select the schearch bar
    print(driver.title)
    elem.clear()
    elem.send_keys(name)
    elem.send_keys(Keys.RETURN)
    time.sleep(5)
    popup = driver.find_element(By.XPATH,
                                "/html/body/c-wiz/div/div/div/div[2]/div[1]/div[3]/div[1]/div[1]/form[2]/div/div/button")
    popup.click()
    time.sleep(2)
    driver.close()


def get_cookie():
    driver = webdriver.Chrome()
    driver.get("https://books.google.com/")

    pickle.dump(driver.get_cookies(), open("pickle.pkl", "wb"))
    driver.close()


def go_look_for_book(name):
    # chrome_options = Options()
    # chrome_options.add_argument("--user-data-dir=chrome-data")
    # driver = webdriver.Chrome(options=chrome_options)
    driver = webdriver.Chrome()
    driver.get("https://books.google.com/")
    assert "Google" in driver.title
    # cookies = pickle.load(open("pickle.pkl", "rb"))
    # for cookie in cookies:                             If u got some problems with the cookies uncomment here and run get cookies before the main
    #    driver.add_cookie(cookie)
    elem = driver.find_element(By.ID, "oc-search-input")  # We select the search bar
    print(driver.title)
    elem.clear()
    elem.send_keys(name)
    elem.send_keys(Keys.RETURN)  # On cherche le livre en question

    time.sleep(2)  # Laisse le temps a la page de charger
    # Clique sur accepter quand la popup viens
    popup = driver.find_element(By.XPATH,
                                "/html/body/c-wiz/div/div/div/div[2]/div[1]/div[3]/div[1]/div[1]/form[2]/div/div/button")
    popup.click()
    time.sleep(2)

    # We verified that there is some result in the page otherwise we send an error
    assert "No results found." not in driver.page_source
    # Closing the session
    driver.close()


if __name__ == '__main__':
    # get_cookie()  # Chopper les cookies
    # time.sleep(3)
    # go_look_for_book("Le parfum")
    test_books("le parfum")
    # If there is some results so we store it in variable and will display it on the cli below

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
