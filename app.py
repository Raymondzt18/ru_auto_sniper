from checker import CheckBot
from register import register_class
import time

check_freq = 10 #Checks for open spot every 10 secs
base_url = 'http://sis.rutgers.edu/oldsoc/courses.json'

###########
#USER INPUT
###########
username = '' #remember to erase before committing and pushing
password = ''
course_code = "01:198:352"
section_numbers = ["03"] #For single digit section numbers, add a 0 to the front
semester_code = "92018"
campus = "NB"
level = "UG"

#Create the bot to check for open sections
checkbot1 = CheckBot(course_code, section_numbers, semester_code, campus, level)

open_sections = []

loop_num = 0
#mainloop
while True:
    open_sections = checkbot1.check(base_url) #returns a list of all open sections of the class the bot is tracking
    if open_sections:
        success = register_class(username, password, open_sections[0].index_number)
        break
    loop_num = loop_num+1
    print("Checked "+ str(loop_num) + " times\n")
    time.sleep(check_freq)






