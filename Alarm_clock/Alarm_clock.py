import time
from playsound import playsound
# pip install playsound (library which is used to play sound in the file)

# ANSI Escape Sequences
CLEAR = "\033[2J"       # This will clear the entire terminal
CLEAR_AND_RETURN = "\033[H"     # It is used to print over what the currently printed

def alarm(seconds):
    time_elaspsed = 0

    print(CLEAR)
    while time_elaspsed < seconds:
        time.sleep(1)
        time_elaspsed += 1

        time_left = seconds - time_elaspsed
        minutes_left = time_left // 60
        seconds_left = time_left % 60

        print(f"{CLEAR_AND_RETURN}Alarm will play in {minutes_left:02d}:{seconds_left:02d}")

    playsound("alarm_sound.mp3") 

print("Set your alarm :)")
minutes = int(input("Enter the minutes: "))
seconds = int(input("Enter the seconds: "))

total_sec = minutes * 60 + seconds
alarm(total_sec)