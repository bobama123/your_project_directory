def reading_time(text):
    if text == "":
        return f"{0} seconds"
    else:
        words_number = len(text.split(" "))
        time = words_number/200 * 60
        return f"{time} seconds"