import pandas as pd
from bs4 import BeautifulSoup
import re



def html_to_csv(options):
  from main import create_folder 

  create_folder("CSV")

  dataframes = []
  counter = 0

  for page in range(0,options, 50):
    with open("HTML/{}-{}.html".format(page + 1,page + 50), "r", encoding = "utf-8") as html:
      list_50 = html.read()

    soup = BeautifulSoup(list_50, "html.parser")

    rows = soup.find_all("tr", class_ = "ranking-list")

    ranks, titles, urls, scores, index = ([] for i in range(5))

    
    for row in rows:
      index.append(counter)
      counter += 1
      ranks.append(row.find("td", class_ = "rank ac").span.text)
      titles.append(re.sub(r'\W+', ' ',row.find("div", class_ = "di-ib clearfix").a.text))
      scores.append(row.find("td", class_ = "score ac fs14").text)
      urls.append(row.find("div", class_ = "di-ib clearfix").a["href"])

    dict = {"Rank": ranks, "Title": titles, "Score": scores, "URL": urls}

    dataframe = pd.DataFrame(dict, index = index)
    
    dataframes.append(dataframe)


  df = pd.concat(dataframes)

  df.to_csv("CSV/All-Shows.csv")
