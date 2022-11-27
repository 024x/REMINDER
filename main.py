
import json
from flask import Flask
import logging
import os
from apscheduler.schedulers.background import BackgroundScheduler
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import requests
logging.basicConfig(level=logging.INFO)
data = {
    "maonday": {
        "test": {
            "title": "Test Header",
            "message": "Test MEssage"
        },

        "07:45": {
            "title": "A1 - SST at IIItKota lab\nA2 - 408",
            "message": "Group: A1\nRoom: IIIT  KOta Computer Lab\nTeacher:RituRAj\n\nGroup: A2\nRoom:408\nTeacher: Neeraja Sharawath"
        },

        "09:45": {
            "title": "Computer science and programming - Room 408",
            "message": "Group: All\nRoom: VLTC 408\nTeacher:Meenakshi Tripati"
        },
        "10:45": {
            "title": "Communication Skills - Room 408",
            "message": "Group: All\nRoom: VLTC 408\nTeacher:Neeraja Sharawath"

        },
        "11:45": {
            "title": "Circut Theory - Room 408",
            "message": "Group: All\nRoom: VLTC 408 PKS"
        },
        "13:45": {
            "title": "Digital design - Room 408",
            "message": "Group: All\nRoom: VLTC 408\nTeacher:Vinita Tiwari"
        },
        "14:45": {
            "title": "Circut Theory - Room 408",
            "message": "Group: A3\nRoom: VLTC 408 \n(Tutorial)"
        },
        "15:45": {
            "title": "A1 - Digital Design (408),A2- Maths - Room (401)",
            "message": "Group: A1\nRoom: VLTC 408 \n(Tutorial)\nClass: DD(408)\nGroup: A2\nClass:M1(401)(Tut)"
        }
    }
}

app = Flask(__name__)


scheduler = BackgroundScheduler(
    {'apscheduler.timezone': 'Asia/Kolkata'}
)


def sendalert(text, title):
    requests.get(
        f"https://api.telegram.org/bot5416961842:AAGrCJZ-Xvmd6BxdojfRVDKhfg086FQ8h2Y/sendMessage?chat_id=-1001810029471&text={title}\n\n\n\n{text}"
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


scheduler.add_job(sendalert, 'cron', hour=23, minute=10, day_of_week="sun",
                  args=[data["maonday"]["test"]["message"],
                        data["maonday"]["test"]["title"]],

                  )
scheduler.add_job(sendalert, 'cron', hour=7, minute=45, day_of_week="mon",
                  args=[data["maonday"]["07:45"]["message"],
                        data["maonday"]["07:45"]["title"]],

                  )
scheduler.add_job(sendalert, 'cron', hour=9, minute=45, day_of_week="mon",
                  args=[data["maonday"]["09:45"]["message"],
                        data["maonday"]["09:45"]["title"]],

                  )
scheduler.add_job(sendalert, 'cron', hour=10, minute=45, day_of_week="mon",
                  args=[data["maonday"]["10:45"]["message"],
                        data["maonday"]["10:45"]["title"]],

                  )
scheduler.add_job(sendalert, 'cron', hour=11, minute=45, day_of_week="mon",
                  args=[data["maonday"]["11:45"]["message"],
                        data["maonday"]["11:45"]["title"]],

                  )
scheduler.add_job(sendalert, 'cron', hour=13, minute=45, day_of_week="mon",
                  args=[data["maonday"]["13:45"]["message"],
                        data["maonday"]["13:45"]["title"]],

                  )
scheduler.add_job(sendalert, 'cron', hour=14, minute=45, day_of_week="mon",
                  args=[data["maonday"]["14:45"]["message"],
                        data["maonday"]["14:45"]["title"]],

                  )
scheduler.add_job(sendalert, 'cron', hour=15, minute=45, day_of_week="mon",
                  args=[data["maonday"]["15:45"]["message"],
                        data["maonday"]["15:45"]["title"]],

                  )


@app.route('/', methods=['GET'])
def def_home():
    return data


scheduler.start()

if __name__ == '__main__':
    app.run(port=os.getenv("PORT", default=5000))
