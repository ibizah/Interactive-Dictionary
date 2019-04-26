import json
from difflib import get_close_matches
data = json.load(open('data .json'))
word= input('Enter the word : \n')
def translation(w):
    return data[w]
if word in data:
    print(translation(word))
else:
     closest=get_close_matches(word, data, n=5, cutoff=0.5)

    choice=input(f' which one do you mean {closest} ? \n')
    if choice in closest:
        print(translation(choice))
    else:
        print('word does not exist')
