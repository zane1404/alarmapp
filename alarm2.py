from datetime import datetime
from playsound import playsound
import winsound

alarm_date = input("enter the date for alarm (DD-MM-YEAR:)").strip()
alarm_time = input("enter alarm time in 24-hrs format (HH:MM)").strip()
alarm_hour = alarm_time[0:2]
alarm_minute = alarm_time [3:5]

music = input("enter 'm' for music").strip().lower()

while True:
    current_time = datetime.now()
    current_hour = current_time.strftime('%H')
    current_minute = current_time.strftime('%M')
    current_date = current_time.strftime('%d-%m-%Y')  



    print("wake-up")

    if music_or_Beep == "m":
        playsound("audio.wav")

    else:
        winsound.Beep(freq,dur)

    break
