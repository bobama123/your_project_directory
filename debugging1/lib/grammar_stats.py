class GrammarStats:
    def __init__(self):
        self.checked = 0
        self.passed = 0

    def check(self, text):
        characters = ".!?"
        if text == "":
            raise Exception("No text given")
        result = text[0].isupper() and text[-1] in characters
        if result:
            self.passed += 1
        self.checked += 1
        return result
        
        

    def percentage_good(self):
        return f"{int(self.passed / self.checked) * 100}%"
