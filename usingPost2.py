# include necessary package
# need to install package [requests BeautifulSoup4]
import requests
from bs4 import BeautifulSoup

# get form data from post
payload = {
	'StartStation':'977abb69-413a-4ccf-a109-0272c24fd490',
	'EndStation':'f2519629-5973-4d08-913b-479cce78a356',
	'SearchDate':'2017/06/28',
	'SearchTime':'06:30',
	'SearchWay':'DepartureInMandarin',
	'RestTime':'',
	'EarlyOrLater':'',
	'DiscountType':'68d9fc7b-7330-44c2-962a-74bc47d2ee8a'
}

# initial set
res = requests.post("https://www.thsrc.com.tw/tw/TimeTable/SearchResult", data = payload)
soup = BeautifulSoup(res.text,"html.parser")

# save data into txt file
file = open('train.txt', 'w', encoding = 'UTF-8')
file.write("車次  行車時間  出發時間  抵達時間\n")
for item in soup.select('.touch_table'):
	train = item.select('.column1')[0].text
	needTime = item.select('.column2')[0].text
	goTime = item.select('.column3')[0].text
	arriveTime = item.select('.column4')[0].text
	file.write(train+"    "+needTime+"    "+goTime+"     "+arriveTime+"\n")
	file.write("-------------------------------\n")

file.close()