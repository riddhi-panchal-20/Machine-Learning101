from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pandas as pd
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webelement import WebElement
from datetime import datetime
import sys
import os

app_path = os.path.dirname(sys.executable)
now = datetime.now()
day_month_year = now.strftime("%d%m%y")

website = "https://www.ndtv.com/"
service = Service(executable_path=r"C:\Users\lenovo\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe")
options = webdriver.ChromeOptions()
options.headless = True
driver = webdriver.Chrome(service=service, options=options)
driver.get(website)

containers = driver.find_elements(by="xpath", value='//div[@class="featured_cont"]/span/ul/li')
titles = []
links = []

for c in containers:
    title = c.find_element(by="xpath", value=".//h2/a[2]").text
    link = c.find_element(by="xpath", value=".//h2/a[2]").get_attribute("href")
    #print(title)
    #print(link)
    titles.append(title)
    links.append(link)

my_dict = {'title': titles, 'link':links}
top_ten = pd.DataFrame(my_dict)

file_name = f'new_headlines{day_month_year}.csv'
final_path = os.path.join(app_path, file_name)
top_ten.to_csv(final_path)
driver.quit()
