# include necessary package
# need to install package [pandas lxml html5lib / datetime / openpyxl]
import pandas
import html5lib
from datetime import datetime

# initial set
dfs = pandas.read_html('http://rate.bot.com.tw/xrt?Lang=zh-TW')
dataFrame = dfs[0]

# get 0~5 columns of data 
USD = dataFrame.ix[0:0,0:5]

# set column name and set as unicode
USD.columns = [u'幣別',u'現金匯率-本行買入',u'現金匯率-本行賣出',u'即期匯率-本行買入',u'即期匯率-本行賣出']

# save time now
USD['時間'] = datetime.now().strftime('%Y-%m-%d')

# set USD
money 	= USD.ix[0,'幣別']
buy1 	= USD.ix[0,'現金匯率-本行買入']
sell1 	= USD.ix[0,'現金匯率-本行賣出']
buy2 	= USD.ix[0,'即期匯率-本行買入']
sell2 	= USD.ix[0,'即期匯率-本行賣出']
time 	= USD.ix[0,'時間']

# ------------------------
# write into txt file    |
# ------------------------
file = open('USD.txt', 'a', encoding = 'UTF-8')
file.write('USD | '+buy1+"  |  "+sell1+"  |  "+buy2+"  |  "+sell2+"  |  "+time+"   \n")

# ------------------------
# read all data          |
# ------------------------
# file = open('USD.txt','r', encoding='UTF-8')
# line = file.read()	
# print(line)

# ------------------------
# read particular line   |
# ------------------------
# file = open('USD.txt','r', encoding='UTF-8')
# line = file.readlines()	
# print(line[idx])

# ---------------------------------------------
# read particular line and particular column  |
# ---------------------------------------------
# file = open('USD.txt','r', encoding='UTF-8')
# line = file.readlines()	
# last = line[-1]
# buy1Num  = float(last[6:13])
# sell1Num = float(last[15:23])
# buy2Num  = float(last[28:34])
# sell2Num = float(last[37:45])
# print( )


file.close()