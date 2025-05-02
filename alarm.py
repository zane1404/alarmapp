from datetime import datetime
from playsound import playsound
import winsound


alarm_date = input('Enter the date for the alarm (DD-MM-YYYY): ').strip()


alarm_time = input("Enter the alarm time in 24-hour format (HH:MM): ").strip()
alarm_hour = alarm_time[0:2]
alarm_minute = alarm_time[3:5]


music_or_beep = input("Enter 'm' for music or 'b' for beep :").strip().lower()

if music_or_beep == 'b':
    dur=int(input("enter the seconds:"))*1000
    freq =int(input("freq of noise:"))


alarm_hour = alarm_time[0:2]
alarm_minute = alarm_time[3:5]
alarm_period=alarm_time[6:8]


while True:
    current_time = datetime.now()
    current_hour = current_time.strftime('%H') 
    current_minute = current_time.strftime('%M')
    current_date = current_time.strftime('%d-%m-%Y') 

    if (current_date == alarm_date and
        current_hour == alarm_hour and
        current_minute == alarm_minute):

        print("WAKE UP")
        

        if music_or_beep == 'm':
            playsound('audio.wav')  
        else:
            winsound.Beep(freq, dur)
        break
