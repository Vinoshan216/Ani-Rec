import os

from scrape import scraper_start
from parse_tables import html_to_csv

def create_folder(path):
  try:
    os.mkdir(path)
  except FileExistsError:
    print(f"Directory '{path}' already exists.")
  except PermissionError:
      print(f"Permission denied: Unable to create '{path}'.")
  except Exception as e:
      print(f"An error occurred: {e}") 

url_start = "https://myanimelist.net/topanime.php?limit={}"
options = 1000

#scraper_start(url_start,options)
html_to_csv(options)
