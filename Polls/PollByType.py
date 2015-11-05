from pollster import Pollster
from datetime import date
import sys

pollster = Pollster()

def pollByTopic(name):
	poll = pollster.charts(topic = name)