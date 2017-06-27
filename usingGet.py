import requests
from bs4 import BeautifulSoup

res = requests.get("http://www.uniqlo.com/tw/store/list/sale/men/tops")
soup = BeautifulSoup(res.text,"html.parser")

for item in soup.select('.unit'):
	print(item.select('.name')[0].text,item.select('.price')[0].text)
