
import requests
from bs4 import BeautifulSoup
import pandas as pd
# html_doc = """
# <html><head><title>The Dormouse's story</title></head>
# <body>
# <p class="title"><b>The Dormouse's story</b></p>

# <p class="story">Once upon a time there were three little sisters; and their names were
# <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
# <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
# <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
# and they lived at the bottom of a well.</p>

# <p class="story">...</p>
# """
# soup = BeautifulSoup(html_doc, "html.parser")

# print(soup.find_all("<p"))

# for link in soup.find_all('a'):
#     print((link.get('href')))

# type(soup)

url = "https://data.gov.my/dashboard/car-popularity"
html = requests.get(url)
soup = BeautifulSoup(html.text, "html.parser")

# table = soup.find('table').prettify
# rows = soup.find_all('tr')

# for r in rows:
#     cols = r.get_text('td')
#     print(cols)
totalNo = soup.find_all("td", class_ = "px-1 py-2 text-end text-sm font-medium tabular-nums")


rows = soup.find_all('td', class_ = 'w-1/2 px-1 py-2 text-start text-sm font-medium capitalize')

totals = [t.text.strip() for t in totalNo]

cars = [c.text.strip() for c in rows]

print(totals)
print(cars)

# for row in rows:
#     print(row.text)

# for jumlah in totalNo:
#     print(jumlah.text)

print("Jumlah Kereta mengikut jenama")

for kereta, jumlah in zip(cars,totals):
    print(f"{kereta} : {jumlah}")

# -----------------------------------------

# url = "https://quotes.toscrape.com"
# response = requests.get(url)
# soup = BeautifulSoup(response.text, "html.parser")
# word500 = soup.prettify()[:500] #print 500 words

# quotes = soup.find_all("span", class_="text")

# for quote in quotes:
#     print(quote.text)


# ----------------------------------------------------

# print to excel

df = pd.DataFrame({
    "Jenama": cars,
})
df.to_excel("Jenama Kerta Malaysia.xlsx",index=False)