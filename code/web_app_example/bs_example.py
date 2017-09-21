import requests
from bs4 import BeautifulSoup

result = requests.get("http://localhost:8080/tasks")
assert result.status_code == 200
print(result.text)

soup = BeautifulSoup(result.text, 'html.parser')
table = soup.find('table')
for tr in table.find_all("tr"):
    x = [td.text for td in tr.find_all("td")]
    print(x)
