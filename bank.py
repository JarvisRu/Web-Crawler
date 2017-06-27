# include necessary package
# need to install package [pandas lxml html5lib]
import pandas
import html5lib

dfs = pandas.read_html('http://rate.bot.com.tw/xrt?Lang=zh-TW')

print(dfs[0])