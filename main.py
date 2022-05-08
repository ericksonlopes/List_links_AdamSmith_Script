from time import sleep
import chromedriver_autoinstaller
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By


def auto_driver() -> webdriver:
    chromedriver_autoinstaller.install()
    chrome_options = Options()

    chrome_options.add_argument("-headless")
    chrome_options.add_argument('--log-level=3')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--disable-dev-shm-usage')

    return webdriver.Chrome(options=chrome_options)


def find_url(id_find: int, driver: webdriver):
    driver.get(f'https://www.adamsmith.haus/python/examples/{id_find}')

    sleep(1)

    try:
        driver.find_element(By.CLASS_NAME, "not-found")

    except NoSuchElementException:
        with open("found_sites.txt", 'a') as file:
            file.write(driver.current_url + '\n')


if __name__ == '__main__':
    driver_for = auto_driver()

    for num in range(5765, 10000):
        print(num)
        find_url(num, driver_for)

    driver_for.close()
