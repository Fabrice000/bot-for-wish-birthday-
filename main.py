import datetime as dt
import pandas
import random
import smtplib
MY_EMAIL = "YOUR EMAIL"
PASSWORD = "YOUR PASSWORD"
today = (dt.datetime.now().month,dt.datetime.now().day)
# you need to fill the birthdays.csv with all your friends informations
data = pandas.read_csv("birthdays.csv") 

birthdays_dict = {(data_row.month,data_row.day):data_row for (index,data_row) in data.iterrows()}

if today in birthdays_dict:
    birthday_person = birthdays_dict[today]
    file_path = f"letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]",birthday_person["name"])
        
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL,password=PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,to_addrs=birthday_person["email"],msg=f"Subject:Happy Birthday!\n\n{contents}")
        