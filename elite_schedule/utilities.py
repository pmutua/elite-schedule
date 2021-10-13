import re

def remove_whitespaces(str):
    output = re.sub(r"\s+", "",str)
    return output
