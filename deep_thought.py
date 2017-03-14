#!/usr/bin/env python3
# Deep Thought Speech and Orchestration Platform Script
import speech_recognition as sr
import subprocess
import os
import time
import sys
spoken_hello = 0
# obtain audio from the microphone

class DeepThought(object):
	def __init__(self):
		self.name = "Richard"


	def listen(self):
		recognizer = sr.Recognizer()
		with sr.Microphone() as source:
			print("Say something!")
			audio = recognizer.listen(source, timeout=2, phrase_time_limit=3)
			print("Done listening")
			self.flash_led()
			return audio, recognizer

	def process_audio(self, audio, recognizer):
		try:
			speech_string = recognizer.recognize_sphinx(audio)
			print(speech_string)
			if ("ell" in speech_string) or ("thought" in speech_string) or ("deep" in speech_string):
				spoken_hello = 1
				os.popen('su - pi -c "sudo python what_would_you_like_to_know.py"')
		except sr.UnknownValueError:
			print("Sphinx could not understand audio")
		except sr.RequestError as e:
			print("Sphinx error; {0}".format(e))
		return speech_string

	def flash_led(self):
		os.popen('sudo python /home/pi/green_think_widestrand.py 2 9 25 123')


def main():
	mhqthought = DeepThought()
	while True:
		speech, recog = mhqthought.listen()
		response_string = mhqthought.process_audio(speech, recog)
		print(response_string)

if __name__ == "__main__":
    main()
