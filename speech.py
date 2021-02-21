# Python program to translate speech to text

import speech_recognition as sr
import pyttsx3

from time import *
import threading
import copy
import pytz
import geocoder
import pytz
import os
import IP2Location


# init the speech recognizer
recog = sr.Recognizer()

# required for threads
global my_timer
my_timer = 0

# use this to change the name of us
global name
name = "peaches"

############################################
#	       Function for text->speech	   #
############################################
def TextToSpeech(inputString):
	# init the imported engine
	engine = pyttsx3.init()
	engine.say(inputString)
	engine.runAndWait()


def find_action(string):
        # assuming "Peaches" has been said

        #  see if we have to set a reminder
        

        # see if we have to say the date
        elif(("date" in string) and ("what is" in string)):
            # see what day they are talking about (today, tomorrow, etc.)
			i = 0

	# see if we have to say the weather
        elif(("what is" in string) and ("weather" in string)):
		# find our IP address
		g = geocoder.ip('me')
		print(g.latlng)

		# find our location
		database = IP2Location.IP2Location(os.path.join("data", "IPV4-COUNTRY.BIN"))
		rec = database.get_all(g)

		# print to see if its right
		print(rec.timezone)

	# see if we have to say the location
        elif( "where am i" in string):
		# find the current location
		g = geocoder.ip('me')
		print(g.lating)
	else:
                # unidentified action

		# TODO List:
                # set a timer
                # calculator
                # spotify
                # pandora
                # multiple users
                i = 0

def countdown(seconds):
	global my_timer

	my_timer = copy.deepcopy(seconds)


	for i in range(seconds):
		my_timer = my_timer - 1
		sleep(1)

	print("Timer done")

# Loop indefinitely for user to speak
while(1):
	# Handle exceptions at run-time
	try:
		# use the microphone as input device
		with sr.Microphone() as source2:
			# adjust to the surrounding noise level (delay)
			recog.adjust_for_ambient_noise(source2, duration=1)

			# listen for input
			audio2 = recog.listen(source2)

			# using google to recognize audio
			outputText = recog.recognize_google(audio2)
			outputText = outputText.lower()

			# error check the results
			print("Did you say: " + outputText)

			# check if they are taking to us
			if(name in outputText):
				print("Got through Peaches")

				timer_thread = threading.Thread(target = countdown(5))

				timer_thread.start()

				#find_action(outputText)

			# else: steal all your data

	except sr.RequestError as e:
		print("Could not request results; {0}".format)

	except sr.UnknownValueError:
		print("Unknown error occured")
