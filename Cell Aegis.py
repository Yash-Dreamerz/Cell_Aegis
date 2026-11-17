# battery 80% and 20% check
# notification
# speak
# at 16% Hybernate
# pyinstaller --onefile --collect-all plyer "G:\My Drive\Programmings!\CODES.py\Dreamer's Projects!\Power_Manager.py"


import pyttsx3 #speaking
import plyer #notifications
import psutil # for battery sensors
import time
import winsound # for beep sound
import os
import requests

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

# Telegram Bot Alert Reminder
def send_alert(Alert_Message):
    token = "9107755507:AAHrJOMS0Okd0tQPP6oTjMMtPGfXAamiB0c"
    chat_id = "8947111594"
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    
    payload = {
        "chat_id": chat_id,
        "text": Alert_Message
    }
    print("Sent!")
    try:
        requests.post(url, json=payload)
    except Exception as e:
        print(f"Telegram Error: {e}")

# Battery check logic
os.system("cls")
speak(f"Hey! I am 'Cell Aegis' The Ultimate Version!\nI'll notify you Whenever your Laptop's Battery Hit, 80 and 20 Percent!\nBut Remember, I'll Make Sure to Hibernate your PC in 30 seconds if not plugged at 16 Percent! ")

while True:
    battery = psutil.sensors_battery()
    plugged = battery.power_plugged
    percentage = battery.percent

    if not plugged and percentage <=16:
        send_alert("Hurry up! You only have 30 seconds to Plugin Your PC's Charger. It's Going to Shutdown")
        notify("Battery Level at 16% ⚡","System Shuting down in 30sec! 😵",10)
        speak("Dreamer, Please plugin the charger, it's 16 percent, otherwise it'll shutdown in 30 seconds. You can also turn off Cell Aegis to not shutdown, but within 30 seconds! ")

        time.sleep(30)
        winsound.Beep(1000,1000)
        speak("Sorry Dreamer, I am Hibernating the PC Instantly!")
        os.system("shutdown /h /t 3")
    
    elif not plugged and percentage <=20:
        send_alert("Hey Dreamer! Plugin Your PC's Charger. It's at 20%!")
        notify("Battery Level 20% ⚡","Please Plug In The Charger 🔌",10)
        speak("Hey Dreamer, Please Plug In The Charger Right Now!")
        print(f"=> Battery is {percentage}% charged!")

    elif plugged and percentage >=80:
        send_alert("Hey Dreamer! Disconned Your PC's Charger. It's at 80%!")
        notify("Battery Level 80% 🔋","Please Disconnect The Charger 🔌",10)
        speak("Dreamer, Please Disconnect The Charger!")
        print(f"=> Battery is {percentage}% charged!")

    else:
        if plugged and percentage <80 and percentage >20:
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print(f"==> Your 'PC' is Plugged Right Now! At {percentage}% 😁🔌!!")
        
        else:
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print(f"==> Your 'PC' is At {percentage}% Chargered ⚡😉!!")

    time.sleep(15)
    os.system("cls") # again for clearing the extra stuffs, you can wait 15 sec and see what happpened