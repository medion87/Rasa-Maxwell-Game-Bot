from __future__ import absolute_import      # __future enables new language features
from __future__ import division
from __future__ import unicode_literals
from __future__ import print_function

import datetime
import time
import random
import re

from random import shuffle
from socket import error as socket_error
from typing import Dict, Text, Any, List, Union
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet, AllSlotsReset
from rasa_sdk.types import DomainDict

class ActionGameScramble(Action):
	def name(self):
		return "actions.game.scramble"
	
	def run(self, dispatcher, tracker, domain):
		filename = '/home/bjorn/wordscramble.txt'
		f = open(filename)
		line = f.readlines()
		word = random.choice(line)
		scramble = list(word)
		shuffle = []
		for i in range(10):
			random.shuffle(scramble)
			shuffle.append(list(scramble))
		scramble = ''.join(scramble)
		scramble = scramble.replace('[', '').replace("'", "").replace(',', '.').replace('\n', '').replace(']', '')
		dispatcher.utter_message(scramble)
		dispatcher.utter_message(word)
		return [SlotSet("scramble_answer", '{}'.format(word))]

class ActionGameScrambleAnwser(Action):
	def name(self):
		return "actions.game.scramble.anwser"

	def run(self, dispatcher, tracker, domain):
		txt = next(tracker.get_latest_entity_values('scramble'), None)
		score = str(tracker.get_slot('scramble_score'))
		answer = str(tracker.get_slot('scramble_answer'))
		if txt == answer:
			if score == 0 :
				new_score = score
			else:
				new_score = int(score) + int(1)
			dispatcher.utter_message(template="utter_game_answer_correct")
			score_re = """Your new score is {}""".format(new_score)
			dispatcher.utter_message(score_re)
		else: 
			response = """I'm sorry, that was not a correct answer. Correct answer was {}""".format(answer)
			dispatcher.utter_message(response)
			new_score = score
		return [SlotSet("scramble_score", '{}'.format(new_score))]