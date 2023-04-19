import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"

html = requests.get(url)

#print(html.text)

s = BeautifulSoup(html.content,'html.parser')
#results = s.find(id='ResultsContainer')
company_name = s.find_all('a')

print(company_name)