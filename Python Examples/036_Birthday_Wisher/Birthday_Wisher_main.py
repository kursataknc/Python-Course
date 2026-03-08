# To run and test the code you need to update 4 places:
# 1. Change MY_EMAIL/MY_PASSWORD to your own details.
# 2. Go to your email provider and make it allow less secure apps.
# 3. Update the SMTP ADDRESS to match your email provider.
# 4. Update birthdays.csv to contain today's month and day.
# See the solution video in the 100 Days of Python Course for explainations.

from datetime import datetime
import pandas
import random
import smtplib
import os

MY_EMAIL = "your_email_here"
MY_PASSWORD = "your_password_here"

today = datetime.now()
today_tuple = (today.month, today.day)

script_directory = os.path.dirname(__file__)
csv_path = os.path.join(script_directory, "birthdays.csv")

data = pandas.read_csv(csv_path)
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}
if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]

    # Rastgele bir mektup şablonu seç
    letter_number = random.randint(1, 3)
    file_path = os.path.join(script_directory, f"letter_templates/letter_{letter_number}.txt")

    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_person["kaan-kozludere@hotmail.com"],
            msg=f"Subject:Happy Birthday!\n\n{contents}"
        )
