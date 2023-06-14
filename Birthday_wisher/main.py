'''sending bday wishes to the person if bday date (dates and names are in csv file) matches with today's date'''

import pandas
import datetime
import random
import ssl
import smtplib
from email.message import EmailMessage

#setup email credentials
email_sender = "anandn9804@gmail.com"
email_password = "ptoyfxljjsjylsgl"

#read the csv file
file = pandas.read_csv('birthdays.csv')

#convert it to dict
bday_dict = {(j.month,j.day):j for i,j in file.iterrows()}

#check if bday date matches with todays date
today = datetime.datetime.now()
today_date = (today.month, today.day)
if today_date in bday_dict:
    # print("found")
    #if found then read letters and send one of them randomly by inserting the name
    #of the person into the [NAME] placeholder in letter
    letter_files_path = f'letter_templates/letter_{random.randint(1,3)}.txt'

    with open(letter_files_path) as letter:
        letter_content = letter.read()
        letter_to_send = letter_content.replace('[NAME]',bday_dict[today_date]['name'])
        # print(letter_to_send)

    #since letter_to_send is ready now send the mail
    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = bday_dict[today_date]["email"]
    em['Subject'] = "Test Subject"
    em.set_content(letter_to_send)

    context = ssl.create_default_context()

    with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
        smtp.starttls(context=context)
        smtp.login(email_sender, email_password)
        smtp.send_message(em)


#this code is in cloud now "https://www.pythonanywhere.com/user/anandneredimilli/tasks_tab/"
#it expires in a month
    