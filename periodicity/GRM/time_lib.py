try:
    import matplotlib.pyplot as plt
except:
    raise

from random import randint
from collections import namedtuple
from datetime import datetime
import networkx as nx
import numpy
import random

def __datetime(date_str):
	return datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S')
				
def int_to_weekday(day):
	to_week = {}
	to_week[1] = "monday"
	to_week[2] = "tuesday"			
	to_week[3] = "wednesday"
	to_week[4] = "thursday"
	to_week[5] = "friday"
	to_week[6] = "saturday"
	to_week[7] = "sunday"
	return to_week[day]

def weekday_to_int(weekday):
	to_int = {}
	to_int["monday"] = 1 
	to_int["tuesday"] = 2 			
	to_int["wednesday"] = 3
	to_int["thursday"] = 4
	to_int["friday"] = 5
	to_int["saturday"] = 6
	to_int["sunday"] = 7
	return to_int[weekday]

