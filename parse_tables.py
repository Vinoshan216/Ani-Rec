import pandas as pd
from bs4 import BeautifulSoup
from io import StringIO



options = 1000

dataframes = []


for page in range(0,options, 50):
  with open("data/{}-{}.html".format(page + 1,page + 50), "r", encoding = "utf-8") as html:
    list_50 = html.read()

  soup = BeautifulSoup(list_50, "html.parser")



  (soup.find("td",class_ = "your-score")).decompose()
  (soup.find("td",class_ = "status")).decompose()



  html_table = soup.find(class_ = "top-ranking-table")



  table = pd.read_html(StringIO(str(html_table)))[0]

  dataframes.append(table)

dataframe_sum = pd.concat(dataframes)

dataframe_sum.to_csv("All-Shows.csv")
