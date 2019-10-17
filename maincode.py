import time
import threading

lowertemp = 25
highertemp = 35

lowerhygro = 50
higherhygro = 70

class navButtons:
	def plus():
		#this function return 1 if pressed, 0 if not
		state = 0
		return state

	def moins():
		#this function return 1 if pressed, 0 if not
		state = 0
		return state

	def higher():
		#this function return 1 if pressed, 0 if not
		state = 0
		return state

	def lower():
		#this function return 1 if pressed, 0 if not
		state = 0
		return state

	def settemp():
		#this function return 1 if pressed, 0 if not
		state = 0
		return state

	def sethygro():
		#this function return 1 if pressed, 0 if not
		state = 0
		return state

class sensors:
	def hygro():
		#this function return value from hygro sensor
		hygro = 73 #73%
		return hygro

	def temp():
		#this function return value from heat sensor
		temp = 35 #35*C
		return temp


def displayLCD(lcdstring, line):
	#function to display text on the lcd screen
	print (line + ":" + lcdstring)

def hour():
	#this function return time value
	hournow = 15 # 15h00
	return hournow

def getKeyValue():
	if navButtons.settemp(): and navButtons.higher() == 1:
		if navButtons.plus() == 1 and navButtons.moins() == 0:
			global highertemp
			highertemp = highertemp + 1
			time.sleep(300)

		elif navButtons.moins() == 1 and navButtons.plus() == 0:
			global highertemp
			highertemp = highertemp - 1
			time.sleep(300)

	elif navButtons.settemp(): and navButtons.lower() == 1:
		if navButtons.plus() == 1 and navButtons.moins() == 0:
			global lowertemp
			highertemp = highertemp + 1
			time.sleep(300)

		elif navButtons.moins() == 1 and navButtons.plus() == 0:
			global lowertemp
			highertemp = highertemp - 1
			time.sleep(300)

	elif navButtons.sethygro(): and navButtons.higher() == 1:
		if navButtons.plus() == 1 and navButtons.moins() == 0:
			global higherhygro
			higherhygro = higherhygro + 1
			time.sleep(300)

		elif navButtons.moins() == 1 and navButtons.plus() == 0:
			global higherhygro
			higherhygro = higherhygro - 1
			time.sleep(300)

	elif navButtons.sethygro(): and navButtons.lower() == 1:
		if navButtons.plus() == 1 and navButtons.moins() == 0:
			global higherhygro
			higherhygro = higherhygro + 1
			time.sleep(300)

		elif navButtons.moins() == 1 and navButtons.plus() == 0:
			global higherhygro
			higherhygro = higherhygro - 1
			time.sleep(300)

while True:
	threadGetKeyValue = threading.Thread(getKeyValue())
	threadGetKeyValue.start()
	threadGetKeyValue.join()

	if sensors.hygro < lowerhygro:
		#code to execute for pull up hygro value
		print ("Watering...")
	elif sensors.hygro > higherhygro:
		#code to execute for pull down hygro value
		print ("Unwatering...")

	if sensors.temp < lowertemp:
		#code to execute for pull up temp value
		print ("Heating...")
	elif sensors.temp > highertemp:
		#code to execute for pull down temp value
		print ("Cooling down...")