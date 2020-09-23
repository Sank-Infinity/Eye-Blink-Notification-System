import time
from plyer import notification

def eyeBlink():
    while True:
        notification.notify(
            title="***Please blink eyes....",
            message="The eye is very easily infected, and if we didn't have the eyelid there to help keep it clean we would develop eye infections much more often.",
            app_icon="eye.ico",
            timeout=20
        )
        #time.sleep(10)
        time.sleep(60*10)


if __name__ == '__main__':
    eyeBlink()
