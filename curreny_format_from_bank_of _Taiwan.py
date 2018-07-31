import requests
from bs4 import BeautifulSoup

res = requests.get("https://rate.bot.com.tw/xrt?Lang=zh-TW")



import lxml
soup = BeautifulSoup(res.text,"lxml")

country = [ tag.text for tag in soup.find_all("div",{"class":"hidden-phone print_show", "style":"text-indent:30px;"})]
country = [y.strip('\r\n \r\n') for y in country]




rate_in_cash =[tag.text for tag in soup.findAll("td",{"data-table":"本行現金買入","class":"text-right display_none_print_show print_width"})]
rate_out_cash =[tag.text for tag in soup.findAll("td",{"data-table":"本行現金賣出","class":"text-right display_none_print_show print_width"})]
rate_in_intime =[tag.text for tag in soup.findAll("td",{"data-table":"本行即期買入","class":"text-right display_none_print_show print_width"})]
rate_out_intime=[tag.text for tag in soup.findAll("td",{"data-table":"本行即期賣出","class":"text-right display_none_print_show print_width"})]




import pandas as pd
rate_df = pd.DataFrame({
    "幣別":country,
    "本行現金買入":rate_in_cash,
    "本行現金賣出":rate_out_cash,
    "本行即期買入":rate_in_intime,
    "本行即期賣出":rate_out_intime
}
    )
rate_df

