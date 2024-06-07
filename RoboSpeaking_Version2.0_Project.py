from gtts import gTTS
from playsound import playsound  #  This module is imported so that we can , play the converted audio
import os

'''
        print("----------------Welcome to Robo Speaker! Lets Have a Fun------------------------")
        inputTxt=input("Enter a text message that user want to speak : \n")
        if inputTxt=='q':
                       break
        sound=gtts.gTTS(inputTxt,lang="en")
        sound.save("Jit.mp3")
        playsound.playsound("Jit.mp3")
'''
while 1:
        print("----------------Welcome to Robo Speaker  Version 2.0 Improved Version! Lets Have a Fun-----------------------")
        Usertext=input("Enter a Text by user : ")
        var = gTTS(text = Usertext,lang = 'en')
        if Usertext=='q':
                    exitText="Ok Bye Bye Chat End Now , will meet Next Time "
                    var = gTTS(text = exitText,lang = 'en')
                    var.save('engw.mp3') 
                    playsound('engw.mp3')
                    os.remove('engw.mp3')
                    break
        var.save('eng.mp3') 
        playsound('eng.mp3')
        os.remove('eng.mp3')
        



#//----------For Hindi Language speaking Robo-------------------
#var=gTTS(text="यह हिंदी में एक उदाहरण है",lang='hi')
#//--------------------------------------------------------------