

from playsound import playsound
# This module is imported so that we can 
# play the converted audio



import os
import pyttsx3    # special library for text to speech , is a text-to-speech conversion library in Python. Unlike alternative libraries, it works offline, and is compatible with both Python 2 and 3.




# //---------------Code is Good and in a Working condition-----Code Start A1-------------------------------


while 1:
        print("-------------Welcome to Robo speaker 1.0 Version---------------")
        eng=pyttsx3.init()
        c=input("Enter a text by user : \n")
        if c=='q':
                eng.say("Now Good BYe BYE and will meet next time")
                vw=eng.getProperty("voices")
                eng.runAndWait()
                break
        eng.say(c)
        v=eng.getProperty("voices")
        eng.runAndWait()
# //------------------------------Code End A1--------------------------------------------------------------





'''

while 1:  
        print("----------------Welcome to Robo Speaker! Lets Have a Fun------------------------")
        inputTxt=input("Enter a text message that user want to speak : \n")
        if inputTxt=='q':
                       break
        sound=gtts.gTTS(inputTxt,lang="en")
        sound.save("Jit.mp3")
        playsound.playsound("Jit.mp3")


'''



'''
from pathlib import Path
from openai import OpenAI

client = OpenAI()

sfp=Path(__file__).parent
res=client.audio.speech.create(model="tts-1", voice="alloy",input="How are you man")

res.stream_to_file("sfp.mp3")
'''
















