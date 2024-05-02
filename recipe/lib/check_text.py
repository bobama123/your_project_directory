def check_text(text):
    if text == "":
        raise Exception("No text set!")
    return text[0].isupper() and text[-1] in ".!?"
