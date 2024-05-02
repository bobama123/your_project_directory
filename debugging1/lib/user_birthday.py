from datetime import datetime, timedelta
import math

class UserBirthday():
    def __init__(self):
        self.records = []

    def add(self, name, birthdate):
        new_entry = {'name': name, 'birthdate': self.convert_date(birthdate), 'card_sent': False}
        self.records.append(new_entry)

    def convert_date(self, date_str):
        date_obj = datetime.strptime(date_str, "%d-%m-%Y")
        return date_obj


    def update_date(self, name, new_date):
        for person in self.records:
            if person['name'] == name:
                person['birthdate'] = self.convert_date(new_date)

    def update_name(self, name, new_name):
        for person in self.records:
            if person['name'] == name:
                person['name'] = new_name

    def reminder(self, date):
        current_date_obj = self.convert_date(date)
        current_plus_30 = current_date_obj + timedelta(days=30)
        self.list_of_birthdays_oncoming = []
        year = current_date_obj.year

        for person in self.records:
            this_year_bday = person['birthdate'].replace(year)
            if current_date_obj < this_year_bday < current_plus_30:
                self.list_of_birthdays_oncoming.append(person)

        return self.list_of_birthdays_oncoming
    
    def age(self, date):
        current_date_obj = self.convert_date(date)
        for person in self.list_of_birthdays_oncoming:
            birthdate = person['birthdate']
            age = int(math.ceil((current_date_obj - birthdate).days / 365.25))
            return f"Upcoming birthday of {person['name']}, age is {age}"



            
        



        
                
