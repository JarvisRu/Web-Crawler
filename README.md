# Web-Crawler
Using python3 and packages
<ol>
  <li>requests : Get the source code of target web</li>
  <li>BeautifulSoup4 : Analysis and filter data</li>
  <li>pandas / lxml / html5lib : To get dataFram easily</li>
  <li>openpyxl : Do some work on excel file like read or write</li>
  <li>datetime : Get time</li>
</ol>

<hr>
Following is my test file:

<h3>usingGet.py</h3>
<i>Need : requests / BeautifulSoup4</i>

<i>Import : requests / BeautifulSoup4</i>
<ol>
  <li>Get source code by <b>Method : Get</b></li>
  <li>Get the Item_Name and Price from <a href="http://www.uniqlo.com/tw/store/list/sale/men/tops">UNIQLO Web Store</a></li>
</ol>


<h3>usingPost.py / usingPost2.py</h3>
<i>Need : requests / BeautifulSoup4</i>

<i>Import : requests / BeautifulSoup4</i>
<ol>
  <li>Get source code by <b>Method : Post</b></li>
  <li>Get the data I select from <a href="https://www.thsrc.com.tw/tw/TimeTable/SearchResult">Taiwan High Speed Rail</a>
  <ul>
    <li>Train Number</li>
    <li>Required Time</li>
    <li>Estimated Time of Departure</li>
    <li>Estimated Time of Arrived</li>
  </ul></li>
  <li>Print the result / Save the resul into .txt file</li>
</ol>

<hr>

<h3>bank</h3>
<h4>bank.py</h4>
<i>Need : pandas / lxml / html5lib / xlms / datetime</i>

<i>Import : pandas / html5lib / datetime </i>
<ol>
  <li>Get source code by <b>pandas.read_html</b></li>
  <li>Change data(table) into dataFrame from <a href="http://rate.bot.com.tw/xrt?Lang=zh-TW">Foreign Exchage Rate</a></li>
  <li>Get the data I select into new table</li>
  <li>Save the reuslt and time now into excel file</li>
</ol>

<h4>bank_USD.py</h4>
<i>Need : pandas / lxml / html5lib / xlms / datetime</i>

<i>Import : pandas / html5lib / datetime </i>
<ol>
  <li>Get source code by <b>pandas.read_html</b></li>
  <li>Change data(table) into dataFrame from <a href="http://rate.bot.com.tw/xrt?Lang=zh-TW">Foreign Exchage Rate</a></li>
  <li>Get the USD data into new table</li>
  <li>Save the reuslt and time now into <b>USD.txt</b> (By append)</li>
  <li>Read:
    <ul>
      <li>Read all</li>
      <li>Read particular line</li>
      <li>Read particular data</li>
    </ul>
  </li>
</ol>

<h4>bank_mail.py</h4>

<i>Import : smtplib / MIMEMultipart / MIMEText </i>

<ol>
  <li>Read data from <b>USD.txt</b></li><li>If the <i>現金匯率-本行賣出"(sell1)</i>  lower than <i>Hit_Price</i></li><li>Send an email to "toAddr" to inform that it's the buying timing</li>
</ol>
<i>Remember to set fromAddress and fromPassword</i>
   



  
