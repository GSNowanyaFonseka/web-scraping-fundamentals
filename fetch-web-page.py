import pandas as pd  # data analysis and manopulation (hanlde tabular dataset)
import requests   # sending http requests to fetch webpage content
from bs4 import BeautifulSoup   # parse HTML and extract data from web pages

# url of the webpage to scrape data 
url = 'https://en.wikipedia.org/wiki/List_of_largest_manufacturing_companies_by_revenue'
response = requests.get(url)  # sends GET requests to the given URL 

# check if the requests successfull
# 200 - success
# 500  - internal server error
# 404 - page not founD
if response.status_code == 200:
    print("Successfully fetched the webpage!")
else:
    print("Faild to fetch the webpage") 

# print(response.text)  html sorce code

# parse the html content of the web page using beautifulsoup
# soup - Object of the BeautifulSoup class (it represents the HTML content in a more structured form)
soup = BeautifulSoup(response.text, "html")

# find all <h2> elements that have the class "product-title"
# this helps locate product titles on the webpage
# products - list 
soup.find("table", class_="wikitable sortable plainrowheads jquery-tablesorter")
table = soup.find_all('table')[0]

world_titles = table.find_all('th')

print(world_titles)

# extract and clean the text from each product title
# .text gets the text inside the tag, and .strip() removes extra spaces
world_table_titles = [title.text.strip() for title in world_titles]

# print the list of extracted product names
print(world_table_titles)

df = pd.DataFrame(columns=world_table_titles)
df

column_data = table.find_all('tr')

for row in column_data[1:]:
    row_data = row.find_all('td')
    individual_row_data = [data.text.strip() for data in row_data]

    length = len(df)
    df.loc[length] = individual_row_data


print(df)

df.to_csv(r'C:\Users\Hp\Desktop\Web Scaping Fundamentals\web-scraping-fundamentals\scraping-data.csv', index=False)






