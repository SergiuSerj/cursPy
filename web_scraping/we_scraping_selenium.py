from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get("https://www.emag.ro")

element = driver.find_element(by=By.ID, value="searchboxTrigger")
element.send_keys("iphone 14")
element.submit()

count_phones = driver.find_elements(by=By.CLASS_NAME, value="card-item")
print(len(count_phones))


for i in range(1, len(count_phones)+1):
    phones = driver.find_element(by=By.XPATH, value= f"// *")