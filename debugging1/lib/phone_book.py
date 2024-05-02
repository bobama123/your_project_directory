import re
class PhoneBook():
    def __init__(self):
        self._numbers = []

    def extract_numbers(self, diary_entry):
        numbers = re.findall(r'\b0[0-9]{10}\b', diary_entry)
        print(numbers)
        self._numbers += numbers


    def list_numbers(self):
        return self._numbers 