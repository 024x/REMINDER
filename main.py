
from pyrogram import Client, filters, idle
import logging
import os
from apscheduler.schedulers.background import BackgroundScheduler
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import requests


RK = "Dr. Rajesh Kuma"
AKS = "Dr. Ankit Sharm"
AN = "Dr. Ajay Nehra"
IPT = "Dr. Isha Pathak Tripathi"
LB = "Dr. Lava Bhargava"
NM = "Dr. Namita Mittal "
DRN = "Dr. Deepak Ranjan Nayak"
GS = "Dr. Gunjan Soni"
PRH = "Dr. Priyanka Harjule"
AMJ = "Dr. Amit M Joshi"
MA = "Dr. Mushtaq Ahmed"
PM = "Dr. Priyanka Mishra"
APM = "Dr. Arka Prokash Mojumdar"
AT = "Dr. Ashish Tripathi"
MT = "Dr. Meenakshi Tripathi"
SSC = "Dr. Satyendra Singh"
NS = "Dr. Niraja Saraswat"
GC = "Dr. Geetanjali"
KS = "Dr. Kushal Sharma"
AJ = "Dr. Arun Johar"
RR = "Dr. Ritu Raj"
SP = "Dr. Saurabh pandey"
GSY = "Dr. Gyan Singh Yadav"
AKH = "Dr. Ashok Kumar Kherodia"
AK = "Dr. Amit Kumar"
CS = "Dr. Chetna Sharma"
PKS = "Dr. Parikshit Kishor Singh"
AKG = "Dr. Amit Kumar Garg"
AKR = "Dr. Anupam Kumar"
BA = "Dr. Basant Agarwal"

VT = "Dr. Vinita Tiwari"
PM = "Dr. Priyanka Mishra"
AA = "Dr. Anand Agarwal"
SSC = "Dr. Satyendra Singh Chouhan"

MJ = "Dr. Mahipal Jadeja"
PV = "Dr. Prerna Vanjani"

R401 = "VLTC 401"
R403 = "VLTC 403"
R406 = "VLTC 406"
R407 = "VLTC 407"
R408 = "VLTC 408"
T401 = "Tuitorial Room 401"


IIITK_lab = "Comp Lab(IIIT Kota)"
Net_Lab = "Project Lab(MNIT CSE)"
SD_lab = " SW(MNIT CSE)"
EMBD_Lab = " Embeded System lab(MNIT ECE)"
CC_Lab1 = " MNIT Computer Centre lab 1"
CC_Lab_11 = "  MNIT Computer Centre lab 11"
CC_Lab_4 = " MNIT Computer Centre lab 4"
HW_Lab = " MNIT Hardware Lab CSE"
IP_Lab = "Image Processing Lab"
NW_Lab = "Project Lab(MNIT CSE)"


data = {
    "tue": [
        {"hour": 8,
            "Group": "A1",
            "Subject": "Csp Lab",
            "Teacher": MJ,
            "Room": SD_lab
         },
        {"hour": 8,
            "Group": "A3",
            "Subject": "DD lab",
            "Teacher": AJ,
            "Room": f"{IP_Lab} (IP LAB 9-11)"
         },
        {"hour": 11,
         "Group": "All",
         "Subject": "DE",
         "Teacher": VT,
         "Room": R408
         },
        {"hour": 12,
         "Group": "All",
         "Subject": "M1",
         "Teacher": GC,
         "Room": R408
         },
        {"hour": 14,
            "Group": "A2",
            "Subject": "DD (T)",
            "Teacher": SP,
            "Room": R408
         },
        {"hour": 14,
            "Group": "A3",
            "Subject": "M-1 (T)",
            "Teacher": GC,
            "Room": T401
         },
        {"hour": 15,
            "Group": "A2",
            "Subject": "ITW -1  lab",
            "Teacher": PRH,
            "Room": NW_Lab
         },

    ]
}


scheduler = BackgroundScheduler(
    {'apscheduler.timezone': 'Asia/Kolkata'}
)


def forma(title, grp, sub, teac, room):
    toret = f"""
<h3><b>{title}</b> </h3>

<i><h5>
Group: {grp}<br>
Subject: {sub}<br>
Teacher: {teac}<br>
Room: {room}<br>
</h5

"""
    return toret


def tele(title, grp, sub, teac, room):
    toret = f"""
<b>{title}</b> 


<i>
Group: {grp}
Subject: {sub}
Teacher: {teac}
Room: {room}
</i>


"""
    return toret


def sendalert(text, title, tg):
    requests.get(
        f"https://api.telegram.org/bot5416961842:AAGrCJZ-Xvmd6BxdojfRVDKhfg086FQ8h2Y/sendMessage?chat_id=-1001810029471&text={tg}&parse_mode=html"
    )
    sender_address = 'torrleechs@gmail.com'
    sender_pass = 'aztdvpeskpaclseo'
    receiver_address = "kotaiiit@googlegroups.com"
    message = MIMEMultipart()
    message['Subject'] = title
    message['From'] = "class-notify@satyendra.in"
    message['To'] = receiver_address
    mail_content = text
    message.attach(MIMEText(mail_content, 'html'))
    session = smtplib.SMTP('smtp.gmail.com', 587)
    session.starttls()
    session.login(sender_address, sender_pass)
    text = message.as_string()
    session.sendmail(sender_address, receiver_address, text)
    session.quit()


bot = Client(
    "my_account",
    api_id=2171111,
    api_hash="fd7acd07303760c52dcc0ed8b2f73086",
    bot_token="5416961842:AAGrCJZ-Xvmd6BxdojfRVDKhfg086FQ8h2Y",
)

scheduler.add_job(sendalert, 'cron', day_of_week='tue', hour=(8 - 1), minute=00, args=[
    forma(title="Hello!", grp="TEst1", sub="Test2", teac="Test3", room="test4",), f"This must a head", tele(title="Hello!", grp="TEst1", sub="Test2", teac="Test3", room="test4")])

for i in data["tue"]:
    scheduler.add_job(sendalert, 'cron', day_of_week='tue', hour=(i["hour"] - 1), minute=45, args=[
                      forma(title="{i['Group']} - {i['Room']}", grp=i["Group"], sub=i["Subject"], teac=i["Teacher"], room=i["Room"],), f"{i['Group']} - {i['Room']}", tele(title="{i['Group']} - {i['Room']}", grp=i["Group"], sub=i["Subject"], teac=i["Teacher"], room=i["Room"])])
    print(f"{i['hour']} , {i['Subject']}")

scheduler.start()

bot.start()
idle()
