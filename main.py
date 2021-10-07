import cv2
import pyautogui
import schedule
from time import sleep
from datetime import date

# Zoom Auto Join program and scheduler
# Make sure to install pyautogui and cv2 or will not work
# Take screenshot of Zoom Join button as png and use its path in script below

print("Today:")

# Auto-Join function:

def join(id, password):

	pyautogui.press('esc',interval=0.1)

	sleep(0.3)

	pyautogui.press('win',interval=0.5)
	pyautogui.write('zoom')
	pyautogui.press('enter',interval=0.5)

	sleep(9)

	img = cv2.imread(r"C:\...\...\joinbutton.png") # Enter your own path to the .png of the Zoom button
	location = pyautogui.locateCenterOnScreen(img)

	pyautogui.moveTo(location)

	sleep(0.1)

	pyautogui.click()

	pyautogui.press('enter',interval=4)
	pyautogui.write(id)
	pyautogui.press('enter',interval=4)
	pyautogui.write(password)
	pyautogui.press('enter',interval = 8)


# Information:

class Course:

	def __init__(self, name, id, password):
		self.name = name
		self.id = id
		self.password = password

	def info(self): # Prints out the course's name, time, ID and password on the command prompt (just to keep things neat)
		print(" ")
		print(" ")
		print(self.name, "at", time)
		print(" ")
		print(self.id)
		print(self.password)

maths = Course("Mathematics", "5725835837", "123456") # Enter all your classes in the same format ("name", "zoom ID", "password")

physics = Course("Physics", "3895628943", "314159") # Another example



# Schedule:

if date.today().weekday() == 0:	# Monday

	time = "08:00" # Enter the meeting time, e.g: "15:10"
	maths.info() # Displays the class information on command prompt
	schedule.every().day.at("%s"%time).do(join, maths.id, maths.password) # Enter the class's .id and .password accordingly # Note that schedule depends on the day

if date.today().weekday() == 1:	# Tuesday

	time = "13:30" # Just another example
	physics.info()
	schedule.every().day.at("%s"%time).do(join, physics.id, physics.password)

""" Remove the comment marks
if date.today().weekday() == 2:	# Wednesday
	time = "//://" # Replace all the //:// with time
	/////.info() # Replace the ///// with the class
	schedule.every().day.at("%s"%time).do(join, /////.id, /////.password)
if date.today().weekday() == 3:	# Thursday
	time = "//://"
	/////.info()
	schedule.every().day.at("%s"%time).do(join, /////.id, /////.password)
if date.today().weekday() == 4:	# Friday
	time = "//://"
	/////.info()
	schedule.every().day.at("%s"%time).do(join, /////.id, /////.password)
"""

if date.today().weekday() == 5 or date.today().weekday() == 6: # Off on the weekends
	exit()

while True: # This keeps the program on the lookout for when the meeting time comes
	schedule.run_pending()
	sleep(1)
