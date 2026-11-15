# battery 80% and 20% check
# notification
# speak
# email : net + without net
# at 16% shut down
# pyinstaller --onefile --collect-all plyer "G:\My Drive\Programmings!\CODES.py\Dreamer's Projects!\Power_Manager.py"


import pyttsx3 #speaking
import plyer #notifications
from email.message import EmailMessage as em
import smtplib
import psutil # for battery sensors
import time
import winsound # for beep sound
import os

# Speak Function
def speak(text):
    engine = pyttsx3.init()
    engine.setProperty("rate",150)
    engine.setProperty("volume",1)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print(text)
    engine.say(text)
    engine.runAndWait()

# Notification function
def notify(heading,sms,timeup):
    notifications = plyer.notification
    notifications.notify(title = heading, message = sms, timeout = timeup)

# E-mail function
def send_email(subj,body):
    try:
        esms = em()
        esms["Subject"] = subj
        esms["From"] = "yash.dreamerz@gmail.com"
        esms["To"] = "yash.dreamerz@gmail.com"
        esms.set_content(body)

        gserver = smtplib.SMTP("smtp.gmail.com", 587)
        gserver.starttls()
        gserver.login("yash.dreamerz@gmail.com", "xaqp gpjv vfny fkwu")
        gserver.send_message(esms)
        gserver.quit()
    
    except Exception as e:
        print(f"Email Error: {e}")

# Battery check logic
os.system("cls")
speak(f"Hey! I am 'Battery Guardian 3.o' The Updated Version!\n\tI'll notify you Whenever your Laptop's Battery Hits: 80 and 20 Percent 🔋!\n\tBUTT... 🫵  Remember, that I'll Make Sure to force shutdown your PC if not plugged at 16% 😵🔌!!! ")

while True:
    battery = psutil.sensors_battery()
    plugged = battery.power_plugged
    percentage = battery.percent

    if not plugged and percentage <=16:
        notify("Battery Level is below 16% ⚡","System will Shutdown in 60sec! 😵", 8)
        speak("Dreamer, Please plugin my charger because it's 16 percent, otherwise I'll shutdown in 60 seconds. You can also turn off Battery Guardian to not shutdown, but within 40 seconds! ")
        send_email("PC shuting down in 60 sec 😵🪫"," SORRY, DREAMER BUT YOUR PC IS SHUTTING DOWN IN LAST 60 SECONDS.\n => Can You Please Connect Your Charger, Hurry up!! 🪫🔌")

        time.sleep(40)
        winsound.Beep(1000,1000)
        speak("Sorry Dreamer, I am shutting down in 20 seconds!")
        os.system("shutdown /s /t 20")
    
    elif not plugged and percentage <=20:
        notify("Battery Level 20% ⚡","Please Plug In The Charger 🔌",10)
        speak("Hey Dreamer, Please Plug In My Charger Right Now!")
        print(f"=> Battery is {percentage}% charged!")
        send_email("Battery Level 20% ⚡","Hey Dreamer, Can you Now check-out your Laptop and \"Please connect the charger 🔌🪫\"‼️")

    elif plugged and percentage >=80:
        notify("Battery Level 80% 🔋","Please Disconnect The Charger 🔌",10)
        speak("Dreamer, Please Disconnect My Charger!")
        print(f"=> Battery is {percentage}% charged!")
        send_email("Battery Level 80% 🔋","Hey Dreamer, Can you Now check-out your Laptop and \"Please Disconnect The Charger 🔋‼️")

    else:
        if plugged and percentage <80 and percentage >20:
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print(f"==> Your 'PC' is Plugged Right Now! At {percentage}% 😁🔌!!")
        
        else:
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print(f"==> Your 'PC' is At {percentage}% Chargered ⚡😉!!")

    time.sleep(15)
    os.system("cls") # again for clearing the extra stuffs, you can wait 30 sec and see what happpened