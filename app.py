from checker import CheckBot

base_url = 'http://sis.rutgers.edu/oldsoc/courses.json'

###########
#USER INPUT
###########
course_code = "01:198:107"
section_numbers = ["01", "03"] #For single digit section numbers, add a 0 to the front
semester_code = "92018"
campus = "NB"
level = "UG"

checkbot1 = CheckBot(course_code, section_numbers, semester_code, campus, level)
open_sections = checkbot1.check(base_url)

print(open_sections)

