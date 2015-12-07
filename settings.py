import random
import json
import datetime
DEBUG = True
SECRET_KEY = '2578f8c1683747bc822d3fa8d5ed3054'
reps_j = {}




######################33
def check_number(To):
	if (To is None) or (len(To)<=10) or (not To.isdigit()):
		return reponse_jsong(401,'Please set valid phone number!','error')
	return True		


