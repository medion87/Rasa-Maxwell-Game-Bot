from __future__ import absolute_import      # __future enables new language features
from __future__ import division
from __future__ import unicode_literals
from __future__ import print_function

import datetime
import time
import random
import re

from socket import error as socket_error
from typing import Dict, Text, Any, List, Union
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet, AllSlotsReset
from rasa_sdk.types import DomainDict

class ActionGameQuiz(Action):
	def name(self):
		return "actions.game.quiz"
	
	def run(self, dispatcher, tracker, domain):
		filename = '/home/bjorn/projects/chatbot/actions/utils/quiz.txt'
		f = open(filename)
		line = f.readlines()
		i = random.choices(line)
		for n in i:
			q = n.split('",')
		q1 = q[0]
		a1 = q[1]
		q2 = q1.replace('["', '')
		a2 = a1.replace('"', '').replace(']', '')
		dispatcher.utter_message(q2)
		f.close
		return [SlotSet("quiz_answer", '{}'.format(a2))]
	
class ActionGameQuizAnwser(Action):
	def name(self):
		return "actions.game.quiz.anwser"

	def run(self, dispatcher, tracker, domain):
		txt = next(tracker.get_latest_entity_values('quiz'), None)
		score = str(tracker.get_slot('quiz_score'))
		answer = str(tracker.get_slot('quiz_answer'))
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
		return [SlotSet("quiz_score", '{}'.format(new_score))]