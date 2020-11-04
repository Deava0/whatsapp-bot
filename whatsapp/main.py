import pyautogui as pt
from time import sleep
import pyperclip
import random

sleep(2)
position1 = pt.locateOnScreen("whatsapp/smiley_paperclip_white.jpg", confidence=.6)
x = position1[0]
y = position1[1]


# Gets Message
def get_message():
    global x, y
    position = pt.locateOnScreen("whatsapp/smiley_paperclip_white.jpg", confidence=.6)
    x = position[0]
    y = position[1]
    pt.moveTo(x, y, duration=.5)
    pt.moveTo(x + 50, y - 50, duration=.5)
    pt.tripleClick()
    pt.rightClick()
    pt.moveRel(12, 15)
    pt.click()
    whatsapp_message = pyperclip.paste()
    print("Message received: " + whatsapp_message)

    return whatsapp_message


# Posts
def post_response(message):
    global x, y

    position = pt.locateOnScreen("whatsapp/smiley_paperclip_white.jpg", confidence=.7)
    x = position[0]
    y = position[1]
    pt.moveTo(x + 200, y + 20, duration=.5)
    pt.click()
    pt.typewrite(message, interval=.01)

    pt.typewrite("\n", interval=.01)


# Process response
def process_response(message):
    random_no = random.randrange(4)

    if "how are you" in str(message).lower():
        return "never been better"
    elif "gay" in str(message).lower():
        return "homophobia is a disease "
    elif "hi" in str(message).lower():
        return "Hi"
    elif "hello" in str(message).lower():
        return "Hello, there"
    elif "?" in str(message).lower():
        return "oh? a question, maybe I'll be able to answer it after a few updates"
    else:
        if random_no == 0:
            return "Processing.... :("
        elif random_no == 1:
            return "I need further input"
        elif random_no == 2:
            return "That's funny, you're funny"
        elif random_no == 3:
            return "WHAT???"
        elif random_no == 4:
            return "Oh no, I had no idea"
        elif random_no == 5:
            return "is that a mana worm in your pocket or are you excited to see me?"
        else:
            return "I'm not familiar with your statement"


# check for messages 38, 45, 49
def check_for_new_messages():
    # pt.moveTo(x + 60, y - 45, duration=.5)
    position1 = pt.locateOnScreen("whatsapp/smiley_paperclip_white.jpg", confidence=.6)
    x = position1[0]
    y = position1[1]

    while True:
        # cont checks for green dots and new messages
        try:
            position = pt.locateOnScreen("whatsapp/green_circle_white.jpg", confidence=.7)

            if position is not None:
                pt.moveTo(position)
                pt.moveRel(-50, 0)
                pt.click()
                sleep(.5)

            if pt.pixelMatchesColor(int(x + 60), int(y - 45), (255, 255, 255), tolerance=10):
                print("Is White (NewMessage)")
                processed_message = process_response(get_message())
                post_response(processed_message)
            else:
                print("NO new Message ")
            sleep(5)
        except (Exception):
            print("No new other users new messages located")


check_for_new_messages()
