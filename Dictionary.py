import json
from difflib import get_close_matches

data = json.load(open("data.json"))


def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input("Did you mean %s ? Enter Y if YES or N if NO:" % get_close_matches(w, data.keys())[0])

        if yn == "Y":
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == "N":
            return "The word doesn't exist. Double Check it"
        else:
            return "we didn't understand your entry"
    else:
        return "The word doesnt exist. Please double check it."


word = input("Enter Word:")
output = translate(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
