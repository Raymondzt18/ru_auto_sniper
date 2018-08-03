import requests
import json

#url = 'http://sis.rutgers.edu/oldsoc/courses.json?subject=198&semester=12018&campus=NB&level=UG'
#url2 = 'http://sis.rutgers.edu/oldsoc/courses.json'

class CheckBot(): #bot that checks if any of the tracked sections are open

        #Each CheckBot has a designated class to track and section numbers to check for
        def __init__(self, course_code, section_numbers, semester_code, campus, level):
            temp = course_code.split(':')
            self.ru_school_code = temp[0]
            self.ru_subject = temp[1]
            self.ru_class = temp[2]
            self.ru_sections = section_numbers
            self.ru_semester_code = semester_code
            self.ru_campus = campus
            self.ru_level = level
        
        #Forms the full url and checks for open sections
        def check(self, base_url): #Accepts soc base url w/o query

            params = {
                "subject": self.ru_subject, #Ex. "198"
                "semester": self.ru_semester_code, #Ex. "12018"
                "campus": self.ru_campus, #Ex. "NB"
                "level": self.ru_level #Ex. "UG"
            }
            response = requests.get(base_url, params)

            data = response.json() #dictionary of classes

            prettyString = json.dumps(data, indent=4)

            #Writes the json data into output.txt for easy human reading
            with open("output.txt", "w") as text_file:
                text_file.write(prettyString)

            #Check for open sections
            open_sections = []
            for ru_class in data:
                if ru_class["courseNumber"] == self.ru_class:
                    #print(ru_class["title"])
                    for ru_section in ru_class["sections"]:
                        #print(ru_section["openStatus"])
                        if ru_section["openStatus"] == True and ru_section["number"] in self.ru_sections:
                            open_sections.append(ru_section["number"])

            return open_sections
