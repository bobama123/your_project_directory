"""
As a user
So I don't forget the details
I want to keep a record of friends' names and birthdates

As a user
So I can make edits when I've got dates wrong
I want to be able to update a record by passing in a name and new date

As a user
So I can make edits when people change their name
I want to be able to update a record by passing in an old and a new name

As a user
So I can remember to send birthday cards at the right time
I want to be able to list friends whose birthdays are coming up soon and to whom I need to send a card

As a user
So I can buy age-appropriate birthday cards
I want to calculate the upcoming ages for friends with birthdays

As a user
So I can keep track of cards sent and to be sent
I want to be able to mark a birthday card for a year as "done"
"""

class UserBirthday():
    def __init__(self):
        self.records = []
    def add(name, birthdate):
        #name is string
        #birthdate is datetime
        #card_sent is boolean (Set to false)
        #Side effects: Adds parameters to dictionary
        pass
    def update_date(name, new_date):
        #name is string
        #new_date is datetime
        #Side effects: Updating an existing date based on the name
        pass
    def update_name(name, new_name):
        #name is string
        #new_name is string
        #Side effects: Updating an existing name based on the name
        pass
    def reminder(date):
        #date is datetime
        #Returns a list of names with dates of birthdays in next 30 days
        pass
    def age(date):
        #date is datetime
        #Returns age as a string
        pass
    def marked(date):
        #date is datetime
        #Side effects: for person, if date is after birthdate, swap card_sent = True
        pass

## TESTS ##
    
"""
Test if an empty list is initialized
"""
user_birthday = UserBirthday()
result = user_birthday.records

assert result == []

"""
Test if two people are added to the records list
"""
user_birthday = UserBirthday()
user_birthday.add("Bobby", "25-11-1998")
user_birthday.add("Dom", 28-1-1992)

result = user_birthday.records

assert result == [{'name': "Bobby", 'birthdate': "25-11-1998", 'card_sent': False}, {'name': "Dom", 'birthdate': "28-1-1992", 'card_sent': False}]

"""
Test if update changes the date on a person
"""
user_birthday = UserBirthday()
user_birthday.add("Bobby", 25-11-1998)
user_birthday.add("Dom", 28-1-1992)
user_birthday.update_date("Bobby", 18-5-2000)

result = user_birthday.records

assert result == [{'name': "Bobby", 'birthdate': 18-5-2000, 'card_sent': False}, {'name': "Dom", 'birthdate': 28-1-1992, 'card_sent': False}]

"""
Test if update changes the name on a person
"""
user_birthday = UserBirthday()
user_birthday.add("Bobby", 25-11-1998, False)
user_birthday.add("Dom", 28-1-1992, False)
user_birthday.update_name("Dom", "Maximillian")

result = user_birthday.records

assert result == [{'name': "Bobby", 'birthdate': 25-11-1998, 'card_sent': False}, {'name': "Maximillian", 'birthdate': 28-1-1992, 'card_sent': False}]

"""
Test if reminder returns a list of names with dates of birthdays in the next 30 days from given date
"""
user_birthday = UserBirthday()
user_birthday.add("Bobby", 25-11-1998, False)
user_birthday.add("Dom", 28-1-1992, False)
result = user_birthday.reminder(16-11-2021)

assert result == [{'name': "Bobby", 'birthdate': 25-11-1998, 'card_sent': False}]


"""
Test if age returns age of users from reminder
"""
user_birthday = UserBirthday()
user_birthday.add("Bobby", 25-11-1998, False)
user_birthday.reminder(16-11-2021)
result = user_birthday.age(16-11-2021)

assert result == "Upcoming birthday of {Bobby}, age is 23"

"""
Test if marked given a name and date, changes card_sent to True for the name
"""
user_birthday = UserBirthday()
user_birthday.add("Bobby", 25-11-1998, False)
user_birthday.add("Dom", 28-1-1992, False)
user_birthday.marked(16-11-2021)

result = user_birthday.records

assert result == [{'name': "Bobby", 'birthdate': 25-11-1998, 'card_sent': False}, {'name': "Dom", 'birthdate': 28-1-1992, 'card_sent': True}]


