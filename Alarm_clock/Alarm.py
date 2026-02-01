# Alarm that waits for user-defined minutes and seconds, then plays alarm.mp3

# import needed libraries
import time
from playsound import playsound

# takes data from the user
seconds = int(input("Seconds: "))
menutes = int(input("Menutes: "))

# convert menutes into seconds
menutes = menutes * 60

# calculate the total time in seconds
total_seconds = menutes + seconds

while total_seconds > 0:
    time.sleep(1)
    total_seconds = total_seconds - 1
    print("remaining time: ", total_seconds)

# when time end this play sound & print done
playsound(r"alarm.mp3")
print("Done.")

