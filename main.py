from selenium import webdriver
import os
import time

def prepare_env():
    os.environ["PATH"] += os.pathsep + os.path.join(os.getcwd(), "chrome_driver")

prepare_env()
print os.environ["PATH"]
driver = webdriver.Chrome()
driver.get("https://www.zhihu.com/question/34672778")
time.sleep(5)

button = driver.find_element_by_css_selector(".Button.ContentItem-action.Button--plain.Button--withIcon.Button--withLabel")
button.click()