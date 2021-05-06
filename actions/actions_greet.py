from __future__ import absolute_import      # __future enables new language features
from __future__ import division
from __future__ import unicode_literals
from __future__ import print_function

import datetime
import time

from socket import error as socket_error
from typing import Dict, Text, Any, List, Union
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionGreetHello(Action):
	def name(self):
		return "actions.greet.hello"

	def run(self, dispatcher, tracker, domain):
		date=datetime.datetime.now()
		h=int(date.strftime('%H'))
		if h<12:
			dispatcher.utter_message(template="utter_greetings_goodmorning")
		elif h<17:
			dispatcher.utter_message(template="utter_greetings_hello")
		elif h<21:
			dispatcher.utter_message(template="utter_greetings_goodevening")
		else:
			dispatcher.utter_message(template="utter_greetings_hello")
		return

class ActionGreetBye(Action):
	def name(self):
		return "actions.greet.bye"

	def run(self, dispatcher, tracker, domain):
		date=datetime.datetime.now()
		h=int(date.strftime('%H'))
		if h<12:
			dispatcher.utter_message(template="utter_greetings_bye")
		elif h<17:
			dispatcher.utter_message(template="utter_greetings_bye")
		elif h<21:
			dispatcher.utter_message(template="utter_greetings_bye")
		else:
			dispatcher.utter_message(template="utter_greetings_goodnight")
		return