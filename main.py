from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import os


def init_driver():
    os.environ["PATH"] += os.pathsep + os.path.join(os.getcwd(), "chrome_driver")
    driver = webdriver.Chrome()
    driver.wait = WebDriverWait(driver, 5)
    return driver


def lookup(driver):
    driver.get("https://www.zhihu.com/question/34672778")
    try:
        driver.wait.until(EC.presence_of_element_located(
            (By.CLASS_NAME, "QuestionHeader-title")))
        button = driver.wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, ".Button.ContentItem-action.Button--plain.Button--withIcon.Button--withLabel")))
        button.click()


        # buttons = driver.find_elements_by_css_selector(".Button.ContentItem-action.Button--plain.Button--withIcon.Button--withLabel")
        # for button in buttons:
        #     button.click()
    except TimeoutException:
        print("Box or Button not found in google.com")


if __name__ == "__main__":
    driver = init_driver()
    lookup(driver)
    # time.sleep(5)
    # driver.quit()