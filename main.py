#                             whatsapp message sending with pyautogui
import pyautogui
import time

try:
    # message count
    count = int(input("Enter the number of messages"))

    # message input
    message = input("Enter your message")

    # wait 5 seconds for us to insert the cursor
    time.sleep(5)

    # for loop to send a message
    for i in range(count):
        # to write our message to the place where we placed the automatic cursor.
        pyautogui.typewrite(message)
        # for automatic dispatch
        pyautogui.press("Enter")

except ValueError as error_message:
    # The error message we will send when you enter the message number with a letter
    print("Enter the number of messages as number.")
    print(error_message)