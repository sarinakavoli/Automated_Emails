import yagmail
import pandas
import datetime
from news import NewsFeed
import time

while True:
    if datetime.datetime.now().hour == 15 and datetime.datetime.now(). minute == 16:
        #df is the abbreviation for DataFrame
        df = pandas.read_excel('people.xlsx')

        for index, row in df.iterrows():
            today = datetime.datetime.now().strftime('%Y-%m-%d')
            yesterday = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime('%Y-%m-%d')
            news_feed = NewsFeed(interest=row['interest'],
                                 from_date=yesterday,
                                 to_date=today)
            email = yagmail.SMTP(user="sarahkhorami5@gmail.com", password="jbdreexhedezcduv")
            email.send(to=row['email'],
                       subject=f"Your {row['interest']} news for today",
                       contents=f"Hi {row['name']},\n See whats on about {row['interest']} today. \n{news_feed.get()}\nArdit")

    time.sleep(60)

