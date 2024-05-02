def make_snippet(string1):
    if string1 == None:
        raise Exception("No string set!")
    
    phrase = string1.split()
    if len(phrase) > 5: 
        first_five = phrase[:5]
        new_string = ' '.join(first_five)
        return f"{new_string} ..."
    else:
        return string1
    

        




    

