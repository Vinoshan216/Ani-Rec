from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
from main import create_folder 



create_folder("data")

def scraper_start(url_start, options):
  for i in range(0,options,50):

    opt = Options()
    opt.add_argument("--headless")

    driver = webdriver.Chrome(options=opt)

    url = url_start.format(i)

    driver.get(url)

    driver.execute_script("window.scrollTo(1,100000)")

    time.sleep(5)

    html = driver.page_source

    with open("data/{}-{}.html".format((i+1),(i+50)), "w+", encoding="utf-8") as f:
      f.write(html)
