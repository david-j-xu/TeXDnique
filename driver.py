from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from html import unescape

# skip if the value is under this number of points
THRESHOLD = 15


driver = webdriver.Chrome()
driver.get("https://texnique.xyz")
start = driver.find_element(By.ID, "start-button-timed")
start.click()

while True:
    try:
        latex = driver.find_element(By.ID, "target").find_element(
            By.TAG_NAME, "annotation").get_attribute("innerHTML")
        latex = unescape(latex)

        pt_value = int(driver.find_element(
            By.ID, "problem-points").get_attribute("innerHTML").split(" ")[0][1:])

        if (pt_value < THRESHOLD):
            driver.find_element(By.ID, "skip-button").click()
            continue

        input = driver.find_element(By.ID, "user-input")

        input.send_keys(latex)
        WebDriverWait(driver, 10).until_not(lambda x: x.find_element(
            By.ID, "user-input") and x.find_element(By.ID, "user-input").get_attribute("value") == latex)
    except Exception as _:
        break

driver.save_screenshot("lel.png")
driver.close()
