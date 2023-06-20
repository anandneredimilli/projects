import requests
import datetime
import sendmail



today_date = datetime.datetime.now().date()
# print(today_date)


STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

 
stock_parameters = {
    "function":"TIME_SERIES_DAILY_ADJUSTED",
    "symbol":STOCK,
    "apikey":"75WEZXPWXY4CZ2P5"
}

news_parameters ={
    'apiKey':"945302b7fe1448c9971e0550c48b145e",
    'q':COMPANY_NAME
}

data = requests.get(url='https://www.alphavantage.co/query', params=stock_parameters).json()['Time Series (Daily)']
data_in_list = [value for (key,value) in data.items()]

yesterday_close = data_in_list[0]['4. close']
day_before_yesterday_close = data_in_list[1]['4. close']

difference = abs(float(yesterday_close) - float(day_before_yesterday_close))

diff_percent = (difference/float(yesterday_close))*100
# print(diff_percent)
up_down_emoji = None
if diff_percent >0:
    up_down_emoji = "🔺"
else:
    up_down_emoji = "🔻"

if abs(diff_percent) >=1:
    news_data = requests.get(NEWS_ENDPOINT,params=news_parameters).json()['articles']
    top_3_news = news_data[:3]
    # print(top_3_news)
    
    
    news_headlines_des = [f"{COMPANY_NAME}: {up_down_emoji} {abs(diff_percent)}headline:{i['title']} \ndescription:{i['description']}" for i in top_3_news]
    
    # print(news_headlines_des)
    for msg in news_headlines_des:
        send_mail = sendmail.SendMail(message=msg)





#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""


