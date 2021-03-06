# include necessary package
# need to install package [pandas lxml html5lib / datetime / openpyxl]
import pandas
import html5lib
from datetime import datetime
# initial set
dfs = pandas.read_html('http://rate.bot.com.tw/xrt?Lang=zh-TW')
dataFrame = dfs[0]

# get 0~5 columns of data 
fiveCol = dataFrame.ix[:,0:5]
# set column name and set as unicode
fiveCol.columns = [u'幣別',u'現金匯率-本行買入',u'現金匯率-本行賣出',u'即期匯率-本行買入',u'即期匯率-本行賣出']
# save time now
fiveCol['時間'] = datetime.now().strftime('%Y-%m-%d')

# # save as excel file
fiveCol.to_excel('bank.xlsx')
