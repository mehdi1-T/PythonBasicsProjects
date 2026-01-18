import time
import winsound

def Count_Down():
    user = int(input("Number: "))

    for i in range(user, 0, -1):
        print(i)
        time.sleep(1)

    winsound.PlaySound("notification.wav", winsound.SND_FILENAME)
    print("Time's up!")

if __name__ == "__main__":
    Count_Down()
