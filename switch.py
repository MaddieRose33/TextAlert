#7-9-2017 Developer Madison
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP)

from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "*********"
# Your Auth Token from twilio.com/console
auth_token  = "*********"

while True:
    #2 GPIO:18 Yellow
    input_state18 = GPIO.input(18) #GPIO 18 means GPIO 24
    if input_state18 == False:
        print('Button Pressed.')
        
        client = Client(account_sid, auth_token)

        message = client.messages.create(
            to="+*********",
            from_="+*********",
            body="There is a stranger at the door attempting entry. Please call security for me.")

        print(message.sid)


    #1 GPIO:16 RedWire
    input_state16 = GPIO.input(16) #GPIO 18 means GPIO 24
    if input_state16 == False:
        print('Button Pressed.')
        
        client = Client(account_sid, auth_token)

        message = client.messages.create(
            to="+*********",
            from_="+*********",
            body="I attempted to phone and was unable to reach you please call me back C# 570-618-3747 or H# 570-828-4587")

        print(message.sid)

    #4 GPIO:27 Orange-Yellow
    input_state27 = GPIO.input(27) #GPIO 18 means GPIO 24
    if input_state27 == False:
        print('Button Pressed.')
        
        client = Client(account_sid, auth_token)

        message = client.messages.create(
            to="+*********",
            from_="+*********",
            body="My power just went out at the house I just wanted to notify you.")

        print(message.sid)

    #3 GPIO:22 Brown
    input_state22 = GPIO.input(22) #GPIO 18 means GPIO 24
    if input_state22 == False:
        print('Button Pressed.')
        
        client = Client(account_sid, auth_token)

        message = client.messages.create(
            to="+1*********",
            from_="+*********",
            body="I am not feeling well please come over")

        print(message.sid)
  
  
