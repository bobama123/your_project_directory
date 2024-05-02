# 1) Describe the Problem

# Put or write the user story here. Add any clarifying notes you may have here.
"""
As a User
So that I can keep track of my phone numbers
I want to keep a record of all phone numbers I use in my diary entries.
"""
# * We may want to look through multiple diary entries
# * Phone numbers are 11-digit numbers, starting with zero



# 2) Design the class interface

# Include the initializer, public properties, and public methods with all
# parameters, return values and side effects.

class PhoneBook():
    def extract_numbers(self, diary_entry):
        #Parameters:
        #   diary_entry: (str) a human-readable text, possibly with phone nos
        #Returns nothing
        pass

    def list_numbers(self):
        #Returns:
        #   A list of strings, representing phone numbers
        pass

# 3) Create Examples as Tests

# Make a list of examples of how the class will behave in different
# situations.
"""
Inititally, there are no phone numbers
"""
phone_book = PhoneBook()
phone_book.list_numbers() # > []

"""
When we add a diary entry with no phone number in it
There are no phone numbers reflected in the list
"""
phone_book = PhoneBook()
phone_book.extract_numbers("My friend's number is not relevant here")
phone_book.list_numbers() # > []

"""
When we add a diary entry with a phone number in it
The phone number is reflected in the list
"""
phone_book = PhoneBook()
phone_book.extract_numbers("My friend's number is 07800000000")
phone_book.list_numbers() # > ["07800000000"]

"""
When we add three diary entries with a phone number in them
We see all phone numbers reflected in the list
"""
phone_book = PhoneBook()
phone_book.extract_numbers("Sarah's number is 07800000003")
phone_book.extract_numbers("Geoff's number is 07800000001")
phone_book.extract_numbers("Alex's number is 07800000002")
phone_book.list_numbers() # > ["07800000003", "07800000001", "07800000002"]

"""
When we add an entry with multiple numbers in it
We see all phone numbers reflected in the list
"""
phone_book = PhoneBook()
phone_book.extract_numbers("Sarah's number is 07800000000 and Geoff's number is 07800000001")
phone_book.list_numbers() # > ["0780000000", "07800000001"]

"""
When we have an entry with a number not starting with 0
It is ignored
"""

phone_book = PhoneBook()
phone_book.extract_numbers("My friend's number is 78000000000")
phone_book.list_numbers() # > []

"""
When we add an entry a non 11 digit number
They are ignored
"""

phone_book = PhoneBook()
phone_book.extract_numbers("My friend's number is 780000 or 07800000000000")
phone_book.list_numbers() # > []

# Encode each example as a test. You can add to the above list as you go.


# 4) Implement the Behaivour

# After each test you write, follow the test-driving process of red, green,
# refactor to implement the behaivour.
