# include necessary package
import requests
from bs4 import BeautifulSoup

# initial set
res = requests.get("http://www.uniqlo.com/tw/store/list/sale/men/tops")
soup = BeautifulSoup(res.text,"html.parser")

# print data i need
for item in soup.select('.unit'):
	print(item.select('.name')[0].text,item.select('.price')[0].text)
