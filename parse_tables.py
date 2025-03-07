import pandas as pd
from bs4 import BeautifulSoup
from io import StringIO
import re



options = 1000

dataframes = []
elements = []

class Show:
  def __init__(self, rank, title, score, url):
    self.rank = rank
    self.title = title
    self.score = score
    self.url = url

for page in range(0,options, 50):
  with open("data/{}-{}.html".format(page + 1,page + 50), "r", encoding = "utf-8") as html:
    list_50 = html.read()

  soup = BeautifulSoup(list_50, "html.parser")

  rows = soup.find_all("tr", class_ = "ranking-list")

  for row in rows:
    show = Show (
      rank = row.find("td", class_ = "rank ac").text,
      title = re.sub(r'\W+', ' ',row.find("div", class_ = "di-ib clearfix").a.text),
      score = row.find("td", class_ = "score ac fs14").text,
      url = str(row.find("div", class_ = "di-ib clearfix").a["href"])
    )
    elements.append(show)


  

  """

  html_table = soup.find(class_ = "top-ranking-table")
  

  (html_table.find("tr", class_ = "table-header")).decompose()


  containers = html_table.find_all("h3", class_ = "fl-l fs14 fw-b anime_ranking_h3")

  
  for container in containers:
    urls.append(container.a["href"])
    




  table = pd.read_html(StringIO(str(html_table)))[0]
  

  


  dataframes.append(table)


dataframe_sum = pd.concat(dataframes)
df = dataframe_sum.drop(columns=[3,4])

df.rename(columns = {0: "Rank", 1: "Title", 2: "Score"}, inplace = True)

df["URLs"] = urls
print(df["Title"])

#dataframe_sum.to_csv("All-Shows.csv")
"""


for element in elements:
  print(element.title)