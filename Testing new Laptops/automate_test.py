import time
from selenium import webdriver
from selenium.webdriver.edge.service import Service

start_time = time.time()

# Path to Microsoft Edge Driver on Windows 11
edge_service = Service('C://WebDrivers/msedgedriver.exe')
# creating a new instance of the Edge Driver
driver = webdriver.Edge(service=edge_service)

# automating tabs to open
for i in range(20):
    driver.execute_script("window.open('https://www.youtube.com');")
    driver.switch_to.window(driver.window_handles[i])


end_time = time.time()
total_time = end_time - start_time
print(f"Total time to open 30 tabs and go to YouTube in each tab: {total_time} seconds.")
